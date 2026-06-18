#!/usr/bin/env python3
import sys, re, json, vtracer

name = sys.argv[1]
png_path = sys.argv[2]
svg_path = sys.argv[3]

vtracer.convert_image_to_svg_py(
    png_path, svg_path,
    colormode='binary',
    hierarchical='stacked',
    filter_speckle=8,
    color_precision=6,
    layer_difference=16,
    corner_threshold=60,
    length_threshold=4.0,
    max_iterations=10,
    splice_threshold=45,
    path_precision=2,
)

with open(svg_path, encoding='utf-8') as f:
    svg_text = f.read()

vb = re.search(r'viewBox="([^"]+)"', svg_text)
viewbox = vb.group(1) if vb else '0 0 512 512'

paths = []
for m in re.finditer(r'<path\s[^>]*>', svg_text):
    tag = m.group(0)
    fill = re.search(r'fill="([^"]+)"', tag)
    d    = re.search(r' d="([^"]+)"', tag)
    if d and fill:
        fv = fill.group(1).lower().strip()
        if fv not in ('#ffffff','white','rgb(255,255,255)','#fff'):
            paths.append({'fill': fill.group(1), 'd': d.group(1)})

result = {'viewBox': viewbox, 'paths': paths}
print(json.dumps(result))
