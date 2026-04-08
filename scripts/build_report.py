#!/usr/bin/env python3
"""Build an HTML evaluation report from template generation results.

Reads evaluation metadata and scores, generates a self-contained HTML report
with embedded images, template inventory, and quality statistics.

Usage:
    python build_report.py                      # Build from test/results/
    python build_report.py --output report.html  # Custom output path
"""

import argparse
import base64
import json
import os
from pathlib import Path
from datetime import datetime

PROJECT_DIR = Path(__file__).parent.parent
RESULTS_DIR = PROJECT_DIR / "test" / "results"
REPORT_DIR = PROJECT_DIR / "report"

TEMPLATE_INFO = {
    "A01": {"name": "Chibi Cartoon", "cat": "Stylization", "pri": "P0", "kw": "chibi, Q版, cartoon"},
    "A02": {"name": "3D Pixar Animation", "cat": "Stylization", "pri": "P0", "kw": "3D, Pixar, Disney"},
    "A03": {"name": "Comic / Manga", "cat": "Stylization", "pri": "P0", "kw": "comic, manga, 漫画"},
    "A04": {"name": "Sketch / Pencil", "cat": "Stylization", "pri": "P0", "kw": "sketch, 素描, pencil"},
    "A05": {"name": "Clay / Claymation", "cat": "Stylization", "pri": "P0", "kw": "clay, 黏土, stop-motion"},
    "A06": {"name": "80s Retro Animation", "cat": "Stylization", "pri": "P0", "kw": "80s, retro, synthwave"},
    "A07": {"name": "Retro-Futurism", "cat": "Stylization", "pri": "P0", "kw": "retro-future, space age"},
    "A08": {"name": "Ukiyo-e / Chinese Painting", "cat": "Stylization", "pri": "P0", "kw": "ukiyo-e, 国风, 古风"},
    "A09": {"name": "Watercolor Portrait", "cat": "Stylization", "pri": "P0", "kw": "watercolor, 水彩"},
    "A10": {"name": "K-Pop Star", "cat": "Stylization", "pri": "P0", "kw": "K-Pop, 韩风, idol"},
    "A11": {"name": "Imperial / Royal", "cat": "Stylization", "pri": "P0", "kw": "imperial, 帝王, royal"},
    "A12": {"name": "90s Yearbook", "cat": "Stylization", "pri": "P0", "kw": "90s, yearbook, 毕业照"},
    "A13": {"name": "High Fashion", "cat": "Stylization", "pri": "P0", "kw": "fashion, vogue, editorial"},
    "A14": {"name": "Cyberpunk Portrait", "cat": "Stylization", "pri": "P0", "kw": "cyberpunk, neon, 赛博朋克"},
    "B01": {"name": "Studio Photoshoot", "cat": "Portrait", "pri": "P0", "kw": "photoshoot, 写真, studio"},
    "B02": {"name": "ID Photo", "cat": "Portrait", "pri": "P0", "kw": "ID photo, 证件照, passport"},
    "B03": {"name": "Pet Humanization", "cat": "Portrait", "pri": "P0", "kw": "pet human, 宠物拟人"},
    "B04": {"name": "Emoji / Sticker Pack", "cat": "Portrait", "pri": "P0", "kw": "emoji, sticker, 表情包"},
    "B05": {"name": "Avatar / Profile Picture", "cat": "Portrait", "pri": "P0", "kw": "avatar, 头像, profile"},
    "C01": {"name": "Pet Stylization", "cat": "Pets & Babies", "pri": "P0", "kw": "pet, 萌宠, kawaii"},
    "C02": {"name": "Baby Comic Grid", "cat": "Pets & Babies", "pri": "P0", "kw": "baby, 宝宝, comic grid"},
    "C03": {"name": "Pet VOGUE Magazine", "cat": "Pets & Babies", "pri": "P0", "kw": "pet magazine, VOGUE"},
    "D01": {"name": "Outfit Change", "cat": "Editing", "pri": "P1", "kw": "outfit, 换装, try-on"},
    "D02": {"name": "Hairstyle Change", "cat": "Editing", "pri": "P1", "kw": "hairstyle, 发型, haircut"},
    "D03": {"name": "Background Change", "cat": "Editing", "pri": "P1", "kw": "background, 换背景"},
    "E01": {"name": "Social Media Post", "cat": "Creative", "pri": "P1", "kw": "social media, quote, 配图"},
    "E02": {"name": "Poster Design", "cat": "Creative", "pri": "P1", "kw": "poster, 海报, flyer"},
    "E03": {"name": "Storyboard", "cat": "Creative", "pri": "P1", "kw": "storyboard, 分镜, comic strip"},
    "E04": {"name": "Handwritten Poster", "cat": "Creative", "pri": "P1", "kw": "手抄报, bulletin"},
    "E05": {"name": "Illustration", "cat": "Creative", "pri": "P1", "kw": "illustration, 插画"},
    "F01": {"name": "E-commerce Main Image", "cat": "Design", "pri": "P1", "kw": "e-commerce, 电商, product"},
    "F02": {"name": "Sticker Set Design", "cat": "Design", "pri": "P1", "kw": "sticker set, 贴纸集"},
    "F03": {"name": "Interior Design", "cat": "Design", "pri": "P1", "kw": "interior, 家装, room"},
    "F04": {"name": "Logo Design", "cat": "Design", "pri": "P1", "kw": "logo, 标志, brand"},
    "F05": {"name": "Merchandise Design", "cat": "Design", "pri": "P1", "kw": "merchandise, 手办, figure"},
    "F06": {"name": "Coloring Book Page", "cat": "Design", "pri": "P1", "kw": "coloring, 涂色, line art"},
}


def image_to_base64(path: str) -> str | None:
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        data = f.read()
    ext = os.path.splitext(path)[1].lower()
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "webp": "image/webp"}
    mime_type = mime.get(ext.lstrip("."), "image/png")
    return f"data:{mime_type};base64,{base64.b64encode(data).decode()}"


def load_scores() -> dict:
    scores_path = RESULTS_DIR / "scores.json"
    if scores_path.exists():
        with open(scores_path) as f:
            return json.load(f)
    return {}


def load_meta() -> dict:
    meta_path = RESULTS_DIR / "evaluation-meta.json"
    if meta_path.exists():
        with open(meta_path) as f:
            return json.load(f)
    return {}


def build_html(output_path: str = None):
    if output_path is None:
        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        output_path = str(REPORT_DIR / "template-report.html")

    scores = load_scores()
    meta = load_meta()

    inventory_rows = []
    for tid, info in sorted(TEMPLATE_INFO.items()):
        score_data = scores.get(tid, {}).get("scores", {})
        overall = score_data.get("overall", "—")
        if isinstance(overall, (int, float)):
            overall = f"{overall:.1f}"

        has_image = False
        image_html = ""
        if tid in meta:
            for run in meta[tid]:
                if run.get("success") and run.get("output"):
                    b64 = image_to_base64(run["output"])
                    if b64:
                        image_html = f'<img src="{b64}" class="thumb" />'
                        has_image = True
                        break

        if not has_image:
            result_dir = RESULTS_DIR / tid
            if result_dir.exists():
                for img_file in sorted(result_dir.glob("*.png")):
                    b64 = image_to_base64(str(img_file))
                    if b64:
                        image_html = f'<img src="{b64}" class="thumb" />'
                        has_image = True
                        break

        status = "generated" if has_image else "pending"
        inventory_rows.append(f"""
        <tr class="{status}">
            <td>{tid}</td>
            <td>{info['name']}</td>
            <td>{info['cat']}</td>
            <td><span class="badge {info['pri'].lower()}">{info['pri']}</span></td>
            <td class="kw">{info['kw']}</td>
            <td class="score">{overall}</td>
            <td class="preview">{image_html if has_image else '<span class="no-img">—</span>'}</td>
        </tr>""")

    scored_templates = [
        (tid, s["scores"]["overall"]) for tid, s in scores.items()
        if "overall" in s.get("scores", {})
    ]
    avg_overall = sum(s for _, s in scored_templates) / len(scored_templates) if scored_templates else 0
    max_template = max(scored_templates, key=lambda x: x[1]) if scored_templates else ("—", 0)
    min_template = min(scored_templates, key=lambda x: x[1]) if scored_templates else ("—", 0)

    total_generated = sum(
        1 for tid in TEMPLATE_INFO
        if tid in meta and any(r.get("success") for r in meta.get(tid, []))
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Image Gen Templates — Evaluation Report</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: #0f0f0f; color: #e0e0e0; padding: 2rem; }}
h1 {{ font-size: 2rem; margin-bottom: 0.5rem; color: #fff; }}
h2 {{ font-size: 1.4rem; margin: 2rem 0 1rem; color: #ccc; border-bottom: 1px solid #333; padding-bottom: 0.5rem; }}
.subtitle {{ color: #888; margin-bottom: 2rem; }}
.stats {{ display: flex; gap: 2rem; margin: 1.5rem 0; flex-wrap: wrap; }}
.stat-card {{ background: #1a1a1a; border: 1px solid #333; border-radius: 12px;
  padding: 1.2rem 1.5rem; min-width: 180px; }}
.stat-card .label {{ font-size: 0.8rem; color: #888; text-transform: uppercase; letter-spacing: 0.05em; }}
.stat-card .value {{ font-size: 1.8rem; font-weight: 700; color: #4fc3f7; margin-top: 0.3rem; }}
.stat-card .detail {{ font-size: 0.85rem; color: #666; margin-top: 0.2rem; }}
table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; }}
th {{ text-align: left; padding: 0.8rem; background: #1a1a1a; color: #aaa;
  font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em;
  border-bottom: 2px solid #333; }}
td {{ padding: 0.7rem 0.8rem; border-bottom: 1px solid #222; vertical-align: middle; }}
tr:hover {{ background: #1a1a1a; }}
.kw {{ font-size: 0.8rem; color: #888; max-width: 200px; }}
.score {{ font-weight: 700; color: #4fc3f7; text-align: center; }}
.badge {{ padding: 0.2rem 0.6rem; border-radius: 4px; font-size: 0.75rem; font-weight: 600; }}
.badge.p0 {{ background: #1b5e20; color: #a5d6a7; }}
.badge.p1 {{ background: #e65100; color: #ffcc80; }}
.thumb {{ width: 80px; height: 80px; object-fit: cover; border-radius: 8px; border: 1px solid #333; }}
.no-img {{ color: #555; }}
.preview {{ text-align: center; }}
.generated td:first-child {{ border-left: 3px solid #4caf50; }}
.pending td:first-child {{ border-left: 3px solid #555; }}
.footer {{ margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #333; color: #555; font-size: 0.8rem; }}
</style>
</head>
<body>
<h1>Image Generation — High-Heat Template Report</h1>
<p class="subtitle">33 curated templates for Gemini 3.1 Flash Image (Nano Banana 2) — Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>

<div class="stats">
  <div class="stat-card">
    <div class="label">Total Templates</div>
    <div class="value">{len(TEMPLATE_INFO)}</div>
    <div class="detail">6 categories</div>
  </div>
  <div class="stat-card">
    <div class="label">Generated</div>
    <div class="value">{total_generated}/{len(TEMPLATE_INFO)}</div>
    <div class="detail">templates with images</div>
  </div>
  <div class="stat-card">
    <div class="label">Avg Overall Score</div>
    <div class="value">{avg_overall:.2f}</div>
    <div class="detail">{len(scored_templates)} scored</div>
  </div>
  <div class="stat-card">
    <div class="label">Best Template</div>
    <div class="value">{max_template[1]:.1f}</div>
    <div class="detail">{max_template[0]}</div>
  </div>
  <div class="stat-card">
    <div class="label">Needs Attention</div>
    <div class="value">{min_template[1]:.1f}</div>
    <div class="detail">{min_template[0]}</div>
  </div>
</div>

<h2>Template Inventory</h2>
<table>
<thead>
<tr><th>ID</th><th>Template</th><th>Category</th><th>Priority</th><th>Keywords</th><th>Score</th><th>Preview</th></tr>
</thead>
<tbody>
{''.join(inventory_rows)}
</tbody>
</table>

<div class="footer">
  <p>Report generated by image-gen-templates build_report.py</p>
  <p>Model: Gemini 3.1 Flash Image (Nano Banana 2) via Compass LLM Proxy</p>
</div>
</body>
</html>"""

    with open(output_path, "w") as f:
        f.write(html)
    print(f"Report saved to {output_path}")

    inventory_json = []
    for tid, info in sorted(TEMPLATE_INFO.items()):
        score_data = scores.get(tid, {}).get("scores", {})
        inventory_json.append({
            "id": tid,
            "name": info["name"],
            "category": info["cat"],
            "priority": info["pri"],
            "keywords": info["kw"],
            "scores": score_data,
            "has_sample": tid in meta and any(r.get("success") for r in meta.get(tid, [])),
        })

    json_path = REPORT_DIR / "template-inventory.json"
    with open(json_path, "w") as f:
        json.dump(inventory_json, f, indent=2, ensure_ascii=False)
    print(f"Inventory JSON saved to {json_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build evaluation report")
    parser.add_argument("--output", help="Output HTML file path")
    args = parser.parse_args()
    build_html(args.output)
