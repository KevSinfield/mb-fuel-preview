// M&B preview: mobile menu and Services submenu. Visit alerts at the end (preview only).
(function () {
  var menuBtn = document.querySelector('.menu-toggle');
  var nav = document.getElementById('site-nav');
  if (menuBtn && nav) {
    menuBtn.addEventListener('click', function () {
      var open = menuBtn.getAttribute('aria-expanded') === 'true';
      menuBtn.setAttribute('aria-expanded', String(!open));
      menuBtn.querySelector('.txt').textContent = open ? 'Menu' : 'Close';
      nav.classList.toggle('open', !open);
    });
  }
  var subBtn = document.querySelector('.sub-toggle');
  var sub = document.getElementById('services-sub');
  function closeSub() { if (subBtn) { subBtn.setAttribute('aria-expanded', 'false'); sub.classList.remove('open'); } }
  if (subBtn && sub) {
    subBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = subBtn.getAttribute('aria-expanded') === 'true';
      subBtn.setAttribute('aria-expanded', String(!open));
      sub.classList.toggle('open', !open);
    });
    document.addEventListener('click', function (e) { if (!sub.contains(e.target)) closeSub(); });
  }
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    if (sub && sub.classList.contains('open')) { closeSub(); subBtn.focus(); return; }
    if (nav && nav.classList.contains('open')) { menuBtn.click(); menuBtn.focus(); }
  });
  // Close the mobile menu after following an in-page link
  if (nav) nav.addEventListener('click', function (e) {
    if (e.target.closest('a') && nav.classList.contains('open')) menuBtn.click();
  });
})();

/* ---------- Visit alerts (preview only; remove before launch) ----------
   A short, anonymous note to Kev's phone via ntfy.sh when the published preview is opened or a
   key button is tapped, as on the other client previews. It sends only the page, the ?for= / ?from=
   link tag (if any), the device type and browser, and the screen width.
   No cookies, no visitor IDs, and we don't log IP addresses. It runs only on the GitHub Pages copy.
   Visit any page with ?me once to stop your own device sending alerts (?me=0 to undo). */
(function () {
  "use strict";
  var TOPIC = "https://ntfy.sh/mbf-preview-0uyi2x4w03";
  function store(kind, k, v) { try { var s = window[kind]; if (v === undefined) return s.getItem(k); if (v === null) s.removeItem(k); else s.setItem(k, v); } catch (e) { return null; } }
  var q = new URLSearchParams(location.search);
  if (q.has("me")) store("localStorage", "mbf-me", q.get("me") === "0" ? null : "1");
  var off = store("localStorage", "mbf-me") === "1" || location.hostname !== "kevsinfield.github.io";
  var tag = (q.get("for") || q.get("from") || "").toLowerCase().replace(/[^a-z0-9-]/g, "").slice(0, 20);
  if (tag) store("sessionStorage", "mbf-from", tag); else tag = store("sessionStorage", "mbf-from") || "";

  function device() {
    var u = navigator.userAgent;
    var d = /iPhone/.test(u) ? "iPhone" : /iPad/.test(u) || (/Macintosh/.test(u) && navigator.maxTouchPoints > 1) ? "iPad"
      : /Android/.test(u) ? "Android" : /Macintosh/.test(u) ? "Mac" : /Windows/.test(u) ? "Windows PC" : "Other device";
    var b = /Edg\//.test(u) ? "Edge" : /CriOS|Chrome\//.test(u) ? "Chrome" : /FxiOS|Firefox\//.test(u) ? "Firefox" : /Safari\//.test(u) ? "Safari" : "";
    return d + (b ? " (" + b + ")" : "") + ", " + screen.width + "px screen";
  }
  function page() {
    var t = (document.title || "").split(" | ")[0];
    return /^M&B Fuel Injection Service$/.test(t) || !/\|/.test(document.title) ? "Homepage" : t;
  }
  function send(title, icon) {
    if (off) return;
    var msg = page() + " · " + device() + (tag ? " · for: " + tag : "");
    try {
      fetch(TOPIC + "?title=" + encodeURIComponent(title) + "&tags=" + (icon || "eyes"),
        { method: "POST", body: msg, keepalive: true, mode: "cors" }).catch(function () {});
    } catch (e) {}
  }

  var key = "mbf-seen-" + location.pathname;
  if (store("sessionStorage", key) !== "1") {
    store("sessionStorage", key, "1");
    var ref = "";
    try { if (document.referrer && new URL(document.referrer).hostname !== location.hostname) ref = " (came from " + new URL(document.referrer).hostname + ")"; } catch (e) {}
    send("M&B preview opened" + (tag ? " by " + tag : "") + ": " + page() + ref, "eyes");
  }

  /* Key taps, once each per page view */
  var done = {};
  function once(k, title, icon) { if (done[k]) return; done[k] = 1; send(title, icon); }
  document.addEventListener("click", function (e) {
    var t = e.target && e.target.closest ? e.target : null; if (!t) return;
    if (t.closest('a[href^="tel:"]')) once("call", "Tapped a Call button", "telephone_receiver");
    else if (t.closest(".wa")) once("wa", "Tapped WhatsApp (not live yet)", "speech_balloon");
    else if (t.closest('a[href*="#estimate"]')) once("est", "Tapped Request a free estimate", "memo");
  });
})();
