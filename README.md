# Lantern Moth Club

Two-page responsive site (Home + Contact) built with Bootstrap 6 (v6.0.0-alpha.1).

- Run with VS Code Live Server (Bootstrap JS loads as a module).
- Theme overrides live in `css/style.css` (primary tokens + solid primary button).
- All illustrations in `images/` are original SVG artwork made for this project.

## Deploying (GitHub Pages)

1. Repo **Settings → Pages → Source: GitHub Actions**.
2. Push to `main`. `.github/workflows/pages.yml` runs `scripts/check_assets.py` first.
   If any linked file is missing or a file has no extension (e.g. `css/style`), the deploy stops
   and the live site is left untouched.
3. Local check before pushing: `python3 scripts/check_assets.py`
