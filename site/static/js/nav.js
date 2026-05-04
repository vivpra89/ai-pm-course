// Dropdown toggle
function toggleDd(id) {
  var el = document.getElementById(id);
  var wasOpen = el.classList.contains('open');
  document.querySelectorAll('.nav-dropdown').forEach(function (d) { d.classList.remove('open'); });
  if (!wasOpen) { el.classList.add('open'); }
}
document.addEventListener('click', function (e) {
  if (!e.target.closest || !e.target.closest('.nav-dropdown')) {
    document.querySelectorAll('.nav-dropdown').forEach(function (d) { d.classList.remove('open'); });
  }
});

// Mobile overlay — class-based for maximum compatibility
function toggleMobile() {
  var ov = document.getElementById('mobile-overlay');
  if (ov) { ov.classList.toggle('open'); }
}

document.addEventListener('DOMContentLoaded', function () {
  // Close mobile overlay when a link inside it is clicked
  var ov = document.getElementById('mobile-overlay');
  if (ov) {
    ov.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { ov.classList.remove('open'); });
    });
  }

  // Week page tabs
  var btns = document.querySelectorAll('.week-tabs button');
  var panels = document.querySelectorAll('.tab-panel');
  btns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      btns.forEach(function (b) { b.classList.remove('active'); });
      panels.forEach(function (p) { p.hidden = true; });
      btn.classList.add('active');
      var panel = document.getElementById(btn.dataset.tab);
      if (panel) { panel.hidden = false; }
    });
  });
});
