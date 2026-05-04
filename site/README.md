# Course website

Two options:

## 1. Fully static HTML

Open **`static/index.html`** in your browser — **no server**, no JavaScript required.

The home page includes a **recommended learning path**, explains **how the three tracks differ**, and each **week page** has section jump links, phase context, prev/next week navigation, and a submissions tip.

Rebuild after you change any `.md` file:

```bash
python3 scripts/build_static_site.py
```

Requires `pip install markdown`. See **[static/README.md](static/README.md)**.

## 2. Dynamic hub (loads live Markdown)

Open **`index.html`** through a **local HTTP server** so Markdown files can load with `fetch()` (browser security blocks `file://` for this version).

From the **repository root** (`AI_PM_course/`, parent of `site/`):

```bash
python3 -m http.server 8080
```

Then: **http://localhost:8080/site/**

### What the dynamic version adds

- Sidebar + hash routing; **week tabs** as separate views without regenerating HTML  

## Deploy (static)

Upload the contents of **`site/static/`** to any static host. No build step on the server.

## Deploy (dynamic)

Serve **repo root** so paths like `/TPM-PM-AI-Technical-Learning-Plan.md` resolve for `fetch()`.
