# Third-Party Notices

This file records third-party material distributed with or adapted for the Witcher 3 HyDE Theme.

**Do not add an external asset to a release until its source and redistribution terms have been recorded here.**

The presence of an item in this file does not replace its original license. The original license remains authoritative.

## Bundled Assets

| Asset / Package | Author / Project | Source | License | Repository Path | Modifications / Notes |
|---|---|---|---|---|---|
| _None recorded yet_ |  |  |  |  |  |

## Referenced but Not Yet Redistributed

Use this section for third-party material that is referenced, selected as an implementation base, or used for development but is not currently packaged in this repository.

| Resource | Author / Project | Source | License | Purpose / Notes |
|---|---|---|---|---|
| HyDE | HyDE Project | https://github.com/HyDE-Project/HyDE | GPL-3.0 | Target desktop environment and technical source of truth for theme integration |
| Colloid GTK Theme | Vince / `vinceliuice` | https://github.com/vinceliuice/Colloid-gtk-theme | GPL-3.0 | Selected structural base for the future `Witcher3` GTK derivative; pinned upstream commit `fe11342f37f124f1b29d44cf33e9a06053f4bba2` from 2026-08-22. No Colloid source or generated GTK package is redistributed by the repository at this stage. See `docs/GTK_BASELINE.md` and `design/gtk/upstream/COLLOID_SOURCE.md`. |
| The Witcher 3: Wild Hunt in-game screenshot wallpaper set | CD PROJEKT RED; screenshots supplied by the project maintainer | https://www.cdprojektred.com/en/fan-content | CD PROJEKT RED Fan Content Guidelines; not an open-source asset license | Candidate 2560×1440 in-game screenshots for `Configs/.config/hyde/themes/Witcher3/wallpapers/`. CD PROJEKT RED's Fan Content Guidelines explicitly list taking screenshots of its games, sharing them online, and turning them into wallpaper as permitted examples when the guidelines are followed. Intended use here is non-commercial and clearly unofficial. Game imagery remains property of its respective rights holders and is not relicensed under this repository's software/artwork license. The applicable game EULA and CD PROJEKT RED User Agreement remain authoritative. |

When the Witcher3 GTK derivative or its corresponding source is added to the repository, move or duplicate the Colloid entry into **Bundled Assets** with the exact repository paths and modification details used by the release.

When a Witcher 3 screenshot is actually committed under `Configs/.config/hyde/themes/Witcher3/wallpapers/`, move the corresponding screenshot entry into **Bundled Assets** and record the exact filename(s). Do not imply that the screenshot itself is licensed under the repository's source-code or original-artwork license.

## Witcher Intellectual Property

The Witcher-related names, characters, symbols, fictional locations, game imagery, and other protected material belong to their respective rights holders.

This project is unofficial and does not claim ownership of CD PROJEKT RED or other third-party intellectual property.

Original project artwork should be independently created rather than copied from commercial game assets unless redistribution is explicitly permitted. In-game screenshots intended as fan-content wallpapers are handled separately under CD PROJEKT RED's applicable fan-content rules and game agreements.

## Adding a New Third-Party Asset

Before committing a redistributable third-party asset:

1. Identify the original source, not a repost or aggregator.
2. Record the author or project.
3. Record the exact license or permission terms.
4. Confirm that redistribution and modification are permitted for the intended use.
5. Preserve required attribution and license files.
6. Record any modifications made by this project.
7. Add the asset to the table above.

If any of these points cannot be established, keep the asset out of the distributable theme.
