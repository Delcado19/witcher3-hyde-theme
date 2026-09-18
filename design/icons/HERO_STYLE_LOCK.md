# Hero Application Style Lock — 2026-09-18

## Status

This document is **authoritative for Applications/Hero artwork**.

If another icon document conflicts with this file, this Hero style lock wins until it is explicitly revised.

## Locked visual target

The accepted high-detail Dolphin medallion from the 2026-09-18 working session defines the required Hero finish level.

The repository does not store that chat reference binary automatically, but its visual characteristics are frozen here:

- forged circular construction where the concept calls for a medallion;
- blackened and weathered iron/steel;
- bright but worn silver identity motif;
- authored scratches, abrasion, edge wear, cracks and patina;
- convincing depth, beveling, local shadow and directional lighting;
- controlled Witcher-red recess, rune and emissive accents;
- strong application identity before decorative detail;
- dark, mature Witcher material language rather than flat desktop-cartoon styling.

This locks the **finish and material language**, not one universal silhouette. Applications must still use varied constructions where their identity calls for them.

## Explicitly rejected Hero treatment

Flat or cartoon-like vector reinterpretations are **not acceptable Hero substitutes** when they materially diverge from the approved raster identity.

The rejected 2026-09-18 Dolphin vector comparison had the wrong silhouette, read as a different animal/object, lost the forged-metal material language, and did not preserve the raster master's color/value structure. Artwork of that kind must not be offered again as a Hero delivery candidate.

For Hero artwork, "simplified SVG" does **not** mean permission to redraw the icon into a different style.

## Hero fidelity rule

For each Hero canonical, the approved high-detail master is the visual source of truth.

An SVG candidate is acceptable only when it preserves, as closely as practical:

- the same recognizable subject and silhouette;
- the same composition and major proportions;
- the same dominant dark-steel / weathered-silver / Witcher-red color hierarchy;
- the same perceived depth and lighting direction;
- the same major bevels, recesses, rune structures and material boundaries;
- enough authored wear/material character that it still belongs to the same Hero artwork.

Minor micro-texture may be reduced where vector economics require it. Major style, shape or color changes are not allowed merely to make vectorization easier.

## PNG-only is an approved outcome

SVG is **optional for Hero icons**.

If a visually faithful SVG cannot be produced at reasonable vector complexity and file size, the canonical must ship as reviewed PNG delivery rather than accepting an inferior vector approximation.

There is no requirement to force SVG at small Hero sizes. A Hero canonical may be PNG-only across all approved fixed sizes.

The wider icon theme can still be hybrid: Glyph and many Emblem families may remain SVG while Hero applications use PNG wherever that produces the correct artwork.

## PNG → SVG reconstruction experiment

A serious PNG-to-SVG workflow is allowed and encouraged as an experiment.

The goal is **not** one-click tracing. The target is a visually guided reconstruction and optimization pipeline that can include:

1. visual/semantic segmentation of the master into major objects and material layers;
2. contour extraction and curve fitting for clean silhouettes;
3. layered vector reconstruction of rings, motifs, runes, bevels and recesses;
4. gradients, masks, clipped highlights and restrained filter effects for depth/lighting;
5. controlled vectorized wear/detail only where it materially contributes at display size;
6. path simplification and duplicate-point removal;
7. gradient/filter reuse and SVG structural cleanup;
8. final SVG optimization followed by raster A/B comparison against the master.

The vector result must remain a **real vector asset**. Embedding the original PNG inside an SVG wrapper does not satisfy this experiment.

A useful vector result should also have a practical SVG-like storage footprint relative to the high-resolution raster source. No hard byte threshold is frozen yet; visual fidelity comes first, then complexity/size is optimized and measured before acceptance.

## Fidelity gate before crossover testing

Hero SVG/PNG crossover testing is now a two-stage process.

**Stage 1 — fidelity gate**

Compare the candidate SVG with the approved PNG master first at large sizes, especially 256 and 512 px. If the vector does not clearly represent the same artwork, reject it immediately.

**Stage 2 — delivery crossover**

Only after an SVG passes the fidelity gate may both forms be compared at 32, 48, 64, 96, 128, 256 and 512 px to determine whether SVG is preferable at any smaller sizes.

If Stage 1 fails, there is no SVG crossover to discover for that candidate: use PNG delivery.

## Reference handling

Chat-supplied or generated working references establish visual direction, but binary files are not automatically committed as redistributable release assets. Promotion of a raster master into repository/release sources still requires clear project ownership or redistribution permission.

## Immediate next experiment

Use the accepted Dolphin raster identity as the first PNG→SVG reconstruction test.

Do not recreate the rejected flat/vector Dolphin. Reconstruct the accepted forged medallion artwork itself, then evaluate:

- visual fidelity;
- SVG complexity and byte size;
- render stability;
- native-size quality.

If that experiment cannot reach the locked visual target efficiently, record the result and treat Dolphin/Hero delivery as PNG-first or PNG-only rather than lowering the style bar.


## Reconstruction tool prototype — 2026-09-18

The active pilot branch now contains \`tools/reconstruct-hero-svg.py\`.

It is a **fidelity reconstruction tool**, not an art-style generator. It does not invent a replacement Dolphin. The current implementation:

1. preserves the source alpha silhouette;
2. uses perceptual superpixel segmentation to find contiguous visual/material regions;
3. clusters region colors from the source PNG itself;
4. traces the regions as real SVG polygons;
5. groups/reuses palette colors instead of embedding raster data;
6. uses compact relative path serialization;
7. optionally runs Scour for structural SVG optimization;
8. can render 256/512 diagnostics and report SSIM/MAE as engineering diagnostics only.

The current \`fidelity\` preset deliberately prioritizes visual similarity over minimum path count. The next optimization target is reducing the visible faceted/superpixel texture at 512 px without exploding SVG size.



## Edge-aware surface smoothing — prototype v2

The reconstruction tool may optionally apply **edge-aware vector surface smoothing** after the real-vector reconstruction.

This is not raster embedding and does not redraw the application identity. The reconstructed path set is stored once inside the SVG. A mild SVG Gaussian blur is used for the low-frequency surface layer, while a second PNG-derived vector mask restores only strong source-image edges sharply. A very low-opacity global detail pass prevents the smoothed layer from becoming sterile.

The intended effect is to reduce visible superpixel/mosaic faceting on broad forged-metal surfaces without softening identity-critical contours, runes, recesses, red accents, or structural metal edges.

This mode must remain optional until visually accepted and renderer compatibility has been validated on the target desktop SVG stack.


## Brilliance fidelity rule

PNG→SVG reconstruction must preserve not only average palette identity but also the source artwork's perceived brilliance.

Palette clustering may reduce local luminance contrast, bright metal highlights, and high-end chroma even when average RGB/L* remains close. A vector candidate should therefore be reviewed for:

- highlight intensity on worn silver/steel;
- black-to-silver dynamic range;
- red recess/emissive impact;
- local material contrast.

The reconstructor may apply a restrained Lab-space palette compensation after clustering, provided it does **not** alter geometry, introduce clipping, or turn Witcher red/steel into exaggerated neon/chrome. The visual master remains the PNG.

## Faceting as a vector-specific Hero treatment

A faithful Hero reconstruction is not required to imitate the raster master's microtexture literally when its vector construction develops a coherent visual character of its own.

For the accepted Dolphin SVG, the project owner explicitly accepts the remaining polygon/facet/mosaic character as a **deliberate vector stylistic feature**, because it preserves more perceived material detail than the tested smoothing pass.

This allowance is conditional:

- the faceting must arise from faithful reconstruction of the PNG rather than a new flat/cartoon redraw;
- application identity, silhouette, composition, major lighting and Witcher material hierarchy must remain faithful;
- faceting must not reduce small-size readability;
- acceptance is per canonical or visually coherent family, not automatic for all Hero artwork.

The Dolphin reference uses `punchy` brilliance compensation to restore highlight/chroma range lost during segmentation and palette clustering.



## Internal vector seam opacity

Faithful faceted reconstructions must remain visually stable on both dark and light backgrounds.

Adjacent facet polygons may use a small same-color stroke overlap to cover renderer anti-aliasing seams. This is not an outline effect and must not visibly thicken semantic edges.

For the current 512-unit reconstruction analysis canvas, Dolphin testing selected **1.25 analysis pixels** as the default seam overlap. This replaces the earlier 0.55 value, which allowed light backgrounds to leak through internal facet boundaries and falsely reduced perceived brilliance.



## Opaque vector underpainting requirement

Faceted Hero SVGs must not rely on thousands of adjacent anti-aliased polygons to provide the icon's only interior opacity.

The reconstructor must place a dark, source-alpha-derived **vector silhouette underpainting** beneath the facet layer by default. This underpainting:

- is a real SVG path, never an embedded PNG;
- follows source alpha topology and preserves intentional holes;
- derives its dark material color from the source artwork;
- prevents light or colored desktop backgrounds from leaking through internal facet boundaries;
- does not replace seam overlap, which remains useful for color continuity between neighboring facets.

A source master itself must also have correct alpha topology. Background removal that leaks into blackened-iron regions invalidates the reconstruction input and any crossover review derived from it.

