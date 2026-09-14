# Witcher 3 HyDE Icon Theme

The v1 design matrix defines **645 real visual assets** before alias expansion.

## Source files

- `witcher-icon-matrix-v1.md` — human-readable specification.
- `witcher-icon-matrix-v1.csv` — machine-readable source for validation/build tooling.

## Core rule

**One matrix row = one genuinely distinct visual design.**  
Aliases never increase the unique-design count.

## Proposed repository layout

```text
witcher3-hyde-icons/
├── README.md
├── matrix/
│   ├── witcher-icon-matrix-v1.md
│   └── witcher-icon-matrix-v1.csv
├── assets/
│   ├── hero/
│   ├── glyph/
│   └── emblem/
├── aliases/
├── scripts/
├── tests/
└── dist/
```

The next pass should verify canonical Linux icon names against the real HyDE/KDE/Waybar environment and expand alias coverage without inflating the artwork count.
