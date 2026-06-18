#!/usr/bin/env python3
"""
generate_figures.py
Generates ISOTYPE-style silhouette PNGs via Replicate FLUX-schnell,
traces each to SVG paths via VTracer, saves path data for plate scripts.
"""
import os, re, json, time, urllib.request
from dotenv import load_dotenv
load_dotenv()
os.environ.setdefault('REPLICATE_API_TOKEN', os.environ.get('REPLICATE_API_TOKEN',''))

import replicate, vtracer

OUTDIR = r'C:\Users\kanta\Documents\remember-forward\reference_images\figures'
os.makedirs(OUTDIR, exist_ok=True)

BASE_PROMPT = (
    'flat black silhouette on pure white background, ISOTYPE pictogram style, '
    'side profile view, no outlines, no gradients, no shading, no internal lines, '
    'no texture, solid black fill only, simple geometric shapes, '
    'high contrast, vector icon style, isolated figure on white, '
    'minimalist, bold black shape'
)

FIGURES = {
    'standing': (
        'adult human figure standing upright in side profile, '
        'arms at sides, weight balanced, full body visible from head to feet, '
    ),
    'lying_sick': (
        'adult human figure lying on their side horizontally, '
        'legs slightly bent toward chest, one arm bent upward, '
        'clearly horizontal body position, full body visible, '
    ),
    'kneeling': (
        'adult human figure kneeling in side profile, '
        'one knee on the ground, other foot forward flat on ground, '
        'torso leaning forward, one arm extended reaching downward, '
        'full body visible, '
    ),
    'pouring': (
        'adult human figure in side profile holding a jug or container tilted forward to pour, '
        'both arms raised and extended forward holding the vessel, '
        'standing upright, full body visible, '
    ),
    'seated': (
        'adult human figure seated cross-legged on the ground in side profile, '
        'torso upright, hands resting on knees, '
        'full body visible, '
    ),
}

results = {}

for name, pose_desc in FIGURES.items():
    print(f'\n--- Generating: {name} ---')
    prompt = pose_desc + BASE_PROMPT

    output = replicate.run(
        'black-forest-labs/flux-schnell',
        input={
            'prompt': prompt,
            'width': 576,
            'height': 576,
            'num_outputs': 1,
            'num_inference_steps': 4,
            'output_format': 'png',
            'go_fast': True,
            'megapixels': '0.25',
        }
    )

    # Handle FileOutput or URL string
    item = output[0] if isinstance(output, list) else output
    url = item.url if hasattr(item, 'url') else str(item)
    png_path = os.path.join(OUTDIR, f'{name}.png')
    urllib.request.urlretrieve(url, png_path)
    print(f'  PNG saved: {png_path}')

    # Trace PNG → SVG
    svg_path = os.path.join(OUTDIR, f'{name}.svg')
    vtracer.convert_image_to_svg_py(
        png_path, svg_path,
        colormode='binary',
        hierarchical='stacked',
        filter_speckle=6,
        color_precision=6,
        layer_difference=16,
        corner_threshold=60,
        length_threshold=4.0,
        max_iterations=10,
        splice_threshold=45,
        path_precision=2,
    )
    print(f'  SVG traced: {svg_path}')

    # Extract path data + viewBox
    with open(svg_path, encoding='utf-8') as f:
        svg_text = f.read()

    vb = re.search(r'viewBox="([^"]+)"', svg_text)
    viewbox = vb.group(1) if vb else '0 0 576 576'

    # Collect all black-fill paths (ignore white background path)
    path_data = []
    for m in re.finditer(r'<path\s[^>]*>', svg_text):
        tag = m.group(0)
        fill = re.search(r'fill="([^"]+)"', tag)
        d    = re.search(r'd="([^"]+)"', tag)
        if d and fill and fill.group(1).lower() not in ('#ffffff','white','rgb(255,255,255)'):
            path_data.append({'fill': fill.group(1), 'd': d.group(1)})

    print(f'  Paths extracted: {len(path_data)}')
    results[name] = {'viewBox': viewbox, 'paths': path_data}
    time.sleep(0.5)

# Save JSON
json_path = os.path.join(OUTDIR, 'figure_paths.json')
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)
print(f'\nDone. Paths saved to: {json_path}')

# Auto-open the output folder
import subprocess
subprocess.Popen(f'explorer "{OUTDIR}"')
