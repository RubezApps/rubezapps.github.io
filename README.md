# rubezapps.github.io

Public website for **Little Days Parents** (by RubezApps), published with GitHub Pages at https://littledaysparents.com (custom domain, file `CNAME`; the old https://rubezapps.github.io addresses redirect there)

| Address | What it is |
|---|---|
| `/` and `/en/` | Little Days Parents homepage (Vietnamese / English) |
| `/little-days/` | Little Days Parents help site — privacy policy, terms, account deletion, support (English; Vietnamese under `/little-days/vi/`) |
| `/privacy`, `/terms`, `/support`, `/delete-account` | Short addresses that forward to the Little Days help pages (`src/redirects.py`) |
| `/sitemap.xml` | Page list for Google, made by `src/sitemap.py` |
| `/app-ads.txt` | AdMob authorised-seller file for the RubezApps AdMob account (pub-9300769352038198) |

Operator and privacy contact: Vũ Trần Nhật Nguyên (RubezApps), appmakernguyen@gmail.com.

## Editing

Page text lives in `src/developer/build-pages.py` and `src/little-days-help/build_pages.py`. After editing, run `./build.sh` from this folder and commit the regenerated pages.

Never add identity documents, ID numbers, dates of birth, home addresses, passwords or API keys to this repository: everything here is public.
