# Vector quality pilot — 2026-09-19

Purpose: test whether the lost post-Packages redesign can be rebuilt as deterministic SVG artwork without consuming image-generation quota.

## Quality bar

The visual target is **not** the legacy/provisional flat SVG set.

The benchmark is the high-detail Witcher3-HyDE quality represented by:
- recovered Dolphin master;
- recovered terminal-forward Kitty master;
- approved Packages / Executables family.

Required characteristics:
- dark blackened/weathered iron and cold steel;
- deep cavities and readable relief;
- controlled Witcher-red recess light;
- authored scratches/wear rather than flat noise;
- conventional desktop semantics;
- strong silhouette at native icon sizes;
- no pasted wolf seal as a substitute for material identity.

## Pilot SVGs

1. `audio-forged-speaker.svg`
   - commit: `142a6368adb1ef532e2de6d0bd939df4bedacb0f`
   - remote Git blob: `0df1a386933970c2aa55832d36cf087b4b48b324`

2. `video-forged-filmstrip.svg`
   - commit: `e35f5895fa713bf8858905a9e91b1f7a1c14b967`
   - remote Git blob: `e88c5624f32bd00b52f7e687054df1f6fa00163e`

3. `archive-forged-bundle.svg`
   - commit: `488b8406616d960cf8c3ba6b5eb38b640474930d`
   - remote Git blob: `4c7ba5e8388f62405176e399bec0d2c6269a2891`

4. `model-forged-axis-cube.svg`
   - commit: `f534ec2ff8fc4cff56ff04b76d85c3caf55f5eba`
   - remote Git blob: `59c9d0b0f143f8a4187507778376ed8f37bb35fa`

All four are true SVG source files. They use vector geometry plus SVG-native gradients, turbulence, displacement, specular-lighting and shadow filters. No image-generation model output is embedded in these SVGs.

## Important correction

The earlier four PNG test generations in chat are invalid for this pilot and are not part of the repository baseline. They must not be treated as project assets, references or recovered artwork.

## Next review step

Judge these four only as a technology/quality pilot against Dolphin and Kitty. Do not expand any family until the pilot quality is accepted or the vector system has been revised.
