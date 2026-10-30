#!/usr/bin/env python3
"""Short addresses on littledaysparents.com (for the app stores and the apps): /privacy, /terms, /support, /delete-account."""
import os
SHORT = {'privacy': '/little-days/privacy/', 'terms': '/little-days/terms/', 'support': '/little-days/support/',
         'delete-account': '/little-days/account-deletion/', 'account-deletion': '/little-days/account-deletion/'}
for name, target in SHORT.items():
    os.makedirs(name, exist_ok=True)
    url = 'https://littledaysparents.com' + target
    open(os.path.join(name, 'index.html'), 'w').write(
        f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Little Days</title>'
        f'<link rel="canonical" href="{url}"><meta http-equiv="refresh" content="0; url={target}">'
        f'<meta name="robots" content="noindex"></head><body><p><a href="{target}">Continue to Little Days</a></p></body></html>\n')
