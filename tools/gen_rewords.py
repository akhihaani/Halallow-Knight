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
    ("SOUL, charms and articles", ["Worldsoul","Kingsoul","Soulful","Sanctum","sanctum","SOULS","SOUL",
        "Souls","souls","Soul","soul","OVERCHARMED","CHARMS","Charms","charms","Charm","charm",
        "a charm","A charm","a Charm","A Charm","a Pantheon","A Pantheon","a pantheon","An Arcane","an Arcane"]),
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
- **`heretic` → `outcast`** — Joni was cast out, which is what the line actually means.
- **`SOUL` → `SPARK`** was chosen because every compound falls out naturally: *Spark Catcher*,
  *Spark Eater*, **Kingspark**, **Worldspark**, *Shade Spark*, *Spark Master*. SOUL is rendered as
  white light in-game, so it also fits visually. `Soul Sanctum` → **Spark Spire** keeps the
  alliteration and is literally accurate, since it is a tower in the City of Tears.
- **Pre-existing uses of "spark" had to be reworked.** Hollow Knight's writing is deliberate, so a
  stray "spark" would read as a reference to the resource: "a **spark** of power woven into their
  cores" → *a trace of power*; "A **spark** of red lights darkest dream" → *A flicker of red*;
  "our life is but a **spark**" → *a flicker*; "wonderful, **sparkling** things" → *glittering*.
- **`charm` → `emblem`** — every shorter alternative was already taken: *mark* (76), *seal* (40),
  *stone* (21), *relic* (18), *trinket* (7 — Salubra already calls charms trinkets), *crest* (6 —
  Defender's Crest), *token* (3 — "Token Marker"), *keepsake*, *talisman*. `emblem` occurs zero
  times in vanilla text.
- **`OVERCHARMED` → `OVERBURDENED`** needs its own rule, since no substitute survives that compound.
- **Article agreement needs its own rules.** "a charm" → "**an** emblem", "a Pantheon" → "**an**
  Ascent", "An Arcane Egg" → "**A** Primal Egg". These are longer keys, so longest-first applies
  them before the bare word rule."""

ROADMAP = """## 5. Roadmap

The scheme covers **divine framing** and **magic**. Three workstreams remain, to be done in this
order. They are largely independent — the charm problem is *not* a subset of the dream problem.

### 5.1 SOUL → SPARK  *(first)*

135 word-instances across ~104 entries: `SOUL` 53, `Soul` 38, `soul` 31, `souls` 8, `Kingsoul` 2,
`Worldsoul` 1, `Souls` 1, `Soulful` 1.

**Decided: `SOUL` → `SPARK`.** It was the only candidate where every compound falls out naturally —
*Spark Catcher*, *Spark Eater*, **Kingspark**, **Worldspark**, *Shade Spark*, *Spark Master* — and
SOUL is rendered as white light in-game, so it fits visually. *Ember* was too fiery and collided
with Grimm's flame; *Lumen* was already crowded by the Luminaries scheme.

Beyond the rename:

- **`Sanctum` must change too**, keeping the alliteration: *Soul Sanctum* → **Spark Spire**
  (it is a tower in the City of Tears, so *spire* is also literally accurate).
- **Drawing SPARK from living creatures** — *Soul Eater*: "used to draw SOUL from **still-living
  creatures**" — is to be judged **case by case, not removed wholesale**. Taking something from a
  living creature is not inherently objectionable; blood is taken from the living too.
- `Soul Master` / `Soul Twister` / `Soul Warrior` (enemies) and the *Soul & Shade* achievement
  follow the rename automatically.

### 5.2 Charms  *(second)*

86 entries — a core UI mechanic: charm names, 40+ descriptions, notches, menus.

The concern is the word and the concept: a *charm* is an object worn for magical protection, i.e.
an amulet. This is **independent of dreams** — only 4 of 45 charms touch dream content at all
(*Dream Wielder*, *Dreamshield*, the *Kingsoul → Void Heart* chain, and *Grimmchild*'s "flame in
dream").

> **Solved approach:** term replacement is a plain substring `String.Replace` with no word
> boundaries, and there are **4 occurrences of "charming"** (Grimm's "A charming performance… a
> pleasure!", the Snail Adept's "Aren't you the charming one"). Those four get **exact overrides**
> so a `charm → …` rule cannot corrupt them into "cresting".

### 5.3 Dreams and the dead  *(third — largest, most entangled)*

~131 entries plus the 272-entry `Enemy Dreams` sheet. Forms: `dreams` 49, `Dream` 43, `dream` 31,
`dreaming` 7, `Dreams` 7, `Dreamborn` 7, `Dreamgate` 6, `dreamed` 5, `Dreamers` 5, `Dreamshield` 1.

**`dream` cannot be a single term rule.** It splits three ways:

1. **Aspiration, and the lore about the dead** — the leading candidates are `hope` and `memory`.
   *memory* is theologically tighter ("memories take the shape of those who have passed away" is
   unambiguously not the person) and the game already glosses it that way itself: the Seer says
   "This kingdom is full of **old memories**… Seek them out, reveal them, and gather Essence."
   *hope* reads better in some names. **Undecided** — "Hope Nail" sounds better than "Memory Nail",
   so the two may not resolve to the same word everywhere.
2. **Ordinary sleeping** — "Troubled dreams beset the maiden", "In my dreams I could see it".
   Neither *hope* nor *memory* fits. Leave, or reword individually.
3. **Proper nouns**, decided one at a time — Dream Nail, Dreamgate, Dreamers, Dreamshield,
   Dream Wielder, Dreamborn. `Dreamers` → **`Sleepers`** is a natural fit, since Monomon, Lurien
   and Herrah literally sleep.

**The game's own text supports the framing.** `WITCH_HINT_XERO`: "Sometimes **dreams take the shape
of** those who have passed away." The lore already says these are dreams shaped like the dead, not
the dead persisting — so the work is mostly vocabulary layered on top of that.

**Decided within this workstream:**

- **`ghost`, `spirit` and `wraith` change.** Note *Howling Wraiths* is a spell name, and Hornet
  calls the player character "**Ghost** of Hallownest".
- **`Shade` stays.** It reads as *shadow*, and that iconography is central to the Knight and to the
  game's lore. This covers *Shade Cloak*, *Lord of Shades*, and the death mechanic.
- **`Essence`** (49) is in scope for review — "fragments of light that dreams are made of",
  gathered from the dreams of the dead.
- The achievements *Ascension*, *Awakening* and *Attunement* are all Essence/Dream Nail milestones,
  so they resolve with this workstream.

### 5.4 Deliberately out of scope

- **The Soul Master's immortality claim** — "he robbed me of my immortality… I will live forever" —
  is villainous delusion, and the story frames it as madness. Kept.

### 5.5 Scope limit to keep in mind

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

    # Substring corruption: a rule key sitting inside a longer word, with no longer rule and no
    # exact override to protect it. This is how "melancholy" once became "melancluminous".
    substring = []
    for key in T:
        if " " in key:
            continue
        pat = re.compile(r"[A-Za-z]*" + re.escape(key) + r"[A-Za-z]*")
        for r in rows:
            sheet, k2 = r[0], r[1]
            if f"{sheet}|{k2}" in E:
                continue
            for m in pat.finditer("\t".join(r[2:])):
                w = m.group()
                if w == key or any(o != key and o in w and len(o) > len(key) for o in T):
                    continue
                substring.append((f"{sheet}|{k2}", key, w))

    # Article agreement introduced by the rewrite ("a emblem", "An Primal").
    art = re.compile(r"\b[Aa] (?=[aeiouAEIOU])[A-Za-z]+|\b[Aa]n (?=[^aeiouAEIOU\W])[A-Za-z]+")
    articles = []
    for sheet, key, kind, o, r in changed:
        before = set(art.findall(o))
        for gmatch in art.findall(r):
            if gmatch not in before:
                articles.append((f"{sheet}|{key}", gmatch))

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
| **`charming`** | the ordinary adjective, unrelated to amulets — kept in all 4 places via exact overrides, so the `charm` rule cannot corrupt it into "embleming" |
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
- **{len(substring)}** substring corruptions (a rule firing inside a longer word — this is how
  *melancholy* once became *melancluminous*, and it is why `charming`, `Charmed` and `spellcaster`
  are exact overrides){chr(10) + "  " + chr(10).join(f"  - `{a}` -> {b!r} inside {c!r}" for a, b, c in substring[:10]) if substring else ""}
- **{len(articles)}** article-agreement errors introduced ("a emblem", "An Primal")
{chr(10).join(f"  - `{a}`: {b!r}" for a, b in articles[:10]) if articles else ""}
""")
    open(OUT, "w", encoding="utf-8").write("\n".join(o))
    print(f"REWORDS.md: {len(changed)} changed / {total} entries, {len(T)} terms, {len(E)} overrides, {len(cascades)} cascades")


if __name__ == "__main__":
    main()
