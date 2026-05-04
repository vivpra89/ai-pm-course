# Static site (no JavaScript, no server)

Pre-built HTML lives in this folder. Open **`index.html`** in your browser.

## Regenerate after editing Markdown

From the repo root:

```bash
python3 scripts/build_static_site.py
```

Requires: `pip install markdown` (Python 3).

## Contents

- `index.html` — Home  
- `learning-plan.html`, `graduate-course.html`, `course-weeks.html`, `practice-env.html`  
- `week-01.html` … `week-14.html` — each week combines Overview, Readings, Practice, Exam (+ Midterm on week 08, Final review on week 14)

## Dynamic hub (optional)

For live Markdown reload via fetch, use **`../index.html`** with a local server — see **`../README.md`**.
