// M&B preview: mobile menu and Services submenu. No tracking, no forms.
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
