# Witcher3-HyDE Icon Art Direction

**Project:** Witcher 3 HyDE Theme  
**Icon theme:** `Witcher3-HyDE`  
**Coverage target:** 645 distinct canonical designs before aliases

This document defines the visual language for the original project artwork used by the `Witcher3-HyDE` icon theme.

The matrix defines **what** each icon represents. This document defines **how** that icon should look. The build contract in `docs/ICON_BUILD.md` defines how accepted artwork is validated and packaged through the hybrid SVG/PNG delivery system.

## 1. Core objective

The icon theme should read as:

> **The Witcher 3 first, dark fantasy second, desktop icon theme third.**

It must not read as:

- a generic black-and-red gaming icon pack;
- a collection of vendor logos pasted onto one repeated medallion;
- a neon cyberpunk theme;
- a collection of copied Witcher game UI assets;
- a photorealistic inventory-icon set that becomes unreadable at desktop sizes.

The project uses original interpretations of desktop semantics. Application identity should remain recognizable, but the artwork must be transformed into the project's own visual language rather than tracing vendor or game artwork.

## 2. Relationship to the project palette

The icon system inherits the production palette from `design/palette/witcher3-color-system.md`.

### Structural colors

| Role | Token | Hex | Typical icon use |
|---|---|---|---|
| Cold near-black | `w3-canvas` | `#0A151E` | deep cavities, silhouette separation |
| Charcoal | `w3-surface` | `#171A1C` | dark body material |
| Warm near-black | `w3-surface-warm` | `#1C1813` | leather/wood shadow |
| Elevated charcoal | `w3-elevated` | `#262729` | raised plates and secondary bodies |
| Weathered steel | `w3-border` / `w3-steel` | `#3D3A39` | structure, dark metal edges |
| Silver | `w3-silver` | `#B0B6C2` | normal bright metal |
| Frost highlight | `w3-text-primary` | `#DEE6F0` | strongest controlled highlight |

### Accent colors

| Role | Token | Hex | Usage rule |
|---|---|---|---|
| Witcher red | `w3-red` | `#B72A18` | primary identity/accent; controlled |
| Deep red | `w3-red-deep` | `#621B0E` | recesses, pressed wax, deep ember |
| Amber | `w3-amber` | `#D58E4D` | fire, warning, warm magical detail |
| Cyan | `w3-cyan` | `#3188A6` | cold magic, information, selected app identity where justified |
| Alchemy green | `w3-alchemy` | `#3DB479` | potion/alchemy/success cues |
| Moss | `w3-moss` | `#505A26` | subdued natural detail only |
| Leather | `w3-leather` | `#7D572C` | straps, wood/leather accent |
| Rare violet | `w3-violet` | `#743874` | exceptional arcane/app-specific detail only |

Pure white should not be the normal highlight. Bright elements should normally stop at the frost/silver range.

## 3. Color budget

An individual icon should normally use:

- **60–80%** dark neutral / metal / warm-dark structure;
- **15–30%** silver, steel, parchment, or material midtones;
- **5–15%** primary accent color;
- at most **one additional saturated secondary accent** unless the application identity genuinely requires more.

Witcher red is the theme's unifying accent, not mandatory surface paint. An icon that is already semantically red does not need a second decorative red layer.

Multicolor application identities may keep several recognizable hues, but the hues should be weathered, materialized, and subordinate to the Witcher material system rather than reproduced as flat corporate color blocks.

## 4. Material vocabulary

The icon family uses a restricted material vocabulary.

### Blackened iron

Primary structural material.

- cool charcoal base;
- irregular but controlled edge wear;
- narrow steel highlights;
- deep blue-black cavities;
- no chrome-like mirror finish.

### Weathered silver / steel

Used for blades, clasps, engraved borders, runes, and readable highlights.

- cool rather than pure white;
- directional highlight rather than a universal outer glow;
- optional subtle scratches or hammered irregularity at Hero scale;
- small Glyphs use simplified solid silver shapes instead of micro-texture.

### Aged leather

Used for straps, books, satchels, map rolls, folders, and warm secondary structure.

- brown is secondary, never the global theme color;
- use broad shape/value changes rather than photographic grain;
- seams and rivets are allowed only where they survive the intended size.

### Parchment / bone / ivory

Used for documents, mail, books, notes, and selected pale motifs.

- warm, muted off-white;
- never clean office-paper white;
- strong enough edge contrast to survive against silver metal.

### Magical / alchemical energy

Used only when semantically useful.

- red ember, cyan magic, green alchemy, or amber fire;
- concentrated cores and restrained spill;
- no permanent neon halo around every icon;
- no rainbow bloom.

## 5. Shape language

Preferred Witcher-inspired construction vocabulary:

- forged plaques;
- medallions;
- sword/blade geometry;
- shield bosses;
- wax seals;
- book and contract forms;
- alchemical vessels;
- rune cuts and engraved marks;
- leather bindings;
- hammered or riveted metal frames;
- monster/animal silhouettes when they serve the semantic concept.

These are a vocabulary, **not mandatory containers**.

Do not place every application inside the same circular medallion, rounded-square tile, or shield. Hero icons must retain varied silhouettes so the launcher remains scannable.

## 6. Platform convention and semantic recognition

The theme must preserve established desktop icon conventions wherever a strong cross-platform convention already exists.

**Convention outranks novelty.** Witcher styling should transform the rendering and material language of a familiar symbol, not needlessly replace the symbol itself.

Examples:

- folders should remain immediately recognizable as folders;
- settings/preferences should normally use a gear, cog, control or equally established settings metaphor;
- audio should normally use a speaker, headphones/headset, microphone, or another established audio metaphor appropriate to the canonical;
- trash should remain recognizably a bin/basket;
- search should normally retain the magnifying-glass metaphor;
- locks/security should retain an established lock/shield/key metaphor where semantically appropriate;
- documents should remain recognizable as documents before any type-specific emblem is added;
- common transport and media controls should retain their established play/pause/stop/skip language.

This rule applies across Hero, Emblem and Glyph classes.

The redesign freedom is primarily in:

- material: blackened iron, weathered silver, leather, parchment, bone, glass, alchemical or magical accents;
- construction: forged frames, rivets, bevels, straps, seals, engravings and controlled damage;
- color/value hierarchy and lighting;
- secondary Witcher-specific ornamentation that does not obscure the semantic base.

A familiar symbol may be replaced only when the replacement is at least as immediately understandable at the intended desktop size and there is a clear semantic reason to do so.

For semantic families, first establish one approved base object or symbol and then derive family variants from it. Example: approve one strong Witcher folder master, then derive Home, Downloads, Documents, Music, Pictures and related folder variants through secondary emblems rather than reinventing the folder silhouette for every canonical.

Secondary emblems must also follow established semantic conventions. They exist to clarify the variant, not merely to decorate it. Do not place a symbol on a familiar base object if users are likely to associate that symbol with a different function. A Home folder should use a home/house cue, Downloads should use a download/downward-transfer cue, Music should use an established music/audio cue, Pictures should use an image/photo cue, and so on. Witcher-themed ornaments may support these cues, but must not replace them with ambiguous swords, runes, monsters, alchemical marks, or other lore motifs that imply a different meaning.

## 7. Canvas, master size, and safe area

Vector artwork should use a square coordinate system. The preferred authoring canvas is:

```text
viewBox="0 0 1024 1024"
```

A different square viewBox is acceptable when imported from a project-owned vector workflow, but exported vector artwork must remain scalable and centered predictably.

Detailed raster artwork should start from a high-resolution square master. **1024×1024 is the initial target, not yet an immutable minimum**; the crossover pilot may justify a larger master if that produces measurably better reviewed derivatives. Raster delivery sizes must be derived from the high-resolution master and then reviewed/optimized individually rather than accepted as blind automatic downsizes.

General safe-area guidance:

- keep essential identity inside roughly the central **82%** of the canvas;
- decorative sparks, blade tips, straps, or small protrusions may extend farther;
- avoid critical detail in the outermost **6%**;
- do not force all silhouettes to fill exactly the same bounding box;
- optical centering takes precedence over mathematical centering.

## 8. Hybrid delivery principle

The artwork class does not automatically determine the file format.

- tiny UI/status/action artwork should stay geometric and clean; vector delivery is expected to be strongest here;
- many Emblems may remain SVG when their symbolic construction benefits from vector delivery;
- Hero/Application artwork is **fidelity-first**: SVG is optional and is accepted only when it remains visually faithful to the approved high-detail artwork;
- a Hero canonical may ship as PNG-only when a practical vector reconstruction would require unacceptable style, shape, color, material or lighting compromises;
- there is no rule that small Hero sizes must use SVG;
- an embedded PNG inside an SVG wrapper is not considered a successful vector reconstruction.

The authoritative Hero-specific policy is [`HERO_STYLE_LOCK.md`](HERO_STYLE_LOCK.md).

A Hero crossover is tested only **after** a candidate SVG passes the visual-fidelity gate against its production-quality PNG master. If it fails that gate, the delivery decision is PNG rather than a lower-quality simplified vector.

### Hero visual-style lock

For Hero artwork, the approved high-detail Witcher treatment is the source of truth. Flat/cartoon redraws, semantically approximate substitute animals/objects, and recolored simplified variants are not acceptable merely because they are easy to express in SVG.

A valid Hero SVG must preserve the raster identity, major composition, color/value hierarchy, depth, lighting and material language closely enough to read as the same artwork.

### Hero raster quality gate

The raster side of a Hero crossover test must itself be **release-quality Hero artwork**. A procedural schematic, flat placeholder, synthetic texture demo, or mechanically decorated SVG-equivalent is not valid evidence.

Before any raster candidate is allowed to influence crossover policy, review its high-resolution master on its own. It must show authored material depth and finish that justify raster delivery: layered construction, coherent lighting, weathered surfaces, material-specific highlights, controlled edge wear, and application identity strong enough to survive simplification.

The approved target quality is comparable to a forged Witcher-style desktop object: blackened/weathered steel, leather or other secondary material where appropriate, engraved accents, controlled red recess/rim light, and a strong central application motif.

## 9. Hero icons — Applications

**Matrix class:** `Hero`  
**Count:** 220

Hero icons are the most detailed family and carry application identity.

### Requirements

1. The application must be recognizable from silhouette or one strong semantic motif before reading small decorative details.
2. A Hero icon should normally have one dominant object, not a miniature scene.
3. Vendor identity may be referenced through geometry, object metaphor, letterform logic, or established semantic motif, but should be substantially transformed into original project artwork.
4. Witcher styling comes from materials, construction, engraving, wear, and accent hierarchy — not from adding a wolf head to every app.
5. Avoid generic black rounded-square backgrounds unless a specific concept genuinely needs a plate.
6. Background containers should vary: open silhouette, disc, plaque, shield, book, tool, vessel, seal, mechanical form, etc.
7. Fine surface texture may exist at large sizes but must not be required to understand the icon.

### Detail hierarchy

At 128 px and larger:

- material texture may be visible;
- secondary engravings may appear;
- controlled scratches, bevel cues, seams, or rivets are allowed;
- detailed Heroes may use raster artwork when it is visibly superior to the simplified vector treatment.

At 48–64 px:

- primary silhouette and app identity must dominate;
- secondary engraving may soften or disappear;
- no critical information may depend on tiny text.

At 16–32 px:

- the icon must remain identifiable primarily by shape and color placement;
- micro-texture is irrelevant;
- internal negative spaces must not collapse.

## 10. Glyph icons — Actions, Status, Panel, Waybar

**Matrix class:** `Glyph`  
**Count:** 195

Glyphs are functional UI symbols. Readability outranks texture.

### Requirements

- strong silhouette;
- minimal internal detail;
- no photographic or painterly texture;
- no thin decorative filigree as a primary cue;
- consistent visual weight across related families;
- clear state differentiation at 16–24 px;
- use negative space deliberately;
- prefer filled or broad-cut geometry over hairline strokes.

Related state families must be designed as systems, not isolated icons. Examples:

- battery levels;
- volume levels;
- microphone states;
- wireless strength;
- weather states;
- CPU/GPU/memory load;
- workspace active/inactive;
- recording/sharing/idle-inhibitor states.

State families should keep the same outer silhouette and change only the minimum geometry needed to communicate state.

### Waybar rule

At typical Waybar sizes, one-glance recognition is mandatory. Decorative material effects should never make a status icon weaker than the equivalent plain symbolic icon.

## 11. Emblem icons — Places, Devices, MIME, Categories

**Matrix class:** `Emblem`  
**Count:** 230

Emblems sit between Hero and Glyph complexity.

### Requirements

- one recognizable base object;
- one clear differentiating emblem or material cue;
- moderate detail;
- shared family construction for related objects;
- readable at 24–48 px;
- richer than a pure monochrome glyph, simpler than a Hero application icon.

Examples:

- folders share a common Witcher folder/chest/manuscript language while the emblem differentiates purpose;
- storage devices share material construction but retain recognizable device silhouettes;
- MIME types use consistent document/container geometry and a strong type-specific emblem;
- preference categories use coherent control/tool metaphors rather than unrelated mini-scenes.

### Native-size format and micro-scale rule

File format is chosen by **native-size visual quality**, not by artwork class. Hero, Emblem, MIME, Places, Devices and other families all follow the same principle: if a faithful SVG is visually indistinguishable or preferable at the target size, use SVG; use PNG only where the approved raster master shows a visible quality advantage.

The current tested Hero reference boundary (Dolphin and Kitty) is **SVG through 512 px and PNG at 1024 px** because native 100% review showed the vector treatment remained visually sound through 512 px. That is a tested baseline, not a class privilege and not an automatic rule for every future icon.

For the current Office/Documents MIME direction, the detailed design itself remains recognizable at 128 px and 64 px, while 48 px is near the semantic/detail readability boundary. This observation **does not by itself choose PNG over SVG**. The same artwork must first undergo a faithful SVG reconstruction and native-size A/B review before any MIME crossover is frozen.

At very small sizes, a separately authored micro-variant is allowed when the full identity no longer reads clearly. A micro-variant may simplify texture, wax seals, scratches, decorative engraving and nonessential text/code lines, while preserving the same semantic silhouette, family construction and dominant type marker. Whether that micro-variant ships as SVG or PNG is again decided by native-size visual quality.

### Mandatory family preflight

Before any new icon family is drawn or generated, its membership must be established first.

Required sequence:

1. query the canonical matrix and list every type currently assigned to the intended family;
2. identify aliases, fallbacks, special cases and obvious mis-groupings;
3. explicitly freeze the review set for that family;
4. only then begin visual generation;
5. do not add attractive but unrelated formats to a review sheet merely because they fit visually.

A generated sheet that mixes unrelated families is reference material only and cannot be treated as a valid family approval.

### Family-master production workflow

For semantically related icon groups, the default production method is **family-first, not canonical-first**.

1. establish one visually approved family master that preserves the conventional semantic base;
2. define the fixed family geometry/material system and the allowed type-marker zone;
3. define how individual members differ without breaking the common silhouette;
4. review the master and a representative set at native sizes;
5. once the family system is accepted, derive the remaining family members as one coherent batch;
6. only outliers or ambiguous members require individual visual review.

A source file being present in the repository does **not** mean the artwork is visually approved. Existing legacy Glyph/Emblem coverage may be replaced when it fails the current quality bar.

This workflow is especially important for MIME/filetype families, folder/place families, device families, and repeated status-state families.

### Emblem/MIME Witcher identity lock

Recent MIME-family exploration showed a drift toward brighter generic fantasy / steampunk styling. That direction is rejected as a release target.

A Witcher3-HyDE Emblem or MIME icon must read as part of the theme **even if its wolf seal or explicit Witcher emblem is removed**. A pasted seal is not sufficient identity.

Required visual bias:

- darker overall value structure, closer to Dolphin / Kitty / Konsole than to bright parchment fantasy UI;
- blackened/weathered iron and cold steel should carry more of the construction;
- parchment, leather, brass and gold are secondary materials, not the dominant brightness source;
- parchment should be aged, muted and locally lit rather than broad bright beige;
- Witcher red stays controlled in recesses, wax, stitching or small accents;
- avoid warm golden global lighting, polished fantasy ornament overload and bright decorative filigree;
- prefer restrained, functional forged construction, authored wear, soot, scratches, cold edge highlights and deeper cavities;
- family members may use different physical metaphors, but all must share the same dark Witcher material and lighting language.

Quality check:

> If the seal/emblem is hidden, the icon should still plausibly belong next to Dolphin, Kitty and Konsole.

This rule applies to MIME, Places, Devices, Categories and other Emblem-class redesigns.

### Container restraint / silhouette variety

Do not overuse box, tile, plaque or framed-card containers merely to force family cohesion.

Use a box-like body only when it is semantically or physically appropriate to the object: package, crate, drive enclosure, terminal slab, framed device, document folio, archive chest, etc.

Otherwise prefer the natural silhouette of the object:

- keys should read as keys;
- scrolls/certificates as scrolls or folios;
- type specimens/quills/letterpress forms should remain typographic objects;
- locks/shields may stay open silhouettes;
- lenses, instruments, tools, seals and medallions should not be forced into rectangular tiles;
- family cohesion should come from material, lighting, edge treatment, accent logic and perspective before a repeated container is introduced.

A repeated rectangular frame is acceptable for category/system groups when it materially improves scanability, but it must not become the universal default for identity-rich MIME, device or application artwork.

## 12. Family consistency rules

Icons in a semantic family must share:

- perspective convention;
- approximate edge treatment;
- highlight direction;
- material vocabulary;
- emblem placement logic;
- stroke/edge weight at small sizes.

They must **not** be simple recolors when the matrix requires genuinely distinct designs.

Aliases reuse one canonical design by symlink and are the only intended cases of identical artwork under multiple names.

## 13. Lighting

Use one restrained desktop-icon lighting model:

- key light from upper-left to upper-front;
- cooler steel highlights;
- warmer local bounce only where leather/fire/parchment justifies it;
- cavities remain dark;
- shadows are compact and structural rather than cinematic background shadows.

No global lens flare, bloom haze, depth-of-field, or environmental background scene.

## 14. Depth and perspective

Hero and Emblem icons may use shallow pseudo-3D depth, bevels, overlapping plates, straps, and object thickness.

Avoid extreme perspective. Icons should feel like crafted objects presented for identification, not screenshots of objects lying on a table.

Glyphs should remain substantially flatter.

## 15. Edge treatment

The icon theme must remain readable on the project's dark surfaces.

Use one or more of:

- controlled silver rim light;
- a dark outer silhouette against bright internal material;
- thin weathered-steel edge separation;
- local contrast between adjacent materials.

Do not solve separation with a universal bright sticker outline.

## 16. Text and letters

Text is discouraged inside icons.

A single letter or short established monogram may be used when it is central to application identity, but it must be treated as vector artwork rather than a font-dependent text object.

Release SVGs should not require an installed font to render correctly.

Long words, UI labels, version numbers, and tiny decorative inscriptions are not allowed as identity-critical elements.

## 17. Gradients and effects

Allowed:

- restrained material gradients;
- metallic edge transitions;
- radial magical cores;
- subtle opacity changes;
- small controlled glows where semantically justified.

Avoid:

- glossy Web-2.0 gradients;
- rainbow gradients without app-specific justification;
- huge blurred drop shadows;
- neon outlines around every object;
- effects that dominate the silhouette.

Any SVG effect must remain self-contained. External image or network references are rejected by the build pipeline.

## 18. Background test surfaces

Every canonical icon should be visually reviewed on at least these project surfaces:

```text
#0A151E  w3-canvas
#171A1C  w3-surface
#1C1813  w3-surface-warm
#262729  w3-elevated
```

The icon should also remain legible on a generic light surface during file-manager or application edge cases. This does not require optimizing the entire design for a light theme; it requires avoiding silhouettes that disappear completely outside the intended dark desktop.

## 19. Required review sizes

Every accepted canonical should be inspected at:

```text
16 px
22 px
24 px
32 px
48 px
64 px
128 px
256 px
```

Hero artwork should additionally be inspected at 512 px or above.

For hybrid candidates, the review sizes are also used to compare the simplified SVG against the detailed raster master/derivative. Candidate crossover sizes currently include 32, 48, 64, 96, 128, 256, and 512 px; this is a test set, **not a frozen delivery ladder**.

The primary verdict must be made from **native-size 100% renders** on the target review surfaces. Enlarged nearest-neighbour or zoomed sheets are diagnostic only.

Review sizes do not automatically imply committed raster variants. A PNG size enters the release only after it demonstrates a visible advantage and passes size-specific optimization review.

## 20. Acceptance criteria

A canonical design is ready to enter `design/icons/src/` only when all of the following are true:

- it matches the matrix concept or an explicitly reviewed improvement;
- it belongs to the correct Hero/Glyph/Emblem family;
- its primary silhouette is readable at the required sizes;
- its palette follows the project color hierarchy;
- it does not rely on copied Witcher game UI artwork;
- it does not embed unlicensed third-party raster art;
- it uses no external network resource;
- vector-delivered artwork has a valid SVG `viewBox`;
- raster-delivered artwork comes from an approved high-resolution master and is not accidentally upscaled;
- its identity does not depend on a locally installed font;
- it is visually distinct from other canonical designs;
- related state/family icons remain coherent;
- the incremental source validator accepts it.

## 21. Artwork workflow

The intended workflow for each reviewed batch is:

1. select matrix IDs for one coherent family or application batch;
2. create original vector artwork outside the release staging directory;
3. compare the result against this art-direction document and the matrix concept;
4. inspect the required small sizes;
5. place accepted vector canonical sources in `design/icons/src/<context>/`; raster-master storage will be frozen only after the crossover pilot;
6. run the applicable source validation; during the current vector-family expansion this remains `python3 tools/validate-icon-sources.py`;
7. commit only the reviewed batch;
8. let CI repeat the validation;
9. continue with the next batch only after the current batch is green.

The release builder remains fail-closed until the source tree reaches all 645 canonical SVGs.
