# aicontrolarchitecture.org — Retype Pro site

This folder builds the docs site for **aicontrolarchitecture.org** with **Retype Pro**, hosted on **Vercel**. It replaces GitBook.

## How it works

- **`docs/`, `mappings/`, `templates/`, `examples/`, and the root READMEs stay the single source of truth.** Edit there, exactly as before.
- `scripts/build-content.mjs` copies that markdown into **`content/`**, organized to mirror the **exact GitBook URLs** (so no external link breaks). `content/` is **generated** and gitignored — never edit it by hand.
- `retype build` turns `content/` into a static site in `.retype/`, which Vercel serves.
- One Retype Pro key covers this domain and everything under it (including a future `/rcdf` folder).

Verified: the organizer produces **73 pages + 7 section landings** with **0 broken internal links**.

---

## Your checklist (do when you're back)

### 1. Add the Pro key (once it's emailed)
- [ ] Install the CLI: `npm i -g retypeapp` (or use the devDependency: `cd site && npm install`).
- [ ] Add your key: `retype wallet --add <YOUR-KEY>` — it's registered to `aicontrolarchitecture.org`.
- [ ] (You have a **15-day** window to change the registered URL once, if you ever need to.)

### 2. Build + preview locally
The site lives here:
```
~/Library/Mobile Documents/com~apple~CloudDocs/Project-AI/ai-control-architecture/site
```
```bash
cd ~/Library/Mobile\ Documents/com~apple~CloudDocs/Project-AI/ai-control-architecture/site
npm install
npm start          # runs the content organizer, then serves a live preview
```
- [ ] Open the preview. Check: nav order, a few pillar pages, search, the home page, and internal links.
- [ ] Confirm the **"Powered by Retype" footer is gone** (that proves the key is active).
- [ ] `npm run build` → confirm it builds `.retype/` cleanly.

### 3. Deploy on Vercel
- [ ] New Vercel project from the `ai-control-architecture` repo → **Root Directory = `site`**.
- [ ] Framework preset: **Other**. Build command: `npm run build`. Output dir: `.retype`.
- [ ] Add your Retype key as a **build env var** (don't commit it) and reference it in the build if needed.
- [ ] Deploy to the **preview URL** first and review end-to-end there.
- [ ] **Fallback if Retype's binary won't run in Vercel's build:** build locally (`retype build`) or via the official `retypeapp/action` GitHub Action, and have Vercel serve the pre-built `.retype/` as a static site. (Try the native build first; this is only if it fails.)

### 4. Domain cutover (~31 Aug, NOT launch morning)
- [ ] Vercel → add domains `aicontrolarchitecture.org` **and** `www.aicontrolarchitecture.org`.
- [ ] GitBook → **remove the custom domain** so it releases it.
- [ ] Registrar → point DNS to Vercel's records.
- [ ] Wait for Vercel to show the domain **Valid**; confirm the live site is served by Vercel (not GitBook); spot-check the launch-post links.
- [ ] Only then unpublish/disconnect GitBook (keep it as one-DNS-change rollback).

### 5. Go live
- [ ] Final read on the live domain.
- [ ] Merge the `site/` branch → `main` so future doc edits auto-deploy.

---

## Things I couldn't verify without the CLI (please eyeball on first build)

1. **Dark-by-default theme.** Set — `scheme.mode: dark` + the ACA cyan accent (`branding.baseColor`). It renders dark in local preview too (via `start.pro`). Visitors can still toggle light.
2. **"Edit this page" links** are intentionally **omitted** — because `content/` is generated, an edit link would point at generated files, not `docs/`. Add later only if you want it, pointing at the `docs/` source.
3. **Social/OG image.** `static/og.png` (the ACA banner) is in place; confirm Retype uses it for link previews, and add a `cover`/meta image setting if not.
4. **`meta:` keys.** Uses only confirmed fields — `meta.siteName` + `meta.title` (a title suffix). Should build clean.
5. **Section landing pages** (`/foundation/`, `/the-ten-pillars/`, …) are new pages that order the sidebar. They're additive (don't break any old URL); restyle or remove if you prefer flat groups.
6. **Link spot-check.** The organizer reports 0 unresolved links, but eyeball a couple of cross-section links and any `#anchors`.

## Adding RCDF later

Drop the RCDF markdown into a new source folder, add a mapping block in `build-content.mjs` (→ `content/rcdf/…`, url `/rcdf/…`), and it publishes under the same domain and key. No new purchase.

## Commands

| Command | Does |
|---|---|
| `npm run content` | Regenerate `content/` from the source markdown |
| `npm start` | Organize + live preview (with editor) |
| `npm run build` | Organize + build static site to `.retype/` |
