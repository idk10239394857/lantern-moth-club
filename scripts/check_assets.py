"""Fail if any local href/src in the HTML pages points to a file that doesn't exist,
or if a required project file is missing (e.g. css/style.css saved without its extension)."""
import pathlib, re, sys

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
required = ["index.html", "contact.html", "css/bootstrap.min.css", "css/style.css", "js/bootstrap.bundle.min.js"]
errors = [f"Missing required file: {p}" for p in required if not (root / p).is_file()]

for page in sorted(root.glob("*.html")):
    for ref in re.findall(r'(?:href|src)="([^"]+)"', page.read_text(encoding="utf-8")):
        if ref.startswith(("#", "http:", "https:", "mailto:", "tel:", "data:")):
            continue
        target = (page.parent / ref.split("#")[0].split("?")[0])
        if not target.is_file():
            errors.append(f"{page.name}: '{ref}' not found")

for f in root.rglob("*"):
    if f.is_file() and f.suffix == "" and ".git" not in f.parts and f.name not in {"LICENSE", "CNAME"}:
        errors.append(f"File has no extension: {f.relative_to(root)}")

print("\n".join(errors) or "All linked files found.")
sys.exit(1 if errors else 0)
