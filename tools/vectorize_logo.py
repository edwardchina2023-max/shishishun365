#!/usr/bin/env python3
from __future__ import annotations
"""Build the production SVG lockup from the approved raster master artwork."""

from pathlib import Path
from xml.sax.saxutils import escape

import cv2
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / "assets" / "images" / "brand"
MASTER = BRAND / "brand-lockup.png"
WORDMARK = BRAND / "wordmark.png"
MARKS = BRAND / "wordmark-photo.png"
OUTPUT = BRAND / "shishishun-logo-4a.svg"


def read_rgba(path: Path) -> np.ndarray:
    image = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)
    if image is None:
        raise FileNotFoundError(path)
    if image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    return cv2.cvtColor(image, cv2.COLOR_BGRA2RGBA)


def path_data(mask: np.ndarray, offset: tuple[int, int] = (0, 0), min_area: float = 0.4) -> str:
    contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    parts: list[str] = []
    ox, oy = offset
    for contour in contours:
        if abs(cv2.contourArea(contour)) < min_area:
            continue
        contour = cv2.approxPolyDP(contour, 0.55, True)
        points = contour.reshape(-1, 2)
        if len(points) < 3:
            continue
        first = points[0]
        commands = [f"M{first[0] - ox:g} {first[1] - oy:g}"]
        commands.extend(f"L{x - ox:g} {y - oy:g}" for x, y in points[1:])
        commands.append("Z")
        parts.append("".join(commands))
    return "".join(parts)


def vectorize_emblem(master: np.ndarray) -> str:
    emblem = master[:, :180]
    alpha = emblem[:, :, 3]
    visible = alpha > 36
    rgb = emblem[:, :, :3]
    lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2LAB)
    samples = lab[visible].astype(np.float32)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 60, 0.15)
    cv2.setRNGSeed(365)
    _, labels, centers = cv2.kmeans(samples, 18, None, criteria, 5, cv2.KMEANS_PP_CENTERS)
    indexed = np.full(alpha.shape, -1, dtype=np.int16)
    indexed[visible] = labels.reshape(-1)
    centers_rgb = cv2.cvtColor(np.uint8(centers)[None, :, :], cv2.COLOR_LAB2RGB)[0]
    counts = np.bincount(labels.reshape(-1), minlength=len(centers))

    layers: list[str] = []
    for cluster in np.argsort(counts)[::-1]:
        mask = np.where(indexed == cluster, 255, 0).astype(np.uint8)
        data = path_data(mask, min_area=0.25)
        if not data:
            continue
        red, green, blue = map(int, centers_rgb[cluster])
        color = f"#{red:02x}{green:02x}{blue:02x}"
        layers.append(f'<path d="{data}" fill="{color}" fill-rule="evenodd"/>')
    return "".join(layers)


def vectorize_gold(image: np.ndarray, crop: tuple[int, int, int, int] | None = None) -> str:
    if crop:
        x, y, width, height = crop
        sample = image[y : y + height, x : x + width]
        offset = (0, 0)
    else:
        sample = image
        offset = (0, 0)
    alpha = sample[:, :, 3]
    rgb = sample[:, :, :3]
    if crop:
        mask = ((rgb[:, :, 0] > 120) & (rgb[:, :, 1] > 75) & (rgb[:, :, 2] < 135) & (alpha > 16))
    else:
        mask = alpha > 42
    return path_data(np.where(mask, 255, 0).astype(np.uint8), offset=offset, min_area=0.3)


def build_svg() -> str:
    master = read_rgba(MASTER)
    wordmark = read_rgba(WORDMARK)
    marks = read_rgba(MARKS)

    emblem_paths = vectorize_emblem(master)
    wordmark_path = vectorize_gold(wordmark)
    registered_path = vectorize_gold(marks, (351, 4, 31, 31))
    seal_path = vectorize_gold(marks, (354, 60, 41, 41))

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 132" role="img" aria-labelledby="logoTitle logoDesc">
  <title id="logoTitle">事事顺酒品牌标志</title>
  <desc id="logoDesc">古井贡酒图形与事事顺金色字标的横向组合标志</desc>
  <metadata>{escape("Optically balanced production lockup · source artwork preserved · 2026")}</metadata>
  <defs>
    <linearGradient id="wordmarkGold" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#f1cf79"/>
      <stop offset="0.48" stop-color="#dca851"/>
      <stop offset="1" stop-color="#b8792d"/>
    </linearGradient>
    <linearGradient id="markGold" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#f0cf7a"/>
      <stop offset="1" stop-color="#c28a39"/>
    </linearGradient>
  </defs>
  <g id="gujing-emblem" transform="translate(0 7) scale(.855)">{emblem_paths}</g>
  <g id="shishishun-wordmark" transform="translate(176 24) scale(.609)">
    <path d="{wordmark_path}" fill="url(#wordmarkGold)" fill-rule="evenodd" stroke="#875018" stroke-width=".55" paint-order="stroke fill"/>
  </g>
  <g id="registered-mark" transform="translate(486 10) scale(.68)">
    <path d="{registered_path}" fill="url(#markGold)" fill-rule="evenodd"/>
  </g>
  <g id="wine-seal" transform="translate(486 64) scale(.7)">
    <path d="{seal_path}" fill="url(#markGold)" fill-rule="evenodd"/>
  </g>
</svg>
'''


if __name__ == "__main__":
    OUTPUT.write_text(build_svg(), encoding="utf-8")
    print(OUTPUT)
