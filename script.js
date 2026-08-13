/* ═══════════════════════════════════════════════════
   GÖRKEM KOÇ — PORTFOLIO  |  script.js
═══════════════════════════════════════════════════ */

/* ── LANGUAGE SYSTEM ──────────────────────────────
   Çeviri elemanları data-tr / data-en taşır.

   DEĞİŞEN: dil artık URL'e de yazılıyor (?lang=tr) ve
   canonical / og:locale / meta description dile göre
   güncelleniyor. Öncesinde Türkçe içerik yalnızca
   localStorage'da yaşıyordu; ne indekslenebiliyordu
   ne de paylaşılabiliyordu.

   Öncelik sırası:  URL  >  localStorage  >  varsayılan (en)
──────────────────────────────────────────────────── */
const LANG_KEY  = 'gk_lang';
const SITE_URL  = 'https://cv.ops-center.org/';
const SUPPORTED = ['en', 'tr'];

const META = {
  en: {
    title: 'Görkem KOÇ — Principal Specialist, System & Infrastructure',
    desc:  'Görkem Koç — Principal Specialist, System & Infrastructure at Etiya. Hybrid identity (AD + Entra ID), endpoint estate at scale, VMware/Hyper-V, ISO 27001 & PCI-DSS operations.',
    ogTitle: 'Görkem Koç — Principal Specialist, System & Infrastructure',
    ogDesc:  'Hybrid identity, endpoint estate and virtualisation at enterprise scale. Etiya · Ankara.',
    locale:  'en_GB',
    altLocale: 'tr_TR',
    canonical: SITE_URL
  },
  tr: {
    title: 'Görkem KOÇ — Principal Specialist, Sistem & Altyapı',
    desc:  'Görkem Koç — Etiya’da Principal Specialist, Sistem & Altyapı. Hibrit kimlik (AD + Entra ID), uç nokta yönetimi, VMware/Hyper-V, ISO 27001 & PCI-DSS operasyonları.',
    ogTitle: 'Görkem Koç — Principal Specialist, Sistem & Altyapı',
    ogDesc:  'Kurumsal ölçekte hibrit kimlik, uç nokta yönetimi ve sanallaştırma. Etiya · Ankara.',
    locale:  'tr_TR',
    altLocale: 'en_GB',
    canonical: SITE_URL + '?lang=tr'
  }
};

function readLangFromUrl() {
  const p = new URLSearchParams(window.location.search).get('lang');
  return SUPPORTED.includes(p) ? p : null;
}

function setMeta(selector, attr, value) {
  const el = document.querySelector(selector);
  if (el) el.setAttribute(attr, value);
}

let currentLang =
  readLangFromUrl() ||
  (SUPPORTED.includes(localStorage.getItem(LANG_KEY)) ? localStorage.getItem(LANG_KEY) : null) ||
  'en';

function applyLang(lang, pushUrl) {
  currentLang = lang;
  try { localStorage.setItem(LANG_KEY, lang); } catch (e) {}

  document.documentElement.setAttribute('data-lang', lang);
  document.documentElement.setAttribute('lang', lang);

  document.querySelectorAll('[data-tr]').forEach(el => {
    const val = el.getAttribute('data-' + lang);
    if (val !== null) el.innerHTML = val;
  });

  const label = document.getElementById('langLabel');
  if (label) {
    label.textContent = lang.toUpperCase();
    const inactive = label.nextElementSibling?.nextElementSibling;
    if (inactive) inactive.textContent = lang === 'tr' ? 'EN' : 'TR';
  }

  /* ── başlık + meta etiketleri ─────────────────────
     Arama motoru ve LinkedIn kazıyıcısı JS çalıştırmasa
     bile HTML'deki İngilizce varsayılanı görür; ?lang=tr
     ile gelen kullanıcı ve TR canonical ise doğru veriyi
     alır. Statik site için ulaşılabilecek en iyi nokta;
     mükemmeli iki ayrı HTML dosyası üretmek olurdu ve
     bu aşamada o karmaşıklığa değmez.
  ──────────────────────────────────────────────────── */
  const m = META[lang];
  document.title = m.title;
  setMeta('meta[name="description"]',    'content', m.desc);
  setMeta('meta[property="og:title"]',   'content', m.ogTitle);
  setMeta('meta[property="og:description"]', 'content', m.ogDesc);
  setMeta('meta[name="twitter:title"]',  'content', m.ogTitle);
  setMeta('meta[name="twitter:description"]', 'content', m.ogDesc);
  setMeta('meta[property="og:locale"]',  'content', m.locale);
  setMeta('meta[property="og:locale:alternate"]', 'content', m.altLocale);
  setMeta('meta[property="og:url"]',     'content', m.canonical);
  setMeta('link[rel="canonical"]',       'href',    m.canonical);

  if (pushUrl) {
    const url = lang === 'tr' ? '?lang=tr' : window.location.pathname;
    history.replaceState({ lang }, '', url + window.location.hash);
  }
}

document.getElementById('langBtn')?.addEventListener('click', () => {
  applyLang(currentLang === 'tr' ? 'en' : 'tr', true);
});

applyLang(currentLang, false);


/* ── DOLDURULMAMIŞ METRİK UYARISI ─────────────────
   index.html'de <b class="todo"> kalan yer varsa
   konsola yazar. Yayına çıkmadan önce DevTools'u aç
   ve konsolun temiz olduğunu gör.
──────────────────────────────────────────────────── */
(function warnOnTodos() {
  const n = document.querySelectorAll('b.todo').length;
  if (n > 0) {
    console.warn(
      '%c[cv] ' + n + ' adet doldurulmamış metrik var (b.todo). ' +
      'Rakamları yazıp class="todo" niteliklerini sil.',
      'color:#b45309;font-weight:600'
    );
  }
})();


/* ── THEME (dark mode) ────────────────────────────── */
function setTheme(theme) {
  if (theme === 'dark') document.documentElement.setAttribute('data-theme', 'dark');
  else document.documentElement.removeAttribute('data-theme');
  try { localStorage.setItem('gk_theme', theme); } catch (e) {}
}
document.getElementById('themeBtn')?.addEventListener('click', () => {
  const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
  setTheme(isDark ? 'light' : 'dark');
});


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
  hamburger.setAttribute('aria-expanded', String(open));
});

mobileMenu?.querySelectorAll('a').forEach(a => {
  a.addEventListener('click', () => {
    hamburger?.classList.remove('open');
    mobileMenu?.classList.remove('open');
    hamburger?.setAttribute('aria-expanded', 'false');
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
const sections   = document.querySelectorAll('section[id]');
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
    const href = a.getAttribute('href');
    if (href === '#' || href.length < 2) return;
    const target = document.querySelector(href);
    if (!target) return;
    e.preventDefault();
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
});


/* ── CHIP TAP FEEDBACK ────────────────────────────── */
document.querySelectorAll('.tags span').forEach(chip => {
  chip.addEventListener('click', () => {
    chip.style.transform = 'scale(.92)';
    setTimeout(() => { chip.style.transform = ''; }, 120);
  });
});

/* ── TEMİZLİK NOTU ────────────────────────────────────
   Eski dosyada .bento-card, .stat-big, .cert-card-body,
   .tl-entry, .tl-logo, .chip, .skill-tags, .tl-tags
   seçicilerine bağlı bloklar vardı; bu sınıfların
   hiçbiri index.html'de yok. Ölü kod olarak
   çıkarıldı — özellikle stat counter bloğu, olmayan
   bir DOM'u her sayfa yüklemesinde tarıyordu.
──────────────────────────────────────────────────── */
