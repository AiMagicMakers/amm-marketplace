# AMM Marketplace

Plugins from **AMM (AI Magic Makers)** for entrepreneurs and small businesses.

| Plugin | What it does |
|---|---|
| [`amm-os-starter`](plugins/amm-os-starter) | Builds your **Second Brain**: an interview in three short rounds, then a plain folder of Markdown files that Claude, ChatGPT or Gemini can read. Also checks, extends, maps and upgrades that folder. |

## Install in Claude

### Claude Code (terminal)

Add the marketplace once, then install the plugin:

```bash
claude plugin marketplace add AiMagicMakers/amm-marketplace
claude plugin install amm-os-starter@amm-marketplace
```

Or inside a Claude Code session:

```
/plugin marketplace add AiMagicMakers/amm-marketplace
/plugin install amm-os-starter@amm-marketplace
```

Then say: **"Build my second brain"**. You can also run the skill directly with `/amm-os-starter:amm-os-starter`.

### Claude desktop app and Cowork

Open **Customize** and add a plugin. If your version lets you add a marketplace from GitHub, use `AiMagicMakers/amm-marketplace`. If it only accepts a file, download `amm-os-starter-vX.Y.Z.zip` from the [latest Release](https://github.com/AiMagicMakers/amm-marketplace/releases/latest) and upload it as it is, without unzipping it. Then say "Build my second brain".

### Other tools

- **ChatGPT and Gemini** have no plugins. Build your Second Brain in Claude first, then paste the one-page `brief.md` it creates at the start of a chat.
- **Other agent tools that read `SKILL.md` files**: copy the folder `plugins/amm-os-starter/skills/amm-os-starter` into that tool's skills folder. The skill needs a tool that can read and write files. The map feature needs Python 3. This route is not tested by us.

## Updates

New versions reach you only when the plugin version changes.

- In Claude Code, run `claude plugin marketplace update amm-marketplace`, then `claude plugin update amm-os-starter@amm-marketplace`. Or open `/plugin`, choose **Marketplaces**, select this marketplace and turn on **Enable auto-update**.
- With the ZIP route, download the new ZIP from Releases and upload it again.

After updating, tell Claude "upgrade my second brain" to bring an existing folder up to date. Your own notes are never rewritten.

## Repository layout

```
amm-marketplace/
  .claude-plugin/marketplace.json    the catalogue (name, owner, list of plugins)
  plugins/
    amm-os-starter/                  one folder per plugin
      .claude-plugin/plugin.json     the plugin manifest and its version
      skills/amm-os-starter/         the skill, its references and script
      README.md                      participant guide
      CHANGELOG.md
  .github/workflows/
    validate.yml                     checks on every push and pull request
    release.yml                      builds the plugin ZIP when you push a v* tag
```

## For maintainers

### Release a new version

1. Edit the plugin. Update `plugins/amm-os-starter/CHANGELOG.md`.
2. Bump `version` in `plugins/amm-os-starter/.claude-plugin/plugin.json`. The skill's `SKILL.md` lists the other places that mention the version.
3. Commit and push to `main`.
4. Tag and push: `git tag vX.Y.Z && git push origin vX.Y.Z`. The release workflow checks the tag matches `plugin.json`, builds the ZIP and publishes a GitHub Release.

Set the version **only** in `plugin.json`, never in `marketplace.json`. If you forget to bump it, users keep their cached copy and do not see your changes.

### Check before pushing

```bash
claude plugin validate .
claude plugin validate ./plugins/amm-os-starter
```

### Add another plugin

Create `plugins/<name>/` with its own `.claude-plugin/plugin.json`, then add an entry to `.claude-plugin/marketplace.json` with `"source": "./plugins/<name>"`. The entry `name` must equal the `name` in the plugin's `plugin.json`.

### Rename safely

Never change a plugin's `name` after people installed it. If you must, add a `renames` map to `marketplace.json`.

## Privacy

The plugin runs on your computer. Your Second Brain stays in a folder you choose. Nothing is sent anywhere by this repository.
