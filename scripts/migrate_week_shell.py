"""
One-time migration: replaces old sidebar shell in week-XX.html files
with the new topnav shell. Content (tabs, panels) is preserved verbatim.
"""
import re
from pathlib import Path

STATIC = Path(__file__).parent.parent / "site" / "static"

NAV_TEMPLATE = """\
<header class="topnav">
  <a class="topnav-logo" href="index.html"><span class="topnav-logo-dot"></span>AI&nbsp;PM&nbsp;Course</a>
  <nav class="topnav-nav">
    <a href="learn/index.html">Learn</a>
    <div class="nav-dropdown" id="dd-weeks">
      <button onclick="toggleDd('dd-weeks')">Weeks ▾</button>
      <div class="nav-dropdown-panel weeks-panel">
        <div class="nav-dropdown-label">Jump to week</div>
        <div class="week-nav-grid">
          <a href="week-01.html" {w01}>01</a><a href="week-02.html" {w02}>02</a><a href="week-03.html" {w03}>03</a><a href="week-04.html" {w04}>04</a><a href="week-05.html" {w05}>05</a><a href="week-06.html" {w06}>06</a><a href="week-07.html" {w07}>07</a>
          <a href="week-08.html" {w08}>08</a><a href="week-09.html" {w09}>09</a><a href="week-10.html" {w10}>10</a><a href="week-11.html" {w11}>11</a><a href="week-12.html" {w12}>12</a><a href="week-13.html" {w13}>13</a><a href="week-14.html" {w14}>14</a>
        </div>
      </div>
    </div>
    <a href="course-weeks.html">Course map</a>
    <a href="learning-plan.html">Library</a>
  </nav>
  <button class="topnav-hamburger" onclick="toggleMobile()">☰</button>
</header>
<div class="mobile-overlay" id="mobile-overlay">
  <div class="mob-section">Learn</div>
  <a class="mob-link" href="learn/index.html">Learn hub</a>
  <a class="mob-link" href="learn/foundations.html">Foundations</a>
  <a class="mob-link" href="learn/prompting.html">Prompting</a>
  <a class="mob-link" href="learn/sql-and-data.html">SQL &amp; data</a>
  <a class="mob-link" href="learn/visualization.html">Visualization</a>
  <a class="mob-link" href="learn/rag.html">RAG</a>
  <a class="mob-link" href="learn/chatbots.html">Chatbots</a>
  <a class="mob-link" href="learn/prototypes.html">Prototypes</a>
  <a class="mob-link" href="learn/agents-and-launch.html">Agents &amp; launch</a>
  <div class="mob-section">Weekly practice</div>
  <div class="mob-week-grid">
    <a class="mob-week-btn {w01}" href="week-01.html">01</a><a class="mob-week-btn {w02}" href="week-02.html">02</a><a class="mob-week-btn {w03}" href="week-03.html">03</a><a class="mob-week-btn {w04}" href="week-04.html">04</a><a class="mob-week-btn {w05}" href="week-05.html">05</a><a class="mob-week-btn {w06}" href="week-06.html">06</a><a class="mob-week-btn {w07}" href="week-07.html">07</a>
    <a class="mob-week-btn {w08}" href="week-08.html">08</a><a class="mob-week-btn {w09}" href="week-09.html">09</a><a class="mob-week-btn {w10}" href="week-10.html">10</a><a class="mob-week-btn {w11}" href="week-11.html">11</a><a class="mob-week-btn {w12}" href="week-12.html">12</a><a class="mob-week-btn {w13}" href="week-13.html">13</a><a class="mob-week-btn {w14}" href="week-14.html">14</a>
  </div>
  <div class="mob-section">Library</div>
  <a class="mob-link" href="course-weeks.html">Course map</a>
  <a class="mob-link" href="learning-plan.html">Learning Plan</a>
  <a class="mob-link" href="practice-env.html">Practice Env</a>
</div>
"""

SUBNAV_TEMPLATE = """\
<nav class="subnav">
  <a href="index.html">Home</a>
  <span class="subnav-sep"></span>
  {week_pills}
</nav>
"""

def week_pills(current: int) -> str:
    pills = []
    for n in range(1, 15):
        cls = ' class="active"' if n == current else ''
        pills.append(f'<a{cls} href="week-{n:02d}.html">W{n:02d}</a>')
    return "\n  ".join(pills)

def build_active_map(current: int) -> dict:
    d = {}
    for n in range(1, 15):
        key = f"w{n:02d}"
        d[key] = 'class="active"' if n == current else ''
    return d

def migrate_week(path: Path) -> None:
    m = re.search(r'week-(\d+)\.html$', path.name)
    if not m:
        return
    wnum = int(m.group(1))

    raw = path.read_text(encoding='utf-8')

    # Extract title
    title_m = re.search(r'<title>(.*?)</title>', raw)
    title = title_m.group(1) if title_m else f"Week {wnum:02d} — AI PM Course"

    # Extract everything between <main ...> and </main> (or <main class="content md-body">)
    content_m = re.search(r'<main[^>]*class="content[^"]*"[^>]*>(.*?)</main>', raw, re.DOTALL)
    if not content_m:
        print(f"  WARNING: could not find <main> in {path.name}")
        return
    content = content_m.group(1).strip()

    active = build_active_map(wnum)
    nav_html = NAV_TEMPLATE.format(**active)
    # clean up empty class="" from nav
    nav_html = nav_html.replace(' class=""', '').replace('"" ', '')

    subnav_html = SUBNAV_TEMPLATE.format(week_pills=week_pills(wnum))

    new_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,600;0,9..40,700;0,9..40,800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/styles.css" />
</head>
<body>
{nav_html}
{subnav_html}
<main class="page has-subnav md-body">
{content}
</main>
<script src="js/nav.js"></script>
</body>
</html>
"""
    path.write_text(new_html, encoding='utf-8')
    print(f"  Migrated {path.name}")


def main():
    files = sorted(STATIC.glob("week-*.html"))
    print(f"Found {len(files)} week files")
    for f in files:
        migrate_week(f)
    print("Done.")


if __name__ == "__main__":
    main()
