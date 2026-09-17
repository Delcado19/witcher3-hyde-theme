# Witcher 3 HyDE Icon Matrix v1

**Target: 645 genuinely distinct visual designs before alias expansion.**

## Design classes

- **Hero** — detailed application icons, master at 1024×1024.
- **Glyph** — reduced, high-contrast symbols for Actions, Status, Waybar and small UI sizes.
- **Emblem** — medium-detail family for folders, devices, MIME and categories.

## Priority

- **P0** — first usable HyDE desktop build.
- **P1** — high-value daily-use coverage.
- **P2** — broad coverage.
- **P3** — specialist/lower-priority coverage.

## Counts

| Group | Unique designs |
|---|---:|
| Applications | 220 |
| Actions/UI | 100 |
| Places/Folders | 65 |
| Status/Panel/Waybar | 95 |
| Devices | 45 |
| MIME/Filetypes | 85 |
| Categories/Misc | 35 |
| **Total** | **645** |

## Alias policy

Aliases do **not** count as designs. `canonical_name` owns the artwork; `aliases` become symlinks or generated aliases during the build. Alias coverage in v1 is a seed and will be expanded in a separate validation pass.

## Matrix

| ID | Group | Canonical name | Witcher concept | Class | Priority | Alias seed | Notes |
|---|---|---|---|---|---|---|---|
| W3-001 | Applications | firefox | Wolf medallion wrapped by a controlled orange Igni flame | Hero | P0 | firefox-bin; firefox-esr; org.mozilla.firefox |  |
| W3-002 | Applications | chromium | Steel swallow-ring enclosing a pale blue alchemical vortex | Hero | P1 | chromium-browser; org.chromium.Chromium |  |
| W3-003 | Applications | google-chrome | Golden Novigrad sun-disc cut by a chrome-like steel ring | Hero | P1 | google-chrome-stable; com.google.Chrome |  |
| W3-004 | Applications | brave-browser | Red lion crest forged as a Witcher shield boss | Hero | P1 | brave; brave-browser-beta; com.brave.Browser |  |
| W3-005 | Applications | vivaldi | Crimson V-shaped rune engraved in blackened Toussaint steel | Hero | P1 | vivaldi-stable; com.vivaldi.Vivaldi |  |
| W3-006 | Applications | microsoft-edge | Sea-green Skellige wave curling around a silver blade | Hero | P2 | microsoft-edge-stable; com.microsoft.Edge |  |
| W3-007 | Applications | tor-browser | Dark onion sigil built from concentric Nilfgaardian filigree | Hero | P2 | torbrowser-launcher; org.torproject.torbrowser-launcher |  |
| W3-008 | Applications | librewolf | White wolf profile over a moonlit Kaer Morhen roundel | Hero | P1 | io.gitlab.librewolf-community; LibreWolf |  |
| W3-009 | Applications | floorp | Fox-tail knot around a compact witcher rune | Hero | P2 | one.ablaze.floorp |  |
| W3-010 | Applications | zen-browser | Minimal silver Zen circle pierced by a witcher sword tip | Hero | P2 | app.zen_browser.zen |  |
| W3-011 | Applications | thunderbird | Blue raven carrying a sealed Witcher contract scroll | Hero | P0 | mozilla-thunderbird; org.mozilla.Thunderbird |  |
| W3-012 | Applications | betterbird | Dark raven pair over a red wax-seal envelope | Hero | P2 | eu.betterbird.Betterbird |  |
| W3-013 | Applications | evolution | Oxenfurt envelope clasp with brass clockwork seal | Hero | P2 | org.gnome.Evolution |  |
| W3-014 | Applications | geary | Compact leather mail satchel with silver swallow clasp | Hero | P2 | org.gnome.Geary |  |
| W3-015 | Applications | kmail | Blue-black courier raven above a folded parchment K-rune | Hero | P1 | org.kde.kmail2; org.kde.kmail |  |
| W3-016 | Applications | proton-mail | Purple magical ward sealing a black envelope | Hero | P2 | protonmail-desktop; me.proton.Mail |  |
| W3-017 | Applications | discord | Twin pale specter-eyes inside a game-master talisman | Hero | P0 | discord-canary; discord-ptb; com.discordapp.Discord |  |
| W3-018 | Applications | vesktop | Discord talisman mounted in a sharper Viper-school frame | Hero | P1 | dev.vencord.Vesktop |  |
| W3-019 | Applications | telegram | Silver paper swallow flying across a cyan magic glyph | Hero | P0 | telegram-desktop; org.telegram.desktop |  |
| W3-020 | Applications | signal-desktop | White speech rune inside a dotted Yrden ward | Hero | P1 | signal; org.signal.Signal |  |
| W3-021 | Applications | element | Green linked-rune matrix around a central obsidian gem | Hero | P2 | im.riot.Riot; im.riot.Riot.desktop |  |
| W3-022 | Applications | slack | Four interlocked colored runestones on a steel buckle | Hero | P2 | com.slack.Slack |  |
| W3-023 | Applications | teams-for-linux | Purple twin-figure guild crest with message tablet | Hero | P2 | teams; com.github.IsmaelMartinez.teams_for_linux |  |
| W3-024 | Applications | zoom | Blue crystal scrying lens with a tiny camera aperture | Hero | P2 | Zoom; us.zoom.Zoom |  |
| W3-025 | Applications | skype | Cloud-blue communication rune etched into polished steel | Hero | P3 | skypeforlinux; com.skype.Client |  |
| W3-026 | Applications | whatsapp | Green whispering-stone with a silver handset rune | Hero | P2 | whatsapp-for-linux; io.github.mimbrero.WhatsAppDesktop |  |
| W3-027 | Applications | steam | Black steel gear-and-piston medallion with frost highlights | Hero | P0 | com.valvesoftware.Steam; steam-native |  |
| W3-028 | Applications | heroic | Golden laurel H crest on a dark Kaer Trolde shield | Hero | P1 | com.heroicgameslauncher.hgl |  |
| W3-029 | Applications | lutris | Red hunting cat skull sigil on hammered black steel | Hero | P0 | net.lutris.Lutris |  |
| W3-030 | Applications | bottles | Three alchemy bottles strapped into a leather witcher kit | Hero | P1 | com.usebottles.bottles |  |
| W3-031 | Applications | prismlauncher | Faceted prism crystal framed by four school-metal corners | Hero | P1 | org.prismlauncher.PrismLauncher |  |
| W3-032 | Applications | minecraft-launcher | Mossy cube carved like an ancient elven stone block | Hero | P1 | minecraft; com.mojang.Minecraft |  |
| W3-033 | Applications | wine | Ruby wine goblet on a Toussaint vineyard crest | Hero | P1 | winecfg; winefile; org.winehq.Wine |  |
| W3-034 | Applications | protonup-qt | Blue mutagen flask under an upward silver arrow | Hero | P1 | net.davidotek.pupgui2 |  |
| W3-035 | Applications | mangohud | Mango-colored performance rune with tiny gauge marks | Hero | P1 | MangoHud |  |
| W3-036 | Applications | gamescope | Framed viewing portal with crossed controller blades | Hero | P1 | gamescope-session |  |
| W3-037 | Applications | retroarch | Twin black-white game glyphs carved into a relic tile | Hero | P2 | org.libretro.RetroArch |  |
| W3-038 | Applications | dolphin-emu | Blue dolphin spirit leaping through an Aard ring | Hero | P2 | org.DolphinEmu.dolphin-emu |  |
| W3-039 | Applications | pcsx2 | Blue twin-tower rune representing mirrored console pillars | Hero | P2 | net.pcsx2.PCSX2 |  |
| W3-040 | Applications | rpcs3 | Three steel rune pillars with a red core crystal | Hero | P2 | net.rpcs3.RPCS3 |  |
| W3-041 | Applications | duckstation | Golden duck sigil rendered as a Skellige totem | Hero | P2 | org.duckstation.DuckStation |  |
| W3-042 | Applications | ryujinx | Red dragon-knot Joy-Con emblem | Hero | P2 | org.ryujinx.Ryujinx |  |
| W3-043 | Applications | cemu | Blue-white C rune as a glowing elven portal | Hero | P3 | info.cemu.Cemu |  |
| W3-044 | Applications | xemu | Green X rune engraved into a heavy iron console plate | Hero | P3 | app.xemu.xemu |  |
| W3-045 | Applications | ppsspp | Four blue crystal tiles around a central silver cross | Hero | P3 | org.ppsspp.PPSSPP |  |
| W3-046 | Applications | steam-rom-manager | Arcane library card catalogue with a Steam gear seal | Hero | P2 | com.steamgriddb.steam-rom-manager |  |
| W3-047 | Applications | obsidian | Deep violet obsidian shard with Witcher glyph fractures | Hero | P0 | md.obsidian.Obsidian |  |
| W3-048 | Applications | joplin | Black notebook with a silver J quill and red bookmark | Hero | P2 | net.cozic.joplin_desktop |  |
| W3-049 | Applications | logseq | Three linked parchment nodes connected by silver thread | Hero | P2 | com.logseq.Logseq |  |
| W3-050 | Applications | notion | Ivory N rune printed on a weathered contract page | Hero | P2 | notion-app-enhanced |  |
| W3-051 | Applications | standard-notes | White sealed journal with a simple steel lock rune | Hero | P3 | org.standardnotes.standardnotes |  |
| W3-052 | Applications | zettlr | Scholar's manuscript with an emerald Z initial | Hero | P3 | com.zettlr.Zettlr |  |
| W3-053 | Applications | typora | Minimal manuscript page with a dark T quill stroke | Hero | P2 | io.typora.Typora |  |
| W3-054 | Applications | marktext | Red M wax seal on a Markdown parchment | Hero | P2 | com.github.marktext.marktext |  |
| W3-055 | Applications | ghostwriter | Spectral blue quill writing on a black parchment sheet | Hero | P2 | org.kde.ghostwriter |  |
| W3-056 | Applications | libreoffice-startcenter | Open folio bound by a bronze office-clasp medallion | Hero | P0 | libreoffice; org.libreoffice.LibreOffice |  |
| W3-057 | Applications | libreoffice-writer | Blue manuscript folio with a silver quill blade | Hero | P0 |  |  |
| W3-058 | Applications | libreoffice-calc | Green alchemist ledger with etched grid lines | Hero | P0 |  |  |
| W3-059 | Applications | libreoffice-impress | Orange herald's presentation board with sunburst rune | Hero | P1 |  |  |
| W3-060 | Applications | libreoffice-draw | Yellow drafting compass crossing a silver stylus | Hero | P2 |  |  |
| W3-061 | Applications | libreoffice-base | Burgundy archive cylinder with stacked database rings | Hero | P2 |  |  |
| W3-062 | Applications | onlyoffice | Red interleaved manuscript sheets with brass corners | Hero | P2 | org.onlyoffice.desktopeditors |  |
| W3-063 | Applications | wps-office | Crimson folded ribbon rune over a dark document plaque | Hero | P3 | wps-office-prometheus |  |
| W3-064 | Applications | okular | Red eye-lens reading a parchment page | Hero | P0 | org.kde.okular |  |
| W3-065 | Applications | evince | Sepia document page held by a brass scholar clip | Hero | P2 | org.gnome.Evince |  |
| W3-066 | Applications | xournalpp | Ink pen and ruler crossed over a parchment notebook | Hero | P1 | com.github.xournalpp.xournalpp |  |
| W3-067 | Applications | calibre | Stack of leather-bound grimoires with a silver C clasp | Hero | P1 | calibre-ebook-viewer; calibre-gui |  |
| W3-068 | Applications | foliate | Open green grimoire with leaf-shaped page tabs | Hero | P2 | com.github.johnfactotum.Foliate |  |
| W3-069 | Applications | koreader | Black e-reader tablet framed like a witcher contract board | Hero | P2 | rocks.koreader.KOReader |  |
| W3-070 | Applications | dolphin | Blue sea-dolphin sigil on a steel file-cabinet shield | Hero | P0 | org.kde.dolphin |  |
| W3-071 | Applications | nautilus | Nautilus shell as an Oxenfurt archive seal | Hero | P2 | org.gnome.Nautilus |  |
| W3-072 | Applications | nemo | Green compass-shell on a leather explorer map | Hero | P2 | nemo.desktop |  |
| W3-073 | Applications | thunar | Grey mouse familiar carrying a tiny folder satchel | Hero | P1 | Thunar; org.xfce.Thunar |  |
| W3-074 | Applications | pcmanfm | Blue filing drawer with an elven P rune | Hero | P3 | pcmanfm-qt |  |
| W3-075 | Applications | krusader | Twin sabres crossing over a two-panel file chest | Hero | P1 | org.kde.krusader |  |
| W3-076 | Applications | yazi | Minimal black terminal chest with a yellow rune-tab | Hero | P1 |  |  |
| W3-077 | Applications | ranger | Forest ranger quiver shaped into a terminal file tree | Hero | P2 |  |  |
| W3-078 | Applications | ark | Iron archive chest with a brass compression clasp | Hero | P0 | org.kde.ark |  |
| W3-079 | Applications | file-roller | Rolled parchment bundle tied with an archive cord | Hero | P2 | org.gnome.FileRoller |  |
| W3-080 | Applications | peazip | Green pea-shaped alchemical capsule in a steel archive ring | Hero | P2 |  |  |
| W3-081 | Applications | 7zip | Seven steel archive plates locked by one heavy clasp | Hero | P2 | 7zFM; 7z; 7za; 7zr |  |
| W3-082 | Applications | konsole | Black rune-terminal slab with a luminous command chevron | Hero | P0 | org.kde.konsole |  |
| W3-083 | Applications | kitty | Cat-school medallion with a terminal prompt etched below | Hero | P0 |  |  |
| W3-084 | Applications | alacritty | Flaming red A rune on a blackened steel terminal plate | Hero | P1 | Alacritty; org.alacritty.Alacritty |  |
| W3-085 | Applications | wezterm | Lightning W rune over a dark terminal crystal | Hero | P1 | org.wezfurlong.wezterm |  |
| W3-086 | Applications | foot | Bootprint rune stamped onto a minimalist terminal plate | Hero | P2 | footclient |  |
| W3-087 | Applications | gnome-terminal | Dark stone terminal slab with green alchemical prompt | Hero | P2 | org.gnome.Terminal |  |
| W3-088 | Applications | tilix | Split terminal panes held in a bronze tiled frame | Hero | P2 | com.gexperts.Tilix |  |
| W3-089 | Applications | cool-retro-term | Amber cathode glow inside a brass retro scrying box | Hero | P3 |  |  |
| W3-090 | Applications | tmux | Three stacked terminal panes bound by a green T rune | Hero | P2 |  |  |
| W3-091 | Applications | zellij | Mosaic terminal panes in a Z-shaped Nilfgaardian frame | Hero | P2 |  |  |
| W3-092 | Applications | code | Blue ribbon chevrons forged as crossed editor blades | Hero | P0 | visual-studio-code; com.visualstudio.code |  |
| W3-093 | Applications | vscodium | Blue-green codium crystal framed by editor chevrons | Hero | P1 | codium; com.vscodium.codium |  |
| W3-094 | Applications | cursor | Black magical cursor arrow over a white arcane circle | Hero | P1 | cursor-editor; Cursor |  |
| W3-095 | Applications | zed | Red Z rune cut through a black steel editor badge | Hero | P2 | dev.zed.Zed |  |
| W3-096 | Applications | kate | Blue quill over a folded KDE manuscript | Hero | P0 | org.kde.kate |  |
| W3-097 | Applications | kwrite | Simple blue quill on a compact parchment page | Hero | P2 | org.kde.kwrite |  |
| W3-098 | Applications | geany | Blue genie lamp reimagined as a code alchemy vessel | Hero | P2 |  |  |
| W3-099 | Applications | sublime-text | Orange S rune carved into an obsidian editor tile | Hero | P2 | sublime_text; com.sublimetext.three |  |
| W3-100 | Applications | jetbrains-toolbox | Black arcane toolbox with four neon rune corners | Hero | P1 |  |  |
| W3-101 | Applications | idea | Black IDE crystal with magenta-blue arcane border | Hero | P1 | idea-ultimate; idea-community |  |
| W3-102 | Applications | pycharm | Black python-serpent grimoire with green rune border | Hero | P1 | pycharm-professional; pycharm-community |  |
| W3-103 | Applications | clion | Black C rune on a red-blue engineering sigil | Hero | P2 |  |  |
| W3-104 | Applications | webstorm | Black web rune on blue-green storm crystal | Hero | P2 |  |  |
| W3-105 | Applications | goland | Black Go rune on a cyan hunter's badge | Hero | P3 |  |  |
| W3-106 | Applications | rustrover | Black rusted R rune on an orange iron plate | Hero | P3 |  |  |
| W3-107 | Applications | android-studio | Green droid familiar under a steel drafting compass | Hero | P2 |  |  |
| W3-108 | Applications | qtcreator | Green Q rune mounted in a technical drafting frame | Hero | P2 |  |  |
| W3-109 | Applications | meld | Three parchment code strips merging into one red center strip | Hero | P1 | org.gnome.meld |  |
| W3-110 | Applications | gitkraken | Sea-monster kraken curling around a Git fork rune | Hero | P1 |  |  |
| W3-111 | Applications | github-desktop | Octocat familiar engraved on a black contract seal | Hero | P2 | io.github.shiftey.Desktop |  |
| W3-112 | Applications | lazygit | Lazy cat-school medallion lounging over a Git branch rune | Hero | P2 |  |  |
| W3-113 | Applications | postman | Orange courier rider carrying an API scroll tube | Hero | P1 | com.getpostman.Postman |  |
| W3-114 | Applications | insomnia | Moonlit API eye under a sleepless violet crescent | Hero | P2 | rest.insomnia.Insomnia |  |
| W3-115 | Applications | dbeaver | Beaver artificer holding a database gear wheel | Hero | P1 | io.dbeaver.DBeaverCommunity |  |
| W3-116 | Applications | beekeeper-studio | Golden bee over a honeycomb database sigil | Hero | P2 | io.beekeeperstudio.Studio |  |
| W3-117 | Applications | sqlitebrowser | Stacked stone tablets with a magnifying rune | Hero | P2 | org.sqlitebrowser.sqlitebrowser |  |
| W3-118 | Applications | redisinsight | Red crystal stack inside an alchemist data vial | Hero | P3 |  |  |
| W3-119 | Applications | docker-desktop | Cargo barge carrying stacked container chests | Hero | P1 |  |  |
| W3-120 | Applications | podman-desktop | Red seal-pup familiar beside stacked container crates | Hero | P2 | io.podman_desktop.PodmanDesktop |  |
| W3-121 | Applications | virt-manager | Two nested scrying mirrors symbolizing virtual machines | Hero | P1 |  |  |
| W3-122 | Applications | virtualbox | Blue rune cube with six engraved virtual faces | Hero | P2 |  |  |
| W3-123 | Applications | qemu | Copper machine core surrounded by four emulation runes | Hero | P2 |  |  |
| W3-124 | Applications | wireshark | Blue shark fin slicing through luminous packet waves | Hero | P1 | org.wireshark.Wireshark |  |
| W3-125 | Applications | nmap | Compass rose scanning a network map parchment | Hero | P2 | zenmap |  |
| W3-126 | Applications | remmina | Two remote viewing mirrors connected by a silver tether | Hero | P1 | org.remmina.Remmina |  |
| W3-127 | Applications | rustdesk | Rust-red remote desk sigil with linked screen plates | Hero | P2 | com.rustdesk.RustDesk |  |
| W3-128 | Applications | anydesk | Twin red diamond portals facing each other | Hero | P2 | com.anydesk.Anydesk |  |
| W3-129 | Applications | filezilla | Red F rune over a transfer bridge spanning two towers | Hero | P2 | org.filezillaproject.Filezilla |  |
| W3-130 | Applications | qbittorrent | Blue torrent swirl trapped in a circular Quen ward | Hero | P0 | org.qbittorrent.qBittorrent |  |
| W3-131 | Applications | transmission | Red transmission lever over a steel download chest | Hero | P2 | com.transmissionbt.Transmission |  |
| W3-132 | Applications | deluge | Blue flood-wave rune filling a download basin | Hero | P2 | org.deluge_torrent.deluge |  |
| W3-133 | Applications | jdownloader | Green downward rune into a brass archive crate | Hero | P2 | org.jdownloader.JDownloader |  |
| W3-134 | Applications | syncthing | Blue linked-orbit nodes around a central sync rune | Hero | P1 | syncthing-gtk; me.kozec.syncthingtk |  |
| W3-135 | Applications | localsend | White paper swallow passing through a blue local ward | Hero | P1 | org.localsend.localsend_app |  |
| W3-136 | Applications | kdeconnect | Phone and desktop plaques linked by a blue magical thread | Hero | P0 | org.kde.kdeconnect.app |  |
| W3-137 | Applications | warpinator | Green teleport ring moving a file scroll between portals | Hero | P2 | org.x.Warpinator |  |
| W3-138 | Applications | nextcloud | Three cloud runes encircling a central silver node | Hero | P1 | com.nextcloud.desktopclient.nextcloud |  |
| W3-139 | Applications | dropbox | Four blue rune tiles folding into a storage box | Hero | P2 |  |  |
| W3-140 | Applications | megasync | Red M seal on a heavy encrypted storage chest | Hero | P2 |  |  |
| W3-141 | Applications | onedrive | Blue cloud crest above a steel storage vault | Hero | P3 |  |  |
| W3-142 | Applications | rclone-browser | Remote cloud scrolls orbiting an R rune | Hero | P3 |  |  |
| W3-143 | Applications | keepassxc | Blue key crossing a black database shield | Hero | P0 | org.keepassxc.KeePassXC |  |
| W3-144 | Applications | bitwarden | Blue castle-shield lock with a narrow gate slit | Hero | P0 | com.bitwarden.desktop |  |
| W3-145 | Applications | 1password | Blue keyhole inside a polished circular vault plate | Hero | P2 | com.1password.1password |  |
| W3-146 | Applications | seahorse | Small seahorse familiar guarding a ring of cryptographic keys | Hero | P2 | org.gnome.seahorse.Application |  |
| W3-147 | Applications | kleopatra | Golden royal profile holding a cryptographic key | Hero | P2 | org.kde.kleopatra |  |
| W3-148 | Applications | veracrypt | Red V rune embedded in a heavy iron vault door | Hero | P1 |  |  |
| W3-149 | Applications | picocrypt | Tiny obsidian lock crystal with a minimalist P rune | Hero | P3 |  |  |
| W3-150 | Applications | gwenview | Silver eye viewing a mountain landscape through a round lens | Hero | P0 | org.kde.gwenview |  |
| W3-151 | Applications | eog | GNOME eye reimagined as a cat-school viewing medallion | Hero | P2 | org.gnome.eog |  |
| W3-152 | Applications | feh | Minimal framed raven-feather photograph plaque | Hero | P2 |  |  |
| W3-153 | Applications | nomacs | Red-black image frame crossed by a silver viewing slash | Hero | P2 | org.nomacs.ImageLounge |  |
| W3-154 | Applications | digikam | Camera aperture built from six Witcher school blades | Hero | P1 | org.kde.digikam |  |
| W3-155 | Applications | darktable | Darkroom table with a luminous photo plate | Hero | P1 | org.darktable.Darktable |  |
| W3-156 | Applications | rawtherapee | Raw crystal image shard polished by an alchemical lens | Hero | P1 | com.rawtherapee.RawTherapee |  |
| W3-157 | Applications | gimp | Grey Wilber familiar holding a Witcher paintbrush dagger | Hero | P0 | org.gimp.GIMP |  |
| W3-158 | Applications | krita | Multicolor painter's feather over a dark round shield | Hero | P0 | org.kde.krita |  |
| W3-159 | Applications | inkscape | Black mountain-ink drop cut into a vector rune | Hero | P0 | org.inkscape.Inkscape |  |
| W3-160 | Applications | blender | Orange eye-and-orbit forge emblem | Hero | P0 | org.blender.Blender |  |
| W3-161 | Applications | freecad | Red-blue gear block assembled like dwarven machinery | Hero | P2 | org.freecad.FreeCAD |  |
| W3-162 | Applications | kdenlive | Film-strip rune surrounding a red play crystal | Hero | P0 | org.kde.kdenlive |  |
| W3-163 | Applications | obs | Black scrying orb with three swirling recording lobes | Hero | P0 | com.obsproject.Studio |  |
| W3-164 | Applications | shotcut | Dark film strip cut diagonally by a silver editor blade | Hero | P2 | org.shotcut.Shotcut |  |
| W3-165 | Applications | openshot | Blue-green film ribbon wrapped around a play rune | Hero | P2 | org.openshot.OpenShot |  |
| W3-166 | Applications | handbrake | Cocktail goblet and pineapple turned into a tavern transcode sign | Hero | P2 | fr.handbrake.ghb |  |
| W3-167 | Applications | makemkv | Green disc emerging from a dark video archive vault | Hero | P2 | com.makemkv.MakeMKV |  |
| W3-168 | Applications | vlc | Orange striped witcher road cone on a small iron base | Hero | P0 | org.videolan.VLC |  |
| W3-169 | Applications | mpv | Purple play-triangle within a circular arcane media ward | Hero | P0 | mpv.desktop; io.mpv.Mpv |  |
| W3-170 | Applications | haruna | Blue play rune inside a KDE crescent frame | Hero | P1 | org.kde.haruna |  |
| W3-171 | Applications | smplayer | Blue play crystal over a film slate shield | Hero | P2 | org.smplayer.SMPlayer |  |
| W3-172 | Applications | celluloid | Celluloid film loop around a minimalist play rune | Hero | P2 | io.github.celluloid_player.Celluloid |  |
| W3-173 | Applications | audacious | Purple sound gem with a silver waveform cut | Hero | P2 |  |  |
| W3-174 | Applications | strawberry | Red strawberry alchemy fruit with a silver music note stem | Hero | P1 | org.strawberrymusicplayer.strawberry |  |
| W3-175 | Applications | elisa | Blue music crystal framed by a KDE ring | Hero | P1 | org.kde.elisa |  |
| W3-176 | Applications | amberol | Amber music disc glowing in a blackened bronze bezel | Hero | P2 | io.bassi.Amberol |  |
| W3-177 | Applications | spotify | Three green sound-wave runes on a black roundel | Hero | P0 | com.spotify.Client |  |
| W3-178 | Applications | tauonmb | Black alchemical record disc with opposing amber-red and cyan-violet quarter sigils | Hero | P3 | com.github.taiko2k.tauonmb |  |
| W3-179 | Applications | clementine | Orange fruit half carved with a musical spiral | Hero | P2 |  |  |
| W3-180 | Applications | deadbeef | Horned red skull wearing tiny music-wave engravings | Hero | P2 |  |  |
| W3-181 | Applications | easy-effects | Three alchemy sliders above an audio waveform | Hero | P1 | com.github.wwmm.easyeffects |  |
| W3-182 | Applications | pavucontrol | Copper audio valve manifold with three volume gauges | Hero | P1 | org.pulseaudio.pavucontrol |  |
| W3-183 | Applications | helvum | Patchbay rune network connecting four audio sockets | Hero | P2 | org.pipewire.Helvum |  |
| W3-184 | Applications | ardour | Red audio wave engraved into a black mixing console plate | Hero | P2 | org.ardour.Ardour |  |
| W3-185 | Applications | lmms | Green-black music forge with beat gears | Hero | P2 | io.lmms.LMMS |  |
| W3-186 | Applications | reaper | White reaper scythe over a black-red audio crest | Hero | P2 |  |  |
| W3-187 | Applications | audacity | Blue-red headphones around a golden waveform crystal | Hero | P1 | org.audacityteam.Audacity |  |
| W3-188 | Applications | tenacity | Blue waveform held by a stronger steel headphone frame | Hero | P2 | org.tenacityaudio.Tenacity |  |
| W3-189 | Applications | kcalc | Runic calculator tablet with brass number studs | Hero | P0 | org.kde.kcalc |  |
| W3-190 | Applications | qalculate | Green alchemical abacus with a Q rune | Hero | P2 | qalculate-gtk; io.github.Qalculate |  |
| W3-191 | Applications | speedcrunch | Red lightning abacus mounted on a steel number plate | Hero | P3 |  |  |
| W3-192 | Applications | spectacle | Framed eye-lens with a capture sparkle rune | Hero | P0 | org.kde.spectacle |  |
| W3-193 | Applications | flameshot | Purple flame striking a screenshot parchment | Hero | P1 | org.flameshot.Flameshot |  |
| W3-194 | Applications | ksnip | Silver shears cutting a rectangular screenshot parchment | Hero | P2 | org.ksnip.ksnip |  |
| W3-195 | Applications | swappy | Blue swap arrows around a captured parchment rectangle | Hero | P2 |  |  |
| W3-196 | Applications | kolourpaint | Painter's palette shield with five alchemical pigment gems | Hero | P2 | org.kde.kolourpaint |  |
| W3-197 | Applications | simple-scan | White manuscript passing beneath a blue scanning beam | Hero | P2 | org.gnome.SimpleScan |  |
| W3-198 | Applications | sane | Scanner plate with a green verification rune | Hero | P3 | xsane; scanimage |  |
| W3-199 | Applications | systemsettings | Steel gear ring enclosing a blue witcher adjustment rune | Hero | P0 | org.kde.systemsettings |  |
| W3-200 | Applications | plasma-discover | Blue shopping satchel with a star-shaped software rune | Hero | P0 | org.kde.discover |  |
| W3-201 | Applications | rofi | Compact black launcher plaque with a silver search sigil | Hero | P0 |  |  |
| W3-202 | Applications | wofi | Minimal Wayland launcher rune on a dark steel plate | Hero | P1 |  |  |
| W3-203 | Applications | fuzzel | Fuzzy search rune surrounded by tiny glowing sparks | Hero | P1 |  |  |
| W3-204 | Applications | walker | Traveler bootprint crossing a launcher search scroll | Hero | P1 |  |  |
| W3-205 | Applications | waybar | Long steel status bar with miniature Witcher sign glyphs | Hero | P0 |  |  |
| W3-206 | Applications | hyprland | Cyan-purple fractured H rune like a magical window rift | Hero | P0 | Hyprland |  |
| W3-207 | Applications | hyprpaper | Layered wallpaper scrolls with a cyan Hypr rune | Hero | P0 |  |  |
| W3-208 | Applications | hyprlock | Obsidian lock shield with a cyan Hypr fracture | Hero | P0 |  |  |
| W3-209 | Applications | hypridle | Hourglass inside a cyan Hypr window frame | Hero | P1 |  |  |
| W3-210 | Applications | awww | Triple wallpaper scrolls rotating in a smooth magic loop | Hero | P1 | swww |  |
| W3-211 | Applications | waypaper | Wallpaper parchment pinned to a Wayland steel board | Hero | P1 |  |  |
| W3-212 | Applications | nwg-look | Mirror panel with GTK runes and a small styling brush | Hero | P2 |  |  |
| W3-213 | Applications | qt5ct | Qt rune with a five-point configuration cog | Hero | P2 |  |  |
| W3-214 | Applications | qt6ct | Qt rune with a six-point configuration cog | Hero | P2 |  |  |
| W3-215 | Applications | kvantum | Glass-like K crystal with theme facets and metallic edges | Hero | P1 | kvantummanager |  |
| W3-216 | Applications | lxappearance | Paintbrush over a lightweight theme parchment | Hero | P2 |  |  |
| W3-217 | Applications | azote | Wallpaper board with a bright A-shaped pin | Hero | P3 |  |  |
| W3-218 | Applications | nwg-displays | Two monitor shields arranged by a blue layout rune | Hero | P1 |  |  |
| W3-219 | Applications | wdisplays | Wayland monitor pair with directional arrangement arrows | Hero | P1 |  |  |
| W3-220 | Applications | nwg-shell-config | Wayland shell crest with a configuration hammer | Hero | P2 |  |  |
| W3-221 | Actions/UI | document-new | Blank parchment with a glowing plus rune | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-222 | Actions/UI | document-open | Open leather folio with outward arrow | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-223 | Actions/UI | document-save | Archive chest with downward seal | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-224 | Actions/UI | document-save-as | Archive chest with quill-tag rune | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-225 | Actions/UI | document-print | Dwarven press stamping parchment | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-226 | Actions/UI | document-properties | Contract parchment with a gear seal | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-227 | Actions/UI | edit-cut | Twin silver shears | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-228 | Actions/UI | edit-copy | Two overlapping contract sheets | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-229 | Actions/UI | edit-paste | Clipboard shield receiving parchment | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-230 | Actions/UI | edit-delete | Broken parchment over red slash | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-231 | Actions/UI | edit-undo | Backward curling Aard-like arrow | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-232 | Actions/UI | edit-redo | Forward curling Aard-like arrow | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-233 | Actions/UI | edit-select-all | Selection frame around four runes | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-234 | Actions/UI | edit-find | Magnifying lens over a contract | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-235 | Actions/UI | edit-find-replace | Lens plus exchange arrows | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-236 | Actions/UI | go-home | Kaer Morhen keep silhouette | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-237 | Actions/UI | go-up | Silver sword-point arrow upward | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-238 | Actions/UI | go-down | Silver sword-point arrow downward | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-239 | Actions/UI | go-next | Right-pointing crossbow bolt | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-240 | Actions/UI | go-previous | Left-pointing crossbow bolt | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-241 | Actions/UI | go-first | Double-left rune arrows | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-242 | Actions/UI | go-last | Double-right rune arrows | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-243 | Actions/UI | go-jump | Leaping wolf over an arrow | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-244 | Actions/UI | go-top | Arrow toward mountain peak | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-245 | Actions/UI | go-bottom | Arrow toward cave floor | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-246 | Actions/UI | view-refresh | Circular swallow flight rune | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-247 | Actions/UI | view-fullscreen | Four expanding corner blades | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-248 | Actions/UI | view-restore | Four contracting corner blades | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-249 | Actions/UI | view-grid | Nine engraved stone tiles | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-250 | Actions/UI | view-list-text | Three parchment rows | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-251 | Actions/UI | view-sort-ascending | Ascending rune bars | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-252 | Actions/UI | view-sort-descending | Descending rune bars | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-253 | Actions/UI | view-filter | Alchemy funnel | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-254 | Actions/UI | view-hidden | Half-veiled eye medallion | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-255 | Actions/UI | zoom-in | Lens with plus sigil | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-256 | Actions/UI | zoom-out | Lens with minus sigil | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-257 | Actions/UI | zoom-fit-best | Lens around framed landscape | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-258 | Actions/UI | zoom-original | Lens with 1:1 rune | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-259 | Actions/UI | window-close | Crossed short blades | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-260 | Actions/UI | window-minimize | Low horizontal steel bar | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-261 | Actions/UI | window-maximize | Square steel frame | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-262 | Actions/UI | window-restore | Overlapping steel frames | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-263 | Actions/UI | window-pin | Dagger pinning parchment | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-264 | Actions/UI | window-keep-above | Crown over window plaque | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-265 | Actions/UI | window-keep-below | Window plaque under stone slab | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-266 | Actions/UI | tab-new | New parchment tab with plus | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-267 | Actions/UI | tab-close | Small tab with blade-cross | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-268 | Actions/UI | list-add | List parchment with plus rune | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-269 | Actions/UI | list-remove | List parchment with minus rune | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-270 | Actions/UI | media-playback-start | Right-facing play spearhead | Glyph | P0 |  | Optimise separately for 16/22/24 px |
| W3-271 | Actions/UI | media-playback-pause | Twin standing sword blades | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-272 | Actions/UI | media-playback-stop | Solid obsidian stop tile | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-273 | Actions/UI | media-skip-forward | Double spearhead right | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-274 | Actions/UI | media-skip-backward | Double spearhead left | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-275 | Actions/UI | media-seek-forward | Fast triple spearhead right | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-276 | Actions/UI | media-seek-backward | Fast triple spearhead left | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-277 | Actions/UI | media-record | Blood-red recording gem | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-278 | Actions/UI | media-eject | Eject wedge over base line | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-279 | Actions/UI | media-playlist-repeat | Twin chasing swallow arrows | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-280 | Actions/UI | media-playlist-shuffle | Crossing path arrows like trail signs | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-281 | Actions/UI | address-book-new | Fresh contact ledger with a silver clasp and small plus rune | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-282 | Actions/UI | appointment-new | New calendar parchment stamped with a red wax date seal | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-283 | Actions/UI | call-start | Raised communication horn with an alchemy-green start rune | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-284 | Actions/UI | call-stop | Lowered communication horn cut by a Witcher-red stop slash | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-285 | Actions/UI | microphone-sensitivity-high | Mic rune with three waves | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-286 | Actions/UI | microphone-sensitivity-medium | Mic rune with two waves | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-287 | Actions/UI | microphone-sensitivity-low | Mic rune with one wave | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-288 | Actions/UI | microphone-sensitivity-muted | Mic rune under red slash | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-289 | Actions/UI | camera-photo | Scrying camera with bright aperture | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-290 | Actions/UI | camera-video | Scrying camera with film rune | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-291 | Actions/UI | camera-switch | Twin camera eyes with swap arrows | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-292 | Actions/UI | mail-send | Raven releasing a sealed letter | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-293 | Actions/UI | mail-receive | Raven catching a sealed letter | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-294 | Actions/UI | mail-reply-sender | Letter with backward raven arrow | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-295 | Actions/UI | mail-reply-all | Letter with twin backward arrows | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-296 | Actions/UI | mail-forward | Letter with forward bolt arrow | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-297 | Actions/UI | mail-mark-read | Opened letter with eye rune | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-298 | Actions/UI | mail-mark-unread | Sealed letter with dark eye | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-299 | Actions/UI | folder-new | Leather folder with plus clasp | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-300 | Actions/UI | folder-open | Open folder with lifted clasp | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-301 | Actions/UI | bookmark-new | Red ribbon bookmark with plus | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-302 | Actions/UI | bookmark-remove | Red ribbon cut by minus rune | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-303 | Actions/UI | insert-image | Picture parchment with plus | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-304 | Actions/UI | insert-link | Twin chain links | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-305 | Actions/UI | insert-text | Quill over a text rune | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-306 | Actions/UI | format-text-bold | Heavy engraved B rune | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-307 | Actions/UI | format-text-italic | Slanted engraved I rune | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-308 | Actions/UI | format-text-underline | U rune over steel underline | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-309 | Actions/UI | format-justify-left | Left-aligned parchment lines | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-310 | Actions/UI | format-justify-center | Centered parchment lines | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-311 | Actions/UI | format-justify-right | Right-aligned parchment lines | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-312 | Actions/UI | format-justify-fill | Even parchment block lines | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-313 | Actions/UI | object-rotate-left | Shield rotating counterclockwise | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-314 | Actions/UI | object-rotate-right | Shield rotating clockwise | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-315 | Actions/UI | object-flip-horizontal | Mirror blades left-right | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-316 | Actions/UI | object-flip-vertical | Mirror blades up-down | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-317 | Actions/UI | system-search | Wolf eye behind magnifying lens | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-318 | Actions/UI | system-run | Bootprint launching from a rune circle | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-319 | Actions/UI | system-lock-screen | Quen shield with padlock | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-320 | Actions/UI | system-log-out | Open gate with outward arrow | Glyph | P1 |  | Optimise separately for 16/22/24 px |
| W3-321 | Places/Folders | folder | Default black leather folio with wolf clasp | Emblem | P0 |  | Folder family should share silhouette and clasp geometry |
| W3-322 | Places/Folders | folder-home | Kaer Morhen home crest on folder | Emblem | P0 |  | Folder family should share silhouette and clasp geometry |
| W3-323 | Places/Folders | folder-desktop | Monitor rune on folder | Emblem | P0 |  | Folder family should share silhouette and clasp geometry |
| W3-324 | Places/Folders | folder-documents | Contract scroll on folder | Emblem | P0 |  | Folder family should share silhouette and clasp geometry |
| W3-325 | Places/Folders | folder-download | Downward bolt into folder | Emblem | P0 |  | Folder family should share silhouette and clasp geometry |
| W3-326 | Places/Folders | folder-music | Lute note on folder | Emblem | P0 |  | Folder family should share silhouette and clasp geometry |
| W3-327 | Places/Folders | folder-pictures | Landscape miniature on folder | Emblem | P0 |  | Folder family should share silhouette and clasp geometry |
| W3-328 | Places/Folders | folder-videos | Film strip on folder | Emblem | P0 |  | Folder family should share silhouette and clasp geometry |
| W3-329 | Places/Folders | folder-publicshare | Open hands sharing a scroll | Emblem | P0 |  | Folder family should share silhouette and clasp geometry |
| W3-330 | Places/Folders | folder-templates | Stencil rune on folder | Emblem | P0 |  | Folder family should share silhouette and clasp geometry |
| W3-331 | Places/Folders | folder-git | Forked branch rune on folder | Emblem | P0 |  | Folder family should share silhouette and clasp geometry |
| W3-332 | Places/Folders | folder-github | Octocat familiar seal on folder | Emblem | P0 |  | Folder family should share silhouette and clasp geometry |
| W3-333 | Places/Folders | folder-code | Angle-bracket rune on folder | Emblem | P0 |  | Folder family should share silhouette and clasp geometry |
| W3-334 | Places/Folders | folder-dev | Hammer-and-rune developer crest | Emblem | P0 |  | Folder family should share silhouette and clasp geometry |
| W3-335 | Places/Folders | folder-projects | Bound project maps in folder | Emblem | P0 |  | Folder family should share silhouette and clasp geometry |
| W3-336 | Places/Folders | folder-games | Crossed controller glyphs | Emblem | P0 |  | Folder family should share silhouette and clasp geometry |
| W3-337 | Places/Folders | folder-steam | Steam gear seal on folder | Emblem | P0 |  | Folder family should share silhouette and clasp geometry |
| W3-338 | Places/Folders | folder-mods | Puzzle-rune medallion on folder | Emblem | P0 |  | Folder family should share silhouette and clasp geometry |
| W3-339 | Places/Folders | folder-comfyui | Node graph etched on folder | Emblem | P0 |  | Folder family should share silhouette and clasp geometry |
| W3-340 | Places/Folders | folder-ai | Glowing neural crystal on folder | Emblem | P0 |  | Folder family should share silhouette and clasp geometry |
| W3-341 | Places/Folders | folder-models | Stacked arcane model tablets | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-342 | Places/Folders | folder-lora | Braided LoRA rune ribbon | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-343 | Places/Folders | folder-workflows | Connected node trail on folder | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-344 | Places/Folders | folder-images | Framed image rune | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-345 | Places/Folders | folder-screenshots | Capture corners over folder | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-346 | Places/Folders | folder-wallpapers | Rolled tapestry on folder | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-347 | Places/Folders | folder-icons | Tiny medallion collection | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-348 | Places/Folders | folder-themes | Palette shield on folder | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-349 | Places/Folders | folder-fonts | Illuminated A manuscript | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-350 | Places/Folders | folder-archive | Iron archive clasp | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-351 | Places/Folders | folder-backup | Circular time rune on folder | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-352 | Places/Folders | folder-cloud | Cloud crest on folder | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-353 | Places/Folders | folder-network | Linked tower nodes | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-354 | Places/Folders | folder-shared | Twin handshake runes | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-355 | Places/Folders | folder-remote | Distant tower with signal waves | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-356 | Places/Folders | folder-temp | Melting ice rune on folder | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-357 | Places/Folders | folder-cache | Dusty rune pile on folder | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-358 | Places/Folders | folder-config | Small gear seal on folder | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-359 | Places/Folders | folder-system | Steel gear crest | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-360 | Places/Folders | folder-root | Ancient tree-root sigil | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-361 | Places/Folders | user-home | Kaer Morhen keep with hearth glow | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-362 | Places/Folders | user-desktop | Desktop desk under wolf banner | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-363 | Places/Folders | user-trash | Discard barrel with broken rune scraps | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-364 | Places/Folders | user-bookmarks | Leather ribbon bundle | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-365 | Places/Folders | network-workgroup | Cluster of village towers linked by roads | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-366 | Places/Folders | network-server | Fortified server keep with signal pennant | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-367 | Places/Folders | network-cloud | Cloud citadel over network nodes | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-368 | Places/Folders | computer | Witcher workstation altar with screen crystal | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-369 | Places/Folders | start-here | Crossroads signpost with wolf medallion | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-370 | Places/Folders | recent | Clock over recent contract stack | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-371 | Places/Folders | search | Map table with magnifying lens | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-372 | Places/Folders | favorites | Golden swallow star charm | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-373 | Places/Folders | important | Red contract exclamation seal | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-374 | Places/Folders | downloads | Crate receiving falling scrolls | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-375 | Places/Folders | documents | Stack of signed contracts | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-376 | Places/Folders | music | Lute resting against a tavern stool | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-377 | Places/Folders | pictures | Painted landscape in carved frame | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-378 | Places/Folders | videos | Film-reel-like scrying wheel | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-379 | Places/Folders | desktop | Desk with candle and monitor crystal | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-380 | Places/Folders | trash-empty | Clean iron discard barrel | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-381 | Places/Folders | trash-full | Overflowing discard barrel of scraps | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-382 | Places/Folders | mount-point | Stone docking pedestal with chain | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-383 | Places/Folders | portable-storage | Travel chest with carrying strap | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-384 | Places/Folders | cloud-storage | Floating vault chest on a cloud rune | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-385 | Places/Folders | vault | Heavy Nilfgaardian vault door | Emblem | P1 |  | Folder family should share silhouette and clasp geometry |
| W3-386 | Status/Panel/Waybar | battery-full | Charged green mutagen vial battery | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-387 | Status/Panel/Waybar | battery-good | Three-quarter mutagen vial | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-388 | Status/Panel/Waybar | battery-050 | Half-filled mutagen vial | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-389 | Status/Panel/Waybar | battery-low | Low amber mutagen vial | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-390 | Status/Panel/Waybar | battery-caution | Red nearly empty mutagen vial | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-391 | Status/Panel/Waybar | battery-empty | Empty cracked mutagen vial | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-392 | Status/Panel/Waybar | battery-050-charging | Half-filled mutagen vial with lightning rune | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-393 | Status/Panel/Waybar | battery-full-charging | Full vial with lightning | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-394 | Status/Panel/Waybar | battery-low-charging | Low vial with lightning | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-395 | Status/Panel/Waybar | ac-adapter | Power rune on a plugged cable talisman | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-396 | Status/Panel/Waybar | network-wired | Linked chain nodes with cable | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-397 | Status/Panel/Waybar | network-wired-disconnected | Broken chain nodes | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-398 | Status/Panel/Waybar | network-wireless-100 | Four radio arcs over tower | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-399 | Status/Panel/Waybar | network-wireless-connected-75 | Three radio arcs over tower | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-400 | Status/Panel/Waybar | network-wireless-connected-50 | Two radio arcs over tower | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-401 | Status/Panel/Waybar | network-wireless-connected-25 | One radio arc over tower | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-402 | Status/Panel/Waybar | network-wireless-disconnected | Tower crossed by slash | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-403 | Status/Panel/Waybar | network-wireless-hotspot | Tower inside concentric ward | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-404 | Status/Panel/Waybar | network-vpn | Quen shield over network link | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-405 | Status/Panel/Waybar | network-error | Network chain with red warning shard | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-406 | Status/Panel/Waybar | network-bluetooth-activated | Blue tooth-rune glowing | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-407 | Status/Panel/Waybar | bluetooth-disabled | Blue tooth-rune under slash | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-408 | Status/Panel/Waybar | bluetooth-paired | Twin tooth-runes linked | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-409 | Status/Panel/Waybar | audio-volume-high | Silver horn with three waves | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-410 | Status/Panel/Waybar | audio-volume-medium | Silver horn with two waves | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-411 | Status/Panel/Waybar | audio-volume-low | Silver horn with one wave | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-412 | Status/Panel/Waybar | audio-volume-muted | Silver horn crossed out | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-413 | Status/Panel/Waybar | mic-on | Bright microphone rune | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-414 | Status/Panel/Waybar | mic-off | Muted microphone rune | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-415 | Status/Panel/Waybar | camera-on | Open scrying eye camera | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-416 | Status/Panel/Waybar | camera-off | Closed scrying eye under slash | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-417 | Status/Panel/Waybar | brightness-high | Sun-disc with eight rays | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-418 | Status/Panel/Waybar | screen-brightness-medium | Sun-disc with four rays | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-419 | Status/Panel/Waybar | brightness-low | Dim crescent sun-disc | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-420 | Status/Panel/Waybar | input-keyboard-brightness | Keyboard plate with glow runes | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-421 | Status/Panel/Waybar | redshift-status-on | Moon over warm ember glow | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-422 | Status/Panel/Waybar | weather-clear | Toussaint sun crest | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-423 | Status/Panel/Waybar | weather-few-clouds | Sun behind small Skellige cloud | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-424 | Status/Panel/Waybar | weather-clouds | Layered storm clouds | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-425 | Status/Panel/Waybar | weather-overcast | Dense grey Skellige sky | Glyph | P0 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-426 | Status/Panel/Waybar | weather-showers | Rain over Kaer Trolde roof | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-427 | Status/Panel/Waybar | weather-rain | Heavy rain streaks over shield | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-428 | Status/Panel/Waybar | weather-storm | Lightning over Wild Hunt cloud | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-429 | Status/Panel/Waybar | weather-snow | Snowflake rune over mountain | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-430 | Status/Panel/Waybar | weather-fog | Mist bands over swamp reeds | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-431 | Status/Panel/Waybar | weather-windy | Three wind strokes around swallow feather | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-432 | Status/Panel/Waybar | temperature-normal | Thermometer with pale rune | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-433 | Status/Panel/Waybar | temperature-warm | Red hot thermometer with Igni spark | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-434 | Status/Panel/Waybar | cpu-usage-low | CPU crystal with one lit quadrant | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-435 | Status/Panel/Waybar | cpu-usage-medium | CPU crystal half lit | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-436 | Status/Panel/Waybar | cpu-usage-high | CPU crystal fully glowing | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-437 | Status/Panel/Waybar | memory-usage-low | Memory tablet with one lit bar | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-438 | Status/Panel/Waybar | memory-usage-medium | Memory tablet with two lit bars | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-439 | Status/Panel/Waybar | memory-usage-high | Memory tablet with three lit bars | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-440 | Status/Panel/Waybar | gpu-usage-low | GPU crystal with one rune lit | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-441 | Status/Panel/Waybar | gpu-usage-medium | GPU crystal half lit | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-442 | Status/Panel/Waybar | gpu-usage-high | GPU crystal blazing | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-443 | Status/Panel/Waybar | disk-idle | Disk platter at rest | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-444 | Status/Panel/Waybar | disk-busy | Spinning disk platter with motion sparks | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-445 | Status/Panel/Waybar | disk-warning | Disk platter with amber crack | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-446 | Status/Panel/Waybar | software-updates-inactive | Closed package chest with check rune | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-447 | Status/Panel/Waybar | software-updates-updates | Package chest with blue sparkle | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-448 | Status/Panel/Waybar | software-updates-important | Package chest with red warning seal | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-449 | Status/Panel/Waybar | security-high | Quen shield fully lit | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-450 | Status/Panel/Waybar | security-medium | Quen shield half lit | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-451 | Status/Panel/Waybar | security-low | Cracked Quen shield | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-452 | Status/Panel/Waybar | software-updates-security | Quen shield with circular arrow | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-453 | Status/Panel/Waybar | notification-inactive | Silent bell talisman | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-454 | Status/Panel/Waybar | notification-active | Bell talisman with blue spark | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-455 | Status/Panel/Waybar | notification-important | Bell talisman with red gem | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-456 | Status/Panel/Waybar | notification-disabled | Moon rune over muted bell | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-457 | Status/Panel/Waybar | mail-unread | Sealed raven letter | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-458 | Status/Panel/Waybar | mail-read | Opened raven letter | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-459 | Status/Panel/Waybar | download-active | Arrow falling into crate | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-460 | Status/Panel/Waybar | upload-active | Arrow rising from crate | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-461 | Status/Panel/Waybar | sync-idle | Twin swallow arrows at rest | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-462 | Status/Panel/Waybar | sync-active | Twin swallow arrows glowing | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-463 | Status/Panel/Waybar | sync-error | Broken sync ring | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-464 | Status/Panel/Waybar | media-playback-playing | Small play spearhead glowing | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-465 | Status/Panel/Waybar | media-playback-paused | Twin pause blades | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-466 | Status/Panel/Waybar | media-playback-stopped | Dark stop stone | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-467 | Status/Panel/Waybar | input-caps-on | Upward rune arrow inside keycap | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-468 | Status/Panel/Waybar | input-num-on | Number rune inside keycap | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-469 | Status/Panel/Waybar | scroll-lock-on | Scroll rune inside keycap | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-470 | Status/Panel/Waybar | battery-profile-performance | Red wolf claw performance crest | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-471 | Status/Panel/Waybar | battery-profile-balanced | Balanced scales over battery | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-472 | Status/Panel/Waybar | battery-profile-powersave | Green leaf over battery | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-473 | Status/Panel/Waybar | workspace-active | Lit runestone workspace | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-474 | Status/Panel/Waybar | workspace-inactive | Dark runestone workspace | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-475 | Status/Panel/Waybar | window-urgent | Window rune with red pulse | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-476 | Status/Panel/Waybar | tray-overflow | Small pouch with three hidden glyphs | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-477 | Status/Panel/Waybar | recording-active | Blood-red recording crystal | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-478 | Status/Panel/Waybar | screen-sharing | Monitor crystal projecting outward | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-479 | Status/Panel/Waybar | idle-inhibitor-on | Open eye over hourglass | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-480 | Status/Panel/Waybar | idle-inhibitor-off | Closed eye over hourglass | Glyph | P1 |  | Waybar/status family; optimise for monochrome and tiny sizes |
| W3-481 | Devices | computer-desktop | Dark workstation altar with monitor crystal | Emblem | P1 |  |  |
| W3-482 | Devices | computer-laptop | Folded travel workstation with glowing screen | Emblem | P1 |  |  |
| W3-483 | Devices | computer-tablet | Slate tablet framed in steel | Emblem | P1 |  |  |
| W3-484 | Devices | phone | Handheld communication rune-slate | Emblem | P1 |  |  |
| W3-485 | Devices | smartphone | Tall black scrying slate | Emblem | P1 |  |  |
| W3-486 | Devices | camera | Mechanical scrying camera | Emblem | P1 |  |  |
| W3-487 | Devices | camera-web | Round eye-camera on a small stand | Emblem | P1 |  |  |
| W3-488 | Devices | printer | Dwarven printing press | Emblem | P1 |  |  |
| W3-489 | Devices | scanner | Flat scanning altar with light beam | Emblem | P1 |  |  |
| W3-490 | Devices | input-keyboard | Steel keyboard plate with rune keys | Emblem | P1 |  |  |
| W3-491 | Devices | input-mouse | Mouse familiar shaped into input device | Emblem | P1 |  |  |
| W3-492 | Devices | input-gaming | Controller shield with twin sticks | Emblem | P1 |  |  |
| W3-493 | Devices | joystick | Flight lever on circular iron base | Emblem | P1 |  |  |
| W3-494 | Devices | audio-headphones | Silver ear-guards around a sound crystal | Emblem | P1 |  |  |
| W3-495 | Devices | audio-headset | Headphones with microphone boom | Emblem | P1 |  |  |
| W3-496 | Devices | audio-input-microphone | Studio speaking rune on stand | Emblem | P1 |  |  |
| W3-497 | Devices | audio-speakers | Twin sound towers with horn runes | Emblem | P1 |  |  |
| W3-498 | Devices | audio-card | Copper audio circuit plate | Emblem | P1 |  |  |
| W3-499 | Devices | video-display | Standalone viewing crystal in metal frame | Emblem | P1 |  |  |
| W3-500 | Devices | monitor-dual | Twin viewing crystals on one stand | Emblem | P1 |  |  |
| W3-501 | Devices | tv | Wide scrying panel with heavy frame | Emblem | P1 |  |  |
| W3-502 | Devices | projector | Light-projecting crystal box | Emblem | P1 |  |  |
| W3-503 | Devices | drive-harddisk | Black iron disk vault | Emblem | P1 |  |  |
| W3-504 | Devices | harddisk-external | Travel disk vault with cable | Emblem | P1 |  |  |
| W3-505 | Devices | ssd | Slim etched solid-state data tablet | Emblem | P1 |  |  |
| W3-506 | Devices | nvme | Narrow rune-studded NVMe blade | Emblem | P1 |  |  |
| W3-507 | Devices | drive-removable-media-usb-pendrive | Small silver data talisman with USB prongs | Emblem | P1 |  |  |
| W3-508 | Devices | media-flash-sd-mmc | Tiny memory rune card | Emblem | P1 |  |  |
| W3-509 | Devices | drive-optical | Disc chamber with silver tray | Emblem | P1 |  |  |
| W3-510 | Devices | media-optical | Shining alchemical data disc | Emblem | P1 |  |  |
| W3-511 | Devices | media-floppy | Ancient square save tablet | Emblem | P2 |  |  |
| W3-512 | Devices | network-card | Linked-node circuit plaque | Emblem | P2 |  |  |
| W3-513 | Devices | router | Signal tower box with four antenna runes | Emblem | P2 |  |  |
| W3-514 | Devices | modem | Compact communication box with wave glyph | Emblem | P2 |  |  |
| W3-515 | Devices | bluetooth-adapter | Small blue tooth-rune dongle | Emblem | P2 |  |  |
| W3-516 | Devices | wifi-adapter | Tiny radio ward dongle | Emblem | P2 |  |  |
| W3-517 | Devices | gpu | Large graphic crystal board with fan rune | Emblem | P2 |  |  |
| W3-518 | Devices | cpu | Square processor sigil with etched contacts | Emblem | P2 |  |  |
| W3-519 | Devices | memory | Long memory talisman with chip runes | Emblem | P2 |  |  |
| W3-520 | Devices | motherboard | Dwarven mainboard map of circuits | Emblem | P2 |  |  |
| W3-521 | Devices | battery | Portable mutagen-cell battery | Emblem | P2 |  |  |
| W3-522 | Devices | battery-ups | Heavy backup power chest | Emblem | P2 |  |  |
| W3-523 | Devices | vr-headset | Twin-lens spectral visor | Emblem | P2 |  |  |
| W3-524 | Devices | smartwatch | Wrist-mounted clock rune crystal | Emblem | P2 |  |  |
| W3-525 | Devices | controller-wheel | Racing wheel carved from black steel | Emblem | P2 |  |  |
| W3-526 | MIME/Filetypes | text-plain | Simple parchment page with text lines | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-527 | MIME/Filetypes | text-markdown | Parchment page with engraved M↓ rune | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-528 | MIME/Filetypes | text-code | Parchment page with angle-bracket runes | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-529 | MIME/Filetypes | text-x-shellscript | Dark parchment terminal page with prompt rune | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-530 | MIME/Filetypes | text-x-python | Blue-yellow serpent pair on code parchment | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-531 | MIME/Filetypes | text-javascript | Golden JS rune on dark code parchment | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-532 | MIME/Filetypes | text-typescript | Blue TS rune on code parchment | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-533 | MIME/Filetypes | application-json | Curly-brace runes on parchment | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-534 | MIME/Filetypes | text-yaml | Red Y rune on configuration parchment | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-535 | MIME/Filetypes | text-toml | Silver T rune on configuration parchment | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-536 | MIME/Filetypes | text-xml | Red angle-tag rune on parchment | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-537 | MIME/Filetypes | text-html | Orange shield-rune on web parchment | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-538 | MIME/Filetypes | text-css | Blue shield-rune on style parchment | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-539 | MIME/Filetypes | text-log | Scroll with timestamp marks | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-540 | MIME/Filetypes | text-config | Gear seal on parchment | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-541 | MIME/Filetypes | text-diff | Red-green split parchment | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-542 | MIME/Filetypes | text-license | Official wax seal on legal parchment | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-543 | MIME/Filetypes | application-pdf | Red PDF contract seal | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-544 | MIME/Filetypes | application-epub+zip | Green open e-book grimoire | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-545 | MIME/Filetypes | application-rtf | Blue rich-text parchment | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-546 | MIME/Filetypes | application-msword | Blue W rune on office folio | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-547 | MIME/Filetypes | application-vnd.oasis.opendocument.text | Blue quill folio | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-548 | MIME/Filetypes | application-vnd.oasis.opendocument.spreadsheet | Green grid ledger | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-549 | MIME/Filetypes | application-vnd.ms-excel | Green X rune on grid ledger | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-550 | MIME/Filetypes | application-vnd.oasis.opendocument.presentation | Orange presentation board | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-551 | MIME/Filetypes | application-vnd.ms-powerpoint | Orange P rune on presentation board | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-552 | MIME/Filetypes | application-vnd.oasis.opendocument.database | Stacked dark data cylinders | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-553 | MIME/Filetypes | application-sql | Database cylinders with SQL rune | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-554 | MIME/Filetypes | application-x-archive | Iron-bound archive chest | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-555 | MIME/Filetypes | application-zip | Compressed chest with zipper-like clasp | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-556 | MIME/Filetypes | application-x-7z-compressed | Seven-notch compression seal | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-557 | MIME/Filetypes | application-vnd.rar | Three bound archive tomes | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-558 | MIME/Filetypes | application-x-tar | Tar-black archive bundle | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-559 | MIME/Filetypes | application-gzip | Archive bundle under pressure gauge | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-560 | MIME/Filetypes | application-x-bzip | Blue compressed archive bundle | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-561 | MIME/Filetypes | application-xz | Silver XZ seal on archive bundle | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-562 | MIME/Filetypes | application-zstd | Zstd rune on compact archive plate | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-563 | MIME/Filetypes | application-vnd.appimage | Portable app crystal with base pedestal | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-564 | MIME/Filetypes | application-flatpak | Stacked package cubes | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-565 | MIME/Filetypes | application-vnd.snap | Snapped rune loop package seal | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-566 | MIME/Filetypes | application-x-executable | Steel gear with green play rune | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-567 | MIME/Filetypes | application-x-sharedlib | Linked library chain glyph | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-568 | MIME/Filetypes | application-x-deb | Debian swirl stamped on package chest | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-569 | MIME/Filetypes | application-x-rpm | Red package gear seal | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-570 | MIME/Filetypes | package-x-generic | Generic package crate | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-571 | MIME/Filetypes | application-x-cd-image | Optical disc over archive case | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-572 | MIME/Filetypes | application-x-bittorrent | Blue torrent spiral on parchment | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-573 | MIME/Filetypes | font-x-generic | Illuminated A type specimen | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-574 | MIME/Filetypes | application-certificate | Signed certificate scroll with seal | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-575 | MIME/Filetypes | application-key | Silver cryptographic key on dark parchment | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-576 | MIME/Filetypes | encrypted | Locked parchment with Quen shield | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-577 | MIME/Filetypes | image-x-generic | Landscape painting in carved frame | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-578 | MIME/Filetypes | image-jpeg | Landscape frame with JPEG rune | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-579 | MIME/Filetypes | image-png | Crystal-clear landscape frame with PNG rune | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-580 | MIME/Filetypes | image-webp | Web-shaped image frame | Emblem | P1 |  | Keep strong family resemblance by file class |
| W3-581 | MIME/Filetypes | image-svg+xml | Vector knot on transparent frame | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-582 | MIME/Filetypes | image-gif | Animated double-frame image tile | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-583 | MIME/Filetypes | image-x-dcraw | Unpolished photo crystal | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-584 | MIME/Filetypes | image-heif | High-efficiency image crystal | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-585 | MIME/Filetypes | image-tiff | Layered archival image parchment | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-586 | MIME/Filetypes | image-vnd.adobe.photoshop | Stacked painted layers with PS rune | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-587 | MIME/Filetypes | application-x-krita | Krita feather over layered canvas | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-588 | MIME/Filetypes | image-x-xcf | GIMP brush over layered canvas | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-589 | MIME/Filetypes | audio-generic | Music note on sound crystal | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-590 | MIME/Filetypes | audio-mp3 | Music note with MP3 rune | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-591 | MIME/Filetypes | audio-flac | Crystal waveform with FLAC rune | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-592 | MIME/Filetypes | audio-wav | Waveform parchment | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-593 | MIME/Filetypes | audio-ogg | Round OGG sound stone | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-594 | MIME/Filetypes | audio-opus | Purple opus waveform gem | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-595 | MIME/Filetypes | audio-m4a | Silver M4A audio tablet | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-596 | MIME/Filetypes | audio-playlist | List parchment with music runes | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-597 | MIME/Filetypes | video-generic | Film strip with play rune | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-598 | MIME/Filetypes | video-mp4 | Film strip with MP4 plaque | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-599 | MIME/Filetypes | video-mkv | Dark film vault with MKV rune | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-600 | MIME/Filetypes | video-webm | Web-like film rune | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-601 | MIME/Filetypes | video-avi | Classic film reel with AVI plate | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-602 | MIME/Filetypes | video-mov | Polished film reel with MOV seal | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-603 | MIME/Filetypes | video-mpeg | Film strip with MPEG rune | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-604 | MIME/Filetypes | model-3d | Wireframe wyvern head | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-605 | MIME/Filetypes | model-blend | Orange forge-eye 3D file rune | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-606 | MIME/Filetypes | model-stl | Triangulated steel sculpture | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-607 | MIME/Filetypes | model-obj | Stone bust with OBJ rune | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-608 | MIME/Filetypes | model-fbx | Rigged puppet rune | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-609 | MIME/Filetypes | model-glb | Faceted 3D crystal | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-610 | MIME/Filetypes | model-gltf | Linked 3D node crystal | Emblem | P2 |  | Keep strong family resemblance by file class |
| W3-611 | Categories/Misc | applications-accessories | Utility pouch with assorted witcher tools | Emblem | P1 |  |  |
| W3-612 | Categories/Misc | applications-development | Hammer and code-rune crossed | Emblem | P1 |  |  |
| W3-613 | Categories/Misc | applications-education | Oxenfurt scholar cap over grimoire | Emblem | P1 |  |  |
| W3-614 | Categories/Misc | applications-engineering | Dwarven gear with compass | Emblem | P1 |  |  |
| W3-615 | Categories/Misc | applications-games | Crossed controller and sword | Emblem | P1 |  |  |
| W3-616 | Categories/Misc | applications-graphics | Painter palette shield | Emblem | P1 |  |  |
| W3-617 | Categories/Misc | applications-internet | World orb with raven route lines | Emblem | P1 |  |  |
| W3-618 | Categories/Misc | applications-multimedia | Lute, film and sound crystal crest | Emblem | P1 |  |  |
| W3-619 | Categories/Misc | applications-office | Quill over ledger and contract | Emblem | P1 |  |  |
| W3-620 | Categories/Misc | applications-science | Alchemy retort and star chart | Emblem | P1 |  |  |
| W3-621 | Categories/Misc | applications-system | Heavy system gear with wolf rune | Emblem | P1 |  |  |
| W3-622 | Categories/Misc | applications-utilities | Belt pouch of tools | Emblem | P1 |  |  |
| W3-623 | Categories/Misc | preferences-desktop | Desktop crystal with gear seal | Emblem | P1 |  |  |
| W3-624 | Categories/Misc | preferences-system | System gear over Quen shield | Emblem | P1 |  |  |
| W3-625 | Categories/Misc | preferences-hardware | Gear and processor crystal | Emblem | P1 |  |  |
| W3-626 | Categories/Misc | preferences-network | Linked network tower sigil | Emblem | P1 |  |  |
| W3-627 | Categories/Misc | preferences-security | Quen shield with key | Emblem | P1 |  |  |
| W3-628 | Categories/Misc | preferences-appearance | Mirror and paintbrush | Emblem | P1 |  |  |
| W3-629 | Categories/Misc | preferences-keyboard | Rune keyboard plate | Emblem | P1 |  |  |
| W3-630 | Categories/Misc | preferences-mouse | Mouse familiar over gear | Emblem | P1 |  |  |
| W3-631 | Categories/Misc | preferences-display | Monitor crystal with sliders | Emblem | P2 |  |  |
| W3-632 | Categories/Misc | preferences-audio | Sound horn with sliders | Emblem | P2 |  |  |
| W3-633 | Categories/Misc | preferences-bluetooth | Blue tooth-rune with gear | Emblem | P2 |  |  |
| W3-634 | Categories/Misc | preferences-power | Mutagen battery with gear | Emblem | P2 |  |  |
| W3-635 | Categories/Misc | preferences-notifications | Bell talisman with gear | Emblem | P2 |  |  |
| W3-636 | Categories/Misc | preferences-users | Twin portrait cameos | Emblem | P2 |  |  |
| W3-637 | Categories/Misc | preferences-time | Clock rune with gear | Emblem | P2 |  |  |
| W3-638 | Categories/Misc | preferences-locale | Globe and language scroll | Emblem | P2 |  |  |
| W3-639 | Categories/Misc | preferences-storage | Disk vault with gear | Emblem | P2 |  |  |
| W3-640 | Categories/Misc | preferences-printer | Printing press with gear | Emblem | P2 |  |  |
| W3-641 | Categories/Misc | system-help | Question rune over open grimoire | Emblem | P2 |  |  |
| W3-642 | Categories/Misc | system-about | Information rune on wolf medallion | Emblem | P2 |  |  |
| W3-643 | Categories/Misc | system-software-install | Package chest with downward arrow | Emblem | P2 |  |  |
| W3-644 | Categories/Misc | system-software-update | Package chest with circular arrow | Emblem | P2 |  |  |
| W3-645 | Categories/Misc | system-shutdown | Power rune forged as a closed portal | Emblem | P2 |  |  |
