# Reworded text

Every change Halallow Knight makes, and every deliberate decision *not* to change something.
Generated against Hollow Knight **1.5.78.11833** — 4,089 localisation entries, of which
**465 are altered** and 3,624 are untouched.

*This file is generated. Run `python3 tools/gen_rewords.py` after editing the config.*

The wording scheme is **Luminaries**: divine authority is recast as light and brilliance rather
than godhood, keeping Hollow Knight's register intact.

---

## 1. Term replacements

Applied to the original string wherever they appear. Longer keys always match first, so compounds
like `Godhome` are handled before the bare `god` inside them.

### Core god vocabulary

| original | becomes |
|---|---|
| `God of Gods` | `Light of Lights` |
| `Higher beings` | `Luminaries` |
| `higher beings` | `luminaries` |
| `Higher being` | `Luminary` |
| `higher being` | `luminary` |
| `Godseekers` | `Lightseekers` |
| `Godseeker` | `Lightseeker` |
| `Godmaster` | `Lightmaster` |
| `Godtuner` | `Attuner` |
| `Godhome` | `Luminance` |
| `godliness` | `brilliance` |
| `godless` | `lightless` |
| `Godly` | `Luminous` |
| `godly` | `luminous` |
| `Gods` | `Luminaries` |
| `gods` | `luminaries` |
| `God` | `Luminary` |
| `god` | `luminary` |
| `Pantheons` | `Ascents` |
| `pantheons` | `ascents` |
| `PANTHEON` | `ASCENT` |
| `Pantheon` | `Ascent` |
| `pantheon` | `ascent` |

### Religious vocabulary

| original | becomes |
|---|---|
| `Worshippers` | `Followers` |
| `worshippers` | `followers` |
| `worshipped` | `honoured` |
| `deified` | `honoured` |
| `Sacred` | `Cherished` |
| `sacred` | `cherished` |
| `Holy` | `Luminous` |
| `holy` | `luminous` |
| `Divine` | `Sublime` |
| `divine` | `sublime` |
| `deity` | `luminary` |
| `Prayer` | `Invocation` |
| `prayers` | `invocations` |
| `Blasphemy` | `Insolence` |
| `blasphemy` | `insolence` |
| `blasphemies` | `insolences` |
| `heretic` | `outcast` |

### Rites, objects and places

| original | becomes |
|---|---|
| `rituals` | `performances` |
| `Ritual` | `Performance` |
| `ritual` | `performance` |
| `idols` | `effigies` |
| `Idol` | `Effigy` |
| `idol` | `effigy` |
| `Shrine` | `Memorial` |
| `shrines` | `memorials` |
| `shrine` | `memorial` |
| `Temples` | `Vaults` |
| `temples` | `vaults` |
| `Temple` | `Vault` |
| `temple` | `vault` |
| `Penitent` | `Remorseful` |

### Magic and its practitioners

| original | becomes |
|---|---|
| `shamans` | `adepts` |
| `Shaman` | `Adept` |
| `shaman` | `adept` |
| `Spells` | `Skills` |
| `spells` | `skills` |
| `Spell` | `Skill` |
| `spell` | `skill` |
| `Conjures` | `Forms` |
| `Conjure` | `Form` |
| `conjures` | `forms` |
| `conjured` | `formed` |
| `conjure` | `form` |
| `Arcane` | `Primal` |
| `arcane` | `hidden` |
| `Hex` | `Vex` |
| `mystical` | `curious` |
| `Enchanting` | `Captivating` |
| `Enchanted` | `Adorned` |
| `Prophet` | `Speaker` |

### SOUL, charms and articles

| original | becomes |
|---|---|
| `Worldsoul` | `Worldspark` |
| `Kingsoul` | `Kingspark` |
| `Soulful` | `Brimming` |
| `Sanctum` | `Spire` |
| `sanctum` | `spire` |
| `SOULS` | `SPARKS` |
| `SOUL` | `SPARK` |
| `Souls` | `Sparks` |
| `souls` | `sparks` |
| `Soul` | `Spark` |
| `soul` | `spark` |
| `OVERCHARMED` | `OVERBURDENED` |
| `CHARMS` | `EMBLEMS` |
| `Charms` | `Emblems` |
| `charms` | `emblems` |
| `Charm` | `Emblem` |
| `charm` | `emblem` |
| `a charm` | `an emblem` |
| `A charm` | `An emblem` |
| `a Charm` | `an Emblem` |
| `A Charm` | `An Emblem` |
| `a Pantheon` | `an Ascent` |
| `A Pantheon` | `An Ascent` |
| `a pantheon` | `an ascent` |
| `An Arcane` | `A Primal` |
| `an Arcane` | `a Primal` |

### Blessing and fortune

| original | becomes |
|---|---|
| `Blessings` | `Boons` |
| `Blessing` | `Boon` |
| `blessings` | `boons` |
| `blessing` | `boon` |
| `Blessed` | `Favoured` |
| `blessed` | `favoured` |
| ` by fortune` | ` by chance` |

**Notes on specific choices**

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
  them before the bare word rule.

---

## 2. Exact overrides

67 entries are replaced outright rather than word-by-word, because a term rule would have
been wrong or clumsy. **Exact overrides bypass term replacements entirely**, so each is written
with all other rewording already applied.

| entry | why |
|---|---|
| `CP3\|GODSEEKER_ENGINE` | "We **pray** that the Gods…" — *pray* meaning *beseech*, not the act of prayer |
| `CP3\|GODSEEKER_ENGINE_PRIME` | same *pray* sense, plus "God of Gods" and two bare "God"s |
| `CP3\|GODSEEKER_ENGINE_3` | "Through **ritual** combat" — *performance combat* is not grammatical |
| `CP3\|PANTHEON_ENTER_3` | "**Pray** will We, Attune will We" — capitalised *Pray*, which must survive elsewhere |
| `Elderbug\|ELDERBUG_TEMPLE_VISITED` | "went there to **pray**" — the literal act, needing a different word |
| `Journal\|NOTE_MAGE_LORD` | "tricks and **rituals** and **prayers**" |
| `Minor NPC\|TUK_DREAM` | "keep searching… and **praying**" |
| `Jiji\|RITUAL_BEGIN` | a summoning, not a show — *"we will begin the performance"* would be wrong |
| `Stag\|STAG_RESTINGGROUNDS` | funeral rites, and the original had **the dead acting** — agency moved back to the living |
| `CP2\|BRUMM_DEEPNEST_2` | "songs of **sacrifice**, of servitude" — the one devotional use of *sacrifice* |
| `Minor NPC\|BRETTA_DIARY_3` | "would break the **spell**" — the moment, not magic |
| `UI\|CHARM_DESC_33` | "**casting** spells" — *cast* cannot be a term rule (it is inside *caste*, *outcast*, *Lancaster*) |
| `UI\|SHOP_DESC_SPELLDMGUP` | "Are you a **spellcaster**" |
| `CP3\|NOTE_PURE_VESSEL` | *spell* carries the shell/spell rhyme; *cell* keeps it and fits the Vessel's imprisonment |
| `Journal\|NOTE_PURE_VESSEL` | duplicate of the above |
| `Zote\|PRECEPT_29` | "a **magical** map inside of your head" — figurative, but the word still goes |
| `Minor NPC\|DUNG_DEFENDER_REPEAT` | "Good **fortune** on the path ahead" — luck, not divination |
| `UI\|SHOP_DESC_TRINKET4` | "a small **fortune**" — money, so it needs a different word again |
| `CP3\|NOTE_NAILMASTERS` | the four verses are **supplications** — "Help Us find the God We seek!" — so they are rewritten as records rather than petitions |
| `Journal\|NOTE_NAILMASTERS` | duplicate |
| `CP3\|NOTE_PAINTMASTER` | "**Reveal to Us** the God most pure!" |
| `Journal\|NOTE_PAINTMASTER` | duplicate |
| `CP3\|NOTE_SAGE_SLY` | "**Sharpen Our nails and show Us** the odds" |
| `Journal\|NOTE_SAGE_SLY` | duplicate |
| `CP3\|NOTE_VOID_IDOL_1` | "devoted their **worship** to… the very darkness itself" — renaming worship is not enough, the concept is removed |
| `CP3\|NOTE_VOID_IDOL_2` | duplicate |
| `CP3\|NOTE_VOID_IDOL_3` | duplicate |
| `Journal\|NOTE_VOID_IDOL_1` | duplicate |
| `Journal\|NOTE_VOID_IDOL_2` | duplicate |
| `Journal\|NOTE_VOID_IDOL_3` | duplicate |
| `Relic Dealer\|RELICDEALER_IDOL_1` | "**worship** was offered through these idols" — an offering, so the line is reworked, not reworded |
| `UI\|INV_DESC_TRINKET3` | "the elusive king was **worshipped** through these idols" — same |
| `Relic Dealer\|RELICDEALER_IDOL_4` | "A ruler seeking **worship**" |
| `Quirrel\|QUIRREL_GREENPATH_1` | "suggests some form of **worship**" |
| `Jiji\|SHAMAN_TEMPLE` | "a place of strange **worships**" |
| `CP3\|PANTHEON_ENTER_0` | "Through **sacred** combat" (*cherished combat* does not read) and "be **damned** for thy arrogance" |
| `CP3\|GODSEEKER_ENGINE_REPEAT_3` | "Our **sacred** attunement" — *cherished* does not fit here either |
| `Minor NPC\|XUN_MEET` | "This cruel, **sinful** world" |
| `Charm Slug\|CHARMSLUG_OVERCHARM` | "a bit of a **sin** to wear too many Charms" |
| `Journal\|NOTE_GHOST_XERO` | "burdened by **sins** and memories" |
| `CP3\|GG_S_BIGBEES` | "Lover gods of **faith** and devotion" — devotional, unlike the idiomatic uses |
| `CP3\|GG_S_GHOST_XERO` | "Dreamborn god of **faith** and betrayal" — same |
| `CP3\|GODSEEKER_WATERWAYS_AWAKE_2` | "What draws thee here, Crawler? **Faith**? Fear?" |
| `Dream Witch\|WITCH_FINAL_2` | "hush whispers of **faith**" — belief in the ancient light |
| `Achievements\|ENDINGD_TEXT` | term rules produced "**Ascend the Ascent** of Hallownest" |
| `CP3\|ENDING_D_TEXT` | duplicate of the above |
| `CP2\|NYMM_MEET` | — |
| `Shaman\|SHAMAN_SCREAM` | — |
| `CP3\|GRIMM_GG_2` | — |
| `Enemy Dreams\|GRIMM_GG_2` | — |
| `Achievements\|CHARMED_TITLE` | — |
| `Charm Slug\|CHARMSLUG_TRUTH` | — |
| `Charm Slug\|CHARMSLUG_MEET_3B` | — |
| `Journal\|NOTE_FLAMEBEARER_MED` | — |
| `Backer Messages\|BELIEVE_TAB_19` | — |
| `Charm Slug\|CHARMSLUG_NOSTOCK` | — |
| `Lore Tablets\|FUNG_TAB_03` | — |
| `Jiji\|RESTING_GROUNDS` | — |
| `CP3\|GODSEEKER_ENGINE_REPEAT_2` | — |
| `UI\|CHARM_DESC_19` | — |
| `CP3\|GODSEEKER_ENGINE_2` | — |
| `Lore Tablets\|DREAM_PLANT_01` | — |
| `Lore Tablets\|DREAM_PLANT_REST_GLADE` | — |
| `General\|PROLOGUE_EXCERPT_02` | — |
| `Lore Tablets\|RANDOM_POEM_STUFF` | — |
| `CP3\|NIGHTMARE_GRIMM_GG_1` | — |
| `Enemy Dreams\|NIGHTMARE_GRIMM_GG_1` | — |

### Full text

**`CP3|GODSEEKER_ENGINE`**

> **Before** — Why hast thou crept into this pantheon, o meagre one? The noise of thine wriggling creates much discord, drowning out the godly resonances we attune Ourselves to!<page>Dost thou mean to thwart our sacred goal? Dost envy drive thou to such madness?<page>We pray that the Gods of this Kingdom punish thee, obliterate thee, utterly destroy thee!

> **After** — Why hast thou crept into this ascent, o meagre one? The noise of thine wriggling creates much discord, drowning out the luminous resonances we attune Ourselves to!<page>Dost thou mean to thwart our cherished goal? Dost envy drive thou to such madness?<page>We will that the Luminaries of this Kingdom punish thee, obliterate thee, utterly destroy thee!

**`CP3|GODSEEKER_ENGINE_PRIME`**

> **Before** — Show reverence, o meagre one. Show fear! Thou approacheth a great and terrible God.<page>Though its worldly body be bound and defiled, the glory of its pure form endures, ruler of this pantheon. Its endless power shall attune Us to the one greater still, a God of Gods!<page>Meagre one, dost thou imagine thyself the equal of this God? Dost thou imagine thyself made in its image? Thou assume a similar shape, and the deep echo within thee seems familiar...<page>Ahh! What thoughts are these? Thou sow blasphemies in Our mind, wretch! Begone! We pray that the God of nothingness silence thee forever!

> **After** — Show reverence, o meagre one. Show fear! Thou approacheth a great and terrible Luminary.<page>Though its worldly body be bound and defiled, the glory of its pure form endures, ruler of this ascent. Its endless power shall attune Us to the one greater still, a Light of Lights!<page>Meagre one, dost thou imagine thyself the equal of this Luminary? Dost thou imagine thyself made in its image? Thou assume a similar shape, and the deep echo within thee seems familiar...<page>Ahh! What thoughts are these? Thou sow doubts in Our mind, wretch! Begone! We will that the Luminary of nothingness silence thee forever!

**`CP3|GODSEEKER_ENGINE_3`**

> **Before** — Thou art painfully persistent! Why dost thou defile this pantheon with thine presence? Seek ye glory, o vain one?<page>Thou misunderstand Our purpose. Through ritual combat are We attuned to the voices of the Gods.<page>Ever higher do they lead Us! Higher and higher and higher! Until through Godly focus do We attain communion with that great power sleeping in the Kingdom's heart...

> **After** — Thou art painfully persistent! Why dost thou defile this ascent with thine presence? Seek ye glory, o vain one?<page>Thou misunderstand Our purpose. Through practised combat are We attuned to the voices of the Luminaries.<page>Ever higher do they lead Us! Higher and higher and higher! Until through Luminous focus do We attain communion with that great power sleeping in the Kingdom's heart...

**`CP3|PANTHEON_ENTER_3`**

> **Before** — O Gods of Hallownest, graciously thee open the way to this greatest of Pantheons! Thy voices grow closer and thy resonance draws Us ever higher!<br><page>Pray will We, Attune will We, until that spark of divine light shines from the deepest darkness!

> **After** — O Luminaries of Hallownest, graciously thee open the way to this greatest of Ascents! Thy voices grow closer and thy resonance draws Us ever higher!<br><page>Seek will We, Attune will We, until that glimmer of sublime light shines from the deepest darkness!

**`Elderbug|ELDERBUG_TEMPLE_VISITED`**

> **Before** — Did you visit that temple? A strange building I've heard, though I'd never dare the journey myself.<page>The braver among us once went there to pray, said they felt at peace within the walls. After a while, they stopped going. I wonder what changed?

> **After** — Did you visit that vault? A strange building I've heard, though I'd never dare the journey myself.<page>The braver among us once went there to sit in silence, said they felt at peace within the walls. After a while, they stopped going. I wonder what changed?

**`Journal|NOTE_MAGE_LORD`**

> **Before** — The bugs of Hallownest tried all kinds of tricks and rituals and prayers to rid themselves of the infection. But to no avail! Perhaps the infection came from somewhere deep inside of them that they could not escape.

> **After** — The bugs of Hallownest tried all kinds of tricks and remedies and desperate measures to rid themselves of the infection. But to no avail! Perhaps the infection came from somewhere deep inside of them that they could not escape.

**`Minor NPC|TUK_DREAM`**

> **Before** — Mmmnnnnnnngghhh... I'll find you again. The water will bring you to me. I just need to keep searching... and praying.<page>When we meet again... I want you to say... that you're sorry.

> **After** — Mmmnnnnnnngghhh... I'll find you again. The water will bring you to me. I just need to keep searching... and hoping.<page>When we meet again... I want you to say... that you're sorry.

**`Jiji|RITUAL_BEGIN`**

> **Before** — Mmmm... I will enjoy this morsel tremendously. Now, as promised, we will begin the ritual.

> **After** — Mmmm... I will enjoy this morsel tremendously. Now, as promised, we will begin.

**`Stag|STAG_RESTINGGROUNDS`**

> **Before** — The Resting Grounds... Passengers would come here to conduct rituals for those who had passed on.<page>Not any more though. Perhaps the dead conduct their own rituals now?

> **After** — The Resting Grounds... Passengers would come here to remember those who had passed on.<page>Not any more though. Perhaps there's no one left who remembers the way.

**`CP2|BRUMM_DEEPNEST_2`**

> **Before** — Endless, repeating songs of sacrifice, of servitude. For the Ritual. For the troupe. For the Master.<page>Even this child was born into invisible chains. Mrmm.

> **After** — Endless, repeating songs of toil, of servitude. For the Performance. For the troupe. For the Master.<page>Even this child was born into invisible chains. Mrmm.

**`Minor NPC|BRETTA_DIARY_3`**

> **Before** — The White Saviour in Darkness<br>Troubled dreams beset the maiden. Her saviour gone, consumed below. Now her only companion the cold wind, moaning at her door. Her heart fluttered with sudden fear...<page>Then still. A sudden calm. Why? A presence. A figure close behind.<page>She doesn't dare look, doesn't dare move, fearful the slightest action would break the spell. She knew the presence at her bed, knew the calm only they could bring.<page>Her white saviour, now protector, standing tall beside, powerful, perfect...

> **After** — The White Saviour in Darkness<br>Troubled dreams beset the maiden. Her saviour gone, consumed below. Now her only companion the cold wind, moaning at her door. Her heart fluttered with sudden fear...<page>Then still. A sudden calm. Why? A presence. A figure close behind.<page>She doesn't dare look, doesn't dare move, fearful the slightest action would break the moment. She knew the presence at her bed, knew the calm only they could bring.<page>Her white saviour, now protector, standing tall beside, powerful, perfect...

**`UI|CHARM_DESC_33`**

> **Before** — Reflecting the desires of the Soul Sanctum for mastery over SOUL, it improves the bearer's ability to cast spells.<br><br>Reduces the SOUL cost of casting spells.

> **After** — Reflecting the desires of the Spark Spire for mastery over SPARK, it improves the bearer's ability to use skills.<br><br>Reduces the SPARK cost of using skills.

**`UI|SHOP_DESC_SPELLDMGUP`**

> **Before** — Are you a spellcaster, you little scoundrel? Ho ho! I'm only teasing.<br><br>If you ever learn any spells you should buy this charm for yourself. I've heard it will make a spell much stronger!

> **After** — Are you a student of SPARK, you little scoundrel? Ho ho! I'm only teasing.<br><br>If you ever learn any skills you should buy this emblem for yourself. I've heard it will make a skill much stronger!

**`CP3|NOTE_PURE_VESSEL`**

> **Before** — "Deepest silence in holy shell,<br>Given nail and named a Knight,<br>Bound by chain and egg and spell,<br>Hear Our plea! Reveal thy Light!"<br>- Prayer to the Vessel

> **After** — "Deepest silence in luminous shell,<br>Given nail and named a Knight,<br>Bound by chain and egg and cell,<br>Sealed away from all our sight."<br>- Song of the Vessel

**`Journal|NOTE_PURE_VESSEL`**

> **Before** — "Deepest silence in holy shell,<br>Given nail and named a Knight,<br>Bound by chain and egg and spell,<br>Hear Our plea! Reveal thy Light!"<br>- Prayer to the Vessel

> **After** — "Deepest silence in luminous shell,<br>Given nail and named a Knight,<br>Bound by chain and egg and cell,<br>Sealed away from all our sight."<br>- Song of the Vessel

**`Zote|PRECEPT_29`**

> **Before** — Precept Twenty-Nine: 'Develop Your Sense of Direction'.<page>It's easy to get lost when travelling through winding, twisting caverns. Having a good sense of direction is like having a magical map inside of your head. Very useful.

> **After** — Precept Twenty-Nine: 'Develop Your Sense of Direction'.<page>It's easy to get lost when travelling through winding, twisting caverns. Having a good sense of direction is like having a perfect map inside of your head. Very useful.

**`Minor NPC|DUNG_DEFENDER_REPEAT`**

> **Before** — Go now, mighty warrior of Hallownest! You've proven your honour! Good fortune on the path ahead.

> **After** — Go now, mighty warrior of Hallownest! You've proven your honour! Strength on the path ahead.

**`UI|SHOP_DESC_TRINKET4`**

> **Before** — Ah! This seems like a simple egg, but it's actually a precious relic from before the birth of Hallownest! <br><br>I'll pay you a small fortune for it. Please sell it to me!

> **After** — Ah! This seems like a simple egg, but it's actually a precious relic from before the birth of Hallownest! <br><br>I'll pay you a great sum for it. Please sell it to me!

**`CP3|NOTE_NAILMASTERS`**

> **Before** — "Gods by toil and nail bound,<br>Brothers sworn to guard the weak,<br>Masters of the sacred ground,<br>Help Us find the God We seek!"<br>- Prayer to the Masters

> **After** — "Luminaries by toil and nail bound,<br>Brothers sworn to guard the weak,<br>Masters of the cherished ground,<br>Ours to find, the ones We seek!"<br>- Song of the Masters

**`Journal|NOTE_NAILMASTERS`**

> **Before** — "Gods by toil and nail bound,<br>Brothers sworn to guard the weak,<br>Masters of the sacred ground,<br>Help Us find the God We seek!"<br>- Prayer to the Masters

> **After** — "Luminaries by toil and nail bound,<br>Brothers sworn to guard the weak,<br>Masters of the cherished ground,<br>Ours to find, the ones We seek!"<br>- Song of the Masters

**`CP3|NOTE_PAINTMASTER`**

> **Before** — "O God inspired, master of arts,<br>Whose works shall eternal endure,<br>Peer beyond Our minds and hearts,<br>Reveal to Us the God most pure!"<br>- Prayer to the Artist

> **After** — "O Luminary inspired, master of arts,<br>Whose works shall eternal endure,<br>Deep beyond Our minds and hearts,<br>There waits the Luminary most pure!"<br>- Song of the Artist

**`Journal|NOTE_PAINTMASTER`**

> **Before** — "O God inspired, master of arts,<br>Whose works shall eternal endure,<br>Peer beyond Our minds and hearts,<br>Reveal to Us the God most pure!"<br>- Prayer to the Artist

> **After** — "O Luminary inspired, master of arts,<br>Whose works shall eternal endure,<br>Deep beyond Our minds and hearts,<br>There waits the Luminary most pure!"<br>- Song of the Artist

**`CP3|NOTE_SAGE_SLY`**

> **Before** — "Sagely God of the cunning and bold,<br>Sharpen Our nails and show Us the odds,<br>O greatest of masters, We wish to behold,<br>That one still greater, the God of Gods!"<br>- Prayer to the Sage

> **After** — "Sagely Luminary of the cunning and bold,<br>Who sharpened Our nails and showed Us the way,<br>O greatest of masters, whom We have beheld,<br>Still greater the Light that awaits Us this day!"<br>- Song of the Sage

**`Journal|NOTE_SAGE_SLY`**

> **Before** — "Sagely God of the cunning and bold,<br>Sharpen Our nails and show Us the odds,<br>O greatest of masters, We wish to behold,<br>That one still greater, the God of Gods!"<br>- Prayer to the Sage

> **After** — "Sagely Luminary of the cunning and bold,<br>Who sharpened Our nails and showed Us the way,<br>O greatest of masters, whom We have beheld,<br>Still greater the Light that awaits Us this day!"<br>- Song of the Sage

**`CP3|NOTE_VOID_IDOL_1`**

> **Before** — "Inspired or mad, those ancient bugs. They devoted their worship to no lord, or power, or strength, but to the very darkness itself."<br>- Lemm

> **After** — "Inspired or mad, those ancient bugs. They devoted themselves to no lord, or power, or strength, but to the very darkness itself."<br>- Lemm

**`CP3|NOTE_VOID_IDOL_2`**

> **Before** — "Inspired or mad, those ancient bugs. They devoted their worship to no lord, or power, or strength, but to the very darkness itself."<br>- Lemm

> **After** — "Inspired or mad, those ancient bugs. They devoted themselves to no lord, or power, or strength, but to the very darkness itself."<br>- Lemm

**`CP3|NOTE_VOID_IDOL_3`**

> **Before** — "Inspired or mad, those ancient bugs. They devoted their worship to no lord, or power, or strength, but to the very darkness itself."<br>- Lemm

> **After** — "Inspired or mad, those ancient bugs. They devoted themselves to no lord, or power, or strength, but to the very darkness itself."<br>- Lemm

**`Journal|NOTE_VOID_IDOL_1`**

> **Before** — "Inspired or mad, those ancient bugs. They devoted their worship to no lord, or power, or strength, but to the very darkness itself."<br>- Lemm

> **After** — "Inspired or mad, those ancient bugs. They devoted themselves to no lord, or power, or strength, but to the very darkness itself."<br>- Lemm

**`Journal|NOTE_VOID_IDOL_2`**

> **Before** — "Inspired or mad, those ancient bugs. They devoted their worship to no lord, or power, or strength, but to the very darkness itself."<br>- Lemm

> **After** — "Inspired or mad, those ancient bugs. They devoted themselves to no lord, or power, or strength, but to the very darkness itself."<br>- Lemm

**`Journal|NOTE_VOID_IDOL_3`**

> **Before** — "Inspired or mad, those ancient bugs. They devoted their worship to no lord, or power, or strength, but to the very darkness itself."<br>- Lemm

> **After** — "Inspired or mad, those ancient bugs. They devoted themselves to no lord, or power, or strength, but to the very darkness itself."<br>- Lemm

**`Relic Dealer|RELICDEALER_IDOL_1`**

> **Before** — A King's Idol, eh?<page>Hallownest's king was an elusive figure, deified by the citizens. With the king rarely seen, worship was offered through these idols.<page>There's an expert craft to them. Few alive could match this skill.

> **After** — A King's Effigy, eh?<page>Hallownest's king was an elusive figure, honoured by the citizens. With the king rarely seen, these stood in his place.<page>There's an expert craft to them. Few alive could match this skill.

**`UI|INV_DESC_TRINKET3`**

> **Before** — A white idol depicting the King of Hallownest. The elusive king was worshipped through these idols.<br><br>Relic from Hallownest's past. This item now holds little value except for those dedicated to the kingdom's history.

> **After** — A white effigy depicting the King of Hallownest. The elusive king was seldom seen, so these stood in his place.<br><br>Relic from Hallownest's past. This item now holds little value except for those dedicated to the kingdom's history.

**`Relic Dealer|RELICDEALER_IDOL_4`**

> **Before** — A King's Idol?<page>I've often wondered the true visage of the king. Depictions are of an imposing, gleaming figure and a fiercely horned crown.<page>I suspect there's much embellishment in the imagery though. A ruler seeking worship tends to hide their blemishes. It'd do no good to appear a common bug.

> **After** — A King's Effigy?<page>I've often wondered the true visage of the king. Depictions are of an imposing, gleaming figure and a fiercely horned crown.<page>I suspect there's much embellishment in the imagery though. A ruler seeking admiration tends to hide their blemishes. It'd do no good to appear a common bug.

**`Quirrel|QUIRREL_GREENPATH_1`**

> **Before** — Oh, hello there! Seems we both tread far from the path.<page>I can hardly believe those dusty old highways led to such a lush and lively place!<page>This building suggests some form of worship, though its idol has clearly been long forgotten. Doubles equally well for a moment's respite.

> **After** — Oh, hello there! Seems we both tread far from the path.<page>I can hardly believe those dusty old highways led to such a lush and lively place!<page>This building suggests some form of assembly, though its effigy has clearly been long forgotten. Doubles equally well for a moment's respite.

**`Jiji|SHAMAN_TEMPLE`**

> **Before** — Yes, I can see the regrets you've left behind. A dark stain in an ancestral mound... a place of strange worships.

> **After** — Yes, I can see the regrets you've left behind. A dark stain in an ancestral mound... a place of strange gatherings.

**`CP3|PANTHEON_ENTER_0`**

> **Before** — Wretch! Thou hast ordained thine own destruction!<br><page>Through sacred combat are We attuned to this Kingdom's greatest beings. By entering this gate thou hast challenged the very Gods of this Kingdom!<br><page>Dost thou consider thyself the equal of this pantheon, of its masters? Draw thy weapon then, fool of fools, and be damned for thy arrogance!

> **After** — Wretch! Thou hast ordained thine own destruction!<br><page>Through trial by combat are We attuned to this Kingdom's greatest beings. By entering this gate thou hast challenged the very Luminaries of this Kingdom!<br><page>Dost thou consider thyself the equal of this ascent, of its masters? Draw thy weapon then, fool of fools, and be undone by thine own arrogance!

**`CP3|GODSEEKER_ENGINE_REPEAT_3`**

> **Before** — Dost thou understand Our words? Will thee allow thyself to be destroyed by the God of this pantheon? Will thee allow Us to resume Our sacred attunement?

> **After** — Dost thou understand Our words? Will thee allow thyself to be destroyed by the Luminary of this ascent? Will thee allow Us to resume Our patient attunement?

**`Minor NPC|XUN_MEET`**

> **Before** — Ahhhh.... Me'hon. This world. This cruel, sinful world. Why does che' wake? Why does che' persist?<page>Ahhh Le'mer, you could not know of tragedy as complete as che's, true lovers stripped apart, two worlds that could not meet.<page>And now meled'lover, dead so long in time. Dead, so far away. Buried, moina? Ai. Amongst its hateful kin that did deny our union, that did reject che's... outside-ness.<page>She doesn't suppose?... Nahlo, Nahlo. Could che' ask? Could che' burden?<page>Le'mer, woulds't you, coulds't you deliver gift to her grave?<page>The gift is, maybe small? But the trek is long. She rests amongst her kind near our Queen's lush refuge.<page>Would such a thing be done? Che' asks perhaps impossible things? Mad things? For Le'mer to take up such quest would be a kindness che' has near forgotten.

> **After** — Ahhhh.... Me'hon. This world. This cruel, pitiless world. Why does che' wake? Why does che' persist?<page>Ahhh Le'mer, you could not know of tragedy as complete as che's, true lovers stripped apart, two worlds that could not meet.<page>And now meled'lover, dead so long in time. Dead, so far away. Buried, moina? Ai. Amongst its hateful kin that did deny our union, that did reject che's... outside-ness.<page>She doesn't suppose?... Nahlo, Nahlo. Could che' ask? Could che' burden?<page>Le'mer, woulds't you, coulds't you deliver gift to her grave?<page>The gift is, maybe small? But the trek is long. She rests amongst her kind near our Queen's lush refuge.<page>Would such a thing be done? Che' asks perhaps impossible things? Mad things? For Le'mer to take up such quest would be a kindness che' has near forgotten.

**`Charm Slug|CHARMSLUG_OVERCHARM`**

> **Before** — It's a bit of a sin to wear too many Charms at once, isn't it? Sometimes less is more! Mmmm!<page>Yes, you shouldn't try to cram on more Charms than you can handle. The effect could be positively overwhelming!

> **After** — It's a bit of a shame to wear too many Emblems at once, isn't it? Sometimes less is more! Mmmm!<page>Yes, you shouldn't try to cram on more Emblems than you can handle. The effect could be positively overwhelming!

**`Journal|NOTE_GHOST_XERO`**

> **Before** — A life defined by tragedy and triumph. A death marred by sorrow and regret. A spirit burdened by sins and memories. Better to wander the world than be cursed with glory.<br>- Xero

> **After** — A life defined by tragedy and triumph. A death marred by sorrow and regret. A spirit burdened by regrets and memories. Better to wander the world than be cursed with glory.<br>- Xero

**`CP3|GG_S_BIGBEES`**

> **Before** — Lover gods of faith and devotion

> **After** — Lover Luminaries of love and devotion

**`CP3|GG_S_GHOST_XERO`**

> **Before** — Dreamborn god of faith and betrayal

> **After** — Dreamborn Luminary of loyalty and betrayal

**`CP3|GODSEEKER_WATERWAYS_AWAKE_2`**

> **Before** — What draws thee here, Crawler? Faith? Fear? Or do thee also seek the Gods?<page>Here. Heart of the Kingdom. We listen for them here. But some Gods are distant still. Must be awoken.<page>Take the Godtuner and seek ye the Gods! Seek! That they may find their way. Tuned to mind. Tuned to home.<page>Reward. As reward for thine services, ye shall be allowed to linger here. Linger and gaze. Linger and gaze on Our magnificent shell. Our overpowering beauty!

> **After** — What draws thee here, Crawler? Wonder? Fear? Or do thee also seek the Luminaries?<page>Here. Heart of the Kingdom. We listen for them here. But some Luminaries are distant still. Must be awoken.<page>Take the Attuner and seek ye the Luminaries! Seek! That they may find their way. Tuned to mind. Tuned to home.<page>Reward. As reward for thine services, ye shall be allowed to linger here. Linger and gaze. Linger and gaze on Our magnificent shell. Our overpowering beauty!

**`Dream Witch|WITCH_FINAL_2`**

> **Before** — And so this kingdom was born from that betrayal. But the memories of that ancient light still lingered, hush whispers of faith... Until all of Hallownest began to dream of that forgotten light.<page>Ah, but what's done is done. And so am I. The Wielder has at last appeared and I've held the memories of my tribe for long enough. It is time for us to be forgotten too.<page>Don't remember us, Wielder. Don't honour us. We do not deserve it...

> **After** — And so this kingdom was born from that betrayal. But the memories of that ancient light still lingered, hush whispers of longing... Until all of Hallownest began to dream of that forgotten light.<page>Ah, but what's done is done. And so am I. The Wielder has at last appeared and I've held the memories of my tribe for long enough. It is time for us to be forgotten too.<page>Don't remember us, Wielder. Don't honour us. We do not deserve it...

**`Achievements|ENDINGD_TEXT`**

> **Before** — Ascend the Pantheon of Hallownest and take your place at its peak

> **After** — Climb the Ascent of Hallownest and take your place at its peak

**`CP3|ENDING_D_TEXT`**

> **Before** — Ascend the Pantheon of Hallownest and take your place at its peak

> **After** — Climb the Ascent of Hallownest and take your place at its peak

**`CP2|NYMM_MEET`**

> **Before** — Ah. Hello! Hello! I'm new around these parts, so it's marvelous to see so friendly a face, in such a sad town.<page>The old bug over there was very welcoming, but still I find the place a little melancholy, what with the wind, and the darkness, and the sense of decline... I was hoping my music could go some way to livening up the place.<page>And now you've arrived with that wonderful, charming aura about you. The whole town feels brighter for it.<page>Before you hurry about your business, I've a small gift to commemorate a wonderful new friendship. No use for it myself, but I believe it'd look rather fancy upon you.<page>Please, enjoy it, and lets hope to see much more of one another about town.

> **After** — Ah. Hello! Hello! I'm new around these parts, so it's marvelous to see so friendly a face, in such a sad town.<page>The old bug over there was very welcoming, but still I find the place a little melancholy, what with the wind, and the darkness, and the sense of decline... I was hoping my music could go some way to livening up the place.<page>And now you've arrived with that wonderful, charming aura about you. The whole town feels brighter for it.<page>Before you hurry about your business, I've a small gift to commemorate a wonderful new friendship. No use for it myself, but I believe it'd look rather fancy upon you.<page>Please, enjoy it, and lets hope to see much more of one another about town.

**`Shaman|SHAMAN_SCREAM`**

> **Before** — Pried a spell out've my larger cousin did you? Aren't you the charming one.<page>She's not usually the generous sort, certainly not as giving as myself, but she does have that wonderful voice! It's no surprise her spells take on such aural force.

> **After** — Pried a skill out've my larger cousin did you? Aren't you the charming one.<page>She's not usually the generous sort, certainly not as giving as myself, but she does have that wonderful voice! It's no surprise her skills take on such aural force.

**`CP3|GRIMM_GG_2`**

> **Before** — A charming ritual... a pleasure!

> **After** — A charming performance... a pleasure!

**`Enemy Dreams|GRIMM_GG_2`**

> **Before** — A charming ritual... a pleasure!

> **After** — A charming performance... a pleasure!

**`Achievements|CHARMED_TITLE`**

> **Before** — Charmed

> **After** — Bedecked

**`Charm Slug|CHARMSLUG_TRUTH`**

> **Before** — My dapper gadfly, would you care to know how charms are made? I don't often tell my customers, what with the truth being a little morbid. But you're a sharp one so you may have guessed already.<page>Few ways a charm appears but mainly it's from final wish, a dying bug's potent desire crystallised into these gorgeous, powerful trinkets.<page>Now don't go getting too sad. There are exceptions of course, and really, it's quite beautiful, makes them all the more precious. Mmhhmm.<page>Just think of all the little bug souls that went into creating your collection! It's like a crowd of strangers in your pouch, or purse, or...err....wherever it is you keep them.

> **After** — My dapper gadfly, would you care to know how emblems are made? I don't often tell my customers, what with the truth being a little morbid. But you're a sharp one so you may have guessed already.<page>Few ways an emblem appears but mainly it's from final wish, a dying bug's potent desire crystallised into these gorgeous, powerful trinkets.<page>Now don't go getting too sad. There are exceptions of course, and really, it's quite beautiful, makes them all the more precious. Mmhhmm.<page>Just think of all the little bug hopes that went into creating your collection! It's like carrying a crowd of strangers' last wishes in your pouch, or purse, or...err....wherever it is you keep them.

**`Charm Slug|CHARMSLUG_MEET_3B`**

> **Before** — Mmm... What were we talking about? Oh yes, Charms! I'm surprised a stylish little gadfly like yourself isn't wearing any, actually.<page>Charms are gorgeous, mystical, one-of-a-kind accessories with a spark of power woven into their cores. Just wearing one is enough to change your life! You'll do things you never thought possible!<page>Take a look at some of the Charms I have for sale. You can take one home with you if you like!

> **After** — Mmm... What were we talking about? Oh yes, Emblems! I'm surprised a stylish little gadfly like yourself isn't wearing any, actually.<page>Emblems are gorgeous, curious, one-of-a-kind accessories with a trace of power woven into their cores. Just wearing one is enough to change your life! You'll do things you never thought possible!<page>Take a look at some of the Emblems I have for sale. You can take one home with you if you like!

**`Journal|NOTE_FLAMEBEARER_MED`**

> **Before** — "A spark of red lights darkest dream,<br>Scarlet nightmares bright and wild,<br>Visions dance and flames do speak,<br>Burn the father, feed the child."<br>- 'The Grimm Troupe'

> **After** — "A flicker of red lights darkest dream,<br>Scarlet nightmares bright and wild,<br>Visions dance and flames do speak,<br>Burn the father, feed the child."<br>- 'The Grimm Troupe'

**`Backer Messages|BELIEVE_TAB_19`**

> **Before** — Samu<br><br>Be the person you would like to meet. If our life is but a spark in the eyes of gods, lets blind them at least once.

> **After** — Samu<br><br>Be the person you would like to meet. If our life is but a flicker in the eyes of luminaries, lets blind them at least once.

**`Charm Slug|CHARMSLUG_NOSTOCK`**

> **Before** — Goodness, goodness. You've gone and bought all my lovely charms! What a stunning, colourful collection you've amassed. Mmmmmm! You're even more the attractive bug, clad in all those wonderful, sparkling things.<page>I may have nothing more to give, but you must come back and visit from time to time. Such a dashing figure frequenting my store. I bet the whole village is jealous. Mmm hmm!

> **After** — Goodness, goodness. You've gone and bought all my lovely emblems! What a stunning, colourful collection you've amassed. Mmmmmm! You're even more the attractive bug, clad in all those wonderful, glittering things.<page>I may have nothing more to give, but you must come back and visit from time to time. Such a dashing figure frequenting my store. I bet the whole village is jealous. Mmm hmm!

**`Lore Tablets|FUNG_TAB_03`**

> **Before** — Strength in the shared self.<br>Strength in the mind united.<br>In every bug that would pass upon our roads,<br>only the melancholy of disparity.

> **After** — Strength in the shared self.<br>Strength in the mind united.<br>In every bug that would pass upon our roads,<br>only the melancholy of disparity.

**`Jiji|RESTING_GROUNDS`**

> **Before** — Yes, I can see the regrets you've left behind. A dark stain in a holy place of repose.

> **After** — Yes, I can see the regrets you've left behind. A dark stain in a quiet place of repose.

**`CP3|GODSEEKER_ENGINE_REPEAT_2`**

> **Before** — Thou can not linger here, o coward of cowards! Step forth, and receive thine holy punishment!

> **After** — Thou can not linger here, o coward of cowards! Step forth, and receive thy due punishment!

**`UI|CHARM_DESC_19`**

> **Before** — Said to contain the knowledge of past generations of shaman.<br><br>Increases the power of spells, dealing more damage to foes.

> **After** — Said to contain the knowledge of past generations of adepts.<br><br>Increases the power of skills, dealing more damage to foes.

**`CP3|GODSEEKER_ENGINE_2`**

> **Before** — Ahh! Will the Gods not relieve Us of this troublesome speck? How it tests Us, seeing this worm raise its filthy weapon to the Gods!<page>Thou hast luck beyond luck, o speck! The Gods of this pantheon, for purpose beyond Our understanding, allow you amongst them.<page>Truly, the divine punishment they must be planning for you will be beyond all reckoning. Prepare thyself! Prepare thyself!

> **After** — Ahh! Will the Luminaries not relieve Us of this troublesome speck? How it tests Us, seeing this worm raise its filthy weapon to the Luminaries!<page>Thou hast luck beyond luck, o speck! The Luminaries of this ascent, for purpose beyond Our understanding, allow you amongst them.<page>Truly, the terrible punishment they must be planning for you will be beyond all reckoning. Prepare thyself! Prepare thyself!

**`Lore Tablets|DREAM_PLANT_01`**

> **Before** — ...Sacred memories...<page>...Honoured souls...

> **After** — ...Cherished memories...<page>...Honoured dead...

**`Lore Tablets|DREAM_PLANT_REST_GLADE`**

> **Before** — ...Sacred memories...<page>...Honoured souls...

> **After** — ...Cherished memories...<page>...Honoured dead...

**`General|PROLOGUE_EXCERPT_02`**

> **Before** — For none could tame our savage souls yet you the challenge met,

> **After** — For none could tame our savage hearts yet you the challenge met,

**`Lore Tablets|RANDOM_POEM_STUFF`**

> **Before** — In wilds beyond they speak your name with reverence and regret,For none could tame our savage souls yet you the challenge met,Under palest watch, you taught, you changed. Base instincts were redeemed,A world you gave to bug and beast as they had never dreamed.                                                          - Excerpt from Ode to Hallownest by Monomon the TeacherOur cherished dreams you granted and delivered more,But in dismay you found too late our desires had no end,What cost to tame our savagery? You gave your all and then gave more.Yet still desires lay unquenched, more dreams remained, your energies spent.Amongst it sprang a dreadful scourge,that forced return our aggressive urge,and turned us back to beasts or husks,Our souls consumed by light above.Within your corpse can still be heard the plaintiff cries of one,Who took our pain, and loss, and dreams inside itself to...Through it' pain we found a truth that must now be confessed,For nothing can contain such things but perfect emptiness.

> **After** — In wilds beyond they speak your name with reverence and regret,For none could tame our savage hearts yet you the challenge met,Under palest watch, you taught, you changed. Base instincts were redeemed,A world you gave to bug and beast as they had never dreamed.                                                          - Excerpt from Ode to Hallownest by Monomon the TeacherOur cherished dreams you granted and delivered more,But in dismay you found too late our desires had no end,What cost to tame our savagery? You gave your all and then gave more.Yet still desires lay unquenched, more dreams remained, your energies spent.Amongst it sprang a dreadful scourge,that forced return our aggressive urge,and turned us back to beasts or husks,Our hearts consumed by light above.Within your corpse can still be heard the plaintiff cries of one,Who took our pain, and loss, and dreams inside itself to...Through it' pain we found a truth that must now be confessed,For nothing can contain such things but perfect emptiness.

**`CP3|NIGHTMARE_GRIMM_GG_1`**

> **Before** — Gods... bound by ritual...

> **After** — Luminaries... bound to this stage...

**`Enemy Dreams|NIGHTMARE_GRIMM_GG_1`**

> **Before** — Gods... bound by ritual...

> **After** — Luminaries... bound to this stage...

---

## 3. Deliberately left unchanged

| kept | reason |
|---|---|
| **Radiance** / **Absolute Radiance** | a proper name, not divine framing |
| **Master** — Grimm's title | a title of rank, not of worship |
| **`witch`** | never actually occurs — every apparent hit is inside **"Switch User"** in the menu, which a naive rule would corrupt |
| **`cult`** | never actually occurs either — all 14 apparent hits are inside **"difficult"** and **"difficulty"** |
| **`summon`** | 3 uses, all ordinary calling: "Did you **summon** them?", "your **summons** heeded", Weaversong's "**Summons** weaverlings" |
| **`possess`** | 9 uses, all ordinary having or owning: "what skills you **possess**", "most prized **possession**", "the rock itself **possessed** a will" |
| `Minor NPC\|TISO_SHIELD` — "**Pray** you never find out what that is" | pure figure of speech |
| `Zote\|ZOTE_COLOSSEUM_REPEAT` — "**Pray** we do not meet in the arena" | same idiom |
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
|---|---:|
| CP3 | 147 |
| UI | 92 |
| Journal | 35 |
| Achievements | 22 |
| Titles | 21 |
| CP2 | 19 |
| Minor NPC | 17 |
| Prompts | 17 |
| Charm Slug | 14 |
| Lore Tablets | 14 |
| Relic Dealer | 9 |
| Enemy Dreams | 8 |
| Shaman | 8 |
| Ghosts | 6 |
| Nailmasters | 5 |
| Backer Messages | 4 |
| Dream Witch | 4 |
| Map Zones | 4 |
| Jiji | 3 |
| Credits List | 2 |
| Elderbug | 2 |
| Quirrel | 2 |
| Cornifer | 1 |
| Dreamers | 1 |
| General | 1 |
| Hornet | 1 |
| Iselda | 1 |
| MainMenu | 1 |
| Nailsmith | 1 |
| Sly | 1 |
| Stag | 1 |
| Zote | 1 |

`CP3` is the Godmaster content pack and `CP2` the Grimm Troupe, which is why those dominate.

---

## 5. Roadmap

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
can only go so far.

---

## 6. Verification

Generated by simulating the mod's own algorithm over all 4,089 dumped entries:

- **465** entries changed, 3,624 untouched
- **65** exact overrides, 400 via term rules
- **106** term rules, **67** exact overrides
- **0** replacement cascades (no rule's output may contain another rule's search key)
- **0** substring corruptions (a rule firing inside a longer word — this is how
  *melancholy* once became *melancluminous*, and it is why `charming`, `Charmed` and `spellcaster`
  are exact overrides)
- **0** article-agreement errors introduced ("a emblem", "An Primal")

