# Halallow Knight — a halal / Muslim-friendly Hollow Knight mod

A client-side [Hollow Knight](https://hollowknight.com) mod that removes the game's religious and
supernatural framing — gods, worship, prayer, idols, magic, spells, souls, charms and the depiction
of the dead — by rewording the text into neutral alternatives.

It changes **words only**. Every boss, bug, item, area, ability and piece of geo is exactly as Team
Cherry made them. Nothing about how the game plays is touched, and no game files are modified.

**Who this is for.** It was built from an Islamic perspective, by a Muslim player who wanted to
play Hollow Knight without its shirk and its magic framing. But nothing about it is faith-specific:
if you would rather play without gods, worship, magic or necromancy in the text for any reason —
religious, parental, or simply personal taste — it does the same job. The wording is also
[yours to change](#using-your-own-wording): it is plain JSON, no rebuild required.

> Looking to remove the **music** as well? See
> **[Halallow Knight Music Remover](https://github.com/akhihaani/Halallow-Knight-Music-Remover)**.

## What it changes

Six areas, **539 of the game's 4,089 text entries**:

| | |
|---|---|
| **Divine framing** | gods, worship, prayer, idols, shrines, temples, blessings, blasphemy. *Higher beings* become **luminaries**, *Godhome* becomes **Luminance**, the *Pantheons* become the **Ascents**. |
| **Magic** | spells, shamans, conjuring, enchantment, hexes, the arcane. *Spells* become **skills**, the *Shaman* becomes the **Adept**. |
| **SOUL** | the game's core resource becomes **SPARK**. *Soul Catcher* → *Spark Catcher*, *Kingsoul* → *Kingspark*, *Soul Sanctum* → *Spark Spire*. |
| **Charms** | become **emblems**, since a charm is an object worn for magical protection. *Charm Notch* → *Emblem Notch*. |
| **Dreams and the dead** | the dream-realm becomes **memory**, the lingering dead become **echoes**, and the *Dream Nail* becomes the **Echo Nail**. *Dreamers* become **Sleepers**. Ghosts, spirits and wraiths are renamed. |
| **Fate** | lines that claim to *know* the future, hold power over it, or dismiss it. Believing in fate is left alone; only claiming mastery of it is changed. |

The remaining 3,550 entries are untouched, and a great deal was left alone **deliberately** —
ordinary sleeping and dreaming, *faith* meaning trust, *spirit* meaning courage, `Shade` for its
shadow imagery. Where a word had several senses, each was judged separately rather than swapped
wholesale.

> **[REWORDS.md](REWORDS.md) documents every single change**, with before-and-after text, the
> reasoning behind the non-obvious choices, and everything deliberately left vanilla and why. If
> you want to know exactly what this does to your game before installing it, read that.

Some examples:

```
"Higher beings, these words are for you alone."
→ "Luminaries, these words are for you alone."

"Spells will deplete SOUL. Replenish SOUL by striking enemies."
→ "Skills will deplete SPARK. Replenish SPARK by striking enemies."

"Lingering dream of a fallen warrior."
→ "Lingering echo of a fallen warrior."

"Ghost of Hallownest, you possess the strength to enact an end of your choosing."
→ "Shadow of Hallownest, you possess the strength to enact an end of your choosing."
```

The wording is one person's choices, not a fixed requirement of the mod. If you want different
words, [swap them](#using-your-own-wording) — no rebuild needed.

## Frequently asked

**Is there a halal mod for Hollow Knight?**
Yes — this one. It rewords the game's divine framing, magic, souls, charms, dreams and the dead
into neutral language, without changing how the game plays.

**Does it remove the gods from Hollow Knight?**
It removes the *framing* of them as gods. Godhome becomes Luminance, the Pantheons become the
Ascents, the Godseeker becomes the Lightseeker, and "higher beings" become "luminaries". The bosses
themselves are untouched — this is a text mod, not a gameplay mod.

**Does it remove magic and spells?**
The wording, yes. Spells become skills, the Shaman becomes the Adept, and conjuring, hexes,
enchantment and the arcane are all reworded. The abilities still work exactly as before.

**What about SOUL, charms and the Dream Nail?**
SOUL becomes SPARK, charms become emblems, and the Dream Nail becomes the Echo Nail. The dream
realm becomes memory and the lingering dead become echoes.

**Does it remove the music?**
Not this mod — music is handled by the separate
[Music Remover](https://github.com/akhihaani/Halallow-Knight-Music-Remover).

**Is it haram to play Hollow Knight?**
That is not a question a README can answer, and this mod does not claim to settle it. What it does
is remove a specific and well-defined set of things from the game's text, all of them listed in
[REWORDS.md](REWORDS.md), so you can judge for yourself what remains.

**Does it work with other mods, and with multiplayer?**
Yes. It hooks a single localisation call and nothing else, so it has almost no surface to conflict
with. The reworded text is local to you, so other players see their own game unchanged.

**Can I change the wording?**
Yes, and you do not need to rebuild anything. See [Using your own wording](#using-your-own-wording).

## Companion mod: Music Remover

**[Halallow Knight Music Remover](https://github.com/akhihaani/Halallow-Knight-Music-Remover)**
removes the game's music while keeping sound effects and atmosphere. It lives in its own
repository, and is a **separate mod on purpose** — this mod hooks
the localisation call and nothing else, and that restraint is what makes it conflict-free. Audio
work needs deeper hooks, so it is kept apart. Install either, or both.

## How it works

Hollow Knight routes essentially all player-facing text — lore tablets, boss titles, area names,
menus, item descriptions — through a single localisation lookup. Halallow Knight hooks that one
call and returns replacement strings.

That's the entire mod. It hooks **nothing else**: no gameplay logic, no scenes, no entities, no
PlayMaker/FSM graphs, and no game files or assets are modified on disk. Everything happens at
runtime, in memory, on your machine only.

Three consequences worth knowing:

- **It plays well with other mods.** Altering nothing but locally displayed text leaves almost no
  surface to conflict with. That includes multiplayer mods — the reworded text is local to you, so
  other players are unaffected and nothing changes on the wire.
- **It's trivially reversible.** Disable or delete it and the text is vanilla again. Your saves are
  never touched.
- **It cannot change mechanics.** Renaming the Dream Nail to the Echo Nail does not stop it
  entering dreams; renaming charms does not change what equipping them does. This is a change of
  words, and only words.

## Requirements

- **Hollow Knight on PC** (Steam or GOG) — Windows, macOS or Linux. Consoles can't be modded.
- **Game version 1.5.78.11833.** The current Steam default branch is a Unity 6 rebuild that the
  Modding API does not support. Downpatch via **Steam → Hollow Knight → Properties → Betas →
  `1.5.78.11833`**.
- **The Hollow Knight Modding API**, easiest via [Lumafly](https://themulhima.github.io/Lumafly/).

Support for the newer game build is planned once the Modding API supports it.

## Installing

Drop the `HalallowKnight/` folder into your game's `Mods` folder. The same DLL works on all three
platforms.

| OS | `Mods` folder, under `.../steamapps/common/Hollow Knight/` |
|---|---|
| Windows | `hollow_knight_Data\Managed\Mods\` |
| Linux | `hollow_knight_Data/Managed/Mods/` |
| macOS | `hollow_knight.app/Contents/Resources/Data/Managed/Mods/` |

Lumafly's **manual install** button does this for you on any OS.

The folder needs `HalallowKnight.dll` and `reword-config.json` together — the DLL alone changes
nothing, since all the wording lives in the JSON. If it loaded, the mod's name and version appear
in the top-left of the title screen.

The version shown comes from the **config**, not the DLL, so editing the wording is enough to bump
it. That is how you confirm at a glance that the game picked up the version you meant.

**Back up your saves before first run**, as with any mod. They live in
`.../unity.Team Cherry.Hollow Knight/` (`%APPDATA%` on Windows, `~/Library/Application Support/`
on macOS, `~/.config/` on Linux).

## Using your own wording

Everything the mod says lives in `reword-config.json` next to the DLL. **It's plain JSON — edit it
and restart the game. No rebuild, no toolchain.**

```json
{
  "dumpMode": false,
  "dumpAll": false,

  "exactOverrides": {
    "Titles|GODHOME_MAIN": "Luminance"
  },

  "termReplacements": {
    "Higher beings": "Luminaries",
    "Godhome": "Luminance"
  }
}
```

- **`termReplacements`** find-and-replace on the original text wherever it appears. Convenient, but
  they hit *every* string containing the term.
- **`exactOverrides`** replace one specific entry outright, keyed by `sheet|key`. Precise, with no
  collateral — use these for names, titles, and any line where a blanket rule would read badly.

Two rules govern them:

1. An exact override **always wins** over term replacements for that entry — and it **bypasses them
   entirely**, so an override must be written with all your other wording already applied.
2. Longer terms are applied **first**, so `Godhome` is matched before the `god` inside it.

### Finding the text to change

Set `"dumpAll": true` and launch once. The mod writes **every** entry the game has loaded to
`language-dump-all.tsv` beside the DLL, so you don't have to reach an area to see its text:

```
sheet <TAB> key <TAB> original text
```

`"dumpMode": true` is the incremental alternative — it changes nothing and records entries as the
game asks for them, which is useful for finding which key a particular line belongs to. Both are
off in the shipped config.

### Two traps worth knowing

Both of these have caused real bugs in this mod, and both are now checked automatically:

- **Substring corruption.** Replacement is plain `String.Replace` with no word boundaries, so a
  rule can fire inside a longer word. A `holy → luminous` rule turns *melancholy* into
  *melancluminous*. Protect such words with an exact override.
- **Stale overrides.** An override written before a later rule exists can never be reached by that
  rule, so renames silently skip it. After any rename, sweep the override texts too.

## Building from source

Requires a [.NET SDK](https://dotnet.microsoft.com/download). Mono is not needed.

```bash
cd src/HalallowKnight
dotnet build -c Release
```

The build locates your game automatically in the usual Steam, GOG and Flatpak locations. If it
can't find it, point it at the folder yourself:

```bash
dotnet build -c Release -p:HkManaged="/path/to/Hollow Knight/.../Managed"
```

Output is `bin/Release/HalallowKnight.dll`. It references the game's assemblies but bundles none of
them, so nothing proprietary is redistributed.

## Verification

Every change is checked by simulating the mod's own replacement engine over a full dump of the
game's text, before anything ships:

```bash
python3 tools/gen_rewords.py [path/to/language-dump-all.tsv]
```

This regenerates REWORDS.md and reports the entry count alongside four checks, all of which must be
zero: replacement cascades, substring corruptions, article-agreement errors (`a emblem`,
`An Primal`), and stale overrides.

**That check has a limit worth understanding.** It reads the language *files*, which proves a
string exists but not that the game ever asks for it through the call this mod hooks. Hollow
Knight's **achievement names come from Steam**, not the language files, so 25 otherwise-correct
rules can never fire. They are kept in the config, and excluded from the count above.

To find any other such gaps, record what the game really requests and compare:

```bash
# set "dumpMode": true, play for a while, then:
python3 tools/check_coverage.py [path/to/language-dump.tsv]
```

Neither dump is committed — they are Team Cherry's text, not ours. Produce your own with
`"dumpAll": true` or `"dumpMode": true` as above.

## Repository layout

```
src/HalallowKnight/
  HalallowKnight.cs        hook, dump mode, replacement engine
  HalallowKnight.csproj    net472 build, cross-platform game detection
  reword-config.json       the shipped wording
tools/
  gen_rewords.py           regenerates REWORDS.md and runs the verification checks
  check_coverage.py        compares the config against text the game actually requests
REWORDS.md                 every change, and everything left alone, with reasoning
```

## Getting it into Lumafly

Lumafly's searchable mod list is driven by **ModLinks** — a single `ModLinks.xml` in the
[hk-modding/modlinks](https://github.com/hk-modding/modlinks) repository, listing every mod with
its download URL and a SHA256 of the release asset. Lumafly downloads that file on startup, which
is how it knows what exists. Getting listed means opening a pull request adding one `<Manifest>`
block.

A ready-to-submit entry lives in [docs/modlinks-entry.xml](docs/modlinks-entry.xml).

**The checksum must match the release asset exactly**, or Lumafly refuses the download. After
cutting any new release, regenerate it:

```bash
shasum -a 256 dist/HalallowKnight-<version>.zip | awk '{print toupper($1)}'
```

and open another pull request updating `<Version>` and `SHA256`. That is the ongoing cost of being
listed: every release needs a modlinks PR, or Lumafly keeps serving the old one.

## Credits

Hollow Knight is by [Team Cherry](https://teamcherry.com.au). This mod contains none of their code
or assets — only a list of words, applied at runtime on your own machine.
