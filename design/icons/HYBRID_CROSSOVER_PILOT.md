# Hybrid Hero Crossover Pilot

## Purpose

Determine whether a Hero/Application icon can first be reconstructed as a **visually faithful SVG** from the approved production-quality artwork, and only then determine whether SVG has any useful delivery range versus PNG.

No crossover size is assumed in advance. SVG is not mandatory for Hero icons.

The authoritative visual policy is [`HERO_STYLE_LOCK.md`](HERO_STYLE_LOCK.md).

## Initial candidates and approved visual anchors

### W3-070 — dolphin

**Current approved Dolphin direction:** a circular forged medallion/seal with a strongly recognizable silver Dolphin emblem, blackened/weathered steel, engraved rune ring, controlled red recess/rim light, and optional secondary scene/detail that does not weaken the Dolphin silhouette.

This corrected medallion treatment supersedes the earlier folder/file-cabinet Dolphin as the intended final Dolphin identity.

**Earlier Dolphin concept:** a layered folder/file-cabinet object with leather bindings, steel plates, rivets, runes, and a large silver Dolphin emblem.

That earlier concept is **retired as final Dolphin artwork**. It may still be used as a **detail-stress-test reference** because its layered materials and depth make it useful for observing how complex raster detail collapses at smaller sizes. It must never be mistaken for the accepted final Dolphin direction.

### W3-083 — kitty

**Current approved Kitty direction:** a circular forged medallion with a distinct cat/wolf-like school head, terminal prompt element, weathered steel, engraved rune ring, and controlled red emissive accents.

Kitty is a valid quality anchor for the Hero raster bar, but it does not establish circular medallions as the default container for Applications.

### Reference handling

The project owner has supplied high-quality Dolphin and Kitty raster references in chat. They establish the **visual quality bar and current art direction**, but the binary images are not committed automatically.

Before any supplied reference image becomes a redistributable repository asset, its provenance and redistribution rights must be clear. Until then, the repository stores the art-direction decision in text and any production master must be project-owned/cleared.

W3-082 `konsole` remains available as a third control if valid production-quality Dolphin and Kitty comparisons do not establish a stable crossover.

## Comparison sizes

- 32 px
- 48 px
- 64 px
- 96 px
- 128 px
- 256 px
- 512 px

These are test points, **not a release PNG ladder**.

## Review surfaces

- `#0A151E`
- `#171A1C`
- `#1C1813`
- `#262729`
- `#F2F0EA`

## Raster / vector workflow

For each Hero candidate:

1. establish and approve one square detailed raster master at 1024×1024 or larger;
2. treat that master as the visual source of truth;
3. attempt a **faithful PNG→SVG reconstruction**, not a stylistic simplification;
4. test the SVG against the raster first at 256 and 512 px for subject, silhouette, composition, color hierarchy, depth, lighting and material fidelity;
5. if the SVG fails that fidelity gate, stop: the candidate remains PNG delivery and no SVG crossover is inferred;
6. only if the SVG passes, generate the seven native-size SVG/PNG comparisons;
7. create size-specific optimized PNGs where needed;
8. judge any actual delivery crossover at normal viewing scale.

A size-specific PNG may adjust local contrast, edge sharpness, silhouette separation, texture strength, highlight placement, and details that otherwise collapse. It is not required to be a blind mechanical resize.

The PNG→SVG experiment may use visual segmentation, layered path reconstruction, gradients, masks, restrained filters and subsequent path/structure optimization. One-click tracing and embedded-raster SVG wrappers do not satisfy the Hero vector experiment.

## Review tool

```text
python3 tools/build-hybrid-icon-review.py \
  --svg design/icons/src/apps/dolphin.svg \
  --raster-master <path-to-master.png> \
  --optimized-dir <optional-size-specific-png-directory> \
  --output build/icons/dolphin-hybrid-review.html \
  --require-raster
```

An optimized directory uses exact target filenames such as `32.png`, `48.png`, `64.png`, `96.png`, `128.png`, `256.png`, and `512.png`. A present exact-size PNG overrides master downscaling only at that size.

## Decision rule

Hero review now has two gates.

1. **Fidelity gate:** the SVG must first look like the same approved artwork at 256 and 512 px. Wrong subject/silhouette, flat/cartoon treatment, major color mismatch, lost material language or visibly different composition is an immediate reject.
2. **Crossover gate:** only a fidelity-passing SVG is compared at 32, 48, 64, 96, 128, 256 and 512 px.

If the fidelity gate fails, PNG-only is an approved result and no crossover size is invented.

If it passes, the crossover is the first size where one delivery form has a clear normal-viewing advantage while both still represent the same artwork.

Review identity/silhouette, edge quality, material readability, useful texture survival, visual noise, dark-surface separation, light-edge-case survival, and SVG complexity/file size.

## Current status

Production-quality Dolphin and Kitty raster references have now been visually accepted as Hero quality anchors.

The earlier procedural Dolphin/Kitty raster generators remain **workflow fixtures only** and provide zero crossover evidence.

The later flat/simplified Dolphin SVG comparison is also **rejected**. It did not preserve the approved Dolphin silhouette, material language, color hierarchy or overall Witcher finish closely enough to count as the same artwork. It must not be used for crossover evidence or offered as a Hero style direction.

No Hero SVG has yet passed the new fidelity gate, and **no SVG↔PNG crossover size has been established**.

## Retired procedural Dolphin review

The procedural Dolphin generator and its comparison sheets were previously treated as a tentative visual review.

That interpretation is **withdrawn**.

The generated artwork is a schematic/process fixture, not a production-quality Witcher3-HyDE Hero. It lacks the material depth, layered construction, authored surface wear, lighting, leather/metal treatment, and overall finish required of the real raster side of the hybrid comparison.

Therefore:

- the procedural Dolphin comparison is **not a valid crossover experiment**;
- the earlier 96 px indication is **void**;
- no size from that comparison may be used to configure delivery policy;
- the generator may remain in the repository only as a deterministic tooling fixture.


## Retired procedural Kitty prototype

`tools/generate-hybrid-pilot-kitty.py` remains useful as a deterministic tooling fixture, but its artwork is **not accepted Hero artwork** and must not be used to infer the crossover.

Status:

- procedural Dolphin fixture: tooling-only;
- procedural Kitty fixture: tooling-only;
- production-quality Dolphin raster Hero: required;
- second production-quality Hero of a materially different construction: required;
- project-owner visual review: required;
- Hero default crossover: **not frozen**.


## Retired procedural review package

The previously generated Dolphin/Kitty review package is retained only as evidence that the review tooling works.

It is **not** a valid art-direction review package and must not be used for crossover decisions.

A valid review package must be rebuilt from production-quality Hero artwork after that artwork has passed the quality gate below.


## Production-quality Hero raster gate — mandatory

A raster candidate may enter the crossover experiment only after it passes a **1024 px Hero quality gate**.

The raster side must look like plausible final-release Hero artwork, not a technical mock-up. It must contain authored detail that a simplified SVG genuinely cannot reproduce economically.

Minimum expectations:

- layered object construction with convincing depth;
- weathered metal with authored scratches, abrasion, edge wear, dents, or patina;
- leather, parchment, wood, glass, bone, or other secondary material where the concept calls for it;
- coherent directional lighting and local shadowing;
- controlled Witcher red used as accent/rim/recess light rather than flat paint;
- material-specific highlights instead of generic flat fills;
- strong application identity at a glance;
- no copied vendor artwork and no copied Witcher game asset;
- no procedural noise used as a substitute for authored surface treatment;
- no placeholder geometry whose only purpose is to make the PNG look "more detailed" than the SVG.

The approved **current Dolphin quality bar** is conceptually:

> a forged circular medallion/seal built from blackened and weathered steel, a large strongly recognizable silver Dolphin emblem, engraved rune geometry, authored scratches and edge wear, controlled red recess/rim light, and enough layered depth/material variation to reward raster delivery at large sizes.

The earlier layered folder/file-cabinet Dolphin remains useful only as a **complex-detail stress-test reference**. It is not the accepted final Dolphin identity.

The approved **Kitty quality bar** uses the same material/finish standard while preserving its own distinct cat/terminal identity.

The exact user-supplied reference images are art-direction references, not redistributable repository assets unless provenance/redistribution is explicitly cleared.

## Valid crossover experiment

Only after a raster master passes the quality gate:

1. build a visually faithful vector reconstruction of the approved canonical;
2. compare SVG and PNG at 256 and 512 px first;
3. reject the SVG immediately if subject, silhouette, composition, color, depth, lighting or material character diverges materially from the PNG;
4. if the SVG passes, export both forms at 32, 48, 64, 96, 128, 256 and 512 px;
5. optimize each candidate PNG size individually where necessary;
6. compare **native-size output at 100% zoom** on all five standard review surfaces;
7. measure/record SVG complexity and byte size alongside visual quality;
8. repeat with at least one materially different production-quality Hero construction if a class-wide rule is still desired;
9. freeze a default Hero crossover only if valid prototypes converge;
10. otherwise encode family/per-canonical delivery rules, including PNG-only where appropriate.

A visually weak raster candidate invalidates the experiment, and a visually unfaithful SVG invalidates the vector side of the experiment.

## Final-vs-stress-test distinction

A rejected Hero concept may still be useful for technical downscale testing when it contains materially richer depth, layered construction, or texture than the accepted final composition.

That use must be labelled explicitly:

- **final identity reference** — defines what the canonical should ultimately look like;
- **quality reference** — defines required finish/material fidelity;
- **detail stress test** — intentionally complex artwork used to expose downscale failure;
- **tooling fixture** — synthetic/procedural output used only to validate the review pipeline.

Only a **production-quality final identity reference** may decide the actual crossover for that canonical. A stress-test image can reveal failure modes but cannot override the approved final art direction.


## Production-quality master milestone — 2026-09-18

Two generated-from-scratch Hero raster masters now pass the visual quality gate in the working session:

- **Dolphin:** corrected circular forged-medallion identity with a large silver Dolphin, blackened/weathered steel, rune geometry, authored surface wear, and restrained red recess light;
- **Kitty:** forged cat/terminal medallion at the same material-fidelity bar.

The project owner visually accepted both as high-quality Hero references.

The generated masters exceed the initial 1024 px minimum. They remain working-session pilot assets; promotion into the final release raster source layout still requires the repository asset/provenance decision.

### Rejected Dolphin SVG control

The attempted `design/icons/hybrid-pilot/dolphin-simplified.svg` comparison was visually rejected by the project owner and is removed from the active branch.

The reason is fundamental, not a small polish issue: the vector did not resemble the approved high-detail Dolphin closely enough, its subject/silhouette read incorrectly, and its colors/material treatment diverged from the raster source.

Therefore the generated comparison is **not valid crossover evidence**.

The next Dolphin vector attempt must reconstruct the accepted forged-medallion PNG identity itself using the PNG→SVG fidelity workflow in `HERO_STYLE_LOCK.md`. If that cannot be done at practical SVG complexity/size, Dolphin will use PNG delivery rather than an inferior vector substitute.

### Important limitation

Dolphin and Kitty are both circular medallions. Kitty confirms the material/finish quality bar, but it does not establish a universal medallion container. Applications still require varied silhouettes/constructions.


## PNG→SVG reconstruction prototype — 2026-09-18

A first serious reconstruction tool now exists at:

\`tools/reconstruct-hero-svg.py\`

Unlike the rejected flat SVG, this tool reconstructs the accepted raster artwork itself. It does not redraw the subject or substitute a new style.

First local Dolphin fidelity run against the accepted 1254×1254 master:

- analysis canvas: **512×512**;
- requested perceptual segments: **8000**;
- actual visible segments: **7308**;
- palette classes: **192**;
- reconstructed polygons: **7295**;
- source PNG size: **2,969,196 bytes**;
- SVG before Scour: **360,994 bytes**;
- SVG after Scour: **263,486 bytes**;
- optimized SVG / PNG byte ratio: **8.87%**;
- 256 px diagnostic: SSIM **0.8616**, MAE **8.25**;
- 512 px diagnostic: SSIM **0.7100**, MAE **10.60**.

Metrics are **diagnostics, not visual acceptance criteria**.

Visual result so far:

- subject, silhouette, composition and dominant Witcher palette are now genuinely the same artwork;
- at 256 px the reconstruction is already close to the PNG;
- at 512 px the current polygon segmentation is still visibly faceted/mosaic-like in the metal surfaces;
- therefore the SVG has **not yet passed the Hero fidelity gate**;
- no crossover decision follows from this prototype.

Next technical target: preserve the same reconstructed geometry while reducing the 512 px faceting, preferably with edge/material-aware refinement rather than merely multiplying polygons until file size becomes raster-like.

