# Witcher3-HyDE Icon Recovery Handoff — 2026-09-19

## Purpose

This handoff exists to prevent any repeat of the lost icon-artwork work from the 2026-09-18 / 2026-09-19 redesign session.

It is a **mandatory operating rule** for all further icon recovery, reconstruction, redesign, review, conversion and production work.

## Non-negotiable persistence rule

**Every change is pushed to the remote repository and then verified from the remote repository before work continues.**

A change is not considered saved merely because it exists:

- in the current chat;
- in a temporary runtime/container;
- in a generated image result;
- in a local working directory;
- in an unpushed commit;
- in memory or handoff prose without the corresponding asset bytes.

For every completed work unit:

1. create or modify the actual source/review/production files;
2. calculate/record useful verification data where appropriate;
3. commit the change;
4. push the commit to the active remote branch;
5. re-read the committed file(s) from GitHub;
6. verify that the remote branch points at the expected commit;
7. only then continue to the next work unit.

For binary artwork, verification must include the actual remote file identity (Git blob SHA and/or cryptographic checksum when available), not merely the presence of a filename.

## SVG / rendered-artifact verification rule

Remote presence and a valid Git blob are **not sufficient** for SVG artwork.

For every SVG that matters to the project:

1. re-read the exact remote SVG bytes after push;
2. render those remote bytes with at least one SVG renderer and preferably a second independent renderer/browser engine;
3. verify that the render is non-empty and contains meaningful opaque/non-background pixels;
4. inspect the rendered result at intended native icon sizes;
5. treat renderer disagreements as a compatibility defect to resolve, not as proof that the SVG itself is universally broken;
6. only then mark the SVG technically valid.

The 2026-09-19 vector quality pilot exposed this requirement: one renderer produced an empty result while another visible client rendered the artwork. Therefore future SVG verification must test actual rendered output, not just file syntax, filename, size or blob identity.

For PNG/raster assets, verification must likewise open/decode the actual remote bytes and verify dimensions plus non-empty pixel/alpha content.

## No chat-only artwork

Any generated or reconstructed artwork that matters to the project must be persisted before moving on.

If an image is reviewed, accepted, used as a reference, or used to make a design decision, its actual bytes must be stored in a durable repository/recovery location whenever technically possible.

A prose statement such as “approved” is not a substitute for the corresponding image asset.

## Recovery-first rule

Before recreating missing artwork:

1. inspect the project rules and current handoff;
2. inspect the surviving approved/recovered assets;
3. search repository branches/history;
4. search the persistent Library/recovery files for exact prior assets or Base64 transfers;
5. recover exact bytes wherever possible;
6. only redraw/reconstruct what cannot actually be recovered.

Recovered exact originals outrank approximations.

## Quality bar

Do **not** use the legacy flat/provisional SVG artwork on `main` as the visual target.

The current benchmark is the approved/recovered high-detail Witcher3-HyDE work, especially:

- Dolphin;
- terminal-forward Kitty;
- selected Konsole direction;
- recovered/approved Packages & Executables artwork;
- the dark MIME-family direction documented in the current handoff and art-direction rules.

Core visual requirements remain:

- Witcher 3 first;
- dark blackened/weathered iron and cold steel;
- deep cavities, authored wear, restrained highlights;
- controlled Witcher-red accents;
- familiar desktop semantics;
- varied natural silhouettes rather than universal boxes/tiles;
- no generic bright fantasy/steampunk drift;
- no pasted seal used as a substitute for actual Witcher material identity.

## Family workflow

Before rebuilding a family:

1. query/freeze exact family membership;
2. resolve canonicals vs aliases vs fallbacks;
3. inspect surviving references;
4. establish the family design system;
5. build the family coherently;
6. review at native sizes;
7. persist every accepted asset;
8. push;
9. verify remotely.

Do not silently expand the canonical matrix because a review sheet contains additional real-world formats.

## Context-handoff rule

Do not wait until the chat context is nearly exhausted.

While substantial icon work is in progress, refresh the handoff **early and proactively**, including:

- active branch and remote HEAD;
- completed/recovered families and exact asset paths;
- outstanding families;
- approved visual decisions;
- rejected/retired directions;
- checksums/blob SHAs for important binary masters;
- exact next step;
- any recovery locations outside the repository that still need migration.

The handoff itself must also be committed, pushed and re-read from GitHub.

## Active recovery branch

At the time this rule was written:

- repository: `Delcado19/witcher3-hyde-theme`
- active recovery/design branch: `icon-hero-hybrid-pilot-1`
- authoritative release branch remains `main`
- do not modify/advance `main` merely to make recovery work appear complete;
- recovery/design work must be verified first, then deliberately integrated.

## Definition of done for any recovered icon

An icon is not “done” until all of the following are true:

- correct semantic identity;
- conforms to the current Witcher3-HyDE art rules;
- source/master is stored;
- required derived assets are stored;
- remote commit exists;
- remote file has been re-read/verified;
- the handoff/status reflects the real repository state.

If any one of these is missing, the icon remains incomplete.
