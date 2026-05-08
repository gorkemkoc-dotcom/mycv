/* ═══════════════════════════════════════════════════
   GÖRKEM KOÇ — PORTFOLIO  |  script.js
═══════════════════════════════════════════════════ */

/* ── LANGUAGE SYSTEM ──────────────────────────────
   All translatable elements carry data-tr / data-en.
   Toggling swaps textContent and updates html[data-lang].
──────────────────────────────────────────────────── */
const LANG_KEY = 'gk_lang';

/* Default to English on first visit; honor the user's previous choice afterwards. */
let currentLang = localStorage.getItem(LANG_KEY) || 'en';

function applyLang(lang) {
  currentLang = lang;
  localStorage.setItem(LANG_KEY, lang);

  document.documentElement.setAttribute('data-lang', lang);

  // swap text on every tagged element
  document.querySelectorAll('[data-tr]').forEach(el => {
    const val = el.getAttribute('data-' + lang);
    if (val !== null) el.innerHTML = val;
  });

  // update nav label
  const label = document.getElementById('langLabel');
  if (label) {
    label.textContent = lang.toUpperCase();
    const inactive = label.nextElementSibling?.nextElementSibling;
    if (inactive) inactive.textContent = lang === 'tr' ? 'EN' : 'TR';
  }

  // swap page title
  document.title = lang === 'tr'
    ? 'Görkem KOÇ — Principal Specialist, Sistem & Altyapı'
    : 'Görkem KOÇ — Principal Specialist, System & Infrastructure';

  // also keep the <html lang> attribute correct for screen readers / SEO
  document.documentElement.setAttribute('lang', lang);
}

// toggle
document.getElementById('langBtn')?.addEventListener('click', () => {
  applyLang(currentLang === 'tr' ? 'en' : 'tr');
});

// init on load
applyLang(currentLang);


/* ── STICKY NAV ───────────────────────────────────── */
const header = document.getElementById('header');
window.addEventListener('scroll', () => {
  header?.classList.toggle('scrolled', window.scrollY > 30);
}, { passive: true });


/* ── HAMBURGER ────────────────────────────────────── */
const hamburger  = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobileMenu');

hamburger?.addEventListener('click', () => {
  const open = hamburger.classList.toggle('open');
  mobileMenu?.classList.toggle('open', open);
});

// close on link click
mobileMenu?.querySelectorAll('a').forEach(a => {
  a.addEventListener('click', () => {
    hamburger?.classList.remove('open');
    mobileMenu?.classList.remove('open');
  });
});


/* ── SCROLL REVEAL ────────────────────────────────── */
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      revealObserver.unobserve(e.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -30px 0px' });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));


/* ── ACTIVE NAV HIGHLIGHT ─────────────────────────── */
const sections  = document.querySelectorAll('section[id]');
const navAnchors = document.querySelectorAll('.nav-links a[href^="#"]');

const navObserver = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      navAnchors.forEach(a => {
        a.style.color = a.getAttribute('href') === '#' + e.target.id
          ? 'var(--text)' : '';
      });
    }
  });
}, { rootMargin: '-40% 0px -55% 0px' });

sections.forEach(s => navObserver.observe(s));


/* ── SMOOTH SCROLL ────────────────────────────────── */
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const target = document.querySelector(a.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
});


/* ── BENTO CARD SUBTLE TILT ───────────────────────── */
if (window.matchMedia('(hover: hover)').matches) {
  document.querySelectorAll('.bento-card').forEach(card => {
    card.addEventListener('mousemove', e => {
      const r   = card.getBoundingClientRect();
      const x   = (e.clientX - r.left) / r.width  - 0.5;
      const y   = (e.clientY - r.top)  / r.height - 0.5;
      card.style.transform = `translateY(-2px) rotateX(${-y * 4}deg) rotateY(${x * 4}deg)`;
      card.style.transformOrigin = 'center center';
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
    });
  });
}


/* ── STAT COUNTER ─────────────────────────────────── */
function easeOutCubic(t) { return 1 - Math.pow(1 - t, 3); }

const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (!e.isIntersecting) return;
    const el     = e.target;
    const target = parseFloat(el.dataset.count);
    const isFloat = el.dataset.float === '1';
    const dur    = 1600;
    const start  = performance.now();

    function tick(now) {
      const t   = Math.min((now - start) / dur, 1);
      const val = easeOutCubic(t) * target;
      el.textContent = isFloat ? val.toFixed(1) : Math.round(val);
      if (t < 1) requestAnimationFrame(tick);
      else el.textContent = isFloat ? target.toFixed(1) : target;
    }
    requestAnimationFrame(tick);
    counterObserver.unobserve(el);
  });
}, { threshold: 0.6 });

// attach data-count to stat numbers
document.querySelectorAll('.stat-big').forEach(el => {
  const text = el.textContent.trim();
  const num  = parseFloat(text.replace(/[^0-9.]/g, ''));
  if (!isNaN(num) && num > 0) {
    // preserve small element (unit suffix)
    const small = el.querySelector('small');
    const suffix = small ? small.outerHTML : '';
    const counter = document.createElement('span');
    counter.dataset.count = num;
    counter.dataset.float = text.includes('.') ? '1' : '0';
    counter.textContent   = '0';
    el.innerHTML = '';
    el.appendChild(counter);
    if (suffix) el.insertAdjacentHTML('beforeend', suffix);
    counterObserver.observe(counter);
  }
});


/* ── TYPING EFFECT (hero subtitle) ───────────────── */
// Only run if there's a typed span we want to add later
// (currently subtitle is static — leaving hook for future use)


/* ── CHIP HOVER RIPPLE ────────────────────────────── */
document.querySelectorAll('.chip, .skill-tags span, .tl-tags span').forEach(chip => {
  chip.addEventListener('click', () => {
    chip.style.transform = 'scale(.92)';
    setTimeout(() => { chip.style.transform = ''; }, 120);
  });
});


/* ── CERT ROW HOVER GLOW ──────────────────────────── */
document.querySelectorAll('.cert-card-body').forEach(card => {
  card.addEventListener('mouseenter', () => {
    const dot = card.closest('.cert-row')?.querySelector('.cert-dot');
    if (dot) dot.style.transform = 'scale(1.3)';
  });
  card.addEventListener('mouseleave', () => {
    const dot = card.closest('.cert-row')?.querySelector('.cert-dot');
    if (dot) dot.style.transform = '';
  });
});


/* ── TIMELINE ENTRY HIGHLIGHT ─────────────────────── */
const tlObserver = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    const logo = e.target.querySelector('.tl-logo');
    if (logo) logo.style.boxShadow = e.isIntersecting
      ? '0 0 0 4px rgba(59 130 246 / .2), 0 0 20px rgba(59 130 246 / .15)'
      : '';
  });
}, { threshold: 0.4 });

document.querySelectorAll('.tl-entry').forEach(el => tlObserver.observe(el));
