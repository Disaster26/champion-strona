# -*- coding: utf-8 -*-
"""Tablica rejestracyjna z napisem CHAMPION nakladana w perspektywie (29.10: user - zamiast zamazanej tablicy)."""
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

F_TXT = r'C:\Windows\Fonts\ARIALNB.TTF'
F_PL = r'C:\Windows\Fonts\arialbd.ttf'


def tablica(napis='CHAMPION', w=1040, h=228):
    t = Image.new('RGB', (w, h), (226, 222, 214))
    d = ImageDraw.Draw(t)
    d.rectangle((0, 0, w - 1, h - 1), outline=(30, 30, 30), width=6)
    pas = int(h * 0.42)
    d.rectangle((6, 6, 6 + pas, h - 7), fill=(0, 51, 153))
    cx, cy, r = 6 + pas / 2, h * 0.33, pas * 0.27
    for i in range(12):
        a = 2 * math.pi * i / 12
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        d.ellipse((x - 5, y - 5, x + 5, y + 5), fill=(255, 204, 0))
    fp = ImageFont.truetype(F_PL, int(h * 0.27))
    d.text((cx, h * 0.76), 'PL', font=fp, fill='white', anchor='mm')
    x0 = 6 + pas + 18
    size = int(h * 0.82)
    ft = ImageFont.truetype(F_TXT, size)
    while d.textlength(napis, font=ft) > w - x0 - 30:
        size -= 2
        ft = ImageFont.truetype(F_TXT, size)
    d.text(((x0 + w - 14) / 2, h / 2 + 4), napis, font=ft, fill=(20, 20, 20), anchor='mm')
    return t


def wspolczynniki(dst, src):
    """Wspolczynniki Image.PERSPECTIVE: dla punktu wyjscia (dst) -> punkt zrodla (src)."""
    import numpy as np
    A, B = [], []
    for (x, y), (u, v) in zip(dst, src):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); B.append(u)
        A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); B.append(v)
    return list(np.linalg.solve(np.array(A, float), np.array(B, float)))


def naklej(im, quad, napis='CHAMPION'):
    """quad = [TL, TR, BR, BL] w pikselach zdjecia."""
    t = tablica(napis)
    xs = [p[0] for p in quad]; ys = [p[1] for p in quad]
    x0, y0, x1, y1 = int(min(xs)) - 2, int(min(ys)) - 2, int(max(xs)) + 3, int(max(ys)) + 3
    lok = [(x - x0, y - y0) for x, y in quad]
    src = [(0, 0), (t.width, 0), (t.width, t.height), (0, t.height)]
    k = wspolczynniki(lok, src)
    W, H = x1 - x0, y1 - y0
    warp = t.transform((W, H), Image.PERSPECTIVE, k, Image.BICUBIC)
    maska = Image.new('L', (W, H), 0)
    ImageDraw.Draw(maska).polygon(lok, fill=255)
    maska = maska.filter(ImageFilter.GaussianBlur(0.6))
    # dopasowanie do zdjecia: lekkie rozmycie i jasnosc jak oryginalna tablica
    warp = warp.filter(ImageFilter.GaussianBlur(0.5))
    im.paste(warp, (x0, y0), maska)
    return im
