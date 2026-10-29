# -*- coding: utf-8 -*-
"""Przygotowanie zdjec strony OSK Champion.

- obrot wg EXIF, kadrowanie, kilka szerokosci WebP (srcset), zapis BEZ EXIF/ICC,
- zamazanie tablic rejestracyjnych, osob postronnych oraz nieaktualnych danych
  poprzedniego wlasciciela (stary telefon 501 449 632, napis "Andrzej Przylepa").

Uruchomienie: python -I _zrodla/zdjecia.py   (wynik: img/*.webp + _zrodla/zdjecia.json)
"""
import os, json
from PIL import Image, ImageOps, ImageFilter, ImageDraw

TU = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(TU, '..', 'img')
NOWE = r"C:\Users\Admin\Downloads\Odrobimy_kampania\klienci\Champion_Witnica\zdjecia_klienta_2810"
STARE = r"C:\Users\Admin\Downloads\Champion_koncept\_src\orig"
os.makedirs(OUT, exist_ok=True)
info = {}


def otworz(sciezka):
    return ImageOps.exif_transpose(Image.open(sciezka)).convert('RGB')


def zamaz(im, boxes, skala=1.0):
    """Pikselizacja + rozmycie prostokatow (wspolrzedne w ukladzie podgladu * skala)."""
    for b in boxes:
        x0, y0, x1, y1 = [int(round(v * skala)) for v in b]
        w, h = x1 - x0, y1 - y0
        if w <= 0 or h <= 0:
            continue
        reg = im.crop((x0, y0, x1, y1))
        k = max(4, min(w, h) // 3)
        reg = reg.resize((max(1, w // k), max(1, h // k)), Image.BILINEAR).resize((w, h), Image.BILINEAR)
        reg = reg.filter(ImageFilter.GaussianBlur(max(2, k // 2)))
        m = Image.new('L', (w, h), 0)
        ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h - 1), radius=min(w, h) // 4, fill=255)
        im.paste(reg, (x0, y0), m)
    return im


def kadr(im, box, skala=1.0):
    return im.crop(tuple(int(round(v * skala)) for v in box))


def proporcja(im, r, cx=.5, cy=.5):
    w, h = im.size
    if w / h > r:
        nw = round(h * r); x = round((w - nw) * cx); return im.crop((x, 0, x + nw, h))
    nh = round(w / r); y = round((h - nh) * cy); return im.crop((0, y, w, y + nh))


def zapisz(im, name, widths, q=72):
    im = im.convert('RGB'); out = []
    for w in widths:
        w = min(w, im.width)
        h = round(im.height * w / im.width)
        fn = f'{name}-{w}.webp'
        im.resize((w, h), Image.LANCZOS).save(os.path.join(OUT, fn), 'WEBP', quality=q, method=6)  # bez EXIF/ICC
        if not out or out[-1][1] != w:
            out.append((fn, w, h))
    info[name] = out
    print(name, [(o[0], os.path.getsize(os.path.join(OUT, o[0])) // 1024) for o in out])


# ---------------- nowe zdjecia od klientki (28.10.2026)
# 1. MAN TGX z naczepa (C+E), 3585x2688, podglad 1400 px
p1 = otworz(os.path.join(NOWE, '1793176157701.jpg')); s1 = p1.width / 1400
zamaz(p1, [(160, 776, 232, 844)], s1)
zapisz(proporcja(p1, 4 / 3), 'kat-ce', [480, 800, 1200])

# 2. Fiat Scudo z przyczepa (B+E), 1195x896
p2 = otworz(os.path.join(NOWE, '1793176657104.jpg'))
# 28.10: tablica CHAMP na Scudo to wizytowka szkoly (klient sam ja tak przygotowal) - NIE zamazujemy
# zamaz(p2, [(260, 675, 384, 736)])
zapisz(p2, 'kat-be', [480, 800, 1195])

# 3. plac - szeroki widok, 4000x3000
p3 = otworz(os.path.join(NOWE, '20261028_092402.jpg')); s3 = p3.width / 1400
zamaz(p3, [(1208, 460, 1246, 485), (1298, 460, 1334, 485), (1146, 440, 1190, 462), (1254, 416, 1292, 446), (778, 463, 806, 483)], s3)
zapisz(p3, 'plac-szeroki', [480, 800, 1200, 1600], q=68)

# 4. plac - MAN TGL OSK Champion (kat. C)
p4 = otworz(os.path.join(NOWE, '20261028_092431.jpg')); s4 = p4.width / 1400
zamaz(p4, [(470, 548, 505, 567), (626, 558, 665, 578), (553, 506, 592, 542), (666, 460, 710, 504), (1276, 530, 1312, 551)], s4)
zapisz(p4, 'plac-ciezarowki', [480, 800, 1200, 1600], q=68)
zapisz(kadr(p4, (540, 350, 960, 665), s4), 'kat-c', [480, 800, 1200])

# 5. plac - Yaris i tyl ciezarowki z napisem kwalifikacji
p5 = otworz(os.path.join(NOWE, '20261028_092518.jpg')); s5 = p5.width / 1400
zamaz(p5, [(348, 501, 387, 520), (528, 493, 562, 509), (412, 396, 449, 412), (1023, 572, 1080, 606)], s5)
zapisz(p5, 'plac-yaris', [480, 800, 1200, 1600], q=68)
zapisz(kadr(p5, (880, 330, 1400, 720), s5), 'kat-b', [480, 800, 1200])
zapisz(kadr(p5, (270, 340, 510, 520), s5), 'kwal', [480, 686])

# ---------------- zdjecia ze starej strony (wizualizacja)
def stare(prefix):
    f = [x for x in os.listdir(STARE) if x.startswith(prefix + '_')][0]
    return otworz(os.path.join(STARE, f))

# Yaris przed biurem: tablica, stary telefon na drzwiach auta i w oknie
h = stare('44'); sh = h.width / 1500
zamaz(h, [(1158, 1102, 1258, 1172), (898, 1008, 1002, 1052)], sh)
# 29.10 user: zamiast zamazanej tablicy przednia tablica z napisem CHAMPION (piksele oryginalu 1536x2048)
import sys; sys.path.insert(0, TU); import tablica
tablica.naklej(h, [(717, 1262), (816, 1280), (815, 1324), (716, 1302)])
zapisz(proporcja(h, 4 / 5, .5, .62), 'hero', [600, 900, 1100])
zapisz(proporcja(h, 3 / 2, .5, .52), 'hero-m', [480, 800, 1100])
og = proporcja(h, 1200 / 630, .5, .55).resize((1200, 630), Image.LANCZOS)
og.save(os.path.join(OUT, 'og.jpg'), 'JPEG', quality=80, optimize=True, progressive=True)  # podglad linku (Facebook), bez EXIF

# siedziba: stare telefony na witrynach
sd = stare('41'); ss = sd.width / 1932
zamaz(sd, [(1168, 1004, 1338, 1048), (1398, 1006, 1552, 1048)], ss)
zapisz(proporcja(sd, 4 / 5, .5, .4), 'siedziba', [480, 900])

zapisz(stare('25'), 'recepcja', [480, 800])
zapisz(kadr(stare('26'), (10, 0, 775, 510)), 'sala', [480, 765])
zapisz(proporcja(stare('35'), 4 / 3), 'okres', [480, 900])
zapisz(proporcja(stare('31'), 1), 'yaris-wnetrze', [480, 900])

# logo (przezroczyste tlo) i ikony
lg = Image.open(os.path.join(TU, 'logo-bez-napisu.png')).convert('RGBA')  # 29.10: logo bez mikroskopijnego 'Nauka jazdy' (napis jest teraz tekstem w HTML)
lg = lg.crop(lg.getbbox())
for w in (180, 360):
    lg.resize((w, round(lg.height * w / lg.width)), Image.LANCZOS).save(os.path.join(OUT, f'logo-{w}.webp'), 'WEBP', quality=90, method=6)
print('logo', lg.size, round(lg.height * 360 / lg.width))
ik = Image.new('RGBA', (512, 512), (0, 0, 0, 0)); d = ImageDraw.Draw(ik)
d.rounded_rectangle((0, 0, 511, 511), radius=96, fill='#3f48cc')
d.ellipse((104, 104, 408, 408), outline='#fff200', width=56)
ik.resize((180, 180), Image.LANCZOS).convert('RGB').save(os.path.join(TU, '..', 'apple-touch-icon.png'), optimize=True)
ik.save(os.path.join(TU, '..', 'favicon.ico'), sizes=[(16, 16), (32, 32), (48, 48)])

json.dump(info, open(os.path.join(TU, 'zdjecia.json'), 'w'), indent=1)
