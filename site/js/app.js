/**
 * AI PM Course — client router + markdown fetch
 * Serve repo root: python3 -m http.server 8080
 * Open: http://localhost:8080/site/
 */

/* global marked, DOMPurify */

const BASE = ""; // fetch from site origin root (repo root when server is AI_PM_course)

const PAGES = {
  "learning-plan": {
    path: "TPM-PM-AI-Technical-Learning-Plan.md",
    title: "Technical Learning Plan",
  },
  "graduate-course": {
    path: "TPM-PM-AI-Graduate-Course.md",
    title: "Graduate Course & Assignments",
  },
  "course-weeks": {
    path: "course-weeks/README.md",
    title: "Weekly Track (Index)",
  },
  "practice-env": {
    path: "practice-env/README.md",
    title: "Practice Environment",
  },
};

/** Learn hub + chapter markdown (topic path) */
const LEARN = {
  hub: { path: "learn/README.md", title: "Learn hub" },
  chapters: {
    foundations: { path: "learn/foundations.md", title: "Foundations" },
    prompting: { path: "learn/prompting.md", title: "Prompting" },
    "sql-and-data": { path: "learn/sql-and-data.md", title: "SQL & data" },
    visualization: { path: "learn/visualization.md", title: "Visualization" },
    rag: { path: "learn/rag.md", title: "RAG" },
    chatbots: { path: "learn/chatbots.md", title: "Chatbots" },
    prototypes: { path: "learn/prototypes.md", title: "Prototypes" },
    "agents-and-launch": { path: "learn/agents-and-launch.md", title: "Agents & launch" },
  },
};

const RELATED_LEARN = {
  "01": { label: "Foundations", slug: "foundations" },
  "02": { label: "Prompting", slug: "prompting" },
  "03": { label: "Prompting", slug: "prompting" },
  "04": { label: "SQL & data", slug: "sql-and-data" },
  "05": { label: "SQL & data", slug: "sql-and-data" },
  "06": { label: "Visualization", slug: "visualization" },
  "07": { label: "RAG", slug: "rag" },
  "08": { label: "RAG", slug: "rag" },
  "09": { label: "Chatbots", slug: "chatbots" },
  "10": { label: "Chatbots", slug: "chatbots" },
  "11": { label: "Prototypes", slug: "prototypes" },
  "12": { label: "Prototypes", slug: "prototypes" },
  "13": { label: "Agents & launch", slug: "agents-and-launch" },
  "14": { label: "Agents & launch", slug: "agents-and-launch" },
};

const WEEK_TAB_ORDER = ["readme", "readings", "practice", "exam", "topics", "midterm", "final_review"];

const WEEK_LABELS = {
  "01": "Fundamentals & jargon",
  "02": "Prompt patterns I",
  "03": "Prompt patterns II + eval",
  "04": "SQL as truth I",
  "05": "SQL safety II",
  "06": "Plots & validation",
  "07": "RAG I",
  "08": "RAG II + midterm",
  "09": "Chatbot I",
  "10": "Chatbot II",
  "11": "Prototypes I",
  "12": "Prototypes II + capstone kickoff",
  "13": "Agentic patterns",
  "14": "Capstone + final review",
};

/** Phase + focus line — keep in sync with scripts/build_static_site.py WEEK_INFO */
const WEEK_CONTEXT = {
  "01": { phase: "Phase 0", focus: "Fundamentals and jargon — tokens, context limits; set up the practice database." },
  "02": { phase: "Phase 1", focus: "Prompt patterns: role/constraints, few-shot, decomposition." },
  "03": { phase: "Phase 1", focus: "Chain-of-thought, self-critique, tool framing; build your 10-question eval sheet." },
  "04": { phase: "Phase 2", focus: "SQL as source of truth — natural language → queries on CloudNote data." },
  "05": { phase: "Phase 2", focus: "Text-to-SQL safety, threat model, finish analytical drills." },
  "06": { phase: "Phase 3", focus: "Plots and quantitative validation — hypotheses tied to charts." },
  "07": { phase: "Phase 4", focus: "RAG pipeline: chunk, retrieve, cite using the corpus." },
  "08": { phase: "Phase 4", focus: "RAG failure modes + timed midterm checkpoint." },
  "09": { phase: "Phase 5", focus: "Chatbot UX: logging, rate limits, streaming concepts." },
  "10": { phase: "Phase 5", focus: "Minimal UI demo + incident playbook." },
  "11": { phase: "Phase 6", focus: "Prototypes — reproducible demos, pinned prompts." },
  "12": { phase: "Phase 6", focus: "Demo script + capstone charter." },
  "13": { phase: "Phase 7", focus: "Agentic patterns — tools, human gates, audit." },
  "14": { phase: "Phase 7 + Capstone", focus: "Integration, extras review, final exam." },
};

const WEEK_FILES = {
  topics: { file: "TOPICS.md", label: "Practice lab sheet" },
  readme: { file: "README.md", label: "Overview" },
  readings: { file: "READINGS.md", label: "Readings" },
  practice: { file: "PRACTICE.md", label: "Practice" },
  exam: { file: "EXAM.md", label: "Exam" },
  midterm: { file: "MIDTERM.md", label: "Midterm", weeks: ["08"] },
  final_review: { file: "FINAL_REVIEW.md", label: "Final review", weeks: ["14"] },
};

function parseHash() {
  const h = (window.location.hash || "#/").slice(1).replace(/^\//, "");
  const parts = h.split("/").filter(Boolean);
  if (parts.length === 0) return { view: "home" };
  if (parts[0] === "learn") {
    const slug = parts[1] || null;
    return { view: "learn", slug };
  }
  if (parts[0] === "week" && parts[1]) {
    const ww = parts[1].padStart(2, "0");
    const tab = parts[2] || "readme";
    return { view: "week", week: ww, tab };
  }
  if (PAGES[parts[0]]) return { view: "page", id: parts[0] };
  return { view: "home" };
}

function setHash(obj) {
  if (obj.view === "home") window.location.hash = "#/";
  else if (obj.view === "page") window.location.hash = "#/" + obj.id;
  else if (obj.view === "learn") {
    if (obj.slug) window.location.hash = "#/learn/" + obj.slug;
    else window.location.hash = "#/learn";
  } else if (obj.view === "week")
    window.location.hash = "#/week/" + obj.week + "/" + (obj.tab || "readme");
}

function fixMarkdownLinks(html, currentMdPath) {
  const div = document.createElement("div");
  div.innerHTML = html;
  const dir = currentMdPath.replace(/[^/]+$/, "");
  const routeMap = {
    "TPM-PM-AI-Technical-Learning-Plan.md": "#/learning-plan",
    "TPM-PM-AI-Graduate-Course.md": "#/graduate-course",
    "course-weeks/README.md": "#/course-weeks",
    "practice-env/README.md": "#/practice-env",
  };
  div.querySelectorAll('a[href]').forEach((a) => {
    let href = a.getAttribute("href");
    if (!href || href.startsWith("http") || href.startsWith("#") || href.startsWith("mailto:"))
      return;
    if (href.endsWith(".md")) {
      const base = href.replace(/^.*\//, "").split("?")[0];
      if (routeMap[base]) {
        a.setAttribute("href", routeMap[base]);
        return;
      }
      // course-weeks/README.md uses links like week-01/README.md
      const shortWeekReadme = href.match(/^week-(\d{2})\/README\.md$/i);
      if (shortWeekReadme) {
        a.setAttribute("href", "#/week/" + shortWeekReadme[1] + "/readme");
        return;
      }
      const shortWeekTopics = href.match(/^week-(\d{2})\/TOPICS\.md$/i);
      if (shortWeekTopics) {
        a.setAttribute("href", "#/week/" + shortWeekTopics[1] + "/topics");
        return;
      }
      const resolved = resolvePath(dir, href);
      if (resolved === "learn/README.md") {
        a.setAttribute("href", "#/learn");
        return;
      }
      const learnChapter = resolved.match(/^learn\/([a-z0-9-]+)\.md$/);
      if (learnChapter && LEARN.chapters[learnChapter[1]]) {
        a.setAttribute("href", "#/learn/" + learnChapter[1]);
        return;
      }
      if (resolved.startsWith("course-weeks/week-")) {
        const m = resolved.match(/course-weeks\/(week-\d{2})\/([^/]+\.md)/);
        if (m) {
          const w = m[1].replace("week-", "");
          const raw = m[2].replace(".md", "").toLowerCase();
          const tabMap = {
            topics: "topics",
            readme: "readme",
            readings: "readings",
            practice: "practice",
            exam: "exam",
            midterm: "midterm",
            final_review: "final_review",
          };
          const tab = tabMap[raw] || "readme";
          a.setAttribute("href", "#/week/" + w + "/" + tab);
          return;
        }
      }
      const pageKey = Object.keys(PAGES).find((k) => PAGES[k].path === resolved);
      if (pageKey) {
        a.setAttribute("href", "#/" + pageKey);
        return;
      }
      a.setAttribute("href", BASE + "/" + resolved);
      a.setAttribute("target", "_blank");
      a.setAttribute("rel", "noopener");
    }
  });
  return div.innerHTML;
}

function resolvePath(dir, href) {
  if (href.startsWith("/")) return href.slice(1);
  const parts = dir.split("/").filter(Boolean);
  href.split("/").forEach((seg) => {
    if (seg === "..") parts.pop();
    else if (seg !== ".") parts.push(seg);
  });
  return parts.join("/");
}

async function fetchMarkdown(path) {
  const url = BASE + "/" + path;
  const r = await fetch(url);
  if (!r.ok) throw new Error("Could not load " + path + " (" + r.status + ")");
  return r.text();
}

function renderMarkdown(md, path) {
  const raw = marked.parse(md, { mangle: false, headerIds: true });
  const safe = DOMPurify.sanitize(raw);
  return fixMarkdownLinks(safe, path);
}

function showHome(contentEl, breadcrumbEl) {
  breadcrumbEl.innerHTML = '<strong>Home</strong>';
  contentEl.innerHTML = document.getElementById("home-template").innerHTML;
  contentEl.querySelectorAll("[data-nav]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const nav = btn.getAttribute("data-nav");
      if (nav.startsWith("week:")) {
        const w = nav.split(":")[1];
        setHash({ view: "week", week: w, tab: "readme" });
      } else if (nav === "learn") setHash({ view: "learn", slug: null });
      else setHash({ view: "page", id: nav });
    });
  });
}

async function showPage(contentEl, breadcrumbEl, id) {
  const p = PAGES[id];
  if (!p) return showHome(contentEl, breadcrumbEl);
  breadcrumbEl.innerHTML = '<a href="#/">Home</a> / <strong>' + p.title + "</strong>";
  contentEl.innerHTML = '<p class="loading">Loading…</p>';
  try {
    const md = await fetchMarkdown(p.path);
    contentEl.innerHTML = '<article class="md-body">' + renderMarkdown(md, p.path) + "</article>";
  } catch (e) {
    contentEl.innerHTML =
      '<p class="error">' +
      e.message +
      '</p><p class="md-body">Start a local server from the course repo root:<br><code style="background:#1a2332;padding:0.2rem 0.5rem;border-radius:4px">python3 -m http.server 8080</code> then open <code style="background:#1a2332;padding:0.2rem 0.5rem;border-radius:4px">http://localhost:8080/site/</code></p>';
  }
}

async function showLearn(contentEl, breadcrumbEl, slug) {
  let path;
  let title;
  if (!slug) {
    path = LEARN.hub.path;
    title = LEARN.hub.title;
  } else {
    const ch = LEARN.chapters[slug];
    if (!ch) {
      setHash({ view: "learn", slug: null });
      return;
    }
    path = ch.path;
    title = ch.title;
  }
  breadcrumbEl.innerHTML =
    '<a href="#/">Home</a> / <a href="#/learn">Learn</a> / <strong>' + title + "</strong>";
  contentEl.innerHTML = '<p class="loading">Loading…</p>';
  try {
    const md = await fetchMarkdown(path);
    contentEl.innerHTML = '<article class="md-body">' + renderMarkdown(md, path) + "</article>";
  } catch (e) {
    contentEl.innerHTML = '<p class="error">' + e.message + "</p>";
  }
}

async function showWeek(contentEl, breadcrumbEl, week, tabIn) {
  const ww = week.padStart(2, "0");
  const label = WEEK_LABELS[ww] || "Week " + ww;

  let fileKey = (tabIn || "readme").toLowerCase().replace(/-/g, "_");
  if (!WEEK_FILES[fileKey]) fileKey = "readme";
  let meta = WEEK_FILES[fileKey];
  if (meta.weeks && !meta.weeks.includes(ww)) fileKey = "readme";
  meta = WEEK_FILES[fileKey];

  const path = "course-weeks/week-" + ww + "/" + meta.file;
  const title = "Week " + ww + " — " + label;

  breadcrumbEl.innerHTML =
    '<a href="#/">Home</a> / <a href="#/course-weeks">Weeks</a> / <strong>' +
    title +
    "</strong>";

  const tabsHtml = buildWeekTabs(ww, fileKey);
  contentEl.innerHTML = tabsHtml + '<article class="md-body"><p class="loading">Loading…</p></article>';

  try {
    const md = await fetchMarkdown(path);
    const ctx = WEEK_CONTEXT[ww];
    let inner = renderMarkdown(md, path);
    let relatedHtml = "";
    const rel = RELATED_LEARN[ww];
    if (rel) {
      relatedHtml =
        '<aside class="related-learn"><strong>Learn chapter:</strong> <a href="#/learn/' +
        rel.slug +
        '">' +
        rel.label +
        "</a> — concepts, videos, and links (study alongside or before practice).</aside>";
    }
    if (ctx) {
      inner =
        '<div class="week-intro"><div class="phase-tag">' +
        ctx.phase +
        '</div><p><strong>Week ' +
        ww +
        ".</strong> " +
        ctx.focus +
        "</p></div>" +
        relatedHtml +
        inner;
    } else if (relatedHtml) {
      inner = relatedHtml + inner;
    }
    inner +=
      '<aside class="work-tip"><strong>Keep your work organized.</strong> Save outputs under <code>my-submissions/week-' +
      ww +
      "/</code> in your clone.</aside>";
    const n = parseInt(ww, 10);
    let pager = '<nav class="week-pager" aria-label="Adjacent weeks">';
    if (n > 1) {
      pager +=
        '<button type="button" class="pager-link" data-pager-week="' +
        String(n - 1).padStart(2, "0") +
        '">← Week ' +
        String(n - 1).padStart(2, "0") +
        "</button>";
    }
    if (n < 14) {
      pager +=
        '<button type="button" class="pager-link pager-link--next" data-pager-week="' +
        String(n + 1).padStart(2, "0") +
        '">Week ' +
        String(n + 1).padStart(2, "0") +
        " →</button>";
    }
    pager += "</nav>";
    inner += pager;

    contentEl.querySelector(".md-body").outerHTML = '<article class="md-body">' + inner + "</article>";
  } catch (e) {
    contentEl.querySelector(".md-body").innerHTML = '<p class="error">' + e.message + "</p>";
  }

  contentEl.querySelectorAll("[data-pager-week]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const w = btn.getAttribute("data-pager-week");
      setHash({ view: "week", week: w, tab: "readme" });
    });
  });

  contentEl.querySelectorAll(".week-tabs button[data-tab]").forEach((btn) => {
    btn.addEventListener("click", () => {
      setHash({ view: "week", week: ww, tab: btn.getAttribute("data-tab") });
    });
  });
}

function buildWeekTabs(ww, activeKey) {
  let buttons = "";
  WEEK_TAB_ORDER.forEach((key) => {
    const v = WEEK_FILES[key];
    if (!v) return;
    if (v.weeks && !v.weeks.includes(ww)) return;
    const active = key === activeKey ? " active" : "";
    buttons +=
      '<button type="button" class="' +
      active.trim() +
      '" data-tab="' +
      key +
      '" data-tab-target="' +
      key +
      '">' +
      v.label +
      "</button>";
  });
  return '<div class="week-tabs">' + buttons + "</div>";
}

function updateSidebarActive(route) {
  document.querySelectorAll(".nav-link").forEach((el) => {
    el.classList.remove("active");
    const learn = el.getAttribute("data-learn");
    if (learn !== null) {
      const hubActive = learn === "" && route.view === "learn" && !route.slug;
      const chapterActive =
        learn && route.view === "learn" && route.slug === learn;
      if (hubActive || chapterActive) el.classList.add("active");
    }
    const nav = el.getAttribute("data-route");
    if (route.view === "page" && nav === route.id) el.classList.add("active");
    if (route.view === "home" && nav === "home") el.classList.add("active");
    if (route.view === "week" && nav === "course-weeks") el.classList.add("active");
  });
}

async function route() {
  const contentEl = document.getElementById("content");
  const breadcrumbEl = document.getElementById("breadcrumb");
  const r = parseHash();

  updateSidebarActive(r);

  if (r.view === "home") showHome(contentEl, breadcrumbEl);
  else if (r.view === "page") await showPage(contentEl, breadcrumbEl, r.id);
  else if (r.view === "learn") await showLearn(contentEl, breadcrumbEl, r.slug);
  else if (r.view === "week") await showWeek(contentEl, breadcrumbEl, r.week, r.tab);

  document.getElementById("sidebar")?.classList.remove("open");
  document.getElementById("overlay")?.classList.remove("show");
}

function initNav() {
  document.querySelectorAll(".nav-link[data-route]").forEach((el) => {
    el.addEventListener("click", (e) => {
      e.preventDefault();
      const id = el.getAttribute("data-route");
      if (id === "home") setHash({ view: "home" });
      else setHash({ view: "page", id });
    });
  });

  document.querySelectorAll(".week-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const w = btn.getAttribute("data-week");
      setHash({ view: "week", week: w, tab: "readme" });
    });
  });

  document.querySelectorAll(".nav-link[data-learn]").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      const raw = btn.getAttribute("data-learn");
      if (raw === null) return;
      if (raw === "") setHash({ view: "learn", slug: null });
      else setHash({ view: "learn", slug: raw });
    });
  });

  window.addEventListener("hashchange", route);

  document.getElementById("menu-toggle")?.addEventListener("click", () => {
    document.getElementById("sidebar").classList.toggle("open");
    document.getElementById("overlay").classList.toggle("show");
  });

  document.getElementById("overlay")?.addEventListener("click", () => {
    document.getElementById("sidebar").classList.remove("open");
    document.getElementById("overlay").classList.remove("show");
  });
}

document.addEventListener("DOMContentLoaded", () => {
  marked.setOptions({ gfm: true, breaks: false });
  initNav();
  route();
});
