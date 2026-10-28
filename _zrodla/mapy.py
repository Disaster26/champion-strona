# -*- coding: utf-8 -*-
"""Statyczne mapy (OpenStreetMap) z pinezka: biuro w Witnicy i plac manewrowy w Gorzowie.
Obrazek zamiast osadzonej mapy Google = brak ciasteczek i szybkie ladowanie.
Uruchomienie: python -I _zrodla/mapy.py
"""
import math, os, io, time, urllib.request
from PIL import Image, ImageDraw

TU = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(TU, '..', 'img')
CACHE = os.path.join(TU, '_kafle'); os.makedirs(CACHE, exist_ok=True)
UA = 'champion-prawojazdy.pl static map build (kontakt: lukasz@bibliotekanaukowa.pl)'

PUNKTY = {
    'mapa-biuro': (52.6732, 14.8977, 17),     # biuro: ul. Gorzowska 6, Witnica (pin od klientki)
    'mapa-plac': (52.72346, 15.19181, 17),    # plac manewrowy: ul. Kostrzynska 12, Gorzow Wlkp.
}
W, H = 1200, 800


def kafel(z, x, y):
    p = os.path.join(CACHE, f'{z}_{x}_{y}.png')
    if not os.path.exists(p):
        req = urllib.request.Request(f'https://tile.openstreetmap.org/{z}/{x}/{y}.png', headers={'User-Agent': UA})
        open(p, 'wb').write(urllib.request.urlopen(req, timeout=30).read()); time.sleep(0.3)
    return Image.open(p).convert('RGB')


def px(lat, lon, z):
    n = 2 ** z * 256
    x = (lon + 180) / 360 * n
    y = (1 - math.log(math.tan(math.radians(lat)) + 1 / math.cos(math.radians(lat))) / math.pi) / 2 * n
    return x, y


for nazwa, (lat, lon, z) in PUNKTY.items():
    cx, cy = px(lat, lon, z)
    cy -= 40  # pinezka nieco ponizej srodka
    x0, y0 = cx - W / 2, cy - H / 2
    im = Image.new('RGB', (W, H))
    for tx in range(int(x0 // 256), int((x0 + W) // 256) + 1):
        for ty in range(int(y0 // 256), int((y0 + H) // 256) + 1):
            im.paste(kafel(z, tx, ty), (int(tx * 256 - x0), int(ty * 256 - y0)))
    # pinezka w kolorze marki
    d = ImageDraw.Draw(im, 'RGBA')
    px_, py_ = cx - x0, cy - y0 + 40
    d.ellipse((px_ - 26, py_ - 9, px_ + 26, py_ + 9), fill=(0, 0, 0, 50))
    d.polygon([(px_ - 30, py_ - 62), (px_ + 30, py_ - 62), (px_, py_)], fill='#3f48cc')
    d.ellipse((px_ - 38, py_ - 118, px_ + 38, py_ - 42), fill='#3f48cc', outline='white', width=6)
    d.ellipse((px_ - 18, py_ - 98, px_ + 18, py_ - 62), outline='#fff200', width=9)
    for w in (600, 1200):
        im.resize((w, round(H * w / W)), Image.LANCZOS).save(os.path.join(OUT, f'{nazwa}-{w}.webp'), 'WEBP', quality=78, method=6)
    print(nazwa, 'ok')
