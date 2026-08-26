using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using Modding;
using Newtonsoft.Json;

namespace HalallowKnight
{
    /// <summary>
    /// Rewords divine / "higher being" framing in displayed text.
    /// Hooks ModHooks.LanguageGetHook and nothing else - no gameplay, scene, FSM or
    /// networked state is touched, which is what keeps this HKMP-safe.
    /// </summary>
    public class HalallowKnight : Mod
    {
        public HalallowKnight() : base("Halallow Knight") { }

        public override string GetVersion() => "0.1.0";

        private Config _cfg = new Config();
        private readonly HashSet<string> _seen = new HashSet<string>();
        private readonly Dictionary<string, string> _cache = new Dictionary<string, string>();
        private string _dir = ".";
        private string _dumpPath = "";

        public override void Initialize()
        {
            _dir = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location) ?? ".";
            _dumpPath = Path.Combine(_dir, "language-dump.tsv");

            LoadConfig();

            ModHooks.LanguageGetHook += OnLanguageGet;

            Log($"Initialized. dumpMode={_cfg.DumpMode}, " +
                $"exactOverrides={_cfg.ExactOverrides.Count}, terms={_cfg.TermReplacements.Count}");
        }

        /// <summary>
        /// LanguageGetProxy: (key, sheetTitle, orig) -> replacement. Must never throw and
        /// must always hand back a usable string, so everything here is wrapped.
        /// </summary>
        private string OnLanguageGet(string key, string sheet, string orig)
        {
            try
            {
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

            // Escape newlines/tabs so one entry stays one line in the TSV.
            string text = (orig ?? "")
                .Replace("\\", "\\\\")
                .Replace("\r", "")
                .Replace("\n", "\\n")
                .Replace("\t", "\\t");

            File.AppendAllText(_dumpPath, id + "\t" + text + Environment.NewLine);
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

        private void LoadConfig()
        {
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
        [JsonProperty("dumpMode")]
        public bool DumpMode = true;

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
