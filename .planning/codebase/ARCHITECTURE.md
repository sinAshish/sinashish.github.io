<!-- refreshed: 2026-05-02 -->
# Architecture

**Analysis Date:** 2026-05-02

## System Overview

```text
┌─────────────────────────────────────────────────────────────┐
│                      Jekyll Build Process                    │
├──────────────────┬──────────────────┬───────────────────────┤
│    Content       │    Templates     │    Configuration      │
│  `_posts/`       │  `_layouts/`     │   `_config.yml`       │
│  `_pages/`       │  `_includes/`    │                       │
└────────┬─────────┴────────┬─────────┴──────────┬────────────┘
         │                  │                     │
         ▼                  ▼                     ▼
┌─────────────────────────────────────────────────────────────┐
│                      Jekyll Core / Plugins                   │
│         `Gemfile` plugins (e.g. jekyll-scholar)              │
└─────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────┐
│                     Static Site (HTML/CSS/JS)                │
│  `_site/` (generated)                                        │
└─────────────────────────────────────────────────────────────┘
```

## Component Responsibilities

| Component | Responsibility | File |
|-----------|----------------|------|
| Config | Defines site metadata, navigation, and plugin settings | `_config.yml` |
| Pages | Main structure/routing pages of the site (e.g., about, CV) | `_pages/*.md` |
| Posts | Blog posts | `_posts/*.md` |
| Includes | Reusable Liquid templates (e.g., analytics, comments, header) | `_includes/` |
| Layouts | Structural HTML templates for different content types | `_layouts/` |
| Plugins | Custom ruby logic for markdown processing and data fetching | `Gemfile` |

## Pattern Overview

**Overall:** Static Site Generation

**Key Characteristics:**
- Content authored in Markdown
- Templates structured in Liquid
- Configured via YAML
- Pre-rendered HTML output

## Layers

**Content Layer:**
- Purpose: Contains text, images, and raw data
- Location: `_pages/`, `_posts/`, `_projects/`, `_news/`, `_data/`
- Contains: Markdown files, YAML data files, images
- Depends on: Layouts layer
- Used by: Jekyll generator

**Presentation Layer:**
- Purpose: Defines visual structure and layout
- Location: `_layouts/`, `_includes/`, `assets/`
- Contains: HTML, Liquid templates, CSS/SCSS, JS
- Depends on: Content layer (injects content)
- Used by: End users' browsers

## Data Flow

### Primary Request Path

1. User requests URL (e.g., `/about/`)
2. GitHub Pages serves pre-rendered HTML file from `_site/about/index.html`
3. Browser downloads associated `assets/` (CSS/JS) and renders page

### Site Generation Flow

1. Jekyll reads `_config.yml`
2. Jekyll processes `_data/`, `_pages/`, `_posts/` files using `_layouts/` and `_includes/`
3. Plugins (e.g., `jekyll-scholar`) process special tags (e.g., bibliographies)
4. Static HTML is output to `_site/`

**State Management:**
- Stateless static content delivery

## Key Abstractions

**Liquid Includes:**
- Purpose: Reusable UI components
- Examples: `_includes/scripts.liquid`, `_includes/disqus.liquid`
- Pattern: Template partials

## Entry Points

**Site Root:**
- Location: `_pages/about.md` (likely acts as `index.html`)
- Triggers: Root URL visit
- Responsibilities: Displays main profile and introduction

## Architectural Constraints

- **Static content:** The site has no backend database; all dynamic behavior must happen client-side (via JS) or at build time (via Jekyll plugins).
- **GitHub Pages:** Must adhere to GitHub Pages build constraints if relying on default workflows (or use GitHub Actions to run custom plugins).

## Anti-Patterns

### Modifying `_site/` directly

**What happens:** Making changes directly in the generated `_site/` directory.
**Why it's wrong:** Changes will be overwritten on the next Jekyll build.
**Do this instead:** Modify the source files (`_pages/`, `_includes/`, `_layouts/`) or `_config.yml`.

## Error Handling

**Strategy:** Build-time failure.

**Patterns:**
- Errors in Liquid syntax or Markdown parsing cause Jekyll build to fail.
- Missing configuration variables evaluate to empty strings in Liquid.

## Cross-Cutting Concerns

**Logging:** Jekyll build logs
**Validation:** Liquid strict mode (if enabled)
**Authentication:** N/A (Public site)

---

*Architecture analysis: 2026-05-02*