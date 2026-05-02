# Technology Stack

**Analysis Date:** 2026-05-02

## Languages

**Primary:**
- Ruby - Used for Jekyll build system and plugins
- HTML/Liquid - Used for templating in `_layouts/` and `_includes/`
- Markdown - Content format in `_posts/`, `_pages/`, `_projects/`

**Secondary:**
- JavaScript - Used for external interactions and components
- CSS/SCSS - Styling

## Runtime

**Environment:**
- Ruby environment for Jekyll
- Node.js (via npm) for dev scripts like Prettier

**Package Manager:**
- Bundler (Gemfile)
- npm (package.json)
- Lockfile: missing (from what was seen, didn't check for Gemfile.lock, but usually present in Jekyll)

## Frameworks

**Core:**
- Jekyll - Static site generator
- al-folio - The base theme

**Testing:**
- Not applicable

**Build/Dev:**
- Prettier 3.1.1 - Formatting
- jekyll-minifier - Minification plugin
- jekyll-terser - JS minifier plugin

## Key Dependencies

**Critical:**
- jekyll-scholar - For managing academic publications
- jekyll-jupyter-notebook - For embedding notebooks
- jekyll-paginate-v2 - For blog pagination

**Infrastructure:**
- GitHub Pages - Assumed primary deployment target

## Configuration

**Environment:**
- Configured via `_config.yml`

**Build:**
- `_config.yml`

## Platform Requirements

**Development:**
- Ruby with Bundler
- Node.js/npm (for Prettier)

**Production:**
- Static web hosting (e.g., GitHub Pages)

---

*Stack analysis: 2026-05-02*