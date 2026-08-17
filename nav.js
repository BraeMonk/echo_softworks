// Shared mobile nav (hamburger menu) behavior — used by index, scripts, marketplace, sell.
(function(){
  const btn = document.getElementById('burgerBtn');
  const wrap = document.getElementById('navLinksWrap');
  const scrim = document.getElementById('navScrim');
  if(!btn || !wrap) return;

  function closeMenu(){
    btn.classList.remove('open');
    wrap.classList.remove('open');
    if(scrim) scrim.classList.remove('open');
    btn.setAttribute('aria-expanded','false');
    document.body.style.overflow='';
  }
  function openMenu(){
    btn.classList.add('open');
    wrap.classList.add('open');
    if(scrim) scrim.classList.add('open');
    btn.setAttribute('aria-expanded','true');
    document.body.style.overflow='hidden';
  }
  btn.addEventListener('click', function(){
    wrap.classList.contains('open') ? closeMenu() : openMenu();
  });
  if(scrim) scrim.addEventListener('click', closeMenu);
  wrap.querySelectorAll('a').forEach(function(a){ a.addEventListener('click', closeMenu); });
  window.addEventListener('resize', function(){ if(window.innerWidth > 860) closeMenu(); });
  window.addEventListener('keydown', function(e){ if(e.key === 'Escape') closeMenu(); });
})();
