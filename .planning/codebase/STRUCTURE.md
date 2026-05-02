# Codebase Structure

**Analysis Date:** 2026-05-02

## Directory Layout

```
/
├── _bibliography/  # Academic publication references (.bib files)
├── _data/          # YAML data files for templating
├── _includes/      # Reusable Liquid template components
├── _layouts/       # Page layout templates
├── _news/          # News items / updates
├── _pages/         # Main site pages (e.g., About, CV, Blog)
├── _plugins/       # Custom Jekyll ruby plugins
├── _posts/         # Blog posts
├── _projects/      # Project pages/portfolio
├── _scripts/       # Automation/build scripts
├── assets/         # Static assets (images, CSS, JS)
├── bin/            # Executable commands
├── old-site/       # Legacy website content backup
├── .github/        # GitHub Actions workflows
├── _config.yml     # Site configuration
├── Gemfile         # Ruby dependencies
└── package.json    # Node.js development dependencies
```

## Directory Purposes

**`_pages/`:**
- Purpose: Standalone static pages (routing).
- Contains: Markdown files like `about.md`, `cv.md`, `publications.md`.
- Key files: `_pages/about.md` (Home page)

**`_includes/`:**
- Purpose: Reusable partial templates.
- Contains: Liquid template snippets.
- Key files: `_includes/scripts.liquid`, `_includes/disqus.liquid`.

**`_layouts/`:**
- Purpose: Structure for different types of content.
- Contains: HTML files with Liquid template variables.

**`assets/`:**
- Purpose: Static resources delivered to the browser.
- Contains: CSS, JavaScript, fonts, profile images.

## Key File Locations

**Entry Points:**
- `_config.yml`: Global site configuration.
- `_pages/about.md`: Usually mapped to the home page `/`.

**Configuration:**
- `Gemfile`: Plugin configuration.
- `package.json`: Dev tools configuration (Prettier).

**Core Logic:**
- `_plugins/`: Custom ruby scripts extending Jekyll functionality.

**Testing:**
- Not strictly present (no testing directory found).

## Naming Conventions

**Files:**
- Posts: `YYYY-MM-DD-title.md` (e.g., `2025-09-11-ug-ml-internships.md`)
- Partials: `kebab-case.liquid` or `kebab-case.html` in `_includes/`

**Directories:**
- Jekyll standard folders prefixed with `_` (e.g., `_posts`, `_layouts`).

## Where to Add New Code

**New Feature (Page):**
- Primary code: `_pages/new-page.md`
- Configuration: Add to `nav` in `_config.yml` if necessary.

**New Component/Module:**
- Implementation: `_includes/new-component.liquid`

**Utilities:**
- Shared styling: `assets/css/`
- Custom ruby logic: `_plugins/`

**New Content:**
- Blog Post: `_posts/YYYY-MM-DD-title.md`
- News Item: `_news/item-name.md`
- Project: `_projects/N_project.md`

## Special Directories

**`old-site/`:**
- Purpose: Contains a backup of an older version of the site (based on directory name).
- Generated: No
- Committed: Yes

---

*Structure analysis: 2026-05-02*