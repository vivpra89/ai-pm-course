#!/usr/bin/env python3
"""
Generate fully static HTML under site/static/ — no fetch(), works via file:// or any static host.

Usage (from repo root):
  python3 scripts/build_static_site.py
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site" / "static"
SITE_CSS_SRC = ROOT / "site" / "css" / "styles.css"

MD_EXTENSIONS = ["tables", "fenced_code", "nl2br", "sane_lists"]

LEARN_LINKS = [
    ("learn/index.html", "learn-hub", "Learn hub"),
    ("learn/foundations.html", "learn-foundations", "Foundations"),
    ("learn/prompting.html", "learn-prompting", "Prompting"),
    ("learn/sql-and-data.html", "learn-sql", "SQL & data"),
    ("learn/visualization.html", "learn-viz", "Visualization"),
    ("learn/rag.html", "learn-rag", "RAG"),
    ("learn/chatbots.html", "learn-chatbots", "Chatbots"),
    ("learn/prototypes.html", "learn-prototypes", "Prototypes"),
    ("learn/agents-and-launch.html", "learn-agents", "Agents & launch"),
]

LIBRARY_LINKS = [
    ("index.html", "home", "Home"),
    ("learning-plan.html", "learning-plan", "Learning Plan"),
    ("graduate-course.html", "graduate-course", "Graduate Course"),
    ("course-weeks.html", "course-weeks", "Weekly Index"),
    ("practice-env.html", "practice-env", "Practice Env"),
]

RELATED_LEARN = {
    "01": ("Foundations", "learn/foundations.html"),
    "02": ("Prompting", "learn/prompting.html"),
    "03": ("Prompting", "learn/prompting.html"),
    "04": ("SQL & data", "learn/sql-and-data.html"),
    "05": ("SQL & data", "learn/sql-and-data.html"),
    "06": ("Visualization", "learn/visualization.html"),
    "07": ("RAG", "learn/rag.html"),
    "08": ("RAG", "learn/rag.html"),
    "09": ("Chatbots", "learn/chatbots.html"),
    "10": ("Chatbots", "learn/chatbots.html"),
    "11": ("Prototypes", "learn/prototypes.html"),
    "12": ("Prototypes", "learn/prototypes.html"),
    "13": ("Agents & launch", "learn/agents-and-launch.html"),
    "14": ("Agents & launch", "learn/agents-and-launch.html"),
}

LEARN_SOURCES = [
    ("learn/index.html", "Learn hub", "learn-hub", ROOT / "learn" / "README.md"),
    ("learn/foundations.html", "Foundations", "learn-foundations", ROOT / "learn" / "foundations.md"),
    ("learn/prompting.html", "Prompting", "learn-prompting", ROOT / "learn" / "prompting.md"),
    ("learn/sql-and-data.html", "SQL & data", "learn-sql", ROOT / "learn" / "sql-and-data.md"),
    ("learn/visualization.html", "Visualization", "learn-viz", ROOT / "learn" / "visualization.md"),
    ("learn/rag.html", "RAG", "learn-rag", ROOT / "learn" / "rag.md"),
    ("learn/chatbots.html", "Chatbots", "learn-chatbots", ROOT / "learn" / "chatbots.md"),
    ("learn/prototypes.html", "Prototypes", "learn-prototypes", ROOT / "learn" / "prototypes.md"),
    ("learn/agents-and-launch.html", "Agents & launch", "learn-agents", ROOT / "learn" / "agents-and-launch.md"),
]

WEEK_INFO = {
    "01": ("Phase 0", "Fundamentals and jargon — tokens, context limits; set up the practice database."),
    "02": ("Phase 1", "Prompt patterns: role/constraints, few-shot, decomposition."),
    "03": ("Phase 1", "Chain-of-thought, self-critique, tool framing; build your 10-question eval sheet."),
    "04": ("Phase 2", "SQL as source of truth — natural language → queries on CloudNote data."),
    "05": ("Phase 2", "Text-to-SQL safety, threat model, finish analytical drills."),
    "06": ("Phase 3", "Plots and quantitative validation — hypotheses tied to charts."),
    "07": ("Phase 4", "RAG pipeline: chunk, retrieve, cite using the corpus."),
    "08": ("Phase 4", "RAG failure modes + timed midterm checkpoint."),
    "09": ("Phase 5", "Chatbot UX: logging, rate limits, streaming concepts."),
    "10": ("Phase 5", "Minimal UI demo + incident playbook."),
    "11": ("Phase 6", "Prototypes — reproducible demos, pinned prompts."),
    "12": ("Phase 6", "Demo script + capstone charter."),
    "13": ("Phase 7", "Agentic patterns — tools, human gates, audit."),
    "14": ("Phase 7 + Capstone", "Integration, extras review, final exam."),
}

PHASE_COLORS = {
    "Phase 0": "#8b5cf6",
    "Phase 1": "#3b82f6",
    "Phase 2": "#06b6d4",
    "Phase 3": "#10b981",
    "Phase 4": "#f59e0b",
    "Phase 5": "#ef4444",
    "Phase 6": "#ec4899",
    "Phase 7": "#f97316",
    "Phase 7 + Capstone": "#f97316",
}


def section_anchor(heading: str) -> str:
    return "section-" + heading.lower().replace(" ", "-").replace("–", "-")


def md_to_html(text: str) -> str:
    return markdown.markdown(text, extensions=MD_EXTENSIONS)


def strip_first_h1(html: str) -> str:
    """Remove the first h1 tag — it duplicates the tab/section label."""
    return re.sub(r"\s*<h1[^>]*>.*?</h1>\s*", "\n", html, count=1, flags=re.DOTALL)


def rewrite_md_links(html: str, depth: int = 0) -> str:
    """Map common .md paths to static .html pages."""
    prefix = "../" * depth
    replacements = [
        ("href=\"TPM-PM-AI-Technical-Learning-Plan.md\"", f'href="{prefix}learning-plan.html"'),
        ("href='TPM-PM-AI-Technical-Learning-Plan.md'", f"href='{prefix}learning-plan.html'"),
        ("href=\"../TPM-PM-AI-Technical-Learning-Plan.md\"", f'href="{prefix}learning-plan.html"'),
        ("href=\"TPM-PM-AI-Graduate-Course.md\"", f'href="{prefix}graduate-course.html"'),
        ("href=\"../TPM-PM-AI-Graduate-Course.md\"", f'href="{prefix}graduate-course.html"'),
        ("href=\"course-weeks/README.md\"", f'href="{prefix}course-weeks.html"'),
        ("href=\"../course-weeks/README.md\"", f'href="{prefix}course-weeks.html"'),
        ("href=\"practice-env/README.md\"", f'href="{prefix}practice-env.html"'),
        ("href=\"../practice-env/README.md\"", f'href="{prefix}practice-env.html"'),
    ]
    for old, new in replacements:
        html = html.replace(old, new)
    # Learning-plan fragment links (../../TPM-PM-AI-Technical-Learning-Plan.md#fragment)
    html = re.sub(
        r'href="(?:\.\./)*TPM-PM-AI-Technical-Learning-Plan\.md(#[^"]*)"',
        rf'href="{prefix}learning-plan.html\1"',
        html,
    )
    html = re.sub(
        r'href="\.\./\.\./learn/([a-z0-9-]+)\.md"',
        f'href="{prefix}learn/\\1.html"',
        html,
    )
    html = re.sub(
        r'href="\.\./course-weeks/(week-\d{2})/README\.md"',
        r'href="../\1.html"',
        html,
    )
    html = re.sub(
        r'href="(foundations|prompting|sql-and-data|visualization|rag|chatbots|prototypes|agents-and-launch)\.md"',
        r'href="\1.html"',
        html,
    )
    html = re.sub(
        r'href="(?:\.\./)*course-weeks/(week-\d{2})/README\.md"',
        rf'href="{prefix}\1.html"',
        html,
    )
    html = re.sub(
        r"href='(?:\.\./)*course-weeks/(week-\d{2})/README\.md'",
        rf"href='{prefix}\1.html'",
        html,
    )
    html = re.sub(
        r'href="(week-\d{2})/README\.md"',
        rf'href="{prefix}\1.html"',
        html,
    )
    html = re.sub(
        r"href='(week-\d{2})/README\.md'",
        rf"href='{prefix}\1.html'",
        html,
    )
    return html


def sidebar(active: str, depth: int = 0) -> str:
    prefix = "../" * depth
    learn_items = []
    for href, sid, label in LEARN_LINKS:
        cls = " active" if sid == active else ""
        learn_items.append(
            f'<a class="nav-link nav-link--compact{cls}" href="{prefix}{href}">{label}</a>'
        )
    learn_block = "\n        ".join(learn_items)
    lib_items = []
    for href, sid, label in LIBRARY_LINKS:
        cls = " active" if sid == active else ""
        lib_items.append(
            f'<a class="nav-link{cls}" href="{prefix}{href}">{label}</a>'
        )
    lib_block = "\n        ".join(lib_items)
    weeks = []
    for i in range(1, 15):
        ww = f"{i:02d}"
        cls = " active" if active == f"week-{ww}" else ""
        weeks.append(
            f'<a class="week-btn{cls}" href="{prefix}week-{ww}.html">{ww}</a>'
        )
    week_grid = "\n          ".join(weeks)
    return f"""    <aside class="sidebar" id="sidebar">
      <div class="sidebar-header">
        <a href="{prefix}index.html" class="sidebar-logo">AI PM Course</a>
        <p class="sidebar-tagline">Learn by topic · weekly practice · labs.</p>
      </div>
      <nav class="nav-scroll" aria-label="Main">
        <div class="nav-section">Learn</div>
        {learn_block}
        <div class="nav-section">Library</div>
        {lib_block}
        <div class="nav-section">Weekly practice</div>
        <div class="week-grid">{week_grid}</div>
      </nav>
    </aside>"""


_MOBILE_JS = """\
  <script>
  (function () {
    var toggle = document.querySelector('.menu-toggle');
    var sidebar = document.getElementById('sidebar');
    var overlay = document.getElementById('overlay');
    if (toggle && sidebar) {
      toggle.addEventListener('click', function () {
        sidebar.classList.toggle('open');
        overlay.classList.toggle('show');
      });
      if (overlay) {
        overlay.addEventListener('click', function () {
          sidebar.classList.remove('open');
          overlay.classList.remove('show');
        });
      }
    }
  })();
  </script>"""


def shell(title: str, active: str, body: str, depth: int = 0) -> str:
    prefix = "../" * depth
    css_href = f"{prefix}css/styles.css"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} — AI PM Course</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,600;0,9..40,700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{css_href}" />
</head>
<body>
  <div class="app">
{sidebar(active, depth)}
    <div class="overlay" id="overlay"></div>
    <div class="main-wrap">
      <header class="topbar">
        <button class="menu-toggle" aria-label="Toggle navigation">&#9776;</button>
        <div class="breadcrumb"><strong>{title}</strong></div>
      </header>
      <main class="content md-body">
{body}
      </main>
    </div>
  </div>
{_MOBILE_JS}
</body>
</html>
"""


_TAB_JS = """\
<script>
(function () {
  var btns = document.querySelectorAll('.week-tabs button');
  var panels = document.querySelectorAll('.tab-panel');
  btns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      btns.forEach(function (b) { b.classList.remove('active'); });
      panels.forEach(function (p) { p.hidden = true; });
      btn.classList.add('active');
      var panel = document.getElementById(btn.dataset.tab);
      if (panel) panel.hidden = false;
    });
  });
})();
</script>"""


def index_html() -> str:
    body = """
      <div class="hero wide-top">
        <span class="time-pill">~6–10 hrs/week · 14 weeks suggested</span>
        <h1>AI for TPM / Technical PM</h1>
        <p>A structured program to go from AI-curious to AI-credible — concepts first, weekly practice second.</p>
      </div>

      <section class="start-here" aria-labelledby="start-heading">
        <p class="section-kicker">Recommended path</p>
        <h2 id="start-heading">Start here (first session)</h2>
        <ol class="steps">
          <li>
            <strong>Read the Learn hub chapters in order</strong>
            <p>Topic-based (Foundations → Prompting → SQL → …) with curated links. Study at your own pace — these are concepts, not calendar weeks.</p>
          </li>
          <li>
            <strong>Set up the practice environment</strong>
            <p>Create <code>cloudnote.db</code> and run the sample script. You'll use it every week for SQL, charts, and RAG labs.</p>
          </li>
          <li>
            <strong>Work through weekly folders for hands-on practice</strong>
            <p>Each week has four tabs — <strong>Overview → Readings → Practice → Exam</strong> — plus a lab sheet. Save your work under <code>my-submissions/week-XX/</code>.</p>
          </li>
        </ol>
      </section>

      <div class="split-learning">
        <div class="panel-learn">
          <h3>Three tracks</h3>
          <ul>
            <li><strong>Learn</strong> — concepts, mental models, curated articles &amp; videos. The main study path.</li>
            <li><strong>Weekly practice</strong> — calendar rhythm: readings, labs, exams, and drills.</li>
            <li><strong>Library</strong> — learning plan, graduate course rubrics, weekly index, env setup.</li>
          </ul>
        </div>
        <div class="panel-learn">
          <h3>Learning habits that work</h3>
          <ul>
            <li>One <strong>artifact</strong> per week (SQL file, prompts, short write-up).</li>
            <li>Do the <strong>Exam</strong> closed-notes, then check the plan's "concepts &amp; intuitions" list.</li>
            <li>Never trust LLM-generated SQL or numbers until you've <strong>run</strong> them on the practice DB.</li>
          </ul>
        </div>
      </div>

      <p class="cards-section-title">Jump to content</p>
      <div class="cards">
        <article class="card card-featured">
          <span class="card-badge">Start here</span>
          <h2>Learn hub</h2>
          <p>Eight chapters from Foundations through Agents &amp; launch — concepts first, then map to practice weeks.</p>
          <p class="card-meta">Recommended before weekly assignments</p>
          <a class="card-action" href="learn/index.html">Open Learn hub →</a>
        </article>
        <article class="card card-featured">
          <span class="card-badge">Hands-on</span>
          <h2>Week 1 — Fundamentals</h2>
          <p>Set up <code>cloudnote.db</code>, complete readings, practice labs, and the exam.</p>
          <a class="card-action" href="week-01.html">Start Week 1 →</a>
        </article>
        <article class="card">
          <h2>Practice environment</h2>
          <p>CloudNote SQLite DB, SQL drills, RAG corpus, Python labs — setup guide.</p>
          <a class="card-action" href="practice-env.html">Setup guide →</a>
        </article>
        <article class="card">
          <h2>Weekly index</h2>
          <p>Table of all 14 weeks with themes and phases at a glance.</p>
          <a class="card-action" href="course-weeks.html">All weeks →</a>
        </article>
        <article class="card">
          <h2>Technical Learning Plan</h2>
          <p>Master roadmap: phases 0–7, job impact table, FAANG prep, capstone.</p>
          <a class="card-action" href="learning-plan.html">Open →</a>
        </article>
        <article class="card">
          <h2>Graduate course</h2>
          <p>PS/L assignments, midterm, rubrics — seminar-style structure.</p>
          <a class="card-action" href="graduate-course.html">Open →</a>
        </article>
        <article class="card">
          <h2>Milestones</h2>
          <p><strong>Week 8</strong> — midterm checkpoint &nbsp;·&nbsp; <strong>Week 14</strong> — capstone &amp; final exam.</p>
          <a class="card-action" href="week-08.html">Week 8 →</a>
          <a class="card-action" href="week-14.html">Week 14 →</a>
        </article>
      </div>
"""
    return shell("Home", "home", body, depth=0)


def related_learn_strip(ww: str, depth: int = 0) -> str:
    if ww not in RELATED_LEARN:
        return ""
    title, href = RELATED_LEARN[ww]
    prefix = "../" * depth
    return (
        f'<aside class="related-learn"><strong>Learn chapter:</strong> '
        f'<a href="{prefix}{href}">{title}</a> — concepts, videos, and links. Study alongside or before practice.</aside>'
    )


def week_page(ww: str) -> str:
    wdir = ROOT / "course-weeks" / f"week-{ww}"
    sections = [
        ("Overview", "README.md"),
        ("Readings", "READINGS.md"),
        ("Practice", "PRACTICE.md"),
        ("Exam", "EXAM.md"),
    ]
    if ww == "08":
        sections.insert(4, ("Midterm", "MIDTERM.md"))
    if ww == "14":
        sections.insert(4, ("Final review", "FINAL_REVIEW.md"))
    sections.append(("Lab sheet", "TOPICS.md"))

    tab_data: list[tuple[str, str, str]] = []
    for heading, fname in sections:
        fp = wdir / fname
        if not fp.exists():
            continue
        aid = section_anchor(heading)
        raw = fp.read_text(encoding="utf-8")
        content_html = strip_first_h1(md_to_html(raw))
        content_html = rewrite_md_links(content_html, depth=0)
        tab_data.append((heading, aid, content_html))

    phase, focus = WEEK_INFO.get(ww, ("", ""))
    phase_color = PHASE_COLORS.get(phase, "var(--accent)")

    intro = f"""<div class="week-intro" style="border-left-color:{phase_color}">
  <div class="phase-tag" style="color:{phase_color}">{phase}</div>
  <p><strong>Week {int(ww)}.</strong> {focus}</p>
</div>
{related_learn_strip(ww, depth=0)}"""

    # Tab navigation
    tab_btns: list[str] = []
    for i, (heading, aid, _) in enumerate(tab_data):
        cls_attr = ' class="active"' if i == 0 else ""
        tab_btns.append(f'<button{cls_attr} data-tab="{aid}">{heading}</button>')
    tabs_html = '<div class="week-tabs">\n  ' + "\n  ".join(tab_btns) + "\n</div>"

    # Tab panels
    panels: list[str] = []
    for i, (_, aid, content) in enumerate(tab_data):
        hidden = "" if i == 0 else " hidden"
        panels.append(f'<div class="tab-panel" id="{aid}"{hidden}>\n{content}\n</div>')
    panels_html = "\n".join(panels)

    # Pager
    n = int(ww)
    pager_parts: list[str] = []
    if n > 1:
        pager_parts.append(f'<a class="pager-link" href="week-{n - 1:02d}.html">← Week {n - 1:02d}</a>')
    if n < 14:
        pager_parts.append(f'<a class="pager-link pager-link--next" href="week-{n + 1:02d}.html">Week {n + 1:02d} →</a>')
    pager = ""
    if pager_parts:
        pager = '<nav class="week-pager" aria-label="Adjacent weeks">\n  ' + "\n  ".join(pager_parts) + "\n</nav>"

    work_tip = (
        f'<aside class="work-tip">\n'
        f'  <strong>Keep your work organized.</strong> Save prompts, SQL, and notes under '
        f'<code>my-submissions/week-{ww}/</code> in your clone so you can review before interviews.'
        f'\n</aside>'
    )

    body = "\n".join([intro, tabs_html, panels_html, _TAB_JS, pager, work_tip])
    return shell(f"Week {ww}", f"week-{ww}", body, depth=0)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "css").mkdir(exist_ok=True)
    shutil.copy(SITE_CSS_SRC, OUT / "css" / "styles.css")

    # index
    (OUT / "index.html").write_text(index_html(), encoding="utf-8")

    singles = [
        ("learning-plan.html", "Technical Learning Plan", "learning-plan", ROOT / "TPM-PM-AI-Technical-Learning-Plan.md"),
        ("graduate-course.html", "Graduate Course", "graduate-course", ROOT / "TPM-PM-AI-Graduate-Course.md"),
        ("course-weeks.html", "Weekly Track", "course-weeks", ROOT / "course-weeks" / "README.md"),
        ("practice-env.html", "Practice Environment", "practice-env", ROOT / "practice-env" / "README.md"),
    ]

    for fname, title, active, path in singles:
        md = path.read_text(encoding="utf-8")
        body = rewrite_md_links(md_to_html(md), depth=0)
        (OUT / fname).write_text(shell(title, active, body, depth=0), encoding="utf-8")

    for i in range(1, 15):
        ww = f"{i:02d}"
        (OUT / f"week-{ww}.html").write_text(week_page(ww), encoding="utf-8")

    (OUT / "learn").mkdir(parents=True, exist_ok=True)
    for fname, title, active, path in LEARN_SOURCES:
        md = path.read_text(encoding="utf-8")
        body = rewrite_md_links(md_to_html(md), depth=1)
        out_path = OUT / fname
        out_path.write_text(shell(title, active, body, depth=1), encoding="utf-8")

    print(f"Wrote static site to {OUT}")


if __name__ == "__main__":
    main()
