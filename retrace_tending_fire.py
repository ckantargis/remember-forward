#!/usr/bin/env python3
"""
retrace_tending_fire.py
Re-traces tending_fire.png with higher simplify + min_area to eliminate the
small rock/stone paths around the fire base, leaving only the main figure body.

The yellow/orange fire in the PNG has grayscale values > 128 so it becomes
white after thresholding and is never traced — no fire paths to worry about.
The rocks are small closed shapes filtered out by min_area.
"""
import os, json, re
import numpy as np
from PIL import Image
from skimage import measure
from skimage.measure import approximate_polygon

FIGDIR  = r'C:\Users\kanta\Documents\remember-forward\reference_images\figures'
PNG     = os.path.join(FIGDIR, 'tending_fire.png')
SVG_OUT = os.path.join(FIGDIR, 'tending_fire_traced.svg')
JSON    = os.path.join(FIGDIR, 'figure_paths.json')

SIMPLIFY = 4.0    # higher = fewer path points (was 1.8)
MIN_AREA = 10000  # keeps only main body (~147k px²); eliminates rocks + pot (~3-9k px²)

img = Image.open(PNG).convert('L')
arr = np.array(img)
h, w = arr.shape
binary = arr < 128
padded = np.pad(binary, 1, mode='constant', constant_values=False)
contours = measure.find_contours(padded.astype(float), 0.5)

paths = []
for contour in contours:
    pts = contour - 1
    if len(pts) < 20:
        continue
    simplified = approximate_polygon(pts, tolerance=SIMPLIFY)
    if len(simplified) < 3:
        continue
    x, y = simplified[:,1], simplified[:,0]
    area = 0.5 * abs(np.dot(x, np.roll(y,-1)) - np.dot(y, np.roll(x,-1)))
    if area < MIN_AREA:
        continue
    d = f'M {simplified[0][1]:.1f} {simplified[0][0]:.1f}'
    for pt in simplified[1:]:
        d += f' L {pt[1]:.1f} {pt[0]:.1f}'
    d += ' Z'
    paths.append((area, d))

paths.sort(key=lambda t: t[0], reverse=True)
print(f'Kept {len(paths)} paths (min_area={MIN_AREA}):')
for area, d in paths:
    pts_count = d.count(' L ')
    print(f'  area={area:.0f}  points={pts_count+1}')

path_ds = [d for _, d in paths]

all_x, all_y = [], []
for d in path_ds:
    nums = re.findall(r'[-\d.]+', d)
    coords = [(float(nums[i]), float(nums[i+1])) for i in range(0, len(nums)-1, 2)]
    all_x += [c[0] for c in coords]
    all_y += [c[1] for c in coords]

bbox = {
    'x': min(all_x), 'y': min(all_y),
    'w': max(all_x)-min(all_x), 'h': max(all_y)-min(all_y),
    'img_w': w, 'img_h': h,
}
print(f'bbox: {bbox["w"]:.0f}x{bbox["h"]:.0f} at ({bbox["x"]:.0f},{bbox["y"]:.0f})')

# Write inspection SVG
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n'
for d in path_ds:
    svg += f'  <path d="{d}" fill="black" fill-rule="nonzero"/>\n'
svg += '</svg>'
with open(SVG_OUT, 'w') as f:
    f.write(svg)
print(f'Inspection SVG: {SVG_OUT}')

# Update figure_paths.json
with open(JSON, encoding='utf-8') as f:
    data = json.load(f)
data['tending_fire'] = {'paths': path_ds, 'bbox': bbox}
with open(JSON, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)
print(f'Updated: {JSON}')

import os as _os
_os.startfile(SVG_OUT)
