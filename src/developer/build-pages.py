"""Little Days Parents homepage: Vietnamese at / and English at /en/ (littledaysparents.com).
Run from src/developer (build.sh does this). Writes dist/index.html, dist/en/index.html and dist/robots.txt."""
from pathlib import Path
import json
ROOT = Path(__file__).parent / 'dist'
SITE = 'https://littledaysparents.com'
APP = 'Little Days Parents'
EMAIL = 'appmakernguyen@gmail.com'

DATA = {
'vi': dict(
 path='/', title=f'{APP} — Theo dõi bé & cộng đồng cha mẹ',
 desc=f'{APP} là ứng dụng theo dõi bé và cộng đồng cha mẹ: ghi lại cữ ăn, giấc ngủ, thay tã, chia sẻ nhật ký với gia đình và hỏi các bố mẹ khác. Sắp có trên Google Play và App Store.',
 skip='Đến nội dung chính', navf='Tính năng', navp='Các gói', navh='Hỗ trợ', lang='English', nav_label='Điều hướng chính',
 eyebrow='THEO DÕI BÉ · CỘNG ĐỒNG CHA MẸ', h1='Mỗi ngày nhỏ.<br><em>Cùng nhau.</em>',
 intro=f'{APP} giúp cha mẹ ghi lại cữ ăn, giấc ngủ và thay tã của bé, chia sẻ nhật ký với cả nhà và hỏi những bố mẹ đã từng trải qua.',
 soon='Sắp có trên Google Play và App Store', cta='Xem tính năng', caption='Khoảnh khắc nhỏ, kỷ niệm lớn.',
 featlabel='01 / TÍNH NĂNG', featright='Dành cho cha mẹ & người chăm sóc',
 apptag='Theo dõi bé & cộng đồng cha mẹ',
 appdesc='Một nơi cho nhật ký chăm bé hằng ngày, cho cả gia đình và cho những câu hỏi mà chỉ các bố mẹ khác mới hiểu.',
 feats=[('Ghi lại nhịp sinh hoạt', 'Sữa bình, bú mẹ, ăn dặm, thay tã và giấc ngủ ở cùng một nơi, với bộ đếm giờ ngủ và tóm tắt theo ngày.'),
        ('Cùng gia đình chăm bé', 'Mời tối đa 4 người vào gia đình. Mỗi người đăng nhập riêng, nhật ký đồng bộ giữa các điện thoại, bạn chọn ai được xem hay chỉnh sửa.'),
        ('Hỏi các bố mẹ khác', 'Đặt câu hỏi, nhận câu trả lời và bình luận, chia sẻ ảnh và video ngắn về những khoảnh khắc của bé.'),
        ('Nhắc cữ ăn & thông báo', 'Lời nhắc cữ ăn và thông báo hẹn giờ ngủ trên điện thoại, theo gói bạn sử dụng.')],
 notice=f'Dành cho cha mẹ và người chăm sóc trưởng thành. Câu trả lời trong cộng đồng đến từ các phụ huynh khác, không phải bác sĩ; {APP} không chẩn đoán, điều trị hoặc thay thế tư vấn y tế.',
 planlabel='02 / CÁC GÓI', plantitle='Bắt đầu miễn phí',
 plans=[('Miễn phí', 'Có quảng cáo', 'Nhật ký của bé và cộng đồng cha mẹ. Gia đình gồm 2 người; có thể mua thêm thành viên theo tháng, tối đa 4 người.'),
        ('Plus', 'Theo tháng', 'Đầy đủ tính năng, không quảng cáo, gia đình tối đa 4 người.'),
        ('Pro', 'Theo năm', 'Giống Plus, thanh toán theo năm.')],
 plannote='Giá và điều kiện gia hạn sẽ hiển thị trong ứng dụng trước khi bạn mua.',
 aboutlabel='03 / NGƯỜI LÀM RA ỨNG DỤNG', abouttitle='Được làm bởi<br>một gia đình.',
 aboutp=f'{APP} được làm bởi RubezApps, một studio ứng dụng nhỏ của một gia đình tại Việt Nam. Vũ Trần Nhật Nguyên, một người mẹ, là chủ sở hữu và điều hành dự án. Chồng chị, Ruben Holder, là giáo viên và phụ trách phần lập trình.',
 team=[('N', 'Vũ Trần Nhật Nguyên', 'Chủ sở hữu & điều hành · Mẹ', 'Lên ý tưởng, quản lý nội dung, cộng đồng và hỗ trợ người dùng.'),
       ('R', 'Ruben Holder', 'Lập trình viên · Giáo viên', 'Xây dựng và bảo trì ứng dụng.')],
 helplabel='04 / THÔNG TIN & HỖ TRỢ', helpright=APP,
 helps=[('Quyền riêng tư', f'Cách thông tin trong {APP} được xử lý.', 'privacy/'),
        ('Hỗ trợ', 'Liên hệ khi gặp vấn đề về tài khoản hoặc nội dung.', 'support/'),
        ('Xóa tài khoản', 'Cách xóa tài khoản hoặc gửi yêu cầu xóa dữ liệu.', 'account-deletion/')],
 read='Xem chi tiết', terms='Điều khoản & nội quy', helpbase='/little-days/vi/',
 contact='Cùng trò chuyện nhé.', contactdesc=f'Câu hỏi về {APP}? Hãy gửi email cho Nguyên.',
 foot='Do Vũ Trần Nhật Nguyên điều hành · Việt Nam', foot2=f'{APP} đang phát triển. Chưa có trên Google Play hoặc App Store.'),
'en': dict(
 path='/en/', title=f'{APP} — Baby tracker & parents community',
 desc=f'{APP} is a baby tracker and parents community app: log feeding, sleep and diapers, share the journal with your family and ask other parents. Coming soon to Google Play and the App Store.',
 skip='Skip to main content', navf='Features', navp='Plans', navh='Help', lang='Tiếng Việt', nav_label='Main navigation',
 eyebrow='BABY TRACKER · PARENTS COMMUNITY', h1='Every little day.<br><em>Together.</em>',
 intro=f'{APP} helps you log your baby’s feeds, sleep and diapers, share the journal with your family, and ask parents who have been there.',
 soon='Coming soon to Google Play and the App Store', cta='See the features', caption='Little moments. Lasting memories.',
 featlabel='01 / FEATURES', featright='For parents & caregivers',
 apptag='Baby tracker & parents community',
 appdesc='One place for everyday baby care, for the whole family, and for the questions only other parents understand.',
 feats=[('Follow the little routines', 'Bottles, breastfeeding, food, diapers and sleep in one place, with a sleep timer and daily summaries.'),
        ('Bring the family along', 'Invite up to 4 people into your family. Everyone signs in with their own account, the journal syncs across phones, and you choose who can view or edit.'),
        ('Ask other parents', 'Post questions, get answers and comments, and share photos and short videos of your baby’s moments.'),
        ('Feeding reminders & alerts', 'Feeding reminders and sleep-timer notifications on your phone, depending on your plan.')],
 notice=f'For adult parents and caregivers. Community answers come from other parents, not doctors; {APP} does not diagnose, treat or replace medical advice.',
 planlabel='02 / PLANS', plantitle='Start for free',
 plans=[('Free', 'With ads', 'Baby journal and the parents community. A family of 2 people; a monthly add-on allows up to 4.'),
        ('Plus', 'Monthly', 'All features, no ads, a family of up to 4 people.'),
        ('Pro', 'Yearly', 'The same as Plus, paid yearly.')],
 plannote='Prices and renewal terms are shown in the app before you buy.',
 aboutlabel='03 / WHO MAKES IT', abouttitle='Made by<br>a family.',
 aboutp=f'{APP} is made by RubezApps, a small family app studio in Vietnam. Vũ Trần Nhật Nguyên, a mom, owns and runs the project. Her husband, Ruben Holder, is a teacher and looks after the coding.',
 team=[('N', 'Vũ Trần Nhật Nguyên', 'Owner & project lead · Mom', 'Shapes the app and looks after content, the community and user support.'),
       ('R', 'Ruben Holder', 'Developer · Teacher', 'Builds and maintains the app.')],
 helplabel='04 / INFORMATION & SUPPORT', helpright=APP,
 helps=[('Your privacy', f'How information in {APP} is handled.', 'privacy/'),
        ('App support', 'Get help with your account or community content.', 'support/'),
        ('Account deletion', 'How to delete an account or request data deletion.', 'account-deletion/')],
 read='Read more', terms='Terms & community rules', helpbase='/little-days/',
 contact='Let’s stay in touch.', contactdesc=f'Questions about {APP}? Email Nguyên.',
 foot='Run by Vũ Trần Nhật Nguyên · Vietnam', foot2=f'{APP} is in development. Not yet available on Google Play or the App Store.'),
}

def structured(d, lang):
    """Tells Google the site name, the app and who makes it."""
    return json.dumps([
        {'@context': 'https://schema.org', '@type': 'WebSite', 'name': APP, 'alternateName': 'Little Days', 'url': SITE + '/', 'inLanguage': ['vi', 'en']},
        {'@context': 'https://schema.org', '@type': 'Organization', 'name': 'RubezApps', 'url': SITE + '/', 'logo': SITE + '/assets/icon-512.png', 'email': EMAIL},
        {'@context': 'https://schema.org', '@type': 'MobileApplication', 'name': APP, 'operatingSystem': 'Android, iOS', 'applicationCategory': 'LifestyleApplication',
         'description': d['desc'], 'url': SITE + d['path'], 'image': SITE + '/assets/icon-512.png', 'inLanguage': lang, 'publisher': {'@type': 'Organization', 'name': 'RubezApps'}},
    ], ensure_ascii=False)

for lang, d in DATA.items():
    other = DATA['en' if lang == 'vi' else 'vi']
    url = SITE + d['path']
    head = (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{d["title"]}</title><meta name="description" content="{d["desc"]}"><meta name="theme-color" content="#fbf9f3">'
            f'<link rel="canonical" href="{url}"><link rel="alternate" hreflang="vi" href="{SITE}/"><link rel="alternate" hreflang="en" href="{SITE}/en/"><link rel="alternate" hreflang="x-default" href="{SITE}/">'
            f'<link rel="icon" type="image/png" sizes="512x512" href="/assets/icon-512.png"><link rel="apple-touch-icon" href="/assets/icon-512.png"><link rel="stylesheet" href="/assets/style.css">'
            f'<meta property="og:type" content="website"><meta property="og:site_name" content="{APP}"><meta property="og:title" content="{d["title"]}"><meta property="og:description" content="{d["desc"]}">'
            f'<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/assets/og-image.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
            f'<meta property="og:locale" content="{"vi_VN" if lang == "vi" else "en_US"}"><meta name="twitter:card" content="summary_large_image">'
            f'<script type="application/ld+json">{structured(d, lang)}</script></head><body>')
    h = head + (
        f'<a class="skip" href="#main">{d["skip"]}</a><header><div class="wrap nav"><a class="brand" href="{d["path"]}"><img class="brandlogo" src="/assets/baby-logo.webp" width="38" height="38" alt="">{APP}</a>'
        f'<nav aria-label="{d["nav_label"]}"><a class="desktop-link" href="#features">{d["navf"]}</a><a class="desktop-link" href="#plans">{d["navp"]}</a><a class="desktop-link" href="#help">{d["navh"]}</a>'
        f'<a class="language" href="{other["path"]}" lang="{"en" if lang == "vi" else "vi"}">{d["lang"]}</a></nav></div></header>'
        f'<main id="main" class="wrap"><section class="hero"><div><div class="eyebrow"><span class="dot"></span>{d["eyebrow"]}</div><h1>{d["h1"]}</h1><p class="intro">{d["intro"]}</p>'
        f'<p class="soon"><span class="status"><span class="dot"></span>{d["soon"]}</span></p><a class="button" href="#features">{d["cta"]} <span aria-hidden="true">↓</span></a></div>'
        f'<div class="studio-art" aria-hidden="true"><div class="art-grid"></div><div class="orb orb-one"></div><div class="orb orb-two"></div>'
        f'<div class="brand-tile app-tile"><img src="/assets/baby-logo.webp" width="110" height="110" alt=""><span>LITTLE DAYS PARENTS</span></div>'
        f'<div class="art-caption"><span>{d["caption"]}</span><span>♡</span></div></div></section>'
        f'<div class="section-label" id="features"><span>{d["featlabel"]}</span><span>{d["featright"]}</span></div><section class="project" aria-labelledby="app-title"><div>'
        f'<div class="app-name"><img src="/assets/baby-logo.webp" width="64" height="64" alt="{APP} logo"><div><h2 id="app-title" class="app-title">{APP}</h2><small>{d["apptag"]}</small></div></div>'
        f'<p>{d["appdesc"]}</p><p class="note">{d["notice"]}</p></div><div class="features">'
        + ''.join(f'<article class="feature"><span class="num">0{i}</span><div><h3>{t}</h3><p>{x}</p></div></article>' for i, (t, x) in enumerate(d['feats'], 1))
        + f'</div></section><section class="areas" id="plans" aria-labelledby="plans-title"><div class="eyebrow">{d["planlabel"]}</div><h2 id="plans-title">{d["plantitle"]}</h2><div class="area-grid">'
        + ''.join(f'<article class="area"><span class="area-status">{s}</span><h3>{n}</h3><p>{x}</p></article>' for n, s, x in d['plans'])
        + f'</div><p class="plan-note">{d["plannote"]}</p></section>'
        f'<section class="about" id="about" aria-labelledby="about-title"><div><div class="eyebrow">{d["aboutlabel"]}</div><h2 id="about-title">{d["abouttitle"]}</h2></div><div><p>{d["aboutp"]}</p><div class="team">'
        + ''.join(f'<div class="person"><span class="initial" aria-hidden="true">{i}</span><div><strong>{n}</strong><small>{r}</small><p>{x}</p></div></div>' for i, n, r, x in d['team'])
        + f'</div></div></section><div class="section-label" id="help"><span>{d["helplabel"]}</span><span>{d["helpright"]}</span></div><section class="resources" aria-label="{d["navh"]}">'
        + ''.join(f'<a class="resource" href="{d["helpbase"] + p}"><h3>{t} <span aria-hidden="true">↗</span></h3><p>{x}</p><span class="link">{d["read"]}</span></a>' for t, x, p in d['helps'])
        + f'</section><section class="contact" id="contact"><div><h2>{d["contact"]}</h2><p>{d["contactdesc"]}</p></div><a class="button light email" href="mailto:{EMAIL}">{EMAIL} <span aria-hidden="true">↗</span></a></section></main>'
        f'<footer><div class="wrap footer-inner"><p><span class="foot-brand">© 2026 {APP} · RubezApps</span><br>{d["foot"]}</p><p>{d["foot2"]}<br><a href="{d["helpbase"]}terms/">{d["terms"]}</a></p></div></footer></body></html>')
    target = ROOT / ('en/index.html' if lang == 'en' else 'index.html')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(h)
(ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
print('Built Vietnamese and English homepages')
