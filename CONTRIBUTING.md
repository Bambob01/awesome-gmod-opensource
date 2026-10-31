# Contributing

Thanks for helping! Every new project, fix and license correction makes this list more useful. If you can edit a text file on GitHub, you can contribute.

## Quick start (about 2 minutes)

1. Open [`README.md`](README.md) and click the pencil icon (**Edit this file**).
2. Find the right section and add your line **in alphabetical order**.
3. Scroll down, click **Commit changes…**, then **Propose changes**, then **Create pull request**.

That's it. GitHub makes a copy for you automatically.

Not comfortable editing? [Open a "Suggest a project" issue](../../issues/new?template=add-project.yml) instead and someone will add it for you.

## The entry format

Projects (every section except Learning Resources and Communities):

```markdown
- [Project Name](https://github.com/owner/repo) - One short, factual sentence about what it does. `License` `Language`
```

Learning resources and communities (no tags):

```markdown
- [Resource Name](https://link) - One short sentence about what you'll find there.
```

Example:

```markdown
- [GLuaTest](https://github.com/CFC-Servers/GLuaTest) - Unit testing framework for GLua projects. `GPL-3.0` `Lua`
```

### License tag

Use the [SPDX identifier](https://spdx.org/licenses/) of the project's license, exactly as the repo states it. Be honest — it helps people decide whether they can use the code.

| Tag | When to use it |
|---|---|
| `MIT`, `GPL-3.0`, `Apache-2.0`, `Unlicense`, ... | The repo has a standard open-source license |
| `MIT/Apache-2.0` | The project is dual-licensed |
| `Custom` | The repo has a license file, but it isn't a standard SPDX license |
| `No license` | The repo has no license file at all |

Tip: GitHub shows the license in the repo sidebar. If it says "View license" or "Other", use `Custom`. If there is no license shown, use `No license`.

### Language tag

The project's main language, as shown in the repo's language bar: `Lua`, `C++`, `Rust`, `C#`, `TypeScript`, `MoonScript` and so on.

## What belongs here

✅ **Yes**

- Free, open-source Garry's Mod addons, gamemodes and frameworks with public source code
- Admin mods, anti-cheat, moderation and server hosting tools
- Libraries, binary modules and base addons for developers
- Editor extensions, linters, test frameworks, profilers and publishing tools
- Client fixes and performance patches
- Learning resources and communities for Garry's Mod developers

Projects should be maintained or still work with the current game. Well-known older projects are fine if they still work.

## What doesn't belong

❌ **No**

- **Cheats, aimbots, Lua injectors, scripthooks or menu-state execution tools** (e.g. glua-steal, Autorun-rs and similar)
- **Lua stealers** or anything that downloads or dumps client-side code from other people's servers
- **Exploit tools or exploit lists** for attacking, crashing or griefing servers you don't own, including net message exploiters, DDoS tools and "backdoor" kits
- **Backdoor or "anti-backdoor" scanners that are themselves obfuscated**, phone home, or can't be audited
- **Leaked, cracked or reuploaded paid addons**, or forks of them, even if they are now hosted on GitHub
- Obfuscators and DRM whose main purpose is hiding code from server owners
- Archived, deleted or broken projects — instead, open a PR to remove them (we're happy to get those too!)
- Closed-source or paid-only addons — this list is for code people can read
- Duplicates — search the README first (Ctrl+F)

If you're unsure whether something fits, open an issue and ask.

## Adding your own project

**Developers are welcome to add their own projects.** Just keep the description factual (no "best", "blazing fast" or all-caps), make sure the repo has a README, and pick the license tag honestly. Adding a license to your repo before submitting is a great idea: it tells server owners and developers what they're allowed to do with your code.

## Other great contributions

- **Remove archived projects** — or ones that no longer work with the current game.
- **Fix a broken link** — our link checker flags these every week.
- **Correct a license or language tag** — repos change licenses over time.
- **Better descriptions** — clearer, shorter, more accurate.
- **New sections** — open an issue first to discuss.

## Checklist before submitting

- [ ] One project per line, added in alphabetical order
- [ ] Link goes to the source repository (or the official site, for resources)
- [ ] Description is one sentence, ends with a period, and has no hype words
- [ ] Projects have exactly two tags: `License` then `Language`; resources have none
- [ ] Not a cheat, stealer, exploit tool or leaked addon, not archived, not a duplicate

An automated check runs on every pull request and will tell you if the formatting is off. You can run it yourself with `python3 scripts/check_format.py`. If it fails, fix it and push again.

## Review

Pull requests are usually reviewed within a few days. If something needs changing, we'll leave a friendly comment. By contributing you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
