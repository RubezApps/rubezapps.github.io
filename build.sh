#!/bin/sh
# Rebuilds the published pages from src/. Run from the repository root.
set -e
for s in developer little-days-help; do mkdir -p src/$s/dist/en src/$s/dist/assets; cp src/$s/assets/* src/$s/dist/assets/; done
(cd src/developer && python3 build-pages.py)
(cd src/little-days-help && python3 build_pages.py)
cp -r src/developer/dist/. .
mkdir -p little-days && cp -r src/little-days-help/dist/. little-days/ && rm -f little-days/robots.txt
rmdir little-days/en 2>/dev/null || true
rm -rf src/developer/dist src/little-days-help/dist
# Short addresses (littledaysparents.com/privacy etc.)
python3 src/redirects.py
