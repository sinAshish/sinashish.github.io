# Theme Switcher Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement a dropdown theme switcher in the navbar that allows users to select between multiple light and dark themes, overriding the system preference, and update the site's typography to JetBrains Mono.

**Architecture:** We will modify the existing theme toggle button to be a dropdown menu. The selected theme will be saved in `localStorage` as `theme` (the specific theme name, e.g., 'catppuccin-mocha' or 'system'). We'll update the `_sass/_themes.scss` to include definitions for the new themes using CSS variables. We will update the global font family to use JetBrains Mono via Google Fonts.

**Tech Stack:** HTML, SCSS, JavaScript (Jekyll environment)

---

### Task 1: Update Global Font to JetBrains Mono

**Files:**
- Modify: `_includes/head.liquid`
- Modify: `_sass/_base.scss`

- [ ] **Step 1: Add JetBrains Mono to Google Fonts in `_includes/head.liquid`**
Add the font link inside the `<head>` tag. Look for the existing google fonts link or add it near the top.

```html
<!-- Fonts & Icons -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,100..800;1,100..800&display=swap">
```

- [ ] **Step 2: Update typography in `_sass/_base.scss`**
Change the font families to use JetBrains Mono as the primary font, falling back to other monospaced fonts. Also remove other generic font-family declarations like `sans-serif` or `serif` from `body` if they exist and force JetBrains Mono.

```scss
// Find the body or root selector and update the font-family
body {
  font-family: "JetBrains Mono", monospace;
  // ... existing properties
}

// Ensure headers also use it if they have specific font-families set
h1, h2, h3, h4, h5, h6 {
  font-family: "JetBrains Mono", monospace;
}
```

- [ ] **Step 3: Commit**

```bash
git add _includes/head.liquid _sass/_base.scss
git commit -m "feat: change global typography to JetBrains Mono"
```

---

### Task 2: Define Theme Colors in SCSS

**Files:**
- Modify: `_sass/_themes.scss`

- [ ] **Step 1: Add theme variables for the new light themes**
Add CSS variable definitions for `[data-theme="catppuccin-latte"]`, `[data-theme="tokyo-day"]`, and ensure the default `light` theme variables exist under `:root` or `html[data-theme="light"]`.

```scss
html[data-theme="catppuccin-latte"] {
  --global-bg-color: #eff1f5;
  --global-text-color: #4c4f69;
  --global-text-color-light: #7c7f93;
  --global-theme-color: #1e66f5;
  --global-hover-color: #1e66f5;
  --global-hover-text-color: #eff1f5;
  --global-footer-bg-color: #e6e9ef;
  --global-footer-text-color: #5c5f77;
  --global-footer-link-color: #4c4f69;
  --global-card-bg-color: #e6e9ef;
  // Add other necessary overrides from the base light theme
}

html[data-theme="tokyo-day"] {
  --global-bg-color: #e1e2e7;
  --global-text-color: #3760bf;
  --global-text-color-light: #6172b0;
  --global-theme-color: #0f4b6e;
  --global-hover-color: #0f4b6e;
  --global-hover-text-color: #e1e2e7;
  --global-footer-bg-color: #cfd3df;
  --global-footer-text-color: #3760bf;
  --global-footer-link-color: #0f4b6e;
  --global-card-bg-color: #cfd3df;
}
```

- [ ] **Step 2: Add theme variables for the new dark themes**
Add CSS variable definitions for `[data-theme="catppuccin-mocha"]`, `[data-theme="monokai"]`, `[data-theme="nord"]`, `[data-theme="tokyo-night"]`, and ensure default `dark` exists.

```scss
html[data-theme="catppuccin-mocha"] {
  --global-bg-color: #1e1e2e;
  --global-text-color: #cdd6f4;
  --global-text-color-light: #a6adc8;
  --global-theme-color: #89b4fa;
  --global-hover-color: #89b4fa;
  --global-hover-text-color: #1e1e2e;
  --global-footer-bg-color: #181825;
  --global-footer-text-color: #bac2de;
  --global-footer-link-color: #cdd6f4;
  --global-card-bg-color: #181825;
}

html[data-theme="monokai"] {
  --global-bg-color: #272822;
  --global-text-color: #f8f8f2;
  --global-text-color-light: #75715e;
  --global-theme-color: #f92672;
  --global-hover-color: #f92672;
  --global-hover-text-color: #272822;
  --global-footer-bg-color: #1e1f1c;
  --global-footer-text-color: #f8f8f0;
  --global-footer-link-color: #f8f8f2;
  --global-card-bg-color: #1e1f1c;
}

html[data-theme="nord"] {
  --global-bg-color: #2e3440;
  --global-text-color: #d8dee9;
  --global-text-color-light: #4c566a;
  --global-theme-color: #88c0d0;
  --global-hover-color: #88c0d0;
  --global-hover-text-color: #2e3440;
  --global-footer-bg-color: #242933;
  --global-footer-text-color: #e5e9f0;
  --global-footer-link-color: #d8dee9;
  --global-card-bg-color: #242933;
}

html[data-theme="tokyo-night"] {
  --global-bg-color: #1a1b26;
  --global-text-color: #c0caf5;
  --global-text-color-light: #565f89;
  --global-theme-color: #7aa2f7;
  --global-hover-color: #7aa2f7;
  --global-hover-text-color: #1a1b26;
  --global-footer-bg-color: #16161e;
  --global-footer-text-color: #a9b1d6;
  --global-footer-link-color: #c0caf5;
  --global-card-bg-color: #16161e;
}
```

- [ ] **Step 3: Commit**

```bash
git add _sass/_themes.scss
git commit -m "feat: add color palettes for new light and dark themes"
```

---

### Task 3: Build the UI Dropdown Switcher

**Files:**
- Modify: `_includes/header.liquid`
- Modify: `_sass/_base.scss` (or a dedicated component scss)

- [ ] **Step 1: Replace the toggle button with a dropdown in `_includes/header.liquid`**
Locate the existing `<button id="light-toggle">` and replace it with a Bootstrap dropdown structure containing all our themes.

```html
<!-- Theme Switcher Dropdown -->
<li class="nav-item dropdown">
  <button class="btn btn-link nav-link dropdown-toggle" id="theme-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" title="Change theme">
    <i class="ti ti-palette"></i> Theme
  </button>
  <div class="dropdown-menu dropdown-menu-right" aria-labelledby="theme-toggle">
    <h6 class="dropdown-header">Light</h6>
    <button class="dropdown-item theme-select" data-theme-value="light">Default Light</button>
    <button class="dropdown-item theme-select" data-theme-value="catppuccin-latte">Catppuccin Latte</button>
    <button class="dropdown-item theme-select" data-theme-value="tokyo-day">Tokyo Day</button>
    <div class="dropdown-divider"></div>
    <h6 class="dropdown-header">Dark</h6>
    <button class="dropdown-item theme-select" data-theme-value="dark">Default Dark</button>
    <button class="dropdown-item theme-select" data-theme-value="catppuccin-mocha">Catppuccin Mocha</button>
    <button class="dropdown-item theme-select" data-theme-value="monokai">Monokai</button>
    <button class="dropdown-item theme-select" data-theme-value="nord">Nord</button>
    <button class="dropdown-item theme-select" data-theme-value="tokyo-night">Tokyo Night</button>
    <div class="dropdown-divider"></div>
    <button class="dropdown-item theme-select" data-theme-value="system">System Default</button>
  </div>
</li>
```

- [ ] **Step 2: Add styles for the dropdown**
Ensure the dropdown looks nice and fits the navbar. Add this to `_sass/_base.scss`.

```scss
.dropdown-menu {
  background-color: var(--global-bg-color);
  border-color: var(--global-divider-color);
}
.dropdown-item {
  color: var(--global-text-color);
  &:hover {
    background-color: var(--global-card-bg-color);
    color: var(--global-theme-color);
  }
}
.dropdown-header {
  color: var(--global-text-color-light);
  font-weight: bold;
}
```

- [ ] **Step 3: Commit**

```bash
git add _includes/header.liquid _sass/_base.scss
git commit -m "feat: add theme switcher dropdown UI"
```

---

### Task 4: Update JavaScript Theme Logic

**Files:**
- Modify: `assets/js/theme.js`

- [ ] **Step 1: Rewrite theme resolution logic**
Currently, `theme.js` expects only "light", "dark", or "system". We need to support the specific theme names, while categorizing them into base "light" or "dark" for third-party scripts (like Mermaid or Chart.js) that only understand binary themes.

```javascript
// At the top of assets/js/theme.js

const LIGHT_THEMES = ['light', 'catppuccin-latte', 'tokyo-day'];
const DARK_THEMES = ['dark', 'catppuccin-mocha', 'monokai', 'nord', 'tokyo-night'];

// Determine if a specific theme is essentially light or dark
const getBaseTheme = (themeName) => {
  if (LIGHT_THEMES.includes(themeName)) return 'light';
  if (DARK_THEMES.includes(themeName)) return 'dark';
  return 'light'; // fallback
};
```

- [ ] **Step 2: Update `determineComputedTheme`**

```javascript
// Determine the actual specific theme to apply
let determineComputedTheme = () => {
  let themeSetting = determineThemeSetting();
  if (themeSetting === "system") {
    const userPref = window.matchMedia;
    if (userPref && userPref("(prefers-color-scheme: dark)").matches) {
      return "dark"; // Default dark when system is dark
    } else {
      return "light"; // Default light when system is light
    }
  } else {
    return themeSetting; // E.g., 'nord', 'catppuccin-latte'
  }
};
```

- [ ] **Step 3: Update `applyTheme` to handle specific vs base themes**

```javascript
let applyTheme = () => {
  let specificTheme = determineComputedTheme();
  let baseTheme = getBaseTheme(specificTheme); // 'light' or 'dark'

  transTheme();
  
  // Apply specific theme to the HTML tag for CSS variables
  document.documentElement.setAttribute("data-theme", specificTheme);
  
  // Third party tools only know 'light' or 'dark' base themes
  setHighlight(baseTheme);
  setGiscusTheme(baseTheme);
  setSearchTheme(baseTheme);

  if (typeof mermaid !== "undefined") setMermaidTheme(baseTheme);
  if (typeof Diff2HtmlUI !== "undefined") setDiff2htmlTheme(baseTheme);
  if (typeof echarts !== "undefined") setEchartsTheme(baseTheme);
  if (typeof Plotly !== "undefined") setPlotlyTheme(baseTheme);
  if (typeof vegaEmbed !== "undefined") setVegaLiteTheme(baseTheme);

  // Add class to tables.
  let tables = document.getElementsByTagName("table");
  for (let i = 0; i < tables.length; i++) {
    if (baseTheme == "dark") {
      tables[i].classList.add("table-dark");
    } else {
      tables[i].classList.remove("table-dark");
    }
  }

  // Set jupyter notebooks themes.
  let jupyterNotebooks = document.getElementsByClassName("jupyter-notebook-iframe-container");
  for (let i = 0; i < jupyterNotebooks.length; i++) {
    let bodyElement = jupyterNotebooks[i].getElementsByTagName("iframe")[0].contentWindow.document.body;
    if (baseTheme == "dark") {
      bodyElement.setAttribute("data-jp-theme-light", "false");
      bodyElement.setAttribute("data-jp-theme-name", "JupyterLab Dark");
    } else {
      bodyElement.setAttribute("data-jp-theme-light", "true");
      bodyElement.setAttribute("data-jp-theme-name", "JupyterLab Light");
    }
  }

  // Updates the background of medium-zoom overlay.
  if (typeof medium_zoom !== "undefined") {
    medium_zoom.update({
      background: getComputedStyle(document.documentElement).getPropertyValue("--global-bg-color") + "ee",
    });
  }
};
```

- [ ] **Step 4: Update event listeners in `initTheme`**

Remove the `toggleThemeSetting` binding to the old `light-toggle` button. Bind events to the new dropdown items.

```javascript
let initTheme = () => {
  let themeSetting = determineThemeSetting();
  setThemeSetting(themeSetting);

  document.addEventListener("DOMContentLoaded", function () {
    const themeSelectors = document.querySelectorAll('.theme-select');
    themeSelectors.forEach(btn => {
      btn.addEventListener('click', (e) => {
        const selectedTheme = e.target.getAttribute('data-theme-value');
        setThemeSetting(selectedTheme);
      });
    });
  });

  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", ({ matches }) => {
    applyTheme();
  });
};
```

- [ ] **Step 5: Clean up old theme toggle logic**
Remove `toggleThemeSetting` function as it's no longer used (we directly set the selected theme now). Remove `html[data-theme-setting="..."]` CSS blocks from `_sass/_themes.scss` if they exist and manage the display of the old toggle icons.

- [ ] **Step 6: Commit**

```bash
git add assets/js/theme.js _sass/_themes.scss
git commit -m "feat: implement javascript logic for multi-theme switching"
```
