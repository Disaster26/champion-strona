# -*- coding: utf-8 -*-
"""Generator stron Nauki Jazdy Champion (Witnica).

  python -I _zrodla/build.py              -> wersja testowa (noindex, formularz na adres testowy, 404 dla GitHub Pages)
  python -I _zrodla/build.py --produkcja  -> wersja na docelowy hosting (indeksowanie wlaczone, formularz na biuro.oskchampion@wp.pl)

Folder _zrodla nie jest publikowany (GitHub Pages pomija go przez _config.yml; na hosting go nie wgrywamy).
Wszystkie dane firmy sa w stalych ponizej - zmiana w jednym miejscu zmienia cala strone.
"""
import json, os, sys, html, re, hashlib
from urllib.parse import quote

PROD = '--produkcja' in sys.argv
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
INFO = json.load(open(os.path.join(os.path.dirname(__file__), 'zdjecia.json'), encoding='utf-8'))

DOMENA = 'https://champion-witnica.pl'
# 29.10: data ostatniej aktualizacji stron (sitemap lastmod); wpisy bloga maja wlasne 'zmiana' albo DATA
AKTUALIZACJA = '2026-10-29'
# produkcja: wlasny skrypt PHP na serwerze home.pl (wyslij.php); test na GitHub Pages (bez PHP): FormSubmit
FORM_ADRES = '/wyslij.php' if PROD else 'https://formsubmit.co/ajax/stasiu2626@gmail.com'
FORM_RODO = ('Wiadomości z formularza są wysyłane z serwera tej strony bezpośrednio na naszą skrzynkę e-mail. Dane mogą trafić do dostawcy hostingu strony i dostawcy poczty e-mail - wyłącznie w zakresie potrzebnym do działania tych usług.' if PROD else
             'Wiadomości z formularza są przekazywane na naszą skrzynkę e-mail za pośrednictwem usługi FormSubmit (formsubmit.co). Dane mogą też trafić do dostawcy hostingu strony i dostawcy poczty e-mail - wyłącznie w zakresie potrzebnym do działania tych usług. Korzystanie z usługi FormSubmit może wiązać się z przekazaniem danych poza Europejski Obszar Gospodarczy.')
BASE_404 = '/' if PROD else '/champion-strona/'
WERSJA = '1'

TEL = ('729 993 243', 'tel:+48729993243')
# 28.10: telefony biura (odbierane caly czas w godzinach pracy biura) - prosba klienta
TEL_BIURO = ('95 718 03 35', 'tel:+48957180335')
TEL_BIURO_KOM = ('737 164 747', 'tel:+48737164747')
MAIL = 'biuro.oskchampion@wp.pl'
# 28.10: konto do wplat za kurs (od klienta) - w cenniku i w kontakcie, jak u wiekszosci OSK
KONTO = '88 1020 1954 0000 7702 0429 0433'
FB = 'https://www.facebook.com/p/Nauka-Jazdy-Champion-Witnica-61584649396147/'
GODZINY = 'poniedziałek - piątek 10:00-17:00'


def lam(t):
    """29.10: miejsca, ktore nie moga sie lamac na koncu wiersza (godziny, pn-pt, 107 B, INFO-KIEROWCA, 17-latkow).
    Fonty Barlow nie maja znaku U+2011 (twardy dywiz), dlatego span.nw zamiast &#8209;."""
    t = re.sub(r'(?<![\d:])(\d{1,2}:\d\d-\d{1,2}:\d\d)(?![\d:])', r'<span class="nw">\1</span>', t)
    t = re.sub(r'\b(pn-pt|INFO-KIEROWCA|\d+-latk\w*)', r'<span class="nw">\1</span>', t)
    return t.replace('107 B', '107 B')


GODZINY_H = lam(GODZINY)
BIURO = (52.6732, 14.8977)
PLAC = (52.72346, 15.19181)
G_BIURO = 'https://www.google.com/maps/search/?api=1&query=52.6732%2C14.8977'
G_BIURO_TRASA = 'https://www.google.com/maps/dir/?api=1&destination=52.6732%2C14.8977'
G_PLAC = 'https://www.google.com/maps/search/?api=1&query=52.72346%2C15.19181'
G_PLAC_TRASA = 'https://www.google.com/maps/dir/?api=1&destination=52.72346%2C15.19181'
PDF_STANDARDY = 'dokumenty/standardy-ochrony-maloletnich.pdf'

NAV = [('oferta/', 'Kursy'), ('cennik/', 'Cennik'), ('galeria/', 'O szkole'), ('blog/', 'Blog'), ('kontakt/', 'Kontakt')]
# w stopce dodatkowo FAQ
NAV_STOPKA = NAV[:4] + [('faq/', 'Pytania (FAQ)')] + NAV[4:]

KURSY_FORM = ['Kategoria B', 'Kategoria B+E', 'Kategoria C', 'Kategoria C+E', 'Kwalifikacja wstępna C, CE', 'Szkolenie okresowe C, CE', 'Inne pytanie']

IKONA_TEL = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
IKONA_FB = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 21v-7.6h2.6l.4-3h-3V8.5c0-.87.25-1.46 1.5-1.46h1.6V4.36A21 21 0 0 0 14.3 4.2c-2.3 0-3.9 1.4-3.9 4v2.2H7.8v3h2.6V21z"/></svg>'


def e(s):
    return html.escape(s, quote=True)


def img(name, alt, sizes, R, eager=False, cls=''):
    v = INFO[name]
    srcset = ', '.join(f'{R}img/{fn} {w}w' for fn, w, h in v)
    mid = [x for x in v if x[1] <= 800] or v[:1]
    fn = mid[-1][0]
    W, H = v[-1][1], v[-1][2]
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ''
    return (f'<img{c} src="{R}img/{fn}" srcset="{srcset}" sizes="{sizes}" alt="{e(alt)}" '
            f'width="{W}" height="{H}" {load} decoding="async">')


def og_jpg(nazwa):
    """29.10: podglad linku (Facebook, komunikatory) jako JPG ~1,91:1, max 1200 px - nie wszystkie serwisy czytaja WebP.
    Tworzony raz z najwiekszego WebP (img/og-<nazwa>.jpg), potem uzywany gotowy plik."""
    from PIL import Image
    fn = f'og-{nazwa}.jpg'
    sc = os.path.join(ROOT, 'img', fn)
    if not os.path.exists(sc):
        im = Image.open(os.path.join(ROOT, 'img', INFO[nazwa][-1][0])).convert('RGB')
        w, h = im.size
        r = 1200 / 630
        if w / h > r:
            nw = round(h * r); im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
        else:
            nh = round(w / r); im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
        W = min(1200, im.width)
        im = im.resize((W, round(W / r)), Image.LANCZOS)
        im.save(sc, 'JPEG', quality=82, optimize=True, progressive=True)
    with Image.open(sc) as im:
        return fn, im.width, im.height


def og_obraz(nazwa=None):
    if nazwa:
        fn, w, h = og_jpg(nazwa)
        return (f'<meta property="og:image" content="{DOMENA}/img/{fn}">\n'
                f'<meta property="og:image:width" content="{w}">\n<meta property="og:image:height" content="{h}">')
    return (f'<meta property="og:image" content="{DOMENA}/img/og.jpg">\n'
            '<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">')


def najwiekszy(name):
    return INFO[name][-1][0]


def preload_img(name, sizes, R, media=''):
    v = INFO[name]
    srcset = ', '.join(f'{R}img/{fn} {w}w' for fn, w, h in v)
    m = f' media="{media}"' if media else ''
    return f'<link rel="preload" as="image" imagesrcset="{srcset}" imagesizes="{sizes}"{m} fetchpriority="high">\n'


# ---------------------------------------------------------------- dane strukturalne
CENNIK = [
    # (kategoria, pojazd, [(pozycja, cena, przypis)], uwagi)
    ('Kategoria B', 'Toyota Yaris', [
        ('Kurs bez teorii lub z teorią online', '4 490 zł'),
        ('Kurs z teorią stacjonarną', '5 100 zł'),
        ('Kurs ekspresowy - dopłata', '1 000 zł'),
        ('Godzina dodatkowa dla kursantów z innych ośrodków', '160 zł'),
        ('Godzina dodatkowa dla kursantów OSK Champion', '150 zł'),
    ], '30 godzin teorii i 30 godzin jazd albo - po zdanym egzaminie teoretycznym w WORD - 4 godziny pierwszej pomocy i 30 godzin jazd. W cenie kursu pół godziny jazdy na placu egzaminacyjnym WORD oraz podręczniki do nauki testów.'),
    ('Kategoria B+E', 'Fiat Scudo z przyczepą', [
        ('Kurs (15 godzin jazd, bez teorii)', '2 900 zł'),
        ('Godzina dodatkowa', '200 zł'),
    ], ''),
    ('Kategoria C', 'MAN TGL 12.240', [
        ('Kurs (20 godzin teorii, 30 godzin jazd)', '5 800 zł'),
        ('Godzina dodatkowa', '250 zł'),
    ], 'Po zdanym egzaminie teoretycznym w WORD: 30 godzin jazd.'),
    ('Kategoria C+E', 'MAN TGX 18.500 z naczepą Wielton', [
        ('Kurs (25 godzin jazd, bez teorii)', '6 500 zł'),
        ('Godzina dodatkowa', '280 zł'),
    ], ''),
    ('Kwalifikacja wstępna C, CE', 'kierowcy zawodowi', [
        ('Kwalifikacja wstępna przyspieszona', '3 500 zł'),
        ('Kwalifikacja wstępna', '5 900 zł'),
    ], ''),
    ('Szkolenie okresowe C, CE', 'kierowcy zawodowi', [
        ('Szkolenie 35 godzin (5 dni)', '1 000 zł'),
    ], 'Wymagany numer PKZ. Po ukończeniu szkolenia wpis kodu 95 do prawa jazdy.'),
]


def cena_liczba(c):
    return c.replace(' ', '').replace('zł', '')


def schema_firma():
    oferty = []
    for kat, poj, poz, uw in CENNIK:
        for nazwa, cena in poz:
            if 'Godzina' in nazwa or 'dopłata' in nazwa:
                continue
            oferty.append({'@type': 'Offer', 'name': f'{kat} - {nazwa}', 'price': cena_liczba(cena), 'priceCurrency': 'PLN'})
    return {
        '@context': 'https://schema.org',
        '@type': 'DrivingSchool',
        '@id': DOMENA + '/#osk',
        'name': 'Nauka Jazdy Champion',
        'alternateName': ['OSK Champion Witnica', 'Ośrodek Szkolenia Kierowców Champion'],
        'legalName': 'Nauka Jazdy Champion Aurelia Gajewska',
        'url': DOMENA + '/',
        'logo': DOMENA + '/img/logo-360.webp',
        'image': DOMENA + '/img/og.jpg',
        'description': 'Ośrodek szkolenia kierowców w Witnicy: kursy prawa jazdy kat. B, B+E, C i C+E, kwalifikacja wstępna i szkolenia okresowe (kod 95). Plac manewrowy w Gorzowie Wielkopolskim.',
        'priceRange': '1 000-6 500 zł',
        'currenciesAccepted': 'PLN',
        'paymentAccepted': 'wpłata w biurze, przelew bankowy',
        'telephone': '+48729993243',
        'contactPoint': [{'@type': 'ContactPoint', 'contactType': 'customer service', 'telephone': t, 'availableLanguage': 'pl'}
                         for t in ('+48729993243', '+48957180335', '+48737164747')],
        'email': MAIL,
        'taxID': '5961210126',
        'foundingDate': '2004-05',
        'address': {'@type': 'PostalAddress', 'streetAddress': 'ul. Gorzowska 6', 'postalCode': '66-460',
                    'addressLocality': 'Witnica', 'addressRegion': 'lubuskie', 'addressCountry': 'PL'},
        'geo': {'@type': 'GeoCoordinates', 'latitude': BIURO[0], 'longitude': BIURO[1]},
        'hasMap': G_BIURO,
        'openingHoursSpecification': [{'@type': 'OpeningHoursSpecification',
                                       'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                                       'opens': '10:00', 'closes': '17:00'}],
        'sameAs': [FB],
        'areaServed': [{'@type': 'City', 'name': n} for n in ['Witnica', 'Gorzów Wielkopolski', 'Kostrzyn nad Odrą', 'Dębno']],
        'location': [
            {'@type': 'Place', 'name': 'Biuro i sala wykładowa', 'address': {'@type': 'PostalAddress', 'streetAddress': 'ul. Gorzowska 6', 'postalCode': '66-460', 'addressLocality': 'Witnica', 'addressCountry': 'PL'},
             'geo': {'@type': 'GeoCoordinates', 'latitude': BIURO[0], 'longitude': BIURO[1]}},
            {'@type': 'Place', 'name': 'Plac manewrowy', 'address': {'@type': 'PostalAddress', 'streetAddress': 'ul. Kostrzyńska 12', 'postalCode': '66-400', 'addressLocality': 'Gorzów Wielkopolski', 'addressCountry': 'PL'},
             'geo': {'@type': 'GeoCoordinates', 'latitude': PLAC[0], 'longitude': PLAC[1]}},
        ],
        'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': 'Kursy prawa jazdy i szkolenia kierowców', 'itemListElement': oferty},
    }


def okruszki(sciezka, nazwa, posrednie=()):
    """posrednie: [(sciezka, nazwa)] miedzy strona glowna a biezaca (np. Blog dla wpisu)."""
    el = [('', 'Strona główna')] + list(posrednie) + [(sciezka, nazwa)]
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': DOMENA + '/' + s} for i, (s, n) in enumerate(el)]}


# ---------------------------------------------------------------- szkielet strony
def strona(sciezka, tytul, opis, tresc, glowna=False, schemy=None, preload='', noindex=False, base=None, og_typ='website', og_img=None):
    R = '../' * sciezka.count('/')
    if base is not None:
        R = base
    robots = '<meta name="robots" content="noindex, nofollow">\n' if (not PROD or noindex) else ''
    nav = ''
    for href, nazwa in NAV:
        cur = ' aria-current="page"' if sciezka == href or (href == 'blog/' and sciezka.startswith('blog/')) else ''
        nav += f'      <a href="{R}{href}"{cur}>{nazwa}</a>\n'
    sch = ''
    for s in (schemy or []):
        sch += '<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False, separators=(',', ':')) + '</script>\n'
    # 29.10: w panelu hamburgera dodatkowo FAQ pod Blogiem (w menu desktopowym nie)
    panel = ''
    for href, nazwa in NAV:
        cur = ' aria-current="page"' if sciezka == href or (href == 'blog/' and sciezka.startswith('blog/')) else ''
        panel += f'    <a href="{R}{href}"{cur}>{nazwa}</a>\n'
        if href == 'blog/':
            cur = ' aria-current="page"' if sciezka == 'faq/' else ''
            panel += f'    <a href="{R}faq/"{cur}>Pytania (FAQ)</a>\n'
    canon = '' if base is not None else f'<link rel="canonical" href="{DOMENA}/{sciezka}">\n'
    dom = R if R else './'
    return f'''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{robots}<title>{e(tytul)}</title>
<meta name="description" content="{e(opis)}">
{canon}<meta name="theme-color" content="#3f48cc">
<meta property="og:type" content="{og_typ}">
<meta property="og:locale" content="pl_PL">
<meta property="og:site_name" content="Nauka Jazdy Champion Witnica">
<meta property="og:title" content="{e(tytul)}">
<meta property="og:description" content="{e(opis)}">
<meta property="og:url" content="{DOMENA}/{sciezka}">
{og_obraz(og_img)}
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{R}favicon.ico" sizes="32x32">
<link rel="icon" href="{R}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{R}apple-touch-icon.png">
<link rel="preload" href="{R}fonts/barlow-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{R}fonts/barlow-sc-700.woff2" as="font" type="font/woff2" crossorigin>
{preload}<link rel="stylesheet" href="{R}style.css?v={WERSJA}">
{sch}</head>
<body{' class="glowna"' if glowna else ''}>
<a class="skip" href="#tresc">Przejdź do treści</a>
<header class="top">
  <div class="wrap top-in">
    <a class="logo" href="{dom}" aria-label="Nauka Jazdy Champion - strona główna">
      <img src="{R}img/logo-180.webp" srcset="{R}img/logo-180.webp 180w, {R}img/logo-360.webp 360w" sizes="134px" width="180" height="70" alt="Champion - nauka jazdy">
      <span class="logo-tag">Nauka jazdy</span>
    </a>
    <nav class="menu" aria-label="Menu główne">
{nav}    </nav>
    <a class="tel" href="{TEL[1]}" aria-label="Zadzwoń: {TEL[0]}">{IKONA_TEL}<span>{TEL[0]}</span></a>
    <button class="ham" id="ham" type="button" aria-expanded="false" aria-controls="panel" aria-label="Otwórz menu"><span></span><span></span><span></span></button>
  </div>
  <nav class="panel" id="panel" hidden aria-label="Menu">
    <a href="{dom}"{' aria-current="page"' if glowna else ''}>Strona główna</a>
{panel}    <a class="panel-fb" href="{FB}" target="_blank" rel="noopener">{IKONA_FB}Facebook - Nauka Jazdy Champion Witnica</a>
    <p class="panel-info">ul. Gorzowska 6, Witnica<br>biuro {GODZINY_H}</p>
  </nav>
</header>

<a class="fb-tab" href="{FB}" target="_blank" rel="noopener" aria-label="Nauka Jazdy Champion Witnica na Facebooku (nowa karta)">{IKONA_FB}<span>Facebook</span></a>

<main id="tresc">
{tresc}
</main>

<footer class="stopka">
  <div class="wrap stopka-in">
    <div class="st-firma">
      <img src="{R}img/logo-180.webp" srcset="{R}img/logo-180.webp 180w, {R}img/logo-360.webp 360w" sizes="134px" width="180" height="70" alt="Champion - nauka jazdy" loading="lazy">
      <p>Nauka Jazdy Champion<br>Ośrodek Szkolenia Kierowców<br>ul. Gorzowska 6, 66-460 Witnica</p>
    </div>
    <div>
      <p class="st-h">Kontakt</p>
      <p><a href="{TEL[1]}">{TEL[0]}</a><br>Biuro: <a href="{TEL_BIURO[1]}">{TEL_BIURO[0]}</a>, <a href="{TEL_BIURO_KOM[1]}">{TEL_BIURO_KOM[0]}</a><br><a href="mailto:{MAIL}">{MAIL}</a><br>Biuro: {GODZINY_H}</p>
      <p><a class="st-fb" href="{FB}" target="_blank" rel="noopener">{IKONA_FB}Facebook</a></p>
    </div>
    <div>
      <p class="st-h">Plac manewrowy</p>
      <p>ul. Kostrzyńska 12<br>66-400 Gorzów Wielkopolski</p>
    </div>
    <ul class="st-nav">
      <li><a href="{dom}">Strona główna</a></li>
{''.join(f'      <li><a href="{R}{h}">{n}</a></li>{chr(10)}' for h, n in NAV_STOPKA)}    </ul>
  </div>
  <div class="wrap st-dol">
    <p>© <span id="rok">2026</span> Nauka Jazdy Champion Aurelia Gajewska, <span class="nw">NIP 596-121-01-26</span>, <span class="nw">REGON 543119611</span></p>
    <p><a href="{R}{PDF_STANDARDY}" target="_blank" rel="noopener">Standardy ochrony małoletnich (PDF)</a> <a href="{R}polityka-prywatnosci/">Polityka prywatności</a></p>
  </div>
</footer>

<div class="mob" id="mob" aria-hidden="true">
  <a class="mob-tel" href="{TEL[1]}" tabindex="-1">{IKONA_TEL}Zadzwoń</a>
  <a class="mob-cta" href="{R}kontakt/#zapis" tabindex="-1">Zapisz się na kurs</a>
</div>

<script src="{R}app.js?v={WERSJA}" defer></script>
</body>
</html>
'''


# 29.10: wersja pliku liczona z zawartosci (GitHub Pages trzyma pliki 10 min - bez tego nowy HTML
# potrafil zaladowac stary style.css i stare obrazki). Dopisywane do kazdego adresu zasobu w HTML.
_ZASOB = re.compile(r'(?<![\w./-])((?:(?:\.\./)+|/champion-strona/|/|https://[\w.-]+/)?)'
                    r'(img/[\w.-]+\.(?:webp|jpg|png)|style\.css|app\.js|favicon\.ico|favicon\.svg|apple-touch-icon\.png)'
                    r'(?:\?v=[\w]*)?(?=["\s,)])')
_HASZE = {}


def hasz(plik):
    if plik not in _HASZE:
        with open(os.path.join(ROOT, plik), 'rb') as f:
            _HASZE[plik] = hashlib.md5(f.read()).hexdigest()[:8]
    return _HASZE[plik]


def wersjonuj(tekst):
    return _ZASOB.sub(lambda m: f'{m.group(1)}{m.group(2)}?v={hasz(m.group(2))}', tekst)


def zapisz(sciezka, tekst, plik='index.html'):
    tekst = wersjonuj(tekst)
    d = os.path.join(ROOT, sciezka)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, plik), 'w', encoding='utf-8', newline='\n') as f:
        f.write(tekst)


# ---------------------------------------------------------------- wspolne bloki
def ph(h1, lead, R, foto=None, foto_alt='', nad=''):
    if foto:
        f = f'\n    <figure class="ph-foto">{img(foto, foto_alt, "(max-width:760px) 100vw, 44vw", R, eager=True)}</figure>'
        cls = 'ph'
    else:
        f = ''; cls = 'ph ph-bez'
    return f'''<section class="{cls}">
  <div class="wrap ph-in">
    <div class="ph-tx">{nad}
      <h1>{h1}</h1>
      <p class="ph-lead">{lead}</p>
    </div>{f}
  </div>
</section>'''


def formularz(R, idf='zapis', naglowek='Zapisz się albo zapytaj', h='h2'):
    opcje = ''.join(f'<option>{k}</option>' for k in KURSY_FORM)
    return f'''<form class="form" id="form-{idf}" novalidate data-adres="{FORM_ADRES}">
        <{h} class="form-h">{naglowek}</{h}>
        <p class="form-sub">Biuro oddzwoni, poda najbliższy termin kursu i powie, jakie dokumenty przygotować.</p>
        <div class="pole">
          <label for="{idf}-kurs">Kurs</label>
          <select id="{idf}-kurs" name="kurs">{opcje}</select>
        </div>
        <div class="pole">
          <label for="{idf}-imie">Imię i nazwisko</label>
          <input id="{idf}-imie" name="imie" type="text" autocomplete="name" required>
        </div>
        <div class="pole-2">
          <div class="pole">
            <label for="{idf}-tel">Telefon</label>
            <input id="{idf}-tel" name="telefon" type="tel" inputmode="tel" autocomplete="tel" required>
          </div>
          <div class="pole">
            <label for="{idf}-mail">E-mail <span>(nieobowiązkowo)</span></label>
            <input id="{idf}-mail" name="email" type="email" autocomplete="email">
          </div>
        </div>
        <div class="pole">
          <label for="{idf}-tresc">Pytanie <span>(nieobowiązkowo)</span></label>
          <textarea id="{idf}-tresc" name="wiadomosc" rows="3"></textarea>
        </div>
        <div class="hp" aria-hidden="true"><label for="{idf}-hp">Nie wypełniaj tego pola</label><input id="{idf}-hp" name="_honey" type="text" tabindex="-1" autocomplete="off"></div>
        <p class="form-info">Dane z formularza wykorzystamy tylko do kontaktu w sprawie kursu. Więcej w <a href="{R}polityka-prywatnosci/">polityce prywatności</a>.</p>
        <button class="btn btn-pel" type="submit">Wyślij zgłoszenie</button>
        <div class="form-wynik" aria-live="polite"></div>
      </form>'''


def mapa(R, nazwa, h, adres, alt, glink, trasa, opis=''):
    return f'''<figure class="mapa">
        <a class="mapa-img" href="{glink}" target="_blank" rel="noopener" aria-label="{e(h)} - otwórz w Mapach Google (nowa karta)">
          <img src="{R}img/{nazwa}-600.webp" srcset="{R}img/{nazwa}-600.webp 600w, {R}img/{nazwa}-1200.webp 1200w" sizes="(max-width:760px) 100vw, 560px" alt="{e(alt)}" width="1200" height="800" loading="lazy" decoding="async">
        </a>
        <figcaption>
          <strong>{h}</strong>
          <span>{adres}</span>{f'<span class="mapa-opis">{opis}</span>' if opis else ''}
          <span class="mapa-przyc"><a href="{trasa}" target="_blank" rel="noopener">Wyznacz trasę</a><a href="{glink}" target="_blank" rel="noopener">Mapy Google</a></span>
        </figcaption>
      </figure>'''


def mapy(R):
    return f'''<div class="mapy-wrap">
    <div class="mapy">
      {mapa(R, 'mapa-biuro', 'Biuro i sala wykładowa', 'ul. Gorzowska 6, 66-460 Witnica', 'Mapa: biuro Nauki Jazdy Champion przy ul. Gorzowskiej 6 w Witnicy', G_BIURO, G_BIURO_TRASA, GODZINY_H)}
      {mapa(R, 'mapa-plac', 'Plac manewrowy', 'ul. Kostrzyńska 12, 66-400 Gorzów Wielkopolski', 'Mapa: plac manewrowy przy ul. Kostrzyńskiej 12 w Gorzowie Wielkopolskim', G_PLAC, G_PLAC_TRASA)}
    </div>
    <p class="mapy-osm">Mapy © <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">autorzy OpenStreetMap</a></p>
    </div>'''


def dane_kontaktowe(h='h2'):
    return f'''<div class="kon-tx">
      <{h}>Kontakt</{h}>
      <dl class="kon-dl">
        <div><dt>Telefon</dt><dd><a class="kon-tel" href="{TEL[1]}">{TEL[0]}</a></dd></div>
        <div><dt>Telefony do biura</dt><dd><a href="{TEL_BIURO[1]}">{TEL_BIURO[0]}</a> (stacjonarny)<br><a href="{TEL_BIURO_KOM[1]}">{TEL_BIURO_KOM[0]}</a> (komórkowy)</dd></div>
        <div><dt>E-mail</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd></div>
        <div><dt>Konto do wpłat za kurs</dt><dd class="konto">{KONTO}</dd></div>
        <div><dt>Biuro</dt><dd>ul. Gorzowska 6, 66-460 Witnica<br>{GODZINY_H}</dd></div>
        <div><dt>Plac manewrowy</dt><dd>ul. Kostrzyńska 12, 66-400 Gorzów Wielkopolski</dd></div>
        <div><dt>Facebook</dt><dd><a href="{FB}" target="_blank" rel="noopener">Nauka Jazdy Champion Witnica</a></dd></div>
      </dl>
    </div>'''


# kafle kursow: (id, foto, alt, kat, tytul, opis, cena)
KAFLE = [
    ('kat-b', 'kat-b', 'Toyota Yaris Nauki Jazdy Champion na placu manewrowym', 'B', 'Samochód osobowy', 'Toyota Yaris, 30 godz. teorii i 30 godz. jazd. Teoria stacjonarna albo online.', 'od 4 490 zł'),
    ('kat-be', 'kat-be', 'Fiat Scudo z przyczepą do nauki jazdy kat. B+E', 'B+E', 'Samochód z przyczepą', 'Fiat Scudo z przyczepą, 15 godz. jazd, bez teorii.', '2 900 zł'),
    ('kat-c', 'kat-c', 'Ciężarówka MAN TGL OSK Champion na placu manewrowym', 'C', 'Samochód ciężarowy', 'MAN TGL 12.240, 20 godz. teorii i 30 godz. jazd.', '5 800 zł'),
    ('kat-ce', 'kat-ce', 'MAN TGX z naczepą do nauki jazdy kat. C+E', 'C+E', 'Ciężarówka z naczepą', 'MAN TGX 18.500 z naczepą Wielton, 25 godz. jazd.', '6 500 zł'),
    ('kwalifikacja', 'kwal', 'Ciężarówka OSK Champion z napisem kwalifikacje wstępne i szkolenia okresowe', 'C, CE', 'Kwalifikacja wstępna', 'Pełna albo przyspieszona - dla przyszłych kierowców zawodowych.', 'od 3 500 zł'),
    ('szkolenie-okresowe', 'okres', 'Pomoce dydaktyczne do zajęć z mocowania ładunku', 'C, CE', 'Szkolenie okresowe', '35 godzin (5 dni), po szkoleniu wpis kodu 95 do prawa jazdy.', '1 000 zł'),
]


def kafle(R, link_pref):
    S = '(max-width:760px) 38vw, (max-width:1024px) 46vw, 380px'
    k = ''
    for idk, foto, alt, kat, tyt, opis, cena in KAFLE:
        kd = ' kat-d' if ',' in kat else ''
        k += f'''      <a class="kafel" href="{link_pref}#{idk}">
        <span class="kafel-foto">{img(foto, alt, S, R)}</span>
        <span class="kafel-txt">
          <span class="kat{kd}">{kat}</span>
          <strong>{tyt}</strong>
          <span class="kafel-op">{opis}</span>
          <em>{cena}</em>
        </span>
      </a>
'''
    return k


# ---------------------------------------------------------------- strona glowna
def glowna():
    R = ''
    S_HERO = '(max-width:760px) 100vw, 46vw'
    hero = INFO['hero']; hm = INFO['hero-m']
    tresc = f'''<section class="hero">
  <figure class="hero-foto">
    <picture>
      <source media="(max-width:760px)" srcset="{', '.join(f'img/{fn} {w}w' for fn, w, h in hm)}" sizes="100vw" width="{hm[-1][1]}" height="{hm[-1][2]}">
      <img src="img/{hero[1][0]}" srcset="{', '.join(f'img/{fn} {w}w' for fn, w, h in hero)}" sizes="46vw" width="{hero[-1][1]}" height="{hero[-1][2]}" alt="Toyota Yaris Nauki Jazdy Champion przed biurem przy ul. Gorzowskiej 6 w Witnicy" fetchpriority="high" decoding="async">
    </picture>
  </figure>
  <div class="hero-in">
    <p class="hero-adr">ul. Gorzowska 6, Witnica - biuro {lam("pn-pt 10:00-17:00")}</p>
    <h1>Prawo jazdy kat. B, B+E, C i C+E w Witnicy</h1>
    <p class="lead">OSK Champion szkoli od 2004 roku. Kurs B robisz na Toyocie Yaris, a manewry ćwiczysz na placu w Gorzowie Wielkopolskim, który jest tylko dla naszych kursantów.</p>
    <div class="hero-cta" id="heroCta">
      <a class="btn" href="#zapisy">Zapisz się na kurs</a>
      <a class="lnk" href="cennik/">Cennik kursów</a>
    </div>
    <nav class="hero-kat" aria-label="Kategorie">
      <a href="oferta/#kat-b"><span class="kat">B</span>Osobowe</a>
      <a href="oferta/#kat-be"><span class="kat">B+E</span>Przyczepa</a>
      <a href="oferta/#kat-c"><span class="kat">C</span>Ciężarowe</a>
      <a href="oferta/#kat-ce"><span class="kat">C+E</span>Naczepa</a>
      <a href="oferta/#szkolenie-okresowe"><span class="kat kat-d">95</span>Kod 95</a>
    </nav>
  </div>
</section>

<section class="sek" id="kursy">
  <div class="wrap">
    <h2>Kursy i szkolenia</h2>
    <p class="sek-lead">Samochód osobowy, przyczepa, ciężarówka i zestaw z naczepą oraz szkolenia dla kierowców zawodowych z kodem 95.</p>
    <div class="kafle">
{kafle(R, 'oferta/')}    </div>
  </div>
</section>

<section class="sek zapisy" id="zapisy">
  <div class="wrap zap-grid">
    <div class="zap-txt">
      <h2>Zapisy na kurs</h2>
      <p>Zapisać się można w biurze przy ul. Gorzowskiej 6 w Witnicy ({lam("pn-pt 10:00-17:00")}), telefonicznie pod numerem <a href="{TEL[1]}">{TEL[0]}</a> albo przez formularz. Biuro poda najbliższy termin rozpoczęcia kursu.</p>
      <ul class="kroki">
        <li><b>Profil kandydata na kierowcę (PKK).</b> Przed kursem potrzebny jest numer PKK - pomagamy przygotować dokumenty.</li>
        <li><b>Teoria.</b> Na kursie kat. B wybierasz teorię stacjonarną w sali wykładowej w Witnicy albo teorię online.</li>
        <li><b>Jazdy.</b> Kat. B na Toyocie Yaris. Manewry ćwiczysz na placu w Gorzowie, w cenie kursu jest też pół godziny jazdy na placu egzaminacyjnym WORD.</li>
      </ul>
      <p>Na kurs kat. B zapraszamy także {lam("17-latków")}. Podręczniki do nauki testów są w cenie kursu.</p>
      <p class="kdr"><img src="img/kdr.webp" width="240" height="151" alt="" loading="lazy"> Honorujemy Kartę Dużej Rodziny.</p>
    </div>
    {formularz(R, 'zapis', 'Zostaw numer - oddzwonimy', 'h3')}
  </div>
</section>

<section class="sek osrodek" id="osrodek">
  <div class="wrap os-grid">
    <figure class="os-foto">{img('siedziba', 'Siedziba Nauki Jazdy Champion przy ul. Gorzowskiej 6 w Witnicy', '(max-width:760px) 100vw, 440px', R)}</figure>
    <div class="os-txt">
      <h2>Biuro w Witnicy, plac w Gorzowie</h2>
      <p>OSK Champion działa od maja 2004 roku, a od listopada 2025 roku prowadzą go nowi właściciele. Biuro i sala wykładowa są przy ul. Gorzowskiej 6 w Witnicy.</p>
      <p>Manewry ćwiczysz na utwardzonym i oświetlonym placu przy ul. Kostrzyńskiej 12 w Gorzowie Wielkopolskim - jest wyłącznie do dyspozycji naszych kursantów. Szkolimy na pojazdach takich samych jak na egzaminie w WORD.</p>
      <div class="os-mini">
        <figure>{img('recepcja', 'Recepcja w biurze OSK Champion', '(max-width:760px) 31vw, 220px', R)}<figcaption>Biuro</figcaption></figure>
        <figure>{img('sala', 'Sala wykładowa w Witnicy', '(max-width:760px) 31vw, 220px', R)}<figcaption>Sala wykładowa</figcaption></figure>
        <figure>{img('plac-ciezarowki', 'Plac manewrowy przy ul. Kostrzyńskiej 12 w Gorzowie', '(max-width:760px) 31vw, 220px', R)}<figcaption>Plac manewrowy</figcaption></figure>
      </div>
      <a class="dalej" href="galeria/">Więcej o szkole i zdjęcia</a>
    </div>
  </div>
</section>

<section class="sek kontakt" id="kontakt">
  <div class="wrap kon-grid">
    {dane_kontaktowe()}
    {mapy(R)}
  </div>
</section>'''
    pre = (f'<link rel="preload" as="image" imagesrcset="{", ".join(f"img/{fn} {w}w" for fn, w, h in hm)}" imagesizes="100vw" media="(max-width:760px)" fetchpriority="high">\n'
           f'<link rel="preload" as="image" imagesrcset="{", ".join(f"img/{fn} {w}w" for fn, w, h in hero)}" imagesizes="46vw" media="(min-width:761px)" fetchpriority="high">\n')
    zapisz('', strona('', 'Nauka Jazdy Champion Witnica - prawo jazdy B, B+E, C, C+E',
                      'Nauka jazdy w Witnicy: prawo jazdy kat. B, B+E, C, C+E, kwalifikacja wstępna i kod 95. Plac manewrowy w Gorzowie Wlkp., biuro pn-pt 10-17. Tel. 729 993 243.',
                      tresc, glowna=True, schemy=[schema_firma()], preload=pre))


# ---------------------------------------------------------------- kursy (oferta)
def oferta():
    R = '../'
    S = '(max-width:760px) 100vw, 520px'
    bloki = [
        ('kat-b', 'Kategoria B - samochód osobowy', 'kat-b', 'Toyota Yaris Nauki Jazdy Champion na placu manewrowym', 'Kategoria B',
         ['Kurs na prawo jazdy kategorii B prowadzimy na Toyocie Yaris. Teorię możesz zrobić stacjonarnie w sali wykładowej w Witnicy albo online.',
          'Jeśli masz już zdany egzamin teoretyczny w WORD, robisz 4 godziny pierwszej pomocy i 30 godzin jazd. Na kurs zapraszamy także ' + lam('17-latków') + '.'],
         [('Pojazd', 'Toyota Yaris'), ('Teoria', '30 godzin - stacjonarnie albo online'), ('Jazdy', '30 godzin'), ('W cenie', 'pół godziny jazdy na placu egzaminacyjnym WORD, podręczniki do nauki testów'),
          ('Cena', '4 490 zł (bez teorii lub z teorią online), 5 100 zł (z teorią stacjonarną)'), ('Kurs ekspresowy', 'dopłata 1 000 zł'), ('Godzina dodatkowa', '150 zł dla kursantów OSK Champion, 160 zł dla kursantów z innych ośrodków')]),
        ('kat-be', 'Kategoria B+E - samochód z przyczepą', 'kat-be', 'Fiat Scudo z przyczepą do nauki jazdy kat. B+E', 'Kategoria B+E',
         ['Prawo jazdy B+E pozwala prowadzić samochód osobowy z cięższą przyczepą, np. z lawetą, przyczepą kempingową albo przyczepą dla koni. Kurs to same jazdy, bez części teoretycznej. Kiedy wystarczy kod 96, a kiedy potrzebne jest B+E, wyjaśniamy we wpisie <a href="../blog/prawo-jazdy-be-przyczepa-b96/">B+E czy kod 96</a>.'],
         [('Pojazd', 'Fiat Scudo z przyczepą'), ('Teoria', 'brak'), ('Jazdy', '15 godzin'), ('Cena', '2 900 zł'), ('Godzina dodatkowa', '200 zł')]),
        ('kat-c', 'Kategoria C - samochód ciężarowy', 'kat-c', 'Ciężarówka MAN TGL OSK Champion na placu manewrowym', 'Kategoria C',
         ['Kurs kategorii C prowadzimy na ciężarówce MAN TGL 12.240. Jeśli masz zdany egzamin teoretyczny w WORD, robisz tylko 30 godzin jazd.'],
         [('Pojazd', 'MAN TGL 12.240'), ('Teoria', '20 godzin'), ('Jazdy', '30 godzin'), ('Cena', '5 800 zł'), ('Godzina dodatkowa', '250 zł')]),
        ('kat-ce', 'Kategoria C+E - ciężarówka z naczepą', 'kat-ce', 'MAN TGX z naczepą do nauki jazdy kat. C+E', 'Kategoria C+E',
         ['Kurs kategorii C+E prowadzimy na ciągniku MAN TGX 18.500 z naczepą Wielton. To same jazdy, bez części teoretycznej.'],
         [('Pojazd', 'MAN TGX 18.500 z naczepą Wielton'), ('Teoria', 'brak'), ('Jazdy', '25 godzin'), ('Cena', '6 500 zł'), ('Godzina dodatkowa', '280 zł')]),
        ('kwalifikacja', 'Kwalifikacja wstępna C, CE', 'kwal', 'Ciężarówka OSK Champion z napisem kwalifikacje wstępne i szkolenia okresowe', 'Kwalifikacja wstępna',
         ['Kwalifikacja wstępna jest dla osób, które chcą zawodowo przewozić rzeczy samochodami ciężarowymi kategorii C i C+E. Prowadzimy kwalifikację pełną i przyspieszoną. Wiek, badania i kod 95 opisujemy we wpisie o <a href="../blog/prawo-jazdy-c-ce-kwalifikacja-wstepna/">prawie jazdy kat. C i C+E</a>.'],
         [('Kwalifikacja wstępna przyspieszona', '3 500 zł'), ('Kwalifikacja wstępna', '5 900 zł')]),
        ('szkolenie-okresowe', 'Szkolenie okresowe C, CE (kod 95)', 'okres', 'Pomoce dydaktyczne do zajęć z mocowania ładunku', 'Szkolenie okresowe',
         ['Szkolenie okresowe dla kierowców zawodowych kategorii C i C+E trwa 35 godzin, czyli 5 dni. Po ukończeniu szkolenia składasz w starostwie wniosek o wpis kodu 95 do prawa jazdy.'],
         [('Czas', '35 godzin (5 dni)'), ('Wymagania', 'numer PKZ'), ('Cena', '1 000 zł')]),
    ]
    b = ''
    for i, (idk, h, foto, alt, kurs, pars, lista) in enumerate(bloki):
        tx = ''.join(f'<p>{p}</p>' for p in pars)
        dl = ''.join(f'<div><dt>{a}</dt><dd>{c}</dd></div>' for a, c in lista)
        b += f'''  <article class="blok{' blok-odw' if i % 2 else ''}" id="{idk}">
    <figure class="blok-foto">{img(foto, alt, S, R)}</figure>
    <div class="blok-tx">
      <h2>{h}</h2>
      {tx}
      <dl class="dane">{dl}</dl>
      <a class="btn btn-maly" href="{R}kontakt/?kurs={quote(kurs)}#zapis">Zapisz się</a>
    </div>
  </article>
'''
    tresc = ph('Kursy prawa jazdy i szkolenia kierowców',
               'Szkolimy na prawo jazdy kategorii B, B+E, C i C+E oraz prowadzimy kwalifikację wstępną i szkolenia okresowe dla kierowców zawodowych. Teoria w Witnicy, manewry na placu w Gorzowie Wielkopolskim.',
               R) + f'''

<nav class="skoki" aria-label="Kursy na tej stronie">
  <div class="wrap skoki-in">
    <a href="#kat-b">B</a><a href="#kat-be">B+E</a><a href="#kat-c">C</a><a href="#kat-ce">C+E</a><a href="#kwalifikacja">Kwalifikacja wstępna</a><a href="#szkolenie-okresowe">Szkolenie okresowe</a>
  </div>
</nav>

<section class="sek sek-bloki">
  <div class="wrap">
{b}  </div>
</section>

<section class="sek sek-alt" id="przed-kursem">
  <div class="wrap dwie">
    <div>
      <h2>Przed kursem</h2>
      <p>Do rozpoczęcia kursu na prawo jazdy potrzebny jest profil kandydata na kierowcę (PKK). Zakłada go wydział komunikacji starostwa albo urzędu miasta na podstawie wniosku, zdjęcia i orzeczenia lekarskiego. Kandydaci na kategorie C i C+E przechodzą też badanie psychologiczne. Osoba niepełnoletnia potrzebuje zgody rodzica lub opiekuna.</p>
      <p>Pomagamy w przygotowaniu dokumentów do uzyskania PKK - zadzwoń do biura, podpowiemy, od czego zacząć. Krok po kroku opisujemy to w poradniku <a href="{R}blog/pierwsza-jazda-jak-przygotowac-sie-do-kursu/">jak przygotować się do kursu prawa jazdy</a>.</p>
    </div>
    <div>
      <h2>Dobrze wiedzieć</h2>
      <ul class="lista">
        <li>Na kurs kat. B zapraszamy także {lam('17-latków')}.</li>
        <li>Podręczniki do nauki testów są w cenie kursu kat. B.</li>
        <li>Dodatkowa godzina jazdy kat. B: 150 zł dla kursantów OSK Champion, 160 zł dla kursantów z innych ośrodków.</li>
        <li>Honorujemy Kartę Dużej Rodziny.</li>
        <li>Wpłaty za kurs można robić w biurze albo przelewem na konto <b class="konto">{KONTO}</b> (w tytule imię i nazwisko kursanta oraz kategoria).</li>
        <li>Plac manewrowy przy ul. Kostrzyńskiej 12 w Gorzowie Wielkopolskim jest utwardzony, oświetlony i dostępny tylko dla naszych kursantów.</li>
      </ul>
      <a class="dalej" href="{R}cennik/">Pełny cennik</a>
    </div>
  </div>
</section>

{cta(R)}'''
    zapisz('oferta', strona('oferta/', 'Kursy prawa jazdy B, B+E, C, C+E i kod 95 | Champion Witnica',
                            'Kurs prawa jazdy kat. B na Toyocie Yaris, B+E, C i C+E, kwalifikacja wstępna i szkolenie okresowe (kod 95). Teoria w Witnicy, plac w Gorzowie Wlkp.',
                            tresc, schemy=[okruszki('oferta/', 'Kursy')]))


def cta(R):
    return f'''<section class="cta">
  <div class="wrap cta-in">
    <div>
      <h2>Zapytaj o najbliższy termin kursu</h2>
      <p>Biuro w Witnicy jest czynne od poniedziałku do piątku w godz. {lam('10:00-17:00')}.</p>
    </div>
    <div class="cta-przyc">
      <a class="cta-tel" href="{TEL[1]}">{IKONA_TEL}{TEL[0]}</a>
      <a class="btn btn-zolty" href="{R}kontakt/#zapis">Formularz zapisu</a>
    </div>
  </div>
</section>'''


# ---------------------------------------------------------------- cennik
def cennik():
    R = '../'
    karty = ''
    for kat, poj, poz, uw in CENNIK:
        dl = ''.join(f'<div><dt>{n}</dt><dd>{c}</dd></div>' for n, c in poz)
        p = f'<p>{uw}</p>' if uw else ''
        karty += f'''    <div class="cen">
      <h2>{kat} <small>{poj}</small></h2>
      <dl>{dl}</dl>
      {p}
    </div>
'''
    tresc = ph('Cennik kursów prawa jazdy',
               'Ceny kursów prawa jazdy i szkoleń dla kierowców zawodowych w OSK Champion. O najbliższy termin i szczegóły zapytaj w biurze w Witnicy albo telefonicznie.',
               R) + f'''

<section class="sek sek-alt">
  <div class="wrap">
    <div class="cen-grid">
{karty}    </div>
    <div class="cen-dol">
      <p class="kdr kdr-jasny"><img src="{R}img/kdr.webp" width="240" height="151" alt="" loading="lazy"> Honorujemy Kartę Dużej Rodziny.</p>
      <p class="konto-p">Wpłaty za kurs: w biurze albo przelewem na konto <b class="konto">{KONTO}</b> (w tytule imię i nazwisko kursanta oraz kategoria).</p>
      <p>Opis kursów, pojazdów i liczby godzin znajdziesz na stronie <a href="{R}oferta/">Kursy</a>. Ile kosztuje całe prawo jazdy kat. B, razem z egzaminami i opłatą za dokument, policzyliśmy we wpisie <a href="{R}blog/prawo-jazdy-kategorii-b-witnica-cena-czas/">Prawo jazdy kat. B w Witnicy - ile kosztuje i ile trwa</a>.</p>
    </div>
  </div>
</section>

{cta(R)}'''
    zapisz('cennik', strona('cennik/', 'Cennik prawa jazdy Witnica - kat. B od 4 490 zł | Champion',
                            'Cennik OSK Champion w Witnicy: kat. B od 4 490 zł, B+E 2 900 zł, C 5 800 zł, C+E 6 500 zł, kwalifikacja wstępna od 3 500 zł, kod 95 1 000 zł.',
                            tresc, schemy=[okruszki('cennik/', 'Cennik')]))


# ---------------------------------------------------------------- o szkole (galeria)
def galeria():
    R = '../'
    S = '(max-width:520px) 100vw, (max-width:1024px) 50vw, 380px'
    grupy = [
        ('Plac manewrowy w Gorzowie Wielkopolskim', 'Utwardzony i oświetlony plac przy ul. Kostrzyńskiej 12 jest wyłącznie do dyspozycji naszych kursantów. Ćwiczymy na nim manewry na samochodzie osobowym, z przyczepą, ciężarówką i zestawem z naczepą.', [
            ('plac-ciezarowki', 'Ciężarówka OSK Champion na placu manewrowym'), ('plac-szeroki', 'Plac manewrowy przy ul. Kostrzyńskiej 12'), ('plac-yaris', 'Toyota Yaris i ciężarówka na placu')]),
        ('Pojazdy szkoleniowe', 'Szkolimy na pojazdach takich samych jak na egzaminie w WORD.', [
            ('kat-b', 'Toyota Yaris - kategoria B'), ('yaris-wnetrze', 'Kokpit Toyoty Yaris'), ('kat-be', 'Fiat Scudo z przyczepą - kategoria B+E'),
            ('kat-c', 'MAN TGL 12.240 - kategoria C'), ('kat-ce', 'MAN TGX 18.500 z naczepą - kategoria C+E'), ('kwal', 'Ciężarówka do szkoleń kierowców zawodowych')]),
        ('Biuro i sala wykładowa w Witnicy', 'Biuro i sala wykładowa mieszczą się przy ul. Gorzowskiej 6. W biurze zapiszesz się na kurs i ustalisz terminy jazd.', [
            ('recepcja', 'Biuro'), ('sala', 'Sala wykładowa')]),
    ]
    g = ''
    for h, opis, zd in grupy:
        figs = ''.join(f'''
      <figure><a href="{R}img/{najwiekszy(n)}" target="_blank" rel="noopener">{img(n, a, S, R)}</a><figcaption>{a}</figcaption></figure>''' for n, a in zd)
        g += f'''  <div class="gal-grupa">
    <h2>{h}</h2>
    <p>{opis}</p>
    <div class="gal">{figs}
    </div>
  </div>
'''
    tresc = ph('O szkole jazdy Champion',
               'OSK Champion powstał w maju 2004 roku, a od listopada 2025 roku prowadzą go nowi właściciele. Biuro i sala wykładowa są w Witnicy, plac manewrowy w Gorzowie Wielkopolskim.',
               R, 'siedziba', 'Siedziba Nauki Jazdy Champion przy ul. Gorzowskiej 6 w Witnicy') + f'''

<section class="sek">
  <div class="wrap dwie">
    <div>
      <h2>Kogo szkolimy</h2>
      <p>Szkolimy na prawo jazdy kategorii B, B+E, C i C+E. Prowadzimy też kwalifikację wstępną i szkolenia okresowe dla kierowców zawodowych kategorii C i C+E.</p>
      <p>Witnica leży między Gorzowem Wielkopolskim a Kostrzynem nad Odrą, niedaleko Dębna - zapraszamy kursantów z całej okolicy. Najbliższy WORD, w którym zdaje się egzamin państwowy, jest w Gorzowie Wielkopolskim.</p>
    </div>
    <div>
      <h2>Na co stawiamy</h2>
      <ul class="lista">
        <li>Skuteczne i rzetelne szkolenia.</li>
        <li>Nowoczesne środki dydaktyczne.</li>
        <li>Doświadczona kadra instruktorska.</li>
        <li>Pojazdy szkoleniowe takie same jak na egzaminie w WORD.</li>
        <li>Plac manewrowy tylko dla naszych kursantów.</li>
      </ul>
    </div>
  </div>
</section>

<section class="sek sek-alt">
  <div class="wrap">
{g}  </div>
</section>

<section class="sek" id="standardy">
  <div class="wrap dwie">
    <div>
      <h2>Standardy ochrony małoletnich</h2>
      <p>Szkolimy także osoby niepełnoletnie, dlatego w ośrodku obowiązują Standardy Ochrony Małoletnich. Dokument jest dostępny do pobrania.</p>
    </div>
    <div class="pdf">
      <a class="btn btn-obrys" href="{R}{PDF_STANDARDY}" target="_blank" rel="noopener">Pobierz dokument (PDF, 5,4 MB)</a>
    </div>
  </div>
</section>

{cta(R)}'''
    zapisz('galeria', strona('galeria/', 'O szkole - plac manewrowy i pojazdy | OSK Champion Witnica',
                             'OSK Champion w Witnicy od 2004 r.: zdjęcia placu manewrowego przy ul. Kostrzyńskiej 12 w Gorzowie Wlkp., pojazdów (Toyota Yaris, Fiat Scudo, MAN) i biura.',
                             tresc, schemy=[okruszki('galeria/', 'O szkole')]))


# ---------------------------------------------------------------- kontakt
def kontakt():
    R = '../'
    tresc = ph('Kontakt',
               f'Zadzwoń: <a href="{TEL[1]}">{TEL[0]}</a> albo odwiedź biuro przy ul. Gorzowskiej 6 w Witnicy, {GODZINY_H}.', R) + f'''

<section class="sek">
  <div class="wrap kon-grid">
    {dane_kontaktowe().replace('<h2>Kontakt</h2>', '<h2>Telefon, e-mail, adresy</h2>')}
    {mapy(R)}
  </div>
</section>

<section class="sek zapisy" id="zapis">
  <div class="wrap zap-grid">
    <div class="zap-txt">
      <h2>Zapisy i pytania</h2>
      <p>Wybierz kurs i zostaw numer telefonu - biuro oddzwoni, poda najbliższy termin i powie, jakie dokumenty przygotować.</p>
      <p>Wolisz od razu porozmawiać? Zadzwoń: <a href="{TEL[1]}">{TEL[0]}</a>.</p>
      <p class="firma">Nauka Jazdy Champion Aurelia Gajewska<br>ul. Gorzowska 6, 66-460 Witnica<br>NIP 596-121-01-26, REGON 543119611</p>
    </div>
    {formularz(R, 'zapis', 'Formularz zapisu', 'h3')}
  </div>
</section>'''
    zapisz('kontakt', strona('kontakt/', 'Kontakt - Nauka Jazdy Champion, ul. Gorzowska 6, Witnica',
                             'Biuro: ul. Gorzowska 6, 66-460 Witnica, pn-pt 10-17. Plac manewrowy: ul. Kostrzyńska 12, Gorzów Wlkp. Tel. 729 993 243, biuro.oskchampion@wp.pl.',
                             tresc, schemy=[schema_firma(), okruszki('kontakt/', 'Kontakt')]))


# ---------------------------------------------------------------- polityka
def polityka():
    R = '../'
    tresc = ph('Polityka prywatności', 'Zasady przetwarzania danych osobowych na stronie Nauki Jazdy Champion.', R) + f'''

<section class="sek">
  <div class="wrap prawny">
    <h2>Administrator danych</h2>
    <p>Administratorem danych osobowych jest Aurelia Gajewska, prowadząca działalność gospodarczą pod nazwą Nauka Jazdy Champion, ul. Gorzowska 6, 66-460 Witnica, NIP 596-121-01-26, REGON 543119611. Kontakt: <a href="mailto:{MAIL}">{MAIL}</a>, tel. <a href="{TEL[1]}">{TEL[0]}</a>.</p>

    <h2>Jakie dane i w jakim celu</h2>
    <p>Przetwarzamy dane, które nam przekazujesz: przez formularz na stronie (imię i nazwisko, numer telefonu, adres e-mail, wybrany kurs i treść pytania), telefonicznie lub e-mailem. Wykorzystujemy je do odpowiedzi na zgłoszenie, ustalenia terminu kursu i zawarcia umowy szkolenia.</p>
    <p>Podstawą prawną jest podjęcie działań na Twoje żądanie przed zawarciem umowy i jej wykonanie (art. 6 ust. 1 lit. b RODO) oraz nasz prawnie uzasadniony interes, czyli udzielenie odpowiedzi na pytanie (art. 6 ust. 1 lit. f RODO). Podanie danych jest dobrowolne, ale bez numeru telefonu nie będziemy mogli oddzwonić.</p>

    <h2>Komu przekazujemy dane</h2>
    <p>{FORM_RODO}</p>

    <h2>Jak długo przechowujemy dane</h2>
    <p>Dane ze zgłoszenia przechowujemy przez czas potrzebny do załatwienia sprawy, a jeśli dojdzie do szkolenia - przez okres wymagany przepisami oraz okres przedawnienia ewentualnych roszczeń.</p>

    <h2>Twoje prawa</h2>
    <p>Masz prawo dostępu do swoich danych, ich sprostowania, usunięcia lub ograniczenia przetwarzania, a także prawo sprzeciwu wobec przetwarzania. W tych sprawach napisz na <a href="mailto:{MAIL}">{MAIL}</a>. Masz też prawo wnieść skargę do Prezesa Urzędu Ochrony Danych Osobowych.</p>

    <h2>Pliki cookies i statystyki</h2>
    <p>Strona nie używa plików cookies ani narzędzi statystycznych i reklamowych. Mapy na stronie są obrazkami - dopiero po ich kliknięciu otwiera się serwis Mapy Google, a po kliknięciu odnośnika do Facebooka - serwis Facebook. Te serwisy działają według własnych zasad prywatności.</p>
  </div>
</section>'''
    zapisz('polityka-prywatnosci', strona('polityka-prywatnosci/', 'Polityka prywatności - Nauka Jazdy Champion Witnica',
                                           'Zasady przetwarzania danych osobowych na stronie Nauki Jazdy Champion w Witnicy: administrator, cel, prawa, pliki cookies.',
                                           tresc))


def nie_znaleziono():
    R = BASE_404
    tresc = f'''<section class="ph ph-bez">
  <div class="wrap ph-in">
    <div class="ph-tx">
      <h1>Nie znaleziono strony</h1>
      <p class="ph-lead">Ta strona nie istnieje albo zmieniła adres. Zobacz <a href="{R}">stronę główną</a>, <a href="{R}oferta/">kursy</a>, <a href="{R}cennik/">cennik</a> lub <a href="{R}kontakt/">kontakt</a>.</p>
    </div>
  </div>
</section>'''
    zapisz('', strona('404', 'Nie znaleziono strony - Nauka Jazdy Champion', 'Strona nie istnieje.', tresc, noindex=True, base=R), '404.html')


def przekierowanie(stary, nowy, nazwa):
    """Strona-zaslepka pod starym adresem WordPressa (dla hostingu bez .htaccess, np. GitHub Pages).
    Na Apache dziala wczesniej prawdziwe 301 z .htaccess."""
    s = f'''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex">
<title>{nazwa} - Nauka Jazdy Champion</title>
<link rel="canonical" href="{DOMENA}/{nowy}">
<meta http-equiv="refresh" content="0; url=../{nowy}">
</head>
<body>
<p>Strona zmieniła adres: <a href="../{nowy}">{nazwa}</a>.</p>
</body>
</html>
'''
    zapisz(stary, s)


# ---------------------------------------------------------------- blog i FAQ
def _wczytaj_blog():
    # tresc wpisow w osobnym pliku; import przez sciezke, bo build jest uruchamiany z -I
    import importlib.util
    spec = importlib.util.spec_from_file_location('blog_tresc', os.path.join(os.path.dirname(__file__), 'blog_tresc.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


BT = _wczytaj_blog()
WPISY = {w['slug']: w for w in BT.WPISY}
S_ART = '(max-width:760px) calc(100vw - 32px), 720px'


def tokeny(t, R):
    t = t.replace('{R}', R).replace('{TEL_H}', TEL[1]).replace('{TEL}', TEL[0])
    # twarde spacje: '3 500 kg', '2 900 zł' nie lamia sie na koncu wiersza (nie dotyczy numerow telefonow - te sa w <a>, nowrap)
    t = re.sub(r'(?<=\d) (?=\d{3}(?!\d))', '\u00a0', t)
    t = re.sub(r'(?<=\d) (?=(?:zł|kg|t|km/h|r\.|lat|dni|godzin|minut)(?![\w]))', '\u00a0', t)
    return lam(t)


def foto_art(t, R):
    def zam(m):
        nazwa, alt, podpis = m.group(1).split('|')
        return (f'<figure class="art-foto">{img(nazwa.strip(), alt.strip(), S_ART, R)}'
                f'<figcaption>{podpis.strip()}</figcaption></figure>')
    return re.sub(r'\[\[FOTO ([^\]]+)\]\]', zam, t)


def faq_html(pary, R):
    return ''.join(f'''
      <details class="faq">
        <summary>{q}</summary>
        <div class="faq-odp"><p>{tokeny(a, R)}</p></div>
      </details>''' for q, a in pary)


def faq_schema(pary):
    czysc = lambda t: html.unescape(re.sub(r'<[^>]+>', '', tokeny(t, ''))).strip()
    return {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': czysc(a)}} for q, a in pary]}


def okr_html(R, posrednie, nazwa):
    a = f'<a href="{R or "./"}">Strona główna</a>'
    for h, n in posrednie:
        a += f'<span aria-hidden="true">/</span><a href="{R}{h}">{n}</a>'
    return f'\n      <nav class="okr" aria-label="Okruszki">{a}<span aria-hidden="true">/</span><span aria-current="page">{nazwa}</span></nav>'


def wpis(w):
    R = '../../'
    sc = f'blog/{w["slug"]}/'
    data = f'\n      <p class="art-data"><time datetime="{BT.DATA}">{BT.DATA_TXT}</time></p>'
    tresc = ph(w['h1'], tokeny(w['lead'], R), R, w['foto'], w['foto_alt'],
               nad=okr_html(R, [('blog/', 'Blog')], w['okr']) + data)
    zob = ''.join(f'<li><a href="{R}blog/{s}/">{WPISY[s]["h1"]}</a></li>' for s in w['zobacz'])
    tresc += f'''

<section class="sek art-sek">
  <article class="wrap art">
{foto_art(tokeny(w['tresc'], R), R)}
    <div class="art-zapis">
      <p><strong>Chcesz zapisać się na kurs albo zapytać o termin?</strong> Zadzwoń: <a href="{TEL[1]}">{TEL[0]}</a> albo zostaw numer w formularzu, a biuro oddzwoni.</p>
      <a class="btn btn-maly" href="{R}kontakt/?kurs={quote(w['kurs'])}#zapis">Zapisz się</a>
    </div>

    <h2 id="pytania">Najczęstsze pytania</h2>
    <div class="faq-lista">{faq_html(w['faq'], R)}
    </div>

    <div class="art-dalej">
      <h2>Przeczytaj też</h2>
      <ul class="lista">{zob}<li><a href="{R}faq/">Pytania o kurs prawa jazdy - wszystko w jednym miejscu</a></li></ul>
      <a class="dalej" href="{R}blog/">Wszystkie wpisy</a>
    </div>
  </article>
</section>

{cta(R)}'''
    fn = INFO[w['foto']][-1][0]
    art = {'@context': 'https://schema.org', '@type': 'BlogPosting',
           'headline': w['h1'], 'description': w['opis'], 'inLanguage': 'pl-PL',
           'image': f'{DOMENA}/img/{fn}', 'datePublished': BT.DATA, 'dateModified': w.get('zmiana', BT.DATA),
           'mainEntityOfPage': {'@type': 'WebPage', '@id': f'{DOMENA}/{sc}'},
           'author': {'@type': 'Organization', 'name': 'Nauka Jazdy Champion', 'url': DOMENA + '/'},
           'publisher': {'@type': 'Organization', '@id': DOMENA + '/#osk', 'name': 'Nauka Jazdy Champion',
                         'logo': {'@type': 'ImageObject', 'url': DOMENA + '/img/logo-360.webp'}}}
    zapisz(sc, strona(sc, w['tytul'], w['opis'], tresc, og_typ='article', og_img=w['foto'],
                      schemy=[art, okruszki(sc, w['okr'], [('blog/', 'Blog')])]))  # 29.10: FAQPage tylko na /faq/


def blog_lista():
    R = '../'
    S = '(max-width:760px) calc(100vw - 32px), (max-width:1024px) 46vw, 380px'
    S1 = '(max-width:760px) calc(100vw - 32px), (max-width:1024px) calc(100vw - 48px), 790px'  # najnowszy wpis - szeroki kafel
    k = ''
    for i, w in enumerate(BT.WPISY):
        k += f'''      <article class="wpis">
        <a class="wpis-foto" href="{R}blog/{w['slug']}/" tabindex="-1" aria-hidden="true">{img(w['foto'], w['foto_alt'], S1 if i == 0 else S, R)}</a>
        <div class="wpis-tx">
          <time datetime="{BT.DATA}">{BT.DATA_TXT}</time>
          <h2><a href="{R}blog/{w['slug']}/">{w['h1']}</a></h2>
          <p>{w['kafel']}</p>
          <a class="dalej" href="{R}blog/{w['slug']}/" aria-hidden="true" tabindex="-1">Czytaj</a>
        </div>
      </article>
'''
    tresc = ph('Blog o prawie jazdy', 'Praktycznie o prawie jazdy: ile kosztuje kurs w Witnicy, jak wygląda egzamin w WORD w Gorzowie Wielkopolskim, kiedy potrzebne jest B+E, a kiedy kwalifikacja wstępna.', R,
               nad=okr_html(R, [], 'Blog')) + f'''

<section class="sek sek-alt">
  <div class="wrap">
    <div class="wpisy">
{k}    </div>
    <p class="wpisy-faq">Szukasz krótkiej odpowiedzi? Zajrzyj do <a href="{R}faq/">pytań i odpowiedzi</a>.</p>
  </div>
</section>

{cta(R)}'''
    lista = {'@context': 'https://schema.org', '@type': 'Blog', 'name': 'Blog Nauki Jazdy Champion', 'url': DOMENA + '/blog/',
             'inLanguage': 'pl-PL', 'publisher': {'@type': 'Organization', '@id': DOMENA + '/#osk', 'name': 'Nauka Jazdy Champion'},
             'blogPost': [{'@type': 'BlogPosting', 'headline': w['h1'], 'url': f"{DOMENA}/blog/{w['slug']}/", 'datePublished': BT.DATA} for w in BT.WPISY]}
    zapisz('blog', strona('blog/', 'Blog o prawie jazdy - Witnica i WORD Gorzów | OSK Champion',
                          'Poradniki OSK Champion: koszt prawa jazdy kat. B w Witnicy, egzamin w WORD Gorzów, B+E i kod 96, kat. C i C+E z kwalifikacją wstępną, numer PKK.',
                          tresc, schemy=[lista, okruszki('blog/', 'Blog')]))


def faq_strona():
    R = '../'
    grupy = ''
    wszystkie = []
    for h, pary in BT.FAQ:
        wszystkie += pary
        grupy += f'''    <div class="faq-grupa">
      <h2>{h}</h2>
      <div class="faq-lista">{faq_html(pary, R)}
      </div>
    </div>
'''
    tresc = ph('Pytania o kurs prawa jazdy', 'Krótkie odpowiedzi na pytania, które najczęściej słyszymy w biurze w Witnicy: zapisy, ceny, egzaminy w WORD Gorzów i kursy na przyczepę oraz ciężarówkę.', R,
               nad=okr_html(R, [], 'Pytania i odpowiedzi')) + f'''

<section class="sek">
  <div class="wrap art">
{grupy}    <p class="faq-dol">Nie ma tu twojego pytania? Zadzwoń: <a href="{TEL[1]}">{TEL[0]}</a> albo napisz przez <a href="{R}kontakt/#zapis">formularz</a>. Dłuższe poradniki znajdziesz na <a href="{R}blog/">blogu</a>.</p>
  </div>
</section>

{cta(R)}'''
    zapisz('faq', strona('faq/', 'FAQ - pytania o kurs prawa jazdy w Witnicy | OSK Champion',
                         'Najczęstsze pytania o kursy prawa jazdy w OSK Champion w Witnicy: zapisy i PKK, ceny i płatności, egzaminy w WORD Gorzów, kursy B+E, C i C+E, kod 95.',
                         tresc, schemy=[faq_schema(wszystkie), okruszki('faq/', 'Pytania i odpowiedzi')]))


def sitemap_robots():
    urls = ['', 'oferta/', 'cennik/', 'galeria/', 'kontakt/', 'blog/'] + [f'blog/{w["slug"]}/' for w in BT.WPISY] + ['faq/', 'polityka-prywatnosci/']
    pri = {'': '1.0', 'polityka-prywatnosci/': '0.3', 'blog/': '0.7', 'faq/': '0.7'}
    pri.update({f'blog/{w["slug"]}/': '0.6' for w in BT.WPISY})
    x = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    mod = {f'blog/{w["slug"]}/': w.get('zmiana', BT.DATA) for w in BT.WPISY}
    for u in urls:
        x += f'  <url><loc>{DOMENA}/{u}</loc><lastmod>{mod.get(u, AKTUALIZACJA)}</lastmod><priority>{pri.get(u, "0.8")}</priority></url>\n'
    x += '</urlset>\n'
    open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8', newline='\n').write(x)
    open(os.path.join(ROOT, 'robots.txt'), 'w', encoding='utf-8', newline='\n').write(
        f'User-agent: *\nAllow: /\n\nSitemap: {DOMENA}/sitemap.xml\n')


def llms_txt():
    """29.10: llms.txt - zwiezly opis szkoly dla asystentow AI, generowany z tych samych stalych co strona."""
    t = ['# Nauka Jazdy Champion (OSK Champion), Witnica', '',
         '> Ośrodek szkolenia kierowców w Witnicy (woj. lubuskie), działa od maja 2004 r. Kursy prawa jazdy kat. B, B+E, C i C+E, '
         'kwalifikacja wstępna oraz szkolenia okresowe kierowców zawodowych (kod 95). Teoria w Witnicy, manewry na własnym placu w Gorzowie Wielkopolskim.', '',
         '## Kontakt', '',
         f'- Telefon: {TEL[0]}',
         f'- Telefony do biura: {TEL_BIURO[0]} (stacjonarny), {TEL_BIURO_KOM[0]} (komórkowy)',
         f'- E-mail: {MAIL}',
         f'- Biuro i sala wykładowa: ul. Gorzowska 6, 66-460 Witnica, {GODZINY}',
         '- Plac manewrowy: ul. Kostrzyńska 12, 66-400 Gorzów Wielkopolski (tylko dla kursantów szkoły)',
         f'- Facebook: {FB}', '',
         '## Pojazdy', '',
         '- Kat. B: Toyota Yaris', '- Kat. B+E: Fiat Scudo z przyczepą', '- Kat. C: MAN TGL 12.240', '- Kat. C+E: MAN TGX 18.500 z naczepą Wielton', '',
         '## Cennik', '']
    for kat, poj, poz, uw in CENNIK:
        t.append(f'- {kat} ({poj}): ' + '; '.join(f'{n} - {c}' for n, c in poz) + (f'. {uw}' if uw else ''))
    t += ['- Honorujemy Kartę Dużej Rodziny. Wpłaty w biurze albo przelewem.', '',
          '## Strony', '',
          f'- [Kursy]({DOMENA}/oferta/): kursy B, B+E, C, C+E, kwalifikacja wstępna i szkolenie okresowe',
          f'- [Cennik]({DOMENA}/cennik/)',
          f'- [O szkole]({DOMENA}/galeria/): plac manewrowy, pojazdy, biuro',
          f'- [Pytania (FAQ)]({DOMENA}/faq/)',
          f'- [Kontakt]({DOMENA}/kontakt/)', '',
          '## Blog', '']
    t += [f'- [{w["h1"]}]({DOMENA}/blog/{w["slug"]}/): {w["kafel"]}' for w in BT.WPISY]
    open(os.path.join(ROOT, 'llms.txt'), 'w', encoding='utf-8', newline='\n').write('\n'.join(t) + '\n')


if __name__ == '__main__':
    glowna(); oferta(); cennik(); galeria(); kontakt(); polityka(); nie_znaleziono()
    blog_lista(); faq_strona()
    for w in BT.WPISY:
        wpis(w)
    przekierowanie('kontakt-2', 'kontakt/', 'Kontakt')
    przekierowanie('polityka-cookies', 'polityka-prywatnosci/', 'Polityka prywatności')
    sitemap_robots(); llms_txt()
    print('Zbudowano:', 'PRODUKCJA' if PROD else 'TEST (noindex, formularz testowy)')
