#!/usr/bin/env python3
"""Writes sitemap.xml: every real page on littledaysparents.com, with its other-language version.
Short forwarding addresses (/privacy, /terms, ...) are left out on purpose: they are noindex redirects."""
from datetime import date
SITE = 'https://littledaysparents.com'
# (Vietnamese page, English page)
PAIRS = [('/', '/en/')] + [(f'/little-days/vi/{p}', f'/little-days/{p}') for p in ['', 'privacy/', 'terms/', 'support/', 'account-deletion/']]
today = date.today().isoformat()
rows = []
for vi, en in PAIRS:
    alt = (f'<xhtml:link rel="alternate" hreflang="vi" href="{SITE}{vi}"/>'
           f'<xhtml:link rel="alternate" hreflang="en" href="{SITE}{en}"/>')
    for loc in (vi, en):
        rows.append(f'<url><loc>{SITE}{loc}</loc><lastmod>{today}</lastmod>{alt}</url>')
open('sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
                               + '\n'.join(rows) + '\n</urlset>\n')
print(f'sitemap.xml: {len(rows)} pages')
