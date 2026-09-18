# Hybrid Hero Crossover Pilot

## Purpose

Determine where detailed raster artwork becomes visibly superior to a deliberately simplified SVG treatment for Witcher3-HyDE Hero/Application icons.

No crossover size is assumed in advance.

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

## Raster workflow

For each candidate:

1. keep the accepted SVG as the simplified/vector comparison;
2. create one square detailed raster master at high resolution, initially 1024×1024 or larger if justified;
3. generate initial downscaled comparisons;
4. where raster appears promising, create size-specific optimized PNGs;
5. rerun the review using those optimized PNGs;
6. judge the crossover at normal viewing scale.

A size-specific PNG may adjust local contrast, edge sharpness, silhouette separation, texture strength, highlight placement, and details that otherwise collapse. It is not required to be a blind mechanical resize.

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

The crossover is the first size where the detailed raster treatment is **clearly and consistently better at normal viewing scale**, not merely more detailed under zoom.

Review identity/silhouette, edge quality, material readability, useful texture survival, visual noise, dark-surface separation, and light-edge-case survival.

Do not freeze a class-wide threshold from one ambiguous result. Compare both Dolphin and Kitty; use Konsole as a third control if needed.

## Current status

Candidate selection and review tooling are defined.

The earlier procedural Dolphin/Kitty raster generators are retained only as **workflow fixtures**. They are useful for testing review-sheet generation, exact-size overrides, and CI wiring, but they do **not** meet the visual quality bar for Hero artwork and therefore provide **zero evidence** for the SVG↔PNG crossover.

No production-quality raster Hero master has yet been accepted, and **no SVG↔PNG crossover size has been established**.


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

1. create or retain a deliberately simplified SVG treatment of the same canonical;
2. export the raster master at 32, 48, 64, 96, 128, 256, and 512 px;
3. optimize each candidate PNG size individually where necessary;
4. compare **native-size output at 100% zoom** on all five standard review surfaces;
5. use enlarged nearest-neighbour sheets only as a diagnostic supplement, never as the primary verdict;
6. record where texture/material/detail first survives without harming identity or edge clarity;
7. repeat with at least one materially different production-quality Hero construction;
8. freeze a default Hero crossover only if the valid prototypes converge;
9. otherwise encode a family/per-canonical exception model.

A visually weak raster candidate invalidates the experiment because it tests artwork quality rather than delivery-format quality.


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

The generated masters are 1254×1254 and exceed the initial 1024 px minimum. They are working-session pilot assets; promotion into the final release raster source layout remains pending until the crossover policy and storage layout are frozen.

### Corrected Dolphin SVG control

The repository now contains:

`design/icons/hybrid-pilot/dolphin-simplified.svg`

This is a deliberately simplified vector treatment of the **same corrected medallion identity** as the raster master.

The previously accepted `design/icons/src/apps/dolphin.svg` still represents the older folder/file-cabinet composition and therefore must not be used as the SVG side of the real crossover experiment.

Native-size SVG/PNG samples have now been rendered at all seven test sizes. This is the first technically valid Dolphin comparison. No crossover threshold is frozen yet.

### Important limitation

Dolphin and Kitty are both circular medallions. Kitty confirms the material/finish quality bar, but it does not satisfy the requirement for a materially different second Hero construction. A second non-medallion Hero is still required before a class-wide default can be considered.
