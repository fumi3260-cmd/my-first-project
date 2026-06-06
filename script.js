/* ============================================================
   PORTFOLIO — script.js
============================================================ */

/* ── Scroll progress bar ──────────────────────────────────── */
const progressBar = document.getElementById('progress-bar');
function updateProgress() {
  const scrolled = window.scrollY;
  const total    = document.documentElement.scrollHeight - window.innerHeight;
  progressBar.style.width = total > 0 ? (scrolled / total * 100) + '%' : '0%';
}

/* ── Nav scroll effect ────────────────────────────────────── */
const nav = document.getElementById('nav');
function onScroll() {
  updateProgress();
  nav.classList.toggle('scrolled', window.scrollY > 50);
}
window.addEventListener('scroll', onScroll, { passive: true });
onScroll(); // run on load

/* ── Mobile hamburger menu ────────────────────────────────── */
const hamburger   = document.querySelector('.hamburger');
const mobileMenu  = document.getElementById('mobile-menu');

hamburger.addEventListener('click', () => {
  const isOpen = hamburger.classList.toggle('open');
  mobileMenu.classList.toggle('open', isOpen);
  hamburger.setAttribute('aria-expanded', isOpen);
  document.body.style.overflow = isOpen ? 'hidden' : '';
});

mobileMenu.querySelectorAll('a').forEach(a => {
  a.addEventListener('click', () => {
    hamburger.classList.remove('open');
    mobileMenu.classList.remove('open');
    hamburger.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  });
});

/* ── IntersectionObserver: fade-in ───────────────────────── */
const io = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    entry.target.classList.add('visible');
    io.unobserve(entry.target);
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.fi').forEach(el => io.observe(el));

/* ── Typing animation in hero ─────────────────────────────── */
const typingTarget = document.getElementById('typing-text');
if (typingTarget) {
  const phrases = [
    'できることを増やす。',
    '業務を自動化する。',
    'データを価値にする。',
    'アイデアを形にする。',
  ];
  let phraseIdx = 0;
  let charIdx   = 0;
  let deleting  = false;
  let paused    = false;

  function type() {
    const current = phrases[phraseIdx];
    if (paused) {
      paused = false;
      setTimeout(type, 1400);
      return;
    }
    if (!deleting) {
      typingTarget.textContent = current.slice(0, ++charIdx);
      if (charIdx === current.length) { deleting = true; paused = true; }
      setTimeout(type, deleting ? 50 : 90);
    } else {
      typingTarget.textContent = current.slice(0, --charIdx);
      if (charIdx === 0) {
        deleting = false;
        phraseIdx = (phraseIdx + 1) % phrases.length;
      }
      setTimeout(type, 45);
    }
  }
  type();
}

/* ── Count-up for stats ───────────────────────────────────── */
function countUp(el) {
  const target = parseFloat(el.dataset.target);
  const suffix = el.dataset.suffix || '';
  const prefix = el.dataset.prefix || '';
  const duration = 1400;
  const start = performance.now();

  function step(now) {
    const progress = Math.min((now - start) / duration, 1);
    const eased    = 1 - Math.pow(1 - progress, 3); // ease-out cubic
    const val      = target * eased;
    el.textContent = prefix + (Number.isInteger(target) ? Math.round(val) : val.toFixed(1)) + suffix;
    if (progress < 1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
}

const statObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    entry.target.querySelectorAll('[data-target]').forEach(el => countUp(el));
    statObserver.unobserve(entry.target);
  });
}, { threshold: 0.4 });

document.querySelectorAll('.stats').forEach(el => statObserver.observe(el));

/* ── Smooth active nav link on scroll ────────────────────── */
const sections     = document.querySelectorAll('section[id]');
const navLinks     = document.querySelectorAll('.nav-links a');

const sectionObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    const id = entry.target.id;
    navLinks.forEach(a => {
      a.classList.toggle('active', a.getAttribute('href') === '#' + id);
    });
  });
}, { rootMargin: '-40% 0px -55% 0px' });

sections.forEach(s => sectionObserver.observe(s));

/* ── Contact form ─────────────────────────────────────────── */
const form  = document.getElementById('contact-form');
const toast = document.getElementById('toast');

form.addEventListener('submit', e => {
  e.preventDefault();

  const name    = form.name.value.trim();
  const email   = form.email.value.trim();
  const message = form.message.value.trim();

  if (!name)    { showToast('お名前を入力してください', '#f97316'); return; }
  if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email))
                { showToast('正しいメールアドレスを入力してください', '#f97316'); return; }
  if (!message) { showToast('メッセージを入力してください', '#f97316'); return; }

  // Simulate async send
  const btn = form.querySelector('.form-submit');
  btn.textContent = '送信中…';
  btn.disabled = true;

  setTimeout(() => {
    form.reset();
    btn.textContent = '送信する';
    btn.disabled = false;
    showToast('✓ メッセージを送信しました！');
  }, 900);
});

function showToast(msg, bg = '#9b5de5') {
  toast.textContent  = msg;
  toast.style.background = bg;
  toast.classList.add('show');
  clearTimeout(toast._t);
  toast._t = setTimeout(() => toast.classList.remove('show'), 3400);
}

/* ── Cursor glow follow (desktop only) ───────────────────── */
if (window.matchMedia('(pointer: fine)').matches) {
  const glow = document.createElement('div');
  glow.style.cssText = `
    position:fixed; pointer-events:none; z-index:9998;
    width:300px; height:300px; border-radius:50%;
    background:radial-gradient(circle, rgba(155,93,229,.06) 0%, transparent 70%);
    transform:translate(-50%,-50%);
    transition:left .12s ease, top .12s ease;
    will-change:left,top;
  `;
  document.body.appendChild(glow);
  window.addEventListener('mousemove', e => {
    glow.style.left = e.clientX + 'px';
    glow.style.top  = e.clientY + 'px';
  }, { passive: true });
}
