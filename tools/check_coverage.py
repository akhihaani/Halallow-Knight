#!/usr/bin/env python3
"""Compare the config against text the game actually asked for.

REWORDS.md is verified against a dump of the language *files*, which proves a string exists but
not that the game ever requests it through the call this mod hooks. Achievements are the known
case where those differ: their text comes from Steam, so no rule can reach it.

This script closes that gap. Set "dumpMode": true, play, and the mod records every real hook call
to language-dump.tsv. Run this against that file to see which of your rules have been observed
firing, and which sheets the hook has never seen.

Usage:  python3 tools/check_coverage.py [path/to/language-dump.tsv]

Coverage grows as you play, so "not yet observed" means exactly that - not that a rule is broken.
"""
import json, os, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = os.path.join(ROOT, "src", "HalallowKnight", "reword-config.json")
DEFAULT = os.path.expanduser(
    "~/Library/Application Support/Steam/steamapps/common/Hollow Knight/hollow_knight.app"
    "/Contents/Resources/Data/Managed/Mods/HalallowKnight/language-dump.tsv")


def main():
    seen_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT
    if not os.path.isfile(seen_path):
        sys.exit(
            f"No hook-traffic dump at {seen_path}\n\n"
            'Set "dumpMode": true in reword-config.json, play for a while, then run this again.\n'
            "Note that dump mode returns the original text, so replacements are off while it runs.")

    cfg = json.load(open(CFG, encoding="utf-8"))
    T, E = cfg["termReplacements"], cfg["exactOverrides"]
    terms = sorted(T.items(), key=lambda kv: -len(kv[0]))

    rows = [l.rstrip("\n").split("\t") for l in open(seen_path, encoding="utf-8")]
    rows = [r for r in rows if len(r) >= 3]
    sheets = collections.Counter(r[0] for r in rows)

    fired_terms, fired_overrides, would_change = set(), set(), 0
    for r in rows:
        ck = f"{r[0]}|{r[1]}"
        orig = "\t".join(r[2:]).replace("\\n", "\n").replace("\\t", "\t")
        if ck in E:
            fired_overrides.add(ck)
            would_change += 1
            continue
        res = orig
        for k, v in terms:
            if k in res:
                res = res.replace(k, v)
                fired_terms.add(k)
        if res != orig:
            would_change += 1

    print(f"Observed {len(rows)} entries the game actually requested, across {len(sheets)} sheets.")
    print(f"Of those, {would_change} would be reworded.\n")

    print("Sheets seen:")
    for s, n in sheets.most_common():
        print(f"  {s:20} {n}")

    unseen_o = [k for k in E if k not in fired_overrides]
    unseen_t = [k for k in T if k not in fired_terms]
    print(f"\nRules observed firing: {len(fired_terms)}/{len(T)} terms, "
          f"{len(fired_overrides)}/{len(E)} overrides.")

    by_sheet = collections.Counter(k.split("|")[0] for k in unseen_o)
    if by_sheet:
        print("\nOverrides not yet observed, by sheet:")
        for s, n in by_sheet.most_common():
            mark = "  <- unreachable" if s == "Achievements" else ""
            print(f"  {s:20} {n}{mark}")
    if unseen_t:
        print(f"\n{len(unseen_t)} terms not yet observed, e.g. "
              + ", ".join(repr(k) for k in unseen_t[:8]))
    print("\nCoverage grows as you play. Only a sheet that never appears after thorough play is\n"
          "evidence of unreachable text.")


if __name__ == "__main__":
    main()
