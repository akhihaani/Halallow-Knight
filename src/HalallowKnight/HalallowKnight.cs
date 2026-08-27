using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;
using Modding;
using Newtonsoft.Json;

namespace HalallowKnight
{
    /// <summary>
    /// Rewords religious and supernatural framing in the game's displayed text.
    /// Hooks ModHooks.LanguageGetHook and nothing else - no gameplay, scene, FSM or
    /// networked state is touched, so it cannot conflict with other mods.
    /// </summary>
    public class HalallowKnight : Mod
    {
        public HalallowKnight() : base("Halallow Knight") { }

        /// <summary>
        /// The wording lives in the config, and changes far more often than this assembly, so the
        /// displayed version comes from the config where possible. That way a new wording list on
        /// its own bumps the number shown on the title screen, with no rebuild - which is how you
        /// confirm at a glance that the game picked up the version you meant.
        /// </summary>
        public override string GetVersion()
        {
            LoadConfig();
            return string.IsNullOrEmpty(_cfg.Version) ? AssemblyVersion : _cfg.Version;
        }

        private const string AssemblyVersion = "0.2.0";

        private Config _cfg = new Config();
        private readonly HashSet<string> _seen = new HashSet<string>();
        private readonly Dictionary<string, string> _cache = new Dictionary<string, string>();
        private string _dir = ".";
        private string _dumpPath = "";
        private string _dumpAllPath = "";
        private bool _dumpedAll;
        private bool _loaded;

        public override void Initialize()
        {
            LoadConfig();

            ModHooks.LanguageGetHook += OnLanguageGet;

            Log($"Initialized. version={GetVersion()}, dumpMode={_cfg.DumpMode}, " +
                $"dumpAll={_cfg.DumpAll}, exactOverrides={_cfg.ExactOverrides.Count}, " +
                $"terms={_cfg.TermReplacements.Count}");
        }

        /// <summary>
        /// LanguageGetProxy: (key, sheetTitle, orig) -> replacement. Must never throw and
        /// must always hand back a usable string, so everything here is wrapped.
        /// </summary>
        private string OnLanguageGet(string key, string sheet, string orig)
        {
            try
            {
                // Fire once, on the first lookup - by then the language data is definitely
                // loaded, which it may not be while Initialize() is still running.
                if (_cfg.DumpAll && !_dumpedAll)
                {
                    _dumpedAll = true;   // set first: a failure must not retry every lookup
                    DumpAll();
                }

                if (_cfg.DumpMode)
                {
                    Dump(key, sheet, orig);
                    return orig;
                }

                return Apply(key, sheet, orig);
            }
            catch (Exception e)
            {
                LogError($"LanguageGet failed for {sheet}|{key}: {e}");
                return orig;
            }
        }

        private void Dump(string key, string sheet, string orig)
        {
            string id = sheet + "\t" + key;
            if (!_seen.Add(id)) return;

            File.AppendAllText(_dumpPath, id + "\t" + Escape(orig) + Environment.NewLine);
        }

        /// <summary>
        /// Development helper. Reads the game's already-loaded localisation table in one go and
        /// writes every (sheet, key, original) to language-dump-all.tsv, so the reword list can be
        /// built without playing to endgame content first.
        ///
        /// This is a read of the same text the hook already sees - it installs no additional hook
        /// and mutates nothing. Off by default in the shipped config.
        /// </summary>
        private void DumpAll()
        {
            const string FieldName = "currentEntrySheets";

            FieldInfo field = typeof(global::Language.Language)
                .GetField(FieldName, BindingFlags.NonPublic | BindingFlags.Static);

            if (field == null)
            {
                LogError($"dumpAll: no static field '{FieldName}' on Language.Language; " +
                         "the game version may differ. Falling back to incremental dump only.");
                return;
            }

            if (!(field.GetValue(null) is Dictionary<string, Dictionary<string, string>> sheets))
            {
                LogError($"dumpAll: '{FieldName}' was null or not the expected dictionary type.");
                return;
            }

            var sb = new StringBuilder();
            int rows = 0;

            // Sorted so re-runs produce a stable, diffable file.
            foreach (string sheet in sheets.Keys.OrderBy(k => k, StringComparer.Ordinal))
            {
                Dictionary<string, string> entries = sheets[sheet];
                if (entries == null) continue;

                foreach (string key in entries.Keys.OrderBy(k => k, StringComparer.Ordinal))
                {
                    sb.Append(sheet).Append('\t')
                      .Append(key).Append('\t')
                      .Append(Escape(entries[key]))
                      .Append(Environment.NewLine);
                    rows++;
                }
            }

            File.WriteAllText(_dumpAllPath, sb.ToString());
            Log($"dumpAll: wrote {rows} entries across {sheets.Count} sheets to {_dumpAllPath}");
        }

        /// <summary>Keeps one entry on one TSV line.</summary>
        private static string Escape(string text)
        {
            return (text ?? "")
                .Replace("\\", "\\\\")
                .Replace("\r", "")
                .Replace("\n", "\\n")
                .Replace("\t", "\\t");
        }

        private string Apply(string key, string sheet, string orig)
        {
            if (string.IsNullOrEmpty(orig)) return orig;

            string ck = sheet + "|" + key;
            if (_cache.TryGetValue(ck, out string hit)) return hit;

            string result;
            if (_cfg.ExactOverrides.TryGetValue(ck, out string exact))
            {
                // Exact sheet|key override always wins - no term pass over it.
                result = exact;
            }
            else
            {
                result = orig;
                // Longest key first, so multi-word phrases beat the short words inside them.
                foreach (KeyValuePair<string, string> kv in _cfg.TermsOrdered)
                    result = result.Replace(kv.Key, kv.Value);
            }

            _cache[ck] = result;
            return result;
        }

        /// <summary>
        /// Idempotent: GetVersion() may run before Initialize(), so either can be first.
        /// </summary>
        private void LoadConfig()
        {
            if (_loaded) return;
            _loaded = true;

            _dir = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location) ?? ".";
            _dumpPath = Path.Combine(_dir, "language-dump.tsv");
            _dumpAllPath = Path.Combine(_dir, "language-dump-all.tsv");

            string path = Path.Combine(_dir, "reword-config.json");
            try
            {
                if (File.Exists(path))
                    _cfg = JsonConvert.DeserializeObject<Config>(File.ReadAllText(path)) ?? new Config();
                else
                    Log($"No reword-config.json at {path}; using defaults (dump mode).");
            }
            catch (Exception e)
            {
                // A broken config must not take the mod down - fall back to dump mode.
                LogError($"Failed to read reword-config.json, using defaults: {e}");
                _cfg = new Config();
            }

            _cfg.Build();
        }
    }

    public class Config
    {
        /// <summary>Shown on the title screen. Lets a config-only change bump the version.</summary>
        [JsonProperty("version")]
        public string Version = "";

        [JsonProperty("dumpMode")]
        public bool DumpMode = true;

        /// <summary>
        /// Development helper: dump the game's entire localisation table once, on first lookup.
        /// Leave false in released builds.
        /// </summary>
        [JsonProperty("dumpAll")]
        public bool DumpAll = false;

        /// <summary>"Sheet|KEY" -> replacement text.</summary>
        [JsonProperty("exactOverrides")]
        public Dictionary<string, string> ExactOverrides = new Dictionary<string, string>();

        /// <summary>"Higher Being" -> "great one", applied to the original text.</summary>
        [JsonProperty("termReplacements")]
        public Dictionary<string, string> TermReplacements = new Dictionary<string, string>();

        [JsonIgnore]
        public List<KeyValuePair<string, string>> TermsOrdered = new List<KeyValuePair<string, string>>();

        public void Build()
        {
            if (ExactOverrides == null) ExactOverrides = new Dictionary<string, string>();
            if (TermReplacements == null) TermReplacements = new Dictionary<string, string>();

            TermsOrdered = TermReplacements
                .OrderByDescending(k => k.Key.Length)
                .ToList();
        }
    }
}
