# Hybrid Hero Crossover Pilot

## Purpose

Determine where detailed raster artwork becomes visibly superior to a deliberately simplified SVG treatment for Witcher3-HyDE Hero/Application icons.

No crossover size is assumed in advance.

## Initial candidates

### W3-070 — dolphin

`Blue sea-dolphin sigil on a steel file-cabinet shield`

Useful because it has a broad object/silhouette, large steel surfaces that can carry raster material detail, and a strong cyan identity cue that remains suitable for simplified SVG.

### W3-083 — kitty

`Cat-school medallion with a terminal prompt etched below`

Useful because its medallion/character construction differs materially from Dolphin, while face, metal wear, engraving, and inset details can benefit from a detailed raster master.

W3-082 `konsole` remains a third control if Dolphin and Kitty disagree materially.

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

The approved Dolphin quality bar is conceptually:

> a layered file/folder or cabinet object built from blackened/weathered steel, leather bindings, engraved/rune accents, controlled red recess/rim light, and a strongly recognizable silver Dolphin emblem.

The exact reference image is an art-direction reference, not a redistributable repository asset unless its provenance/license is explicitly cleared.

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
