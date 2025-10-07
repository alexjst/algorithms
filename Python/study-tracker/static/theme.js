// Theme Toggle Functionality - Shared across all pages
function initTheme() {
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);
    updateHighlightTheme(savedTheme);
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
    updateHighlightTheme(newTheme);
}

function updateThemeIcon(theme) {
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        themeToggle.textContent = theme === 'dark' ? '☀️' : '🌙';
        themeToggle.title = theme === 'dark' ? 'Switch to Light Mode' : 'Switch to Dark Mode';
    }
}

function updateHighlightTheme(theme) {
    const lightHighlight = document.getElementById('highlight-light');
    const darkHighlight = document.getElementById('highlight-dark');

    if (theme === 'dark') {
        if (lightHighlight) lightHighlight.disabled = true;
        if (darkHighlight) darkHighlight.disabled = false;
    } else {
        if (lightHighlight) lightHighlight.disabled = false;
        if (darkHighlight) darkHighlight.disabled = true;
    }
}

// Initialize theme as early as possible to prevent flash
initTheme();

// Setup event listener when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    }
});
