# Witcher 3 HyDE Theme — Project Status

**Purpose:** compact handoff for continuing work without depending on old ChatGPT conversations.  
**Tracked branch:** `main`  
**Last status update:** 2026-09-17

> Keep this file short. Detailed design rules, matrices, build documentation, and historical reasoning belong in their existing source documents. Update this file whenever a work session changes the current task, completes a meaningful step, or establishes a new next action.

## Current focus

The active workstream is the **Witcher3-HyDE icon matrix / naming validation**.

- Matrix target: **645 distinct canonical designs before alias expansion**.
- Matrix source of truth: [`design/icons/matrix/witcher-icon-matrix-v1.md`](../design/icons/matrix/witcher-icon-matrix-v1.md)
- Machine-oriented matrix: [`design/icons/matrix/witcher-icon-matrix-v1.csv`](../design/icons/matrix/witcher-icon-matrix-v1.csv)
- Current matrix item under review: **W3-574 — `application-certificate`**
- Current concept in the matrix: **Signed certificate scroll with seal**
- Context/class/priority: **MIME/Filetypes · Emblem · P1**

## Current handoff

### W3-574 — `application-certificate`

Status: **verification started, not yet concluded**.

The previous work session began a strict read-only canonical-name check and did not establish a final naming decision before it ended.

Next action:

1. Verify `application-certificate` against the project's pinned Freedesktop icon-naming snapshot.
2. Verify the same canonical against the pinned Breeze reference used by the naming audit.
3. Do **not** substitute a semantically narrower certificate format merely because such an icon exists.
4. Only change the matrix if the evidence supports a better canonical under the project's naming rules.
5. Record the conclusion here when W3-574 is closed, then advance `Current matrix item under review` to the next unresolved item.

Until that verification is completed, the existing matrix row remains authoritative:

```text
W3-574 | MIME/Filetypes | application-certificate | Signed certificate scroll with seal | Emblem | P1
```

## Repository sources of truth

Use these documents instead of reconstructing decisions from chat history:

- [`design/icons/matrix/witcher-icon-matrix-v1.md`](../design/icons/matrix/witcher-icon-matrix-v1.md) — canonical 645-item design matrix.
- [`design/icons/matrix/README.md`](../design/icons/matrix/README.md) — matrix methodology and supporting reference material.
- [`design/icons/ART_DIRECTION.md`](../design/icons/ART_DIRECTION.md) — icon visual language and design constraints.
- [`design/icons/PILOT_BATCH.md`](../design/icons/PILOT_BATCH.md) — 14-icon pilot definition and acceptance gates.
- [`docs/ICON_NAMING_BASELINE.md`](ICON_NAMING_BASELINE.md) — naming rules and standards baseline.
- [`docs/ICON_BUILD.md`](ICON_BUILD.md) — icon build and packaging behavior.
- [`docs/HYDE_REFERENCE_MATRIX.md`](HYDE_REFERENCE_MATRIX.md) — HyDE integration baseline.
- [`design/palette/witcher3-color-system.md`](../design/palette/witcher3-color-system.md) — project color system.

## Working rule for future sessions

At the end of any meaningful work session:

1. make the actual repository changes first;
2. update this file with the completed item/result;
3. identify the exact next action;
4. remove stale handoff details instead of accumulating a chronological diary;
5. keep full technical reasoning in the relevant permanent document, commit history, tests, or matrix notes.

This file is a **current-state handoff**, not a changelog. Historical release-level changes belong in [`CHANGELOG.md`](../CHANGELOG.md) and detailed technical decisions belong in their dedicated documents.
