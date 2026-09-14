# Asset Policy

This document defines which visual assets may be committed or shipped with the Witcher 3 HyDE Theme.

## Goals

The repository should remain:

- redistributable where possible
- traceable to original asset sources
- clear about third-party ownership
- free of unexplained copied game assets
- usable as a long-term community project

## Asset Classes

### 1. Original Project Artwork

Artwork created specifically for this project should be retained in the appropriate source directory and documented sufficiently to allow future maintenance.

Examples:

- Witcher-inspired icon artwork
- custom folder emblems
- original glyphs
- original wallpapers
- original logos that do not falsely imply official status

### 2. Third-Party Open Assets

Third-party assets may be included only if their license permits the intended redistribution.

Their provenance must be recorded in `THIRD_PARTY_NOTICES.md`.

### 3. Third-Party Proprietary Assets

Do not include proprietary artwork merely because it can be downloaded from the web.

Examples requiring particular caution include:

- extracted game textures
- official promotional artwork
- screenshots used as distributable wallpaper
- commercial icon sets
- proprietary fonts
- logos or key art copied directly from a game installation

### 4. Reference Material

Reference images used during design should not automatically become distributable project assets.

If reference material must be retained for internal development, keep it outside release packages and document its source where appropriate.

## Generated Artwork

AI-assisted or procedurally generated artwork must still comply with the project's provenance and IP rules.

Generation does not make copied trademarks, copyrighted source artwork, or unlicensed third-party material automatically redistributable.

## Wallpapers

Every wallpaper intended for `Configs/.config/hyde/themes/Witcher3/wallpapers/` must have a known source and redistribution status.

If the project creates original wallpapers, prefer those over unknown web images.

## Icons

Icons should be original interpretations designed for desktop semantics.

Avoid tracing or directly reproducing official game UI icons unless the relevant rights clearly allow redistribution.

## Release Check

Before tagging a release:

- review all new binary assets
- verify `THIRD_PARTY_NOTICES.md`
- verify required attribution files are present
- remove development-only references and unlicensed temporary assets
