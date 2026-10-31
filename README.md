# Awesome Garry's Mod Open Source [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> A community-curated list of free, open-source Garry's Mod admin tools, gamemodes, frameworks, libraries, binary modules and developer tools.

This list covers projects whose source code you can read, run and learn from, for both server owners and addon developers. It is the free counterpart to paid marketplaces. **No leaked or paid addons, and no cheats, Lua stealers or exploit tools.**

**Know a project that's missing, or one that has been archived?** [Add it in two minutes](CONTRIBUTING.md). Developers are welcome to add their own projects.

### Tag legend

Project entries have two tags: **license**, then **main language**.

**License:** an [SPDX identifier](https://spdx.org/licenses/) such as `MIT`, `GPL-3.0` or `Unlicense` · `Custom` the repo has a license file that isn't a standard one, so read it before reusing code · `No license` the repo has no license file, so the author keeps all rights by default (ask before redistributing)

**Language:** the main language GitHub reports, such as `Lua`, `C++`, `Rust`

## Contents

- [Server Administration and Anti-Cheat](#server-administration-and-anti-cheat)
- [Gamemodes and Frameworks](#gamemodes-and-frameworks)
- [Addon Development Tools](#addon-development-tools)
- [Libraries and Binary Modules](#libraries-and-binary-modules)
- [Client Fixes and Performance](#client-fixes-and-performance)
- [Learning Resources and Communities](#learning-resources-and-communities)
- [Contributing](#contributing)

## Server Administration and Anti-Cheat

Admin mods, anti-cheat, moderation, hosting and other tools for running a server.

- [CFC Error Forwarder](https://github.com/CFC-Servers/cfc_err_forwarder) - Sends both server-side and client-side Lua errors to a Discord channel. `No license` `Lua`
- [EasyChat](https://github.com/Earu/EasyChat) - Modular chat replacement with an API that other addons can extend. `GPL-3.0` `Lua`
- [Falco's Prop Protection](https://github.com/FPtje/Falcos-Prop-protection) - Prop protection addon that controls who can touch, use and damage other players' props. `No license` `Lua`
- [Garry's Mod Family Sharing](https://github.com/C0nw0nk/Garrys-Mod-Family-Sharing) - Stops banned players from rejoining on Steam Family Sharing or alternate accounts. `Custom` `Lua`
- [garrysmod-docker](https://github.com/ceifa/garrysmod-docker) - Docker image for hosting a Garry's Mod dedicated server. `MIT` `Dockerfile`
- [gmod_discord_relay](https://github.com/troit5ky/gmod_discord_relay) - Relays chat between a Garry's Mod server and a Discord channel. `MIT` `Lua`
- [gmsv_serversecure](https://github.com/danielga/gmsv_serversecure) - Server binary module that mitigates known Source engine networking exploits. `Custom` `C++`
- [Nova Defender](https://github.com/Freilichtbuehne/nova-defender) - Server security addon combining anti-cheat, ban-evasion detection and VPN checks. `GPL-3.0` `Lua`
- [Server Creation Tool](https://github.com/Zeromix9/Server-Creation-Tool) - Desktop tool for creating dedicated game servers through SteamCMD. `GPL-3.0` `C#`
- [ULib](https://github.com/TeamUlysses/ulib) - Lua library for server development that ULX and many other admin addons are built on. `Custom` `Lua`
- [ULX](https://github.com/TeamUlysses/ulx) - Long-running admin mod with user groups, permissions, bans and an in-game menu. `Custom` `Lua`
- [xAdmin](https://github.com/TheXYZNetwork/xAdmin) - Free, basic administration system for Garry's Mod servers. `Unlicense` `Lua`

## Gamemodes and Frameworks

Complete gamemodes you can host, and frameworks for building your own. The base Sandbox and TTT gamemodes live in [Facepunch/garrysmod](https://github.com/Facepunch/garrysmod).

- [Begotten III](https://github.com/DETrooper/Begotten-III) - Public source release of the Begotten III dark-fantasy roleplay gamemode. `Custom` `Lua`
- [Cinema](https://github.com/PurrCoding/cinema) - Gamemode where players watch synchronised video streams together in a multiplayer theater. `GPL-3.0` `Lua`
- [DarkRP](https://github.com/FPtje/DarkRP) - Non-serious roleplay gamemode with jobs, an economy and a large ecosystem of addons. `MIT` `Lua`
- [Fretta13](https://github.com/JetBoom/fretta13) - Updated version of the Fretta base for building small round-based gamemodes. `Unlicense` `Lua`
- [Helix](https://github.com/NebulousCloud/helix) - Roleplay framework where servers build their own schemas and plugins on a shared core. `MIT` `Lua`
- [Lambda](https://github.com/GMLambda/Lambda) - Cooperative multiplayer gamemode for the Half-Life 2 series campaigns. `MIT` `Lua`
- [Lilia](https://github.com/LiliaFramework/Lilia) - Actively developed roleplay framework for building custom server schemas. `GPL-3.0` `Lua`
- [Murder](https://github.com/MechanicalMind/murder) - Social deduction gamemode where bystanders try to find a hidden murderer. `No license` `Lua`
- [NutScript](https://github.com/NutScript/NutScript) - Roleplay framework created by Chessnut and Black Tea, now continued by a community team. `MIT` `Lua`
- [Prop Hunt X2Z](https://github.com/Wolvin-NET/prophuntx) - Modernised, customisable version of the classic Prop Hunt hide-and-seek gamemode. `No license` `Lua`
- [TTT2](https://github.com/TTT-2/TTT2) - Extended Trouble in Terrorist Town with many more roles, a reworked HUD and APIs for addon developers. `No license` `Lua`
- [Zombie Survival](https://github.com/JetBoom/zombiesurvival) - Wave-based gamemode where human players hold out against player-controlled zombies. `Custom` `Lua`

## Addon Development Tools

Editors, linters, test runners, profilers and publishing tools, plus in-game creation tools.

- [BadCoderz](https://github.com/ExtReMLapin/BadCoderz) - In-game tool that finds unoptimised code in the addons running on a server. `MIT` `Lua`
- [fastgmad](https://github.com/WilliamVenner/fastgmad) - Fast reimplementation of gmad.exe and gmpublish.exe for packing and publishing addons. `Apache-2.0` `Rust`
- [FProfiler](https://github.com/FPtje/FProfiler) - In-game profiler that shows which functions and hooks take the most time. `LGPL-2.1` `Lua`
- [GLua API Snippets](https://github.com/luttje/glua-api-snippets) - Builds Lua Language Server annotations from the Garry's Mod wiki for IDE autocompletion. `MIT` `TypeScript`
- [glua.dev](https://github.com/CFC-Servers/glua.dev) - Web service that starts short-lived Garry's Mod servers for development and testing. `GPL-3.0` `TypeScript`
- [GLuaFixer](https://github.com/FPtje/GLuaFixer) - Linter and pretty-printer for Garry's Mod Lua, also known as glualint. `LGPL-2.1` `Haskell`
- [GLuaTest](https://github.com/CFC-Servers/GLuaTest) - Unit testing framework for GLua projects. `GPL-3.0` `Lua`
- [gm_content_optimizer](https://github.com/wrefgtzweve/gm_content_optimizer) - Reduces the file size of Source engine content such as addon assets. `GPL-3.0` `Python`
- [gmad](https://github.com/Facepunch/gmad) - Facepunch's command-line tool for creating and extracting .gma addon files. `No license` `C++`
- [gmpublisher](https://github.com/WilliamVenner/gmpublisher) - Desktop app for packing, publishing and updating Steam Workshop addons. `GPL-3.0` `Rust`
- [GTerm](https://github.com/Earu/GTerm) - External console for Garry's Mod with WebSocket and MCP support. `MIT` `C#`
- [pac3](https://github.com/CapsAdmin/pac3) - In-game editor for building custom player outfits and effects from models, props and particles. `GPL-3.0` `Lua`
- [StarfallEx](https://github.com/thegrb93/StarfallEx) - Sandboxed in-game scripting for building chips, similar to Expression 2 but written in Lua. `Custom` `Lua`
- [vscode-glua-enhanced](https://github.com/WilliamVenner/vscode-glua-enhanced) - VS Code extension with GLua autocompletion, wiki integration, snippets and a color palette. `GPL-3.0` `JavaScript`
- [vscode-gmod-glua-ls](https://github.com/Pollux12/vscode-gmod-glua-ls) - VS Code extension bundling a GLua language server, debugger and toolkit. `MIT` `TypeScript`

## Libraries and Binary Modules

Lua libraries, binary (C++, Rust, .NET) modules and base addons that other projects build on.

- [chttp](https://github.com/timschumi/gmod-chttp) - Binary module that provides an HTTP()-compatible function backed by curl. `MIT` `C++`
- [garrysmod_common](https://github.com/danielga/garrysmod_common) - Shared headers and build scripts for compiling Garry's Mod binary modules. `Custom` `C++`
- [gm_express](https://github.com/CFC-Servers/gm_express) - Out-of-band networking library for sending large amounts of data in both directions. `GPL-3.0` `Lua`
- [gm_luaerror](https://github.com/danielga/gm_luaerror) - Binary module that adds hooks for catching Lua errors on the client and server. `Custom` `C++`
- [gmod-rs](https://github.com/WilliamVenner/gmod-rs) - Rust library for writing Garry's Mod binary modules. `MIT` `Rust`
- [GmodDotNet](https://github.com/GmodNET/GmodDotNet) - Cross-platform platform for writing Garry's Mod modules in .NET. `MIT` `C#`
- [gmsv_reqwest](https://github.com/WilliamVenner/gmsv_reqwest) - Drop-in replacement for the HTTP function, built on the Rust reqwest library. `MIT` `Rust`
- [gmsv_workshop](https://github.com/WilliamVenner/gmsv_workshop) - Server module that adds steamworks.DownloadUGC for fetching Workshop items server-side. `MIT` `Rust`
- [GWSockets](https://github.com/FredyH/GWSockets) - WebSocket client module for GLua. `MIT` `C++`
- [HolyLib](https://github.com/RaphaelIT7/gmod-holylib) - Server binary module that adds extra functions, optimisations and engine bug fixes. `No license` `C++`
- [MySQLOO](https://github.com/FredyH/MySQLOO) - Object-oriented MySQL module for connecting servers to MySQL databases. `LGPL-2.1` `C++`
- [PIXEL UI](https://github.com/TomDotBat/pixel-ui) - Optimised UI library intended to replace Derma and slower built-in drawing functions. `GPL-3.0` `Lua`
- [RNDX](https://github.com/Srlion/RNDX) - Lightweight library for drawing rounded shapes quickly. `MIT` `Lua`
- [VJ Base](https://github.com/DrVrej/VJ-Base) - Collection of bases for creating NPCs, weapons and other types of addons. `No license` `Lua`
- [Wiremod](https://github.com/wiremod/wire) - Addon for wiring up gates, sensors, screens and chips to build automated contraptions. `Apache-2.0` `Lua`

## Client Fixes and Performance

Patches, fixes and tools that make the game launch, run or perform better.

- [Garry's Mod RTX Remixed](https://github.com/Xenthio/garrys-mod-rtx-remixed) - Project for running Garry's Mod with NVIDIA RTX Remix ray tracing. `GPL-2.0` `C++`
- [glua-patches](https://github.com/Pika-Software/glua-patches) - Pack of in-game fixes that make the game faster and more stable without changing gameplay. `MIT` `Lua`
- [gmod-linux-patcher](https://github.com/ret-0/gmod-linux-patcher) - Script that makes the native Linux version of Garry's Mod more playable and faster. `No license` `Shell`
- [gmod_perfutils](https://github.com/wrefgtzweve/gmod_perfutils) - Collection of scripts for finding performance bottlenecks in Garry's Mod. `No license` `Lua`
- [GModPatchTool](https://github.com/solsticegamestudios/GModPatchTool) - Updates the game's Chromium (CEF) and fixes common launch and performance issues, especially on Linux, Proton and macOS. `GPL-3.0` `Rust`
- [Hook Library](https://github.com/Srlion/Hook-Library) - Faster, lightweight replacement for the default hook system with priority support. `MIT` `Lua`
- [SRC Repair](https://github.com/xvitaly/srcrepair) - Tool for tuning and cleaning up Steam and Source engine games, including Garry's Mod. `GPL-3.0` `C#`

## Learning Resources and Communities

- [CFC GLua Style Guidelines](https://github.com/CFC-Servers/cfc_glua_style_guidelines) - Style guide for writing clean, consistent GLua code.
- [Facepunch/garrysmod](https://github.com/Facepunch/garrysmod) - Official repository of the game's Lua code, including Sandbox and TTT, which accepts pull requests.
- [Garry's Mod Discord](https://discord.gg/gmod) - Large Discord server for Garry's Mod players and developers.
- [Garry's Mod issue tracker](https://github.com/Facepunch/garrysmod-issues) - Facepunch's official tracker for reporting bugs in the game.
- [Garry's Mod Wiki](https://wiki.facepunch.com/gmod/) - Official GLua API reference and tutorials, edited by the community.
- [gmodwiki](https://github.com/CFC-Servers/gmodwiki) - Lightweight, self-hostable mirror of the Garry's Mod wiki.
- [r/GLua](https://www.reddit.com/r/GLua/) - Subreddit for help with Garry's Mod Lua scripting.
- [r/gmod](https://www.reddit.com/r/gmod/) - Main subreddit for Garry's Mod players, servers and addons.

## Contributing

Contributions are welcome. Read the [contributing guide](CONTRIBUTING.md), or [suggest a project](../../issues/new?template=add-project.yml) and we'll add it for you.

Spotted an archived project, broken link or wrong license tag? [Let us know](../../issues/new?template=update.yml), or fix it directly.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE)

This list is released into the public domain under [CC0](LICENSE). Each linked project keeps its own license. Garry's Mod is a trademark of Facepunch Studios; this list is not affiliated with Facepunch.
