#!/usr/bin/env python3
"""
trace_figures.py
Traces all figure PNGs to SVG paths using scikit-image marching squares.
Saves figure_paths.json with path data + bounding boxes for plate embedding.
"""
import os, json, re
import numpy as np
from PIL import Image
from skimage import measure
from skimage.measure import approximate_polygon

OUTDIR = r'C:\Users\kanta\Documents\remember-forward\reference_images\figures'

SELECTED = {
    'standing':   'standing.png',
    'lying_sick': 'lying_sick.png',
    'kneeling':   'kneeling.png',
    'pouring':    'pouring_v2.png',
    'seated':     'seated_v2.png',
}

def trace_png(png_path, simplify=1.8, min_area=50):
    img = Image.open(png_path).convert('L')
    arr = np.array(img)
    h, w = arr.shape
    binary = arr < 128
    padded = np.pad(binary, 1, mode='constant', constant_values=False)
    contours = measure.find_contours(padded.astype(float), 0.5)

    paths = []
    for contour in contours:
        pts = contour - 1  # remove padding offset
        if len(pts) < 20:
            continue
        simplified = approximate_polygon(pts, tolerance=simplify)
        if len(simplified) < 3:
            continue
        # Compute area (shoelace) to filter noise
        x, y = simplified[:,1], simplified[:,0]
        area = 0.5 * abs(np.dot(x, np.roll(y,-1)) - np.dot(y, np.roll(x,-1)))
        if area < min_area:
            continue
        d = f'M {simplified[0][1]:.1f} {simplified[0][0]:.1f}'
        for pt in simplified[1:]:
            d += f' L {pt[1]:.1f} {pt[0]:.1f}'
        d += ' Z'
        paths.append(d)

    # Compute overall bounding box from all path coordinates
    all_x, all_y = [], []
    for d in paths:
        nums = re.findall(r'[-\d.]+', d)
        coords = [(float(nums[i]), float(nums[i+1])) for i in range(0, len(nums)-1, 2)]
        all_x += [c[0] for c in coords]
        all_y += [c[1] for c in coords]

    bbox = {
        'x': min(all_x), 'y': min(all_y),
        'w': max(all_x)-min(all_x), 'h': max(all_y)-min(all_y),
        'img_w': w, 'img_h': h,
    } if all_x else {'x':0,'y':0,'w':w,'h':h,'img_w':w,'img_h':h}

    return paths, bbox

results = {}
for name, fname in SELECTED.items():
    png_path = os.path.join(OUTDIR, fname)
    print(f'Tracing {name}...')
    paths, bbox = trace_png(png_path)
    print(f'  {len(paths)} contours, bbox: {bbox["w"]:.0f}x{bbox["h"]:.0f} at ({bbox["x"]:.0f},{bbox["y"]:.0f})')
    results[name] = {'paths': paths, 'bbox': bbox}

    # Also write standalone SVG for inspection
    w, h = int(bbox['img_w']), int(bbox['img_h'])
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n'
    for d in paths:
        svg += f'  <path d="{d}" fill="black" fill-rule="evenodd"/>\n'
    svg += '</svg>'
    with open(os.path.join(OUTDIR, f'{name}_traced.svg'), 'w') as f:
        f.write(svg)

json_path = os.path.join(OUTDIR, 'figure_paths.json')
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)
print(f'\nSaved: {json_path}')
