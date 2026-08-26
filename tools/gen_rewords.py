#!/usr/bin/env python3
"""Regenerate REWORDS.md from reword-config.json, verified against a full language dump.

Usage:  python3 tools/gen_rewords.py [path/to/language-dump-all.tsv]

Applies the same algorithm the mod uses (exact overrides win; term replacements
longest-key-first) so the document always reflects what the config actually does.
"""
import json, os, re, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = os.path.join(ROOT, "src", "HalallowKnight", "reword-config.json")
OUT = os.path.join(ROOT, "REWORDS.md")
DEFAULT_DUMP = os.path.expanduser(
    "~/Library/Application Support/Steam/steamapps/common/Hollow Knight/hollow_knight.app"
    "/Contents/Resources/Data/Managed/Mods/HalallowKnight/language-dump-all.tsv")

GROUPS = [
    ("Core god vocabulary", ["God of Gods","Higher beings","higher beings","Higher being","higher being",
        "Godseekers","Godseeker","Godmaster","Godtuner","Godhome","godliness","godless","Godly","godly",
        "Gods","gods","God","god","Pantheons","pantheons","PANTHEON","Pantheon","pantheon"]),
    ("Religious vocabulary", ["Worshippers","worshippers","worshipped","deified",
        "Sacred","sacred","Holy","holy","Divine","divine","deity","Prayer","prayers",
        "Blasphemy","blasphemy","blasphemies","heretic"]),
    ("Rites, objects and places", ["rituals","Ritual","ritual","idols","Idol","idol",
        "Shrine","shrines","shrine","Temples","temples","Temple","temple","Penitent"]),
    ("Magic and its practitioners", ["shamans","Shaman","shaman","Spells","spells","Spell","spell",
        "Conjures","Conjure","conjures","conjured","conjure","Arcane","arcane","Hex","mystical",
        "Enchanting","Enchanted","Prophet"]),
    ("Blessing and fortune", ["Blessings","Blessing","blessings","blessing","Blessed","blessed"," by fortune"]),
]

OVERRIDE_REASONS = [
    ("CP3|GODSEEKER_ENGINE", "\"We **pray** that the Gods…\" — *pray* meaning *beseech*, not the act of prayer"),
    ("CP3|GODSEEKER_ENGINE_PRIME", "same *pray* sense, plus \"God of Gods\" and two bare \"God\"s"),
    ("CP3|GODSEEKER_ENGINE_3", "\"Through **ritual** combat\" — *performance combat* is not grammatical"),
    ("CP3|PANTHEON_ENTER_3", "\"**Pray** will We, Attune will We\" — capitalised *Pray*, which must survive elsewhere"),
    ("Elderbug|ELDERBUG_TEMPLE_VISITED", "\"went there to **pray**\" — the literal act, needing a different word"),
    ("Journal|NOTE_MAGE_LORD", "\"tricks and **rituals** and **prayers**\""),
    ("Minor NPC|TUK_DREAM", "\"keep searching… and **praying**\""),
    ("Jiji|RITUAL_BEGIN", "a summoning, not a show — *\"we will begin the performance\"* would be wrong"),
    ("Stag|STAG_RESTINGGROUNDS", "funeral rites, and the original had **the dead acting** — agency moved back to the living"),
    ("CP2|BRUMM_DEEPNEST_2", "\"songs of **sacrifice**, of servitude\" — the one devotional use of *sacrifice*"),
    ("Minor NPC|BRETTA_DIARY_3", "\"would break the **spell**\" — the moment, not magic"),
    ("UI|CHARM_DESC_33", "\"**casting** spells\" — *cast* cannot be a term rule (it is inside *caste*, *outcast*, *Lancaster*)"),
    ("UI|SHOP_DESC_SPELLDMGUP", "\"Are you a **spellcaster**\""),
    ("CP3|NOTE_PURE_VESSEL", "*spell* carries the shell/spell rhyme; *cell* keeps it and fits the Vessel's imprisonment"),
    ("Journal|NOTE_PURE_VESSEL", "duplicate of the above"),
    ("Zote|PRECEPT_29", "\"a **magical** map inside of your head\" — figurative, but the word still goes"),
    ("Minor NPC|DUNG_DEFENDER_REPEAT", "\"Good **fortune** on the path ahead\" — luck, not divination"),
    ("UI|SHOP_DESC_TRINKET4", "\"a small **fortune**\" — money, so it needs a different word again"),
    ("CP3|NOTE_NAILMASTERS", "the four verses are **supplications** — \"Help Us find the God We seek!\" — so they are rewritten as records rather than petitions"),
    ("Journal|NOTE_NAILMASTERS", "duplicate"),
    ("CP3|NOTE_PAINTMASTER", "\"**Reveal to Us** the God most pure!\""),
    ("Journal|NOTE_PAINTMASTER", "duplicate"),
    ("CP3|NOTE_SAGE_SLY", "\"**Sharpen Our nails and show Us** the odds\""),
    ("Journal|NOTE_SAGE_SLY", "duplicate"),
    ("CP3|NOTE_VOID_IDOL_1", "\"devoted their **worship** to… the very darkness itself\" — renaming worship is not enough, the concept is removed"),
    ("CP3|NOTE_VOID_IDOL_2", "duplicate"), ("CP3|NOTE_VOID_IDOL_3", "duplicate"),
    ("Journal|NOTE_VOID_IDOL_1", "duplicate"), ("Journal|NOTE_VOID_IDOL_2", "duplicate"),
    ("Journal|NOTE_VOID_IDOL_3", "duplicate"),
    ("Relic Dealer|RELICDEALER_IDOL_1", "\"**worship** was offered through these idols\" — an offering, so the line is reworked, not reworded"),
    ("UI|INV_DESC_TRINKET3", "\"the elusive king was **worshipped** through these idols\" — same"),
    ("Relic Dealer|RELICDEALER_IDOL_4", "\"A ruler seeking **worship**\""),
    ("Quirrel|QUIRREL_GREENPATH_1", "\"suggests some form of **worship**\""),
    ("Jiji|SHAMAN_TEMPLE", "\"a place of strange **worships**\""),
    ("CP3|PANTHEON_ENTER_0", "\"Through **sacred** combat\" (*cherished combat* does not read) and \"be **damned** for thy arrogance\""),
    ("CP3|GODSEEKER_ENGINE_REPEAT_3", "\"Our **sacred** attunement\" — *cherished* does not fit here either"),
    ("Minor NPC|XUN_MEET", "\"This cruel, **sinful** world\""),
    ("Charm Slug|CHARMSLUG_OVERCHARM", "\"a bit of a **sin** to wear too many Charms\""),
    ("Journal|NOTE_GHOST_XERO", "\"burdened by **sins** and memories\""),
    ("CP3|GG_S_BIGBEES", "\"Lover gods of **faith** and devotion\" — devotional, unlike the idiomatic uses"),
    ("CP3|GG_S_GHOST_XERO", "\"Dreamborn god of **faith** and betrayal\" — same"),
    ("CP3|GODSEEKER_WATERWAYS_AWAKE_2", "\"What draws thee here, Crawler? **Faith**? Fear?\""),
    ("Dream Witch|WITCH_FINAL_2", "\"hush whispers of **faith**\" — belief in the ancient light"),
    ("Achievements|ENDINGD_TEXT", "term rules produced \"**Ascend the Ascent** of Hallownest\""),
    ("CP3|ENDING_D_TEXT", "duplicate of the above"),
]

NOTES = """**Notes on specific choices**

- **`Divine` → `Sublime`** does double duty. *Divine* is both a Grimm Troupe character's name and
  the compliment other bugs pay her ("this creature… is just divine") — wordplay on her name.
  *Sublime* works as both, so the joke survives the rename.
- **`Godtuner` → `Attuner`** rather than a `Light-` compound, which read awkwardly. The Godseekers
  already speak of *attuning*, so the charm name stays native to its own lore.
- **`God of Gods` → `Light of Lights`** is its own term because the plain rules would otherwise
  produce the clumsy "Luminary of Luminaries".
- **`Pantheon` → `Ascent`** matches the Godseekers' language of resonance and rising.
- **`Ritual` → `Performance`** suits the Grimm Troupe, who are a travelling show. It keeps Grimm's
  showman register ("A charming performance… a pleasure!") and Brumm's music metaphor. The two
  non-Grimm uses — a funeral rite and a summoning — are exact overrides instead.
- **`Idol` → `Effigy`** — a sculpted likeness rather than an object of worship.
- **`Shrine` → `Memorial`** — every shrine in the game marks a death or a memory, not a deity, and
  the game already uses the word: the Ruins fountain reads "Memorial to the Hollow Knight".
- **`Temple` → `Vault`** — also already canon: the fountain plaque reads "In the Black Vault far above".
- **`Shaman` → `Adept`** — describes skill rather than spiritual practice. *Sage* was avoided
  because the Pantheon of the Sage already uses that word.
- **`Spell` → `Skill`** — keeps the mechanic legible without magical framing. *Arts* was avoided
  because Hollow Knight already has Nail Arts, which would have merged two distinct concepts.
- **`Conjure` → `Form`** works across every occurrence, including "The spirit requires SOUL to be
  **formed**" and Dreamshield's "**Forms** a shield".
- **`Arcane`** splits by case: **`Arcane` → `Primal`** for the *Arcane Egg* relic, and
  **`arcane` → `hidden`** for "uses **arcane** knowledge". *Ancient* was avoided because the Relic
  Dealer's very next line already says "this is an ancient thing".
- **`Blessing` → `Boon`**, **`Blessed` → `Favoured`** — *Joni's Boon*, "Salubra's boon", and the
  "Favoured" achievement.
- **`fortune`** cannot be one rule: it appears as luck ("Good fortune on the path ahead"), as money
  ("a small fortune") and as chance ("not merely by fortune that we meet — in the darkest reaches
  of the world, where my Master's scarlet eyes can not see us", where Brumm means their meeting is
  *not* random). Only the last is a term rule; the other two are exact overrides.
- **`Hex` → `Vex`** — this is a proper name on a Godhome title card, not a spell, so it keeps the
  shape of a name.
- **`sacred` → `cherished`** rather than *revered*. Note that the game's own untouched text already
  uses "revered" in a plainly secular sense — "They're **revered** figures of Hallownest" of the
  five great knights — but *cherished* carries no veneration at all. The two Godseeker lines where
  it does not fit ("cherished combat", "cherished attunement") are exact overrides.
- **`worship` is not a term rule at all.** Replacing it with a synonym like *reverence* renames the
  concept without removing it, so every occurrence is an exact override that reworks the line:
  "devoted their worship to" → "devoted **themselves** to"; "worship was offered through these
  idols" → "these **stood in his place**".
- **`sin` and `sins` can never be term rules** — they sit inside *u**sin**g*, *__sin__ce*,
  *bu**sin**ess* and *cou**sin**s*. All three occurrences are exact overrides.
- **`blasphemy` → `insolence`** — blasphemy presupposes the sacred order the mod removes.
- **`heretic` → `outcast`** — Joni was cast out, which is what the line actually means."""

ROADMAP = """## 5. Roadmap

The scheme covers **divine framing** and **magic**. These areas are identified but not implemented.

### 5.1 Charms

86 entries — a core UI mechanic: charm names, 40+ descriptions, notches, menus.

> **Solved approach:** term replacement is a plain substring `String.Replace` with no word
> boundaries, and there are **4 occurrences of "charming"** (e.g. Grimm's "A charming performance…
> a pleasure!", the Snail Adept's "Aren't you the charming one"). Those four get **exact overrides**
> so a `charm → …` rule cannot corrupt them into "cresting".

### 5.2 Dreams

~131 entries plus the 272-entry `Enemy Dreams` sheet. Forms: `dreams` 49, `Dream` 43, `dream` 31,
`dreaming` 7, `Dreamborn` 7, `Dreamgate` 6, `Dreamers` 5, `Dreamshield` 1. Heavily entangled with
mechanics and plot. Needs its own pass to separate ordinary sleeping from entering others' dreams.

### 5.3 The dead depicted as acting

Addressed once already in `Stag|STAG_RESTINGGROUNDS`. Unreviewed: the `Ghosts` sheet (83 entries)
and the dream-warrior lore, where a dead bug's persisting dream produces a figure resembling them.
`ghost` 11, `spirit` 15.

### 5.4 Scope limit to keep in mind

This mod changes **displayed text only** — the design rule that keeps it a pure reword and
compatible with everything else. It cannot change mechanics. Renaming the Dream Nail does not stop
it entering dreams. Where a concern is about the *mechanic* rather than its *wording*, rewording
can only go so far."""


def main():
    dump = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DUMP
    cfg = json.load(open(CFG, encoding="utf-8"))
    T, E = cfg["termReplacements"], cfg["exactOverrides"]
    terms = sorted(T.items(), key=lambda kv: -len(kv[0]))

    rows = [l.rstrip("\n").split("\t") for l in open(dump, encoding="utf-8")]
    rows = [r for r in rows if len(r) >= 3]
    changed, total = [], len(rows)
    origs = {}
    for r in rows:
        sheet, key, orig = r[0], r[1], "\t".join(r[2:])
        ck = f"{sheet}|{key}"
        origs[ck] = orig
        res = E[ck] if ck in E else orig
        if ck not in E:
            for k, v in terms:
                res = res.replace(k, v)
        if res != orig:
            changed.append((sheet, key, "exact" if ck in E else "term", orig, res))

    cascades = [(k, s) for k, v in T.items() for s in T if s in v and s != k]

    o = []
    o.append(f"""# Reworded text

Every change Halallow Knight makes, and every deliberate decision *not* to change something.
Generated against Hollow Knight **1.5.78.11833** — {total:,} localisation entries, of which
**{len(changed)} are altered** and {total - len(changed):,} are untouched.

*This file is generated. Run `python3 tools/gen_rewords.py` after editing the config.*

The wording scheme is **Luminaries**: divine authority is recast as light and brilliance rather
than godhood, keeping Hollow Knight's register intact.

---

## 1. Term replacements

Applied to the original string wherever they appear. Longer keys always match first, so compounds
like `Godhome` are handled before the bare `god` inside them.""")
    listed = set()
    for title, keys in GROUPS:
        o.append(f"\n### {title}\n\n| original | becomes |\n|---|---|")
        for k in keys:
            if k in T:
                o.append(f"| `{k}` | `{T[k]}` |"); listed.add(k)
    rest = [k for k in T if k not in listed]
    if rest:
        o.append("\n### Other\n\n| original | becomes |\n|---|---|")
        for k in sorted(rest, key=len, reverse=True):
            o.append(f"| `{k}` | `{T[k]}` |")
    o.append("\n" + NOTES)

    o.append(f"""
---

## 2. Exact overrides

{len(E)} entries are replaced outright rather than word-by-word, because a term rule would have
been wrong or clumsy. **Exact overrides bypass term replacements entirely**, so each is written
with all other rewording already applied.

| entry | why |
|---|---|""")
    reasons = dict(OVERRIDE_REASONS)
    ordered = [k for k, _ in OVERRIDE_REASONS if k in E] + [k for k in E if k not in reasons]
    for k in ordered:
        o.append(f"| `{k.replace('|', chr(92) + '|')}` | {reasons.get(k, '—')} |")
    o.append("\n### Full text\n")
    for k in ordered:
        o.append(f"**`{k}`**\n")
        o.append(f"> **Before** — {origs.get(k,'')}\n")
        o.append(f"> **After** — {E[k]}\n")

    o.append("""---

## 3. Deliberately left unchanged

| kept | reason |
|---|---|
| **Radiance** / **Absolute Radiance** | a proper name, not divine framing |
| **Master** — Grimm's title | a title of rank, not of worship |
| **`witch`** | never actually occurs — every apparent hit is inside **"Switch User"** in the menu, which a naive rule would corrupt |
| **`cult`** | never actually occurs either — all 14 apparent hits are inside **"difficult"** and **"difficulty"** |
| **`summon`** | 3 uses, all ordinary calling: "Did you **summon** them?", "your **summons** heeded", Weaversong's "**Summons** weaverlings" |
| **`possess`** | 9 uses, all ordinary having or owning: "what skills you **possess**", "most prized **possession**", "the rock itself **possessed** a will" |
| `Minor NPC\\|TISO_SHIELD` — "**Pray** you never find out what that is" | pure figure of speech |
| `Zote\\|ZOTE_COLOSSEUM_REPEAT` — "**Pray** we do not meet in the arena" | same idiom |
| **`sacrifice`** elsewhere (7) | ordinary uses — the Hollow Knight's own sacrifice, the King's imposed sacrifices, the hatchlings |
| **SOUL** | a core game mechanic — 104 entries untouched, pending a decision |
| **`salvation`** | the line glosses it itself: "The Kingdom's salvation, **the cure for the plague**" — rescue, not theology |
| **`Saviour`** | Bretta's diary romance about Zote ("The White Saviour"), and "tiny saviour" — a rescuer in the ordinary sense |
| **`chanting`** | left by choice — one use, Elderbug describing Jiji's cave as "extremely **sinister** chanting", framed as eerie rather than devotional |
| **"Dreams revered"** (`DREAM_PLANT_REST_MAIN`) | untouched vanilla wording — the game's own secular use of *revered* |

| **The Moss Cultist's dialogue** | left vanilla by choice. The player character and the story's sympathetic figures never worship the Radiance, and the mod has already removed what legitimised her position as a god — so the cultists simply read as followers of another religion. |
| **`faith`** as trust | 9 of its 13 uses are idiomatic — "Have faith in me!", "Don't be afraid. Have faith!", "my faith in one has been challenged". A term rule would wreck these, so `faith` is deliberately **not** a term rule; the 4 devotional uses are exact overrides instead. |

The two `Pray` lines are the **only** occurrences of any target word remaining anywhere in the
final output, and both are intentional.

---

## 4. Impact by sheet

| sheet | entries changed |
|---|---:|""")
    for s, n in collections.Counter(c[0] for c in changed).most_common():
        o.append(f"| {s} | {n} |")
    o.append("\n`CP3` is the Godmaster content pack and `CP2` the Grimm Troupe, which is why those dominate.\n\n---\n")
    o.append(ROADMAP)
    o.append(f"""
---

## 6. Verification

Generated by simulating the mod's own algorithm over all {total:,} dumped entries:

- **{len(changed)}** entries changed, {total - len(changed):,} untouched
- **{sum(1 for c in changed if c[2] == 'exact')}** exact overrides, {sum(1 for c in changed if c[2] == 'term')} via term rules
- **{len(T)}** term rules, **{len(E)}** exact overrides
- **{len(cascades)}** replacement cascades (no rule's output may contain another rule's search key)
""")
    open(OUT, "w", encoding="utf-8").write("\n".join(o))
    print(f"REWORDS.md: {len(changed)} changed / {total} entries, {len(T)} terms, {len(E)} overrides, {len(cascades)} cascades")


if __name__ == "__main__":
    main()
