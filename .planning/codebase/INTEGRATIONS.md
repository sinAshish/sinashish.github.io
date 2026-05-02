# External Integrations

**Analysis Date:** 2026-05-02

## APIs & External Services

**Analytics:**
- Google Analytics
  - Config: `site.google_analytics` in `_config.yml`
- Cronitor RUM Analytics
  - Config: `site.cronitor_analytics` in `_config.yml`
- Pirsch Analytics
  - Config: `site.pirsch_analytics` in `_config.yml`
- Openpanel Analytics
  - Config: `site.openpanel_analytics` in `_config.yml`

**Comments:**
- Disqus
  - Config: `site.disqus_shortname` in `_config.yml`
  - Client: `_includes/disqus.liquid`

## Data Storage

**Databases:**
- None (Static site)

**File Storage:**
- Local filesystem only (`assets/`)

**Caching:**
- None

## Authentication & Identity

**Auth Provider:**
- None

## Monitoring & Observability

**Error Tracking:**
- None

**Logs:**
- Google Analytics / external analytics providers

## CI/CD & Deployment

**Hosting:**
- GitHub Pages (inferred from URL `https://sinashish.github.io`)

**CI Pipeline:**
- GitHub Actions (presence of `.github/`)

## Environment Configuration

**Required env vars:**
- Configured via `_config.yml` variables rather than env vars.

**Secrets location:**
- Not applicable for static site

## Webhooks & Callbacks

**Incoming:**
- None

**Outgoing:**
- None

---

*Integration audit: 2026-05-02*