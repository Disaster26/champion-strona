# -*- coding: utf-8 -*-
"""Generator stron Nauki Jazdy Champion (Witnica).

  python -I _zrodla/build.py              -> wersja testowa (noindex, formularz na adres testowy, 404 dla GitHub Pages)
  python -I _zrodla/build.py --produkcja  -> wersja na docelowy hosting (indeksowanie wlaczone, formularz na biuro.oskchampion@wp.pl)

Folder _zrodla nie jest publikowany (GitHub Pages pomija go przez _config.yml; na hosting go nie wgrywamy).
Wszystkie dane firmy sa w stalych ponizej - zmiana w jednym miejscu zmienia cala strone.
"""
import json, os, sys, html
from urllib.parse import quote

PROD = '--produkcja' in sys.argv
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
INFO = json.load(open(os.path.join(os.path.dirname(__file__), 'zdjecia.json'), encoding='utf-8'))

DOMENA = 'https://champion-prawojazdy.pl'
FORM_ADRES = 'https://formsubmit.co/ajax/' + ('biuro.oskchampion@wp.pl' if PROD else 'stasiu2626@gmail.com')
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
BIURO = (52.6732, 14.8977)
PLAC = (52.72346, 15.19181)
G_BIURO = 'https://www.google.com/maps/search/?api=1&query=52.6732%2C14.8977'
G_BIURO_TRASA = 'https://www.google.com/maps/dir/?api=1&destination=52.6732%2C14.8977'
G_PLAC = 'https://www.google.com/maps/search/?api=1&query=52.72346%2C15.19181'
G_PLAC_TRASA = 'https://www.google.com/maps/dir/?api=1&destination=52.72346%2C15.19181'
PDF_STANDARDY = 'dokumenty/standardy-ochrony-maloletnich.pdf'

NAV = [('oferta/', 'Kursy'), ('cennik/', 'Cennik'), ('galeria/', 'O szkole'), ('kontakt/', 'Kontakt')]

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
        'telephone': '+48729993243',
        'contactPoint': [{'@type': 'ContactPoint', 'contactType': 'biuro', 'telephone': '+48957180335'},
                         {'@type': 'ContactPoint', 'contactType': 'biuro', 'telephone': '+48737164747'}],
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


def okruszki(sciezka, nazwa):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Strona główna', 'item': DOMENA + '/'},
        {'@type': 'ListItem', 'position': 2, 'name': nazwa, 'item': DOMENA + '/' + sciezka}]}


# ---------------------------------------------------------------- szkielet strony
def strona(sciezka, tytul, opis, tresc, glowna=False, schemy=None, preload='', noindex=False, base=None):
    R = '' if sciezka == '' else '../'
    if base is not None:
        R = base
    robots = '<meta name="robots" content="noindex, nofollow">\n' if (not PROD or noindex) else ''
    nav = ''
    for href, nazwa in NAV:
        cur = ' aria-current="page"' if sciezka == href else ''
        nav += f'      <a href="{R}{href}"{cur}>{nazwa}</a>\n'
    sch = ''
    for s in (schemy or []):
        sch += '<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False, separators=(',', ':')) + '</script>\n'
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
<meta property="og:type" content="website">
<meta property="og:locale" content="pl_PL">
<meta property="og:site_name" content="Nauka Jazdy Champion Witnica">
<meta property="og:title" content="{e(tytul)}">
<meta property="og:description" content="{e(opis)}">
<meta property="og:url" content="{DOMENA}/{sciezka}">
<meta property="og:image" content="{DOMENA}/img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
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
{nav.replace('      <a', '    <a')}    <a class="panel-fb" href="{FB}" target="_blank" rel="noopener">{IKONA_FB}Facebook - Nauka Jazdy Champion Witnica</a>
    <p class="panel-info">ul. Gorzowska 6, Witnica<br>biuro {GODZINY}</p>
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
      <p><a href="{TEL[1]}">{TEL[0]}</a><br>Biuro: <a href="{TEL_BIURO[1]}">{TEL_BIURO[0]}</a>, <a href="{TEL_BIURO_KOM[1]}">{TEL_BIURO_KOM[0]}</a><br><a href="mailto:{MAIL}">{MAIL}</a><br>Biuro: {GODZINY}</p>
      <p><a class="st-fb" href="{FB}" target="_blank" rel="noopener">{IKONA_FB}Facebook</a></p>
    </div>
    <div>
      <p class="st-h">Plac manewrowy</p>
      <p>ul. Kostrzyńska 12<br>66-400 Gorzów Wielkopolski</p>
    </div>
    <ul class="st-nav">
      <li><a href="{dom}">Strona główna</a></li>
{''.join(f'      <li><a href="{R}{h}">{n}</a></li>{chr(10)}' for h, n in NAV)}    </ul>
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


def zapisz(sciezka, tekst, plik='index.html'):
    d = os.path.join(ROOT, sciezka)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, plik), 'w', encoding='utf-8', newline='\n') as f:
        f.write(tekst)


# ---------------------------------------------------------------- wspolne bloki
def ph(h1, lead, R, foto=None, foto_alt=''):
    if foto:
        f = f'\n    <figure class="ph-foto">{img(foto, foto_alt, "(max-width:760px) 100vw, 44vw", R, eager=True)}</figure>'
        cls = 'ph'
    else:
        f = ''; cls = 'ph ph-bez'
    return f'''<section class="{cls}">
  <div class="wrap ph-in">
    <div class="ph-tx">
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
      {mapa(R, 'mapa-biuro', 'Biuro i sala wykładowa', 'ul. Gorzowska 6, 66-460 Witnica', 'Mapa: biuro Nauki Jazdy Champion przy ul. Gorzowskiej 6 w Witnicy', G_BIURO, G_BIURO_TRASA, GODZINY)}
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
        <div><dt>Biuro</dt><dd>ul. Gorzowska 6, 66-460 Witnica<br>{GODZINY}</dd></div>
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
    <p class="hero-adr">ul. Gorzowska 6, Witnica - biuro pn-pt 10:00-17:00</p>
    <h1>Prawo jazdy kat. B, B+E, C i C+E w Witnicy</h1>
    <p class="lead">Ośrodek Szkolenia Kierowców Champion szkoli od 2004 roku. Kurs B robisz na Toyocie Yaris, a manewry ćwiczysz na placu w Gorzowie Wielkopolskim, który jest tylko dla naszych kursantów.</p>
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
      <p>Zapisać się można w biurze przy ul. Gorzowskiej 6 w Witnicy (pn-pt 10:00-17:00), telefonicznie pod numerem <a href="{TEL[1]}">{TEL[0]}</a> albo przez formularz. Biuro poda najbliższy termin rozpoczęcia kursu.</p>
      <ul class="kroki">
        <li><b>Profil kandydata na kierowcę (PKK).</b> Przed kursem potrzebny jest numer PKK - pomagamy przygotować dokumenty.</li>
        <li><b>Teoria.</b> Na kursie kat. B wybierasz teorię stacjonarną w sali wykładowej w Witnicy albo teorię online.</li>
        <li><b>Jazdy.</b> Kat. B na Toyocie Yaris. Manewry ćwiczysz na placu w Gorzowie, w cenie kursu jest też pół godziny jazdy na placu egzaminacyjnym WORD.</li>
      </ul>
      <p>Na kurs kat. B zapraszamy także 17-latków. Podręczniki do nauki testów są w cenie kursu.</p>
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
                      'Ośrodek Szkolenia Kierowców Champion w Witnicy: kursy prawa jazdy kat. B, B+E, C, C+E, kwalifikacja wstępna i szkolenia okresowe (kod 95). Plac manewrowy w Gorzowie Wlkp. Tel. 729 993 243.',
                      tresc, glowna=True, schemy=[schema_firma()], preload=pre))


# ---------------------------------------------------------------- kursy (oferta)
def oferta():
    R = '../'
    S = '(max-width:760px) 100vw, 520px'
    bloki = [
        ('kat-b', 'Kategoria B - samochód osobowy', 'kat-b', 'Toyota Yaris Nauki Jazdy Champion na placu manewrowym', 'Kategoria B',
         ['Kurs na prawo jazdy kategorii B prowadzimy na Toyocie Yaris. Teorię możesz zrobić stacjonarnie w sali wykładowej w Witnicy albo online.',
          'Jeśli masz już zdany egzamin teoretyczny w WORD, robisz 4 godziny pierwszej pomocy i 30 godzin jazd. Na kurs zapraszamy także 17-latków.'],
         [('Pojazd', 'Toyota Yaris'), ('Teoria', '30 godzin - stacjonarnie albo online'), ('Jazdy', '30 godzin'), ('W cenie', 'pół godziny jazdy na placu egzaminacyjnym WORD, podręczniki do nauki testów'),
          ('Cena', '4 490 zł (bez teorii lub z teorią online), 5 100 zł (z teorią stacjonarną)'), ('Kurs ekspresowy', 'dopłata 1 000 zł'), ('Godzina dodatkowa', '150 zł dla kursantów OSK Champion, 160 zł dla kursantów z innych ośrodków')]),
        ('kat-be', 'Kategoria B+E - samochód z przyczepą', 'kat-be', 'Fiat Scudo z przyczepą do nauki jazdy kat. B+E', 'Kategoria B+E',
         ['Prawo jazdy B+E pozwala prowadzić samochód osobowy z cięższą przyczepą, np. z lawetą, przyczepą kempingową albo przyczepą dla koni. Kurs to same jazdy, bez części teoretycznej.'],
         [('Pojazd', 'Fiat Scudo z przyczepą'), ('Teoria', 'brak'), ('Jazdy', '15 godzin'), ('Cena', '2 900 zł'), ('Godzina dodatkowa', '200 zł')]),
        ('kat-c', 'Kategoria C - samochód ciężarowy', 'kat-c', 'Ciężarówka MAN TGL OSK Champion na placu manewrowym', 'Kategoria C',
         ['Kurs kategorii C prowadzimy na ciężarówce MAN TGL 12.240. Jeśli masz zdany egzamin teoretyczny w WORD, robisz tylko 30 godzin jazd.'],
         [('Pojazd', 'MAN TGL 12.240'), ('Teoria', '20 godzin'), ('Jazdy', '30 godzin'), ('Cena', '5 800 zł'), ('Godzina dodatkowa', '250 zł')]),
        ('kat-ce', 'Kategoria C+E - ciężarówka z naczepą', 'kat-ce', 'MAN TGX z naczepą do nauki jazdy kat. C+E', 'Kategoria C+E',
         ['Kurs kategorii C+E prowadzimy na ciągniku MAN TGX 18.500 z naczepą Wielton. To same jazdy, bez części teoretycznej.'],
         [('Pojazd', 'MAN TGX 18.500 z naczepą Wielton'), ('Teoria', 'brak'), ('Jazdy', '25 godzin'), ('Cena', '6 500 zł'), ('Godzina dodatkowa', '280 zł')]),
        ('kwalifikacja', 'Kwalifikacja wstępna C, CE', 'kwal', 'Ciężarówka OSK Champion z napisem kwalifikacje wstępne i szkolenia okresowe', 'Kwalifikacja wstępna',
         ['Kwalifikacja wstępna jest dla osób, które chcą zawodowo przewozić rzeczy samochodami ciężarowymi kategorii C i C+E. Prowadzimy kwalifikację pełną i przyspieszoną.'],
         [('Kwalifikacja wstępna przyspieszona', '3 500 zł'), ('Kwalifikacja wstępna', '5 900 zł')]),
        ('szkolenie-okresowe', 'Szkolenie okresowe C, CE (kod 95)', 'okres', 'Pomoce dydaktyczne do zajęć z mocowania ładunku', 'Szkolenie okresowe',
         ['Szkolenie okresowe dla kierowców zawodowych kategorii C i C+E trwa 35 godzin, czyli 5 dni. Po ukończeniu szkolenia do prawa jazdy wpisywany jest kod 95.'],
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
      <p>Pomagamy w przygotowaniu dokumentów do uzyskania PKK - zadzwoń do biura, podpowiemy, od czego zacząć.</p>
    </div>
    <div>
      <h2>Dobrze wiedzieć</h2>
      <ul class="lista">
        <li>Na kurs kat. B zapraszamy także 17-latków.</li>
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
    zapisz('oferta', strona('oferta/', 'Kursy prawa jazdy B, B+E, C, C+E i kod 95 - Witnica | OSK Champion',
                            'Kurs prawa jazdy kat. B na Toyocie Yaris, B+E, C i C+E oraz kwalifikacja wstępna i szkolenie okresowe (kod 95). Teoria w Witnicy, plac manewrowy w Gorzowie Wlkp.',
                            tresc, schemy=[okruszki('oferta/', 'Kursy')]))


def cta(R):
    return f'''<section class="cta">
  <div class="wrap cta-in">
    <div>
      <h2>Zapytaj o najbliższy termin kursu</h2>
      <p>Biuro w Witnicy jest czynne od poniedziałku do piątku w godz. 10:00-17:00.</p>
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
    tresc = ph('Cennik kursów',
               'Ceny kursów prawa jazdy i szkoleń dla kierowców zawodowych w OSK Champion. O najbliższy termin i szczegóły zapytaj w biurze w Witnicy albo telefonicznie.',
               R) + f'''

<section class="sek sek-alt">
  <div class="wrap">
    <div class="cen-grid">
{karty}    </div>
    <div class="cen-dol">
      <p class="kdr kdr-jasny"><img src="{R}img/kdr.webp" width="240" height="151" alt="" loading="lazy"> Honorujemy Kartę Dużej Rodziny.</p>
      <p class="konto-p">Wpłaty za kurs: w biurze albo przelewem na konto <b class="konto">{KONTO}</b> (w tytule imię i nazwisko kursanta oraz kategoria).</p>
      <p>Opis kursów, pojazdów i liczby godzin znajdziesz na stronie <a href="{R}oferta/">Kursy</a>.</p>
    </div>
  </div>
</section>

{cta(R)}'''
    zapisz('cennik', strona('cennik/', 'Cennik kursów prawa jazdy Witnica - B od 4 490 zł | OSK Champion',
                            'Cennik OSK Champion Witnica: kat. B od 4 490 zł, B+E 2 900 zł, C 5 800 zł, C+E 6 500 zł, kwalifikacja wstępna od 3 500 zł, szkolenie okresowe 1 000 zł. Godziny dodatkowe.',
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
    tresc = ph('O szkole',
               'Ośrodek Szkolenia Kierowców Champion powstał w maju 2004 roku, a od listopada 2025 roku prowadzą go nowi właściciele. Biuro i sala wykładowa są w Witnicy, plac manewrowy w Gorzowie Wielkopolskim.',
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
    zapisz('galeria', strona('galeria/', 'O szkole i zdjęcia - plac manewrowy, pojazdy, biuro | OSK Champion Witnica',
                             'OSK Champion działa w Witnicy od 2004 roku. Zdjęcia placu manewrowego przy ul. Kostrzyńskiej 12 w Gorzowie Wlkp., pojazdów szkoleniowych (Toyota Yaris, Fiat Scudo, MAN), biura i sali wykładowej.',
                             tresc, schemy=[okruszki('galeria/', 'O szkole')]))


# ---------------------------------------------------------------- kontakt
def kontakt():
    R = '../'
    tresc = ph('Kontakt',
               f'Zadzwoń: <a href="{TEL[1]}">{TEL[0]}</a> albo odwiedź biuro przy ul. Gorzowskiej 6 w Witnicy, {GODZINY}.', R) + f'''

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
                             'Nauka Jazdy Champion: biuro ul. Gorzowska 6, 66-460 Witnica (pn-pt 10-17), plac manewrowy ul. Kostrzyńska 12, Gorzów Wlkp. Tel. 729 993 243, biuro.oskchampion@wp.pl.',
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
    <p>Przetwarzamy dane, które przekazujesz nam sam: przez formularz na stronie (imię i nazwisko, numer telefonu, adres e-mail, wybrany kurs i treść pytania), telefonicznie lub e-mailem. Wykorzystujemy je do odpowiedzi na zgłoszenie, ustalenia terminu kursu i zawarcia umowy szkolenia.</p>
    <p>Podstawą prawną jest podjęcie działań na Twoje żądanie przed zawarciem umowy i jej wykonanie (art. 6 ust. 1 lit. b RODO) oraz nasz prawnie uzasadniony interes, czyli udzielenie odpowiedzi na pytanie (art. 6 ust. 1 lit. f RODO). Podanie danych jest dobrowolne, ale bez numeru telefonu nie będziemy mogli oddzwonić.</p>

    <h2>Komu przekazujemy dane</h2>
    <p>Wiadomości z formularza są przekazywane na naszą skrzynkę e-mail za pośrednictwem usługi FormSubmit (formsubmit.co). Dane mogą też trafić do dostawcy hostingu strony i dostawcy poczty e-mail - wyłącznie w zakresie potrzebnym do działania tych usług. Korzystanie z usługi FormSubmit może wiązać się z przekazaniem danych poza Europejski Obszar Gospodarczy.</p>

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


def sitemap_robots():
    urls = ['', 'oferta/', 'cennik/', 'galeria/', 'kontakt/', 'polityka-prywatnosci/']
    pri = {'': '1.0', 'polityka-prywatnosci/': '0.3'}
    x = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        x += f'  <url><loc>{DOMENA}/{u}</loc><priority>{pri.get(u, "0.8")}</priority></url>\n'
    x += '</urlset>\n'
    open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8', newline='\n').write(x)
    open(os.path.join(ROOT, 'robots.txt'), 'w', encoding='utf-8', newline='\n').write(
        f'User-agent: *\nAllow: /\n\nSitemap: {DOMENA}/sitemap.xml\n')


if __name__ == '__main__':
    glowna(); oferta(); cennik(); galeria(); kontakt(); polityka(); nie_znaleziono()
    przekierowanie('kontakt-2', 'kontakt/', 'Kontakt')
    przekierowanie('polityka-cookies', 'polityka-prywatnosci/', 'Polityka prywatności')
    sitemap_robots()
    print('Zbudowano:', 'PRODUKCJA' if PROD else 'TEST (noindex, formularz testowy)')
