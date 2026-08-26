# Halallow Knight

A client-side [Hollow Knight](https://hollowknight.com) mod that rewords divine and
"higher being" framing in the game's text into neutral alternatives.

It changes **words only**. Bosses, bugs, items, geo, charms, enemies and every other part of the
game are exactly as Team Cherry made them — the mod never touches gameplay.

> **Status:** working, but shipped with an empty replacement list. Out of the box it runs in
> *dump mode*, which records the game's text so you can decide what to reword. See
> [Configuring](#configuring).

## How it works

Hollow Knight routes essentially all player-facing text — lore tablets, boss titles, area names,
menus, dream dialogue — through a single localisation lookup. Halallow Knight hooks that one call
and returns replacement strings.

That's the entire mod. It hooks **nothing else**: no gameplay logic, no scenes, no entities, no
PlayMaker/FSM graphs, no game files or assets are modified on disk. Everything happens at runtime,
in memory, on your machine only.

Two useful consequences:

- **It plays well with other mods.** Since it alters nothing but locally displayed text, it has
  essentially no surface to conflict with. That includes multiplayer mods — reworded text is local
  to you, so other players are unaffected and nothing changes on the wire.
- **It's trivially reversible.** Disable or delete it and the text is vanilla again.

## Requirements

- **Hollow Knight on PC** (Steam or GOG) — Windows, macOS or Linux. Consoles can't be modded.
- **Game version 1.5.78.11833.** The current Steam default branch is a Unity 6 rebuild that the
  Modding API does not support. Downpatch via **Steam → Hollow Knight → Properties → Betas →
  `1.5.78.11833`**.
- **The Hollow Knight Modding API**, easiest via [Lumafly](https://themulhima.github.io/Lumafly/).

Support for the newer game build is planned once the Modding API supports it.

## Installing

Download the release folder (or build it yourself, below) and drop `HalallowKnight/` into your
game's `Mods` folder. The same DLL works on all three platforms.

| OS | `Mods` folder, under `.../steamapps/common/Hollow Knight/` |
|---|---|
| Windows | `hollow_knight_Data\Managed\Mods\` |
| Linux | `hollow_knight_Data/Managed/Mods/` |
| macOS | `hollow_knight.app/Contents/Resources/Data/Managed/Mods/` |

Lumafly's **manual install** button does this for you on any OS.

The folder should contain `HalallowKnight.dll` and `reword-config.json`. If it loaded, the mod's
name and version appear in the top-left of the title screen.

**Back up your saves before first run.** They live in `.../unity.Team Cherry.Hollow Knight/`
(`%APPDATA%` on Windows, `~/Library/Application Support/` on macOS, `~/.config/` on Linux).

## Configuring

All configuration is `reword-config.json`, next to the DLL.

### 1. Find the text you want to change

Ship default is `"dumpMode": true`. In this mode the mod **changes nothing** and instead records
every unique piece of text the game asks for, into `language-dump.tsv` beside the DLL:

```
sheet <TAB> key <TAB> original text
```

Play through the content you care about — the file fills as you go. Each entry is recorded once.

Setting `"dumpAll": true` instead writes **every** entry the game has loaded to
`language-dump-all.tsv` in one go, so you don't have to reach a given area to see its text. It runs
once per launch and is off by default.

### 2. Write your replacements

Turn dump mode off and fill in either or both maps:

```json
{
  "dumpMode": false,

  "exactOverrides": {
    "Titles|SOME_KEY": "Your exact replacement text"
  },

  "termReplacements": {
    "Higher Beings": "great ones",
    "Higher Being": "great one"
  }
}
```

- **`exactOverrides`** replace one specific entry outright, keyed by `sheet|key` straight from your
  dump. Precise, with no collateral — best for names and titles.
- **`termReplacements`** do a find-and-replace on the original text wherever it appears. Convenient,
  but they hit every string containing the term, so use them deliberately.

Rules: an exact override always wins over term replacements for the same entry, and longer terms
are applied first, so `"Higher Being"` is matched before a shorter `"Being"` inside it.

Restart the game to apply changes.

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

## What it changes

**[REWORDS.md](REWORDS.md) documents every single change** — each term replacement, each
individually rewritten line with its before-and-after, the reasoning behind the non-obvious
choices, and, just as importantly, everything that was deliberately **left alone** and why.
If you want to know exactly what this mod does to your game before installing it, read that.

The shipped wording recasts divine authority as light and brilliance rather than godhood:

| | |
|---|---|
| *higher beings* | *luminaries* |
| *Godhome* | *Luminance* |
| *the Pantheons* | *the Ascents* |
| *Godseeker* | *Lightseeker* |
| *Spell* | *Skill* |
| *King's Idol* | *King's Effigy* |

> *"**Higher beings**, these words are for you alone."* → *"**Luminaries**, these words are for you alone."*

**465 of the game's 4,089 text entries are altered**; the other 3,624 are untouched. The scheme
currently covers divine framing and magic. Charms, dreams and the depiction of the dead are noted
as future work in REWORDS.md.

Every release is verified by simulating the replacement engine over a full dump of the game's text,
checking that no target word survives unintentionally and that no replacement rule corrupts
another's output.

## Repository layout

```
src/HalallowKnight/
  HalallowKnight.cs        the mod: hook, dump mode, replacement engine
  HalallowKnight.csproj    net472 build, cross-platform game detection
  reword-config.json       the shipped replacement list
tools/
  gen_rewords.py           regenerates REWORDS.md from the config, with verification
REWORDS.md                 every change, and what was left alone
```

## Contributing a different wording

The replacement list is just JSON — you do not need to rebuild the mod to change it. Edit
`reword-config.json` in your installed `Mods/HalallowKnight/` folder and restart the game.

If you are changing the list in the repo, run `python3 tools/gen_rewords.py` afterwards to
regenerate REWORDS.md. It applies the mod's own algorithm to a full language dump and reports the
entry count, cascade check and override count, so the document cannot drift from the config.
