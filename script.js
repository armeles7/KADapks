// Interactivité générale du site KADapks
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;
const downloadCount = document.getElementById('download-count');

// Thème sombre / clair
const savedTheme = localStorage.getItem('kada-theme');
if (savedTheme === 'dark') {
  body.classList.add('dark');
  themeToggle.textContent = '☀️ Mode clair';
} else {
  body.classList.remove('dark');
  themeToggle.textContent = '🌙 Mode sombre';
}

themeToggle.addEventListener('click', () => {
  body.classList.toggle('dark');
  const isDark = body.classList.contains('dark');
  localStorage.setItem('kada-theme', isDark ? 'dark' : 'light');
  themeToggle.textContent = isDark ? '☀️ Mode clair' : '🌙 Mode sombre';
  themeToggle.setAttribute('aria-label', isDark ? 'Activer le mode clair' : 'Activer le mode sombre');
});

// Suivi de téléchargements
let count = Number(localStorage.getItem('kada-downloads') || 0);
downloadCount.textContent = count;

const handleDownload = (event) => {
  const appName = event.currentTarget.dataset.download;
  count += 1;
  localStorage.setItem('kada-downloads', count);
  downloadCount.textContent = count;

  const message = `${appName} ajouté au suivi de téléchargements.`;
  const notice = document.createElement('div');
  notice.className = 'download-toast';
  notice.textContent = message;
  document.body.appendChild(notice);

  setTimeout(() => {
    notice.remove();
  }, 1800);
};

document.querySelectorAll('[data-download]').forEach((link) => {
  link.addEventListener('click', handleDownload);
});
