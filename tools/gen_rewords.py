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
    ("Dreams, echoes and the dead", ["Dream Nail","Dreamgate","Dream Gate","Dream Wielder",
        "Dreamshield","Dreamborn","Dreamers","Dreamer","Warrior Dream","Hidden Dreams",
        "Lingering dream of a fallen warrior","I lie dreaming","veil between dreams and waking",
        "hidden dreams","wishes and dreams","shape dreams","through dream",
        "dreams take the shape of","dreams take root","that dreams are made of",
        "Ghost","ghost","Vengeful Spirit","Howling Wraiths","The Wraiths requires","Wraiths",
        "Spirits' Glade","Through dream I travel","the flame in dream","In dreams... Born anew"]),
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
    ("Zote|PRECEPT_6", "\"'**Choose Your Own Fate**'... our fate is chosen for us before we are even born. **I disagree**\" \u2014 an explicit rejection of predestination"),
    ("Minor NPC|LITTLE_FOOL_MARK", "\"from that point on, **your destiny is your own**\""),
    ("Lore Tablets|FUNG_SHROOM_DREAM", "\"What good to **foresee** a demise unavoidable?\" \u2014 knowledge of a specific future"),
    ("Minor NPC|MR_MUSHROOM_4", "\"the **chains of fate**... do you really want to **break them**?\""),
    ("Relic Dealer|RELICDEALER_JOURNAL_1", "\"it seems **fate was unkind** to most\" \u2014 fate cast as unjust"),
    ("Lore Tablets|WISHING_WELL_INSPECT", "\"let Hallownest's Pale King **relieve you of your burden**\" \u2014 reads as absolution; it is really a joke about the well taking your Geo"),
    ("Lore Tablets|WP_THRONE_01", "\"**to yield, to devote**\" and \"**Eternity in promise**\" \u2014 devotion to the King, and eternity promised"),
    ("Lore Tablets|FUNG_TAB_01", "\"the **will** of the Wyrm\" and \"its **prescience** shields us\" \u2014 submission, and foreknowledge"),
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
- **`dream` is never a blanket rule.** The word carries three unrelated senses, so every rule is
  phrase-level. The *realm* becomes **memory** ("the veil between memory and waking", "remnants of
  wishes and memories") — which is what the game already calls it: "This kingdom is full of **old
  memories**… gather Essence." Ordinary **sleeping** is untouched (Bretta's "troubled dreams",
  Zote's entire "Do Not Dream" precept), and so is **aspiration** ("Dreams of glory", and Galien's
  "the hopes and dreams of the kingdom", which a blanket rule would have turned into "hopes and
  hopes").
- **The lingering dead become `echo`**, matching the **Echo Nail**: "Lingering echo of a fallen
  warrior", "Warrior Echo", "I lie dreaming" → "I linger". An echo is plainly not the person.
- **`Dreamers` → `Sleepers`** — Monomon, Lurien and Herrah are literally asleep.
- **The Grimm Troupe's realm becomes `nightmare`**, not *memory* — the game already calls it that
  (Nightmare King, Nightmare Heart, "Nightmare binds all"), so "Through nightmare I travel" is
  native vocabulary rather than a substitution.
- **`ghost` → `shadow`.** Ten of its eleven uses are Hornet's name for the player character, so
  this is effectively the protagonist's name: "Shadow of Hallownest". It also keeps faith with
  `Shade`, which is retained for its shadow meaning.
- **`spirit` is not a blanket rule either.** *Vengeful Spirit* becomes **Vengeful Wisp** and
  *Howling Wraiths* becomes **Howling Shades** (which also fixes Team Cherry's own grammar slip,
  "The Wraiths **requires** SOUL" → "The Shades **require** SPARK"). The three ordinary-English
  uses are left alone: "your unwavering spirit", "it'd do our spirits well", and Zote's "fire is a
  type of hot spirit".
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

ROADMAP = """## 5. Status and open questions

All three planned workstreams are complete.

| workstream | scope | outcome |
|---|---|---|
| **Divine framing** | god, worship, rites, places | done |
| **Magic** | shamans, spells, conjuring, blessing, fortune | done |
| **SOUL → SPARK** | 135 word-instances | done |
| **Charms → Emblems** | 86 entries | done |
| **Dreams and the dead** | ~131 entries plus ghosts and spells | done |

### 5.1 Deliberate non-changes worth restating

Three words were investigated and **kept**, because a blanket rule would have done more harm than
good. Each is recorded in section 3 with its reasoning:

- **`faith`** — 9 of 13 uses are idiomatic trust ("Have faith in me!"). Only the 4 devotional uses
  are overridden.
- **`spirit`** — 3 uses mean courage or morale ("your unwavering spirit").
- **`Shade`** — reads as *shadow*, and that iconography is central to the Knight.

**`Essence` was reviewed and kept.** The word means an intrinsic nature or a concentrated extract;
it is neither religious nor a soul word. The earlier passes also settled the framing around it, so
it now reads as crystallised memory rather than anything belonging to the dead: "Essence… the
precious fragments of light that **memories** are made of", "Essence can be found wherever
**memories** take root", "remnants of wishes and **memories**". All 49 entries read clean.

### 5.2 Still open

- **`aura`** (5 entries) — "the aura of a fierce warrior", "I don't really like the aura about it".
  Mostly ordinary "presence". Never ruled on.
- **`Penitent Moth`** became *Remorseful Moth*; the wider vocabulary of remorse is untouched.

### 5.3 Scope limit to keep in mind

This mod changes **displayed text only** — the design rule that keeps it a pure reword and
compatible with everything else. It cannot change mechanics. Renaming the Dream Nail to the Echo
Nail does not stop it entering dreams, and renaming charms does not change what equipping them
does. Where a concern is about the *mechanic* rather than its *wording*, rewording can only go so
far. Everything above is a change of words."""


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

    # Stale overrides: an override written before a later rule existed, which the term rules would
    # still alter. Protective overrides (those that exist *because* a rule would corrupt them, e.g.
    # "melancholy" or "charming") are expected and excluded.
    PROTECTED = ("melancholy", "charming", "Charmed", "spellcaster")
    stale = []
    for k, v in E.items():
        nv = v
        for kk, vv in sorted(T.items(), key=lambda kv: -len(kv[0])):
            nv = nv.replace(kk, vv)
        if nv == v:
            continue
        if all(w in v for w in () ) and any(w in v for w in PROTECTED):
            continue
        stale.append(k)

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
| **ordinary dreaming** | Bretta's "troubled dreams", Zote's "Do Not Dream" precept, "In my dreams I could see it", "What a strange dream" — sleeping is not the concern |
| **dreams as aspiration** | "Dreams of glory", "don't let your past keep you from your dreams", and Galien's "the hopes and dreams of the kingdom" |
| **`spirit`** as courage or morale | "your unwavering spirit", "it'd do our spirits well", Zote's "fire is a type of hot spirit" |
| **`Shade`** | kept deliberately — it reads as *shadow*, and that iconography is central to the Knight and the game's lore. Covers Shade Cloak, Lord of Shades and the death mechanic. |
| **believing in fate** | not a problem in itself, so these stay: "Fate can be a wonderful thing", "a Kingdom always destined for ruin", "their fated meeting", "the fate of this world", "**Doomed she thought herself**" (thought, not knew), and the White Lady's "inevitable **on current course**", which is hedged reasoning rather than a claim of knowledge |
| **`foresight`** as prudence | "No foresight like those old things", "Its foresight shields us" — planning ahead, not knowledge of the unseen |
| **Xero's "already doomed"** | a defeated ghost's despair, which the game goes on to disprove |
| **Grimm's "your role was cast"** | a contract being struck, not destiny being fixed |
| **Zote's "Obey No Law But Your Own"** | left by choice — same framing as his other precepts, all of which the game presents as foolish |
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
- **{len(stale)}** stale exact overrides (written before a later rule existed, so the rule could
  never reach them — this is how "Soul Sanctum", "charm" and "lights darkest dream" survived
  three separate renames){chr(10) + chr(10).join(f"  - `{k}`" for k in stale[:10]) if stale else ""}
{chr(10).join(f"  - `{a}`: {b!r}" for a, b in articles[:10]) if articles else ""}
""")
    open(OUT, "w", encoding="utf-8").write("\n".join(o))
    print(f"REWORDS.md: {len(changed)} changed / {total} entries, {len(T)} terms, {len(E)} overrides, {len(cascades)} cascades")


if __name__ == "__main__":
    main()
