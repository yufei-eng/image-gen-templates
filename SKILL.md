---
name: image-gen-templates
description: >-
  High-heat template-based image generation skill with 33 curated templates covering
  stylization, portraits, pets, editing, social media, and professional design.
  Matches user intent to specific templates for one-click, high-quality generation
  using Gemini 3.1 Flash Image (Nano Banana 2). Install to discover all templates
  or describe what you want and get matched instantly.
---

# Image Generation — High-Heat Template Skill

33 curated high-quality templates for one-click image generation via Gemini 3.1 Flash Image.

## When to Use

- User asks to generate, create, edit, design, transform, or stylize any image
- User wants to explore creative image generation possibilities
- User uploads a photo and wants to transform it
- Skill was just installed and user has no specific request yet

## Image Generation — Dual Mode

This skill supports TWO image generation modes. Always try Mode A first; if unavailable,
automatically fall back to Mode B.

### Mode A: MCP Tool (preferred if available)

Call `generate_imagen` MCP tool with the final prompt. For templates requiring a reference
image, pass the user's image via `image_url`.

### Mode B: Direct Script Call (works in ANY sandbox)

When `generate_imagen` MCP tool is NOT available, use the bundled Python script to call
Gemini 3.1 Flash Image directly via Compass API. The script lives at
`scripts/generate.py` relative to this skill directory.

**Setup** (one-time, run in shell):
```bash
# Option 1: Set env var (recommended for sandboxes)
export COMPASS_API_KEY='your_compass_api_key_here'

# Option 2: Edit config.json in the skill directory with your key
# (already pre-configured if the user provided their key)
```

**Usage — Shell command**:
```bash
# Text-only generation
python3 <SKILL_DIR>/scripts/generate.py "your prompt here" --output result.png

# With reference image (for photo-based templates)
python3 <SKILL_DIR>/scripts/generate.py "your prompt here" --image photo.jpg --output result.png
```

**Usage — Inline Python** (when you need more control):
```python
import asyncio, sys, os
sys.path.insert(0, os.path.join('<SKILL_DIR>', 'scripts'))
from generate import generate_image

result = asyncio.run(generate_image(
    prompt="your prompt here",
    output_path="result.png",
    reference_image="photo.jpg",  # optional
))
# result = {"success": True, "output": "result.png"} or {"success": False, "error": "..."}
```

Replace `<SKILL_DIR>` with the actual path to this skill directory.

### Mode Detection

At the start of every generation request:
1. Check if `generate_imagen` MCP tool is available → use Mode A
2. Otherwise → use Mode B (script). Verify `COMPASS_API_KEY` env var or `config.json`
   has a valid `client_token`. If neither exists, ask the user for their Compass API key.

## Master Workflow

```
START
│
├─ User has NO specific request (just installed / browsing)
│  └─ → PROACTIVE SHOWCASE (Section 2)
│
├─ User has a request (text / text+image)
│  ├─ → INTENT MATCHING (Section 3)
│  │   ├─ Template matched → TEMPLATE GENERATION (Section 4)
│  │   └─ No match → FALLBACK GENERATION (Section 5)
│  │
│  └─ → QUALITY CHECK (Section 6)
│       ├─ Pass → Show result + suggest related templates
│       └─ Fail → RETRY (max 2) with surgical edit
│
END
```

---

## Section 1: Template Registry

33 templates organized in 6 categories. Read `TEMPLATES.md` in the same skill directory
for the full prompt patterns.

### Category A: Stylization (14 templates) — P0

| ID | Template | Keywords (EN) | Keywords (ZH) | Input |
|----|----------|---------------|---------------|-------|
| A01 | Chibi Cartoon | chibi, Q-version, cute cartoon, mini me | Q版, 卡通, 萌版, 迷你 | Photo |
| A02 | 3D Pixar Animation | 3D, Pixar, Disney, animated | 3D, 皮克斯, 迪士尼, 动画 | Photo |
| A03 | Comic / Manga | comic, manga, anime, graphic novel | 漫画, 动漫, 日漫 | Photo |
| A04 | Sketch / Pencil | sketch, pencil, drawing, graphite | 素描, 铅笔画, 手绘 | Photo |
| A05 | Clay / Claymation | clay, claymation, plasticine, stop-motion | 黏土, 粘土, 定格动画 | Photo |
| A06 | 80s Retro Animation | 80s, retro, synthwave, vintage cartoon | 80年代, 复古, 怀旧动画 | Photo |
| A07 | Retro-Futurism | retro-future, space age, vintage sci-fi | 未来复古, 复古科幻 | Photo |
| A08 | Ukiyo-e / Chinese Painting | ukiyo-e, Chinese painting, ink wash | 浮世绘, 国画, 国风, 古风, 水墨 | Photo |
| A09 | Watercolor Portrait | watercolor, aquarelle, painting | 水彩, 水彩画 | Photo |
| A10 | K-Pop Star | K-Pop, Korean idol, idol photo | K-Pop, 韩风, 韩国偶像, 明星 | Photo |
| A11 | Imperial / Royal | imperial, royal, king, queen, emperor | 帝王, 皇帝, 王室, 帝王范 | Photo |
| A12 | 90s Yearbook | 90s, yearbook, high school, retro photo | 90年代, 毕业照, 复古照 | Photo |
| A13 | High Fashion | high fashion, vogue, editorial, couture | 高级时尚, 时尚大片, 杂志 | Photo |
| A14 | Cyberpunk Portrait | cyberpunk, neon, cyber, futuristic | 赛博朋克, 赛博, 霓虹 | Photo |

### Category B: Portrait (5 templates) — P0

| ID | Template | Keywords (EN) | Keywords (ZH) | Input |
|----|----------|---------------|---------------|-------|
| B01 | Studio Photoshoot | photoshoot, studio, professional portrait | 写真, 棚拍, 专业照 | Photo |
| B02 | ID Photo | ID photo, passport, headshot | 证件照, 一寸照, 登记照 | Photo |
| B03 | Pet Humanization | pet humanization, anthropomorphic | 宠物拟人, 宠物拟人化 | Pet photo |
| B04 | Emoji / Sticker Pack | emoji, sticker, emoticon | 表情包, 贴纸, 表情 | Photo |
| B05 | Avatar / Profile Picture | avatar, profile, pfp, icon | 头像, 个性头像, 头像生成 | Photo |

### Category C: Pets & Babies (3 templates) — P0

| ID | Template | Keywords (EN) | Keywords (ZH) | Input |
|----|----------|---------------|---------------|-------|
| C01 | Pet Stylization | cute pet, pet portrait, kawaii pet | 萌宠, 宠物造型, 宠物 | Pet photo |
| C02 | Baby Comic Grid | baby comic, baby expressions, grid | 宝宝, 宝宝漫画, 宫格 | Baby photo |
| C03 | Pet VOGUE Magazine | pet magazine, pet cover, VOGUE | 宠物杂志, 宠物封面 | Pet photo |

### Category D: Try-on & Editing (3 templates) — P1

| ID | Template | Keywords (EN) | Keywords (ZH) | Input |
|----|----------|---------------|---------------|-------|
| D01 | Outfit Change | outfit, clothes, wardrobe, try-on | 换装, 换衣服, 试穿 | Photo + text |
| D02 | Hairstyle Change | hairstyle, haircut, hair color | 发型, 换发型, 理发 | Photo + text |
| D03 | Background Change | background, backdrop, remove bg | 换背景, 抠图, 背景 | Photo + text |

### Category E: Social Media & Creative (5 templates) — P1

| ID | Template | Keywords (EN) | Keywords (ZH) | Input |
|----|----------|---------------|---------------|-------|
| E01 | Social Media Post | social media, Instagram, quote card | 配图, 朋友圈, 社交, 名言 | Text (+photo) |
| E02 | Poster Design | poster, flyer, banner, event | 海报, 传单, 横幅 | Text |
| E03 | Storyboard / Comic Strip | storyboard, comic strip, panels | 分镜, 漫画条, 故事板 | Text (+photo) |
| E04 | Handwritten Poster | handwritten, bulletin, class poster | 手抄报, 板报 | Text |
| E05 | Illustration | illustration, artwork, digital art | 插画, 插图, 绘画 | Text |

### Category F: Professional Design (6 templates) — P1

| ID | Template | Keywords (EN) | Keywords (ZH) | Input |
|----|----------|---------------|---------------|-------|
| F01 | E-commerce Main Image | e-commerce, product, Amazon, shop | 电商, 头图, 产品图 | Product photo/text |
| F02 | Sticker Set Design | sticker set, character stickers | 贴纸集, 表情贴纸 | Photo |
| F03 | Interior Design | interior, room design, home decor | 家装, 室内设计, 装修 | Room photo |
| F04 | Logo Design | logo, brand, identity, icon | Logo, 标志, 品牌 | Text |
| F05 | Merchandise Design | merchandise, keychain, figure | 手办, 钥匙扣, 周边 | Photo/text |
| F06 | Coloring Book Page | coloring, line art, coloring page | 涂色, 线稿, 涂色页 | Text (+photo) |

---

## Section 2: Proactive Showcase

When the skill is activated and the user has NO specific image request, present this
template menu to inspire exploration. Use this EXACT format:

```
I can help you create amazing images with 33 high-quality templates! Here are the
most popular ones to try:

🎨 **STYLIZATION** (transform your photo into a new style)
  • Chibi Cartoon — Turn yourself into an adorable Q-version character
  • 3D Pixar Animation — Become a Disney/Pixar movie character
  • Clay/Claymation — Transform into a cute clay figure
  • Comic/Manga — Get your manga character portrait
  • Sketch/Pencil — Beautiful hand-drawn pencil portrait

📸 **PORTRAITS & IDENTITY**
  • K-Pop Star — Get the idol concept photo treatment
  • High Fashion — Vogue cover-worthy editorial portrait
  • 90s Yearbook — Nostalgic retro yearbook photo
  • Studio Photoshoot — Professional portrait photography

🐾 **PETS & BABIES**
  • Pet Humanization — Your pet in a business suit
  • Pet VOGUE Magazine — Your pet on a fashion magazine cover
  • Baby Comic Grid — Adorable 4-panel baby expression comic

✏️ **EDITING**
  • Outfit Change — Try on any clothes instantly
  • Hairstyle Change — Preview a new look
  • Background Change — Teleport to any location

🎯 **CREATIVE & DESIGN**
  • Poster Design — Professional event posters
  • Logo Design — Brand identity from scratch
  • E-commerce Product — Stunning product photography
  • Interior Design — Redesign any room

Just upload a photo and tell me which template to use, or describe what you want
and I'll match the best template for you!
```

---

## Section 3: Intent Matching

When the user provides a request, match it to a template using these rules:

### Step 1: Check for direct keyword match

Scan the user's request (in any language) against ALL keyword columns in the
Template Registry above. If a keyword matches, select that template.

### Step 2: Check for intent patterns

| User intent pattern | Matched template |
|---------------------|-----------------|
| "turn me into" / "变成" / "make me look like" + style word | Category A (match specific style) |
| "把我变成" / "帮我生成...风格" | Category A |
| photo + "cartoon" / "anime" / "卡通" / "动漫" | A01 (Chibi) or A03 (Comic) |
| photo + "3D" / "皮克斯" / "Pixar" | A02 |
| photo + "sketch" / "draw" / "素描" | A04 |
| photo + "clay" / "黏土" | A05 |
| photo + "古风" / "国风" / "水墨" | A08 |
| photo + "水彩" / "watercolor" | A09 |
| photo + "写真" / "portrait" / "photoshoot" | B01 |
| photo + "证件照" / "ID photo" / "passport" | B02 |
| pet photo + "拟人" / "humanize" / "as human" | B03 |
| photo + "表情包" / "sticker" / "emoji" | B04 |
| photo + "头像" / "avatar" / "profile" | B05 |
| pet photo + styling keywords | C01 |
| baby photo + "漫画" / "comic" / "grid" | C02 |
| pet photo + "杂志" / "magazine" / "VOGUE" | C03 |
| photo + "换装" / "换衣服" / "try on" / "outfit" | D01 |
| photo + "发型" / "hairstyle" / "hair" | D02 |
| photo + "背景" / "background" | D03 |
| text about social media / quotes / cards | E01 |
| text about events / posters / flyers | E02 |
| text about stories / panels / storyboard | E03 |
| text about 手抄报 / bulletin | E04 |
| text about illustration / artwork / scene | E05 |
| product + "电商" / "e-commerce" / "product shot" | F01 |
| photo + "贴纸集" / "sticker set" | F02 |
| room photo + "设计" / "design" / "装修" | F03 |
| text about logo / brand / identity | F04 |
| photo/text + "手办" / "钥匙扣" / "figure" | F05 |
| text about coloring / 涂色 / line art | F06 |

### Step 3: Ambiguity resolution

If multiple templates could match:
1. Prefer the MORE SPECIFIC template (e.g., "Q版卡通" → A01, not generic A03)
2. If the user provided a photo, prefer photo-based templates
3. If still ambiguous, ask the user to choose between the top 2-3 candidates

### Step 4: No match → Fallback (Section 5)

---

## Section 4: Template Generation

Once a template is matched:

1. **Read the template** from `TEMPLATES.md` (file in the same skill directory)
2. **Fill placeholders** with user-provided information:
   - Use the user's description for `{placeholder}` values
   - For unfilled placeholders, use the `default:` value in the template
   - For photo-based templates, the user's uploaded image is the reference
3. **Construct the final prompt** by completing the template pattern
4. **Generate the image** using the appropriate mode (see "Image Generation — Dual Mode"):
   - **Mode A** (MCP tool): call `generate_imagen` with `text` = completed prompt, `image_url` = user's reference image
   - **Mode B** (script): call `generate.py` via shell or inline Python:
     ```bash
     python3 <SKILL_DIR>/scripts/generate.py "completed prompt" --image user_photo.jpg --output output.png
     ```
5. **Run Quality Check** (Section 6)
6. **Present the result** to the user with:
   - The generated image
   - A brief description of what was generated
   - 2-3 related template suggestions for further exploration

---

## Section 5: Fallback Generation

When no template matches the user's request, use the General-Detail-General
prompt rewriting methodology:

### Core Rewrite Principles

1. **General-Detail-General structure** — overview → details (primary to secondary) → style anchor
2. **Narrative prose, not keyword soup** — write as if briefing a human artist
3. **Spec-first, style-second, constraints-last**
4. **Exact text in "double quotes"** with explicit typography
5. **Camera + lighting language** — focal length, angle, light source, temperature
6. **Material specificity** — "brushed steel", "matte obsidian with metallic flake"
7. **Film stock for photo scenarios** — "Kodak Gold 200", "Fuji Superia 400"
8. **Aspect ratio stated explicitly**
9. **Negative constraints** at the end — what to exclude
10. **Style anchoring sentence** — final ≤20 words summarizing the target aesthetic

### Fallback Prompt Template

```
Overview: [Medium/style] of [subject + one-sentence description].

Detail-Subject:
[Primary subject with physical details. 2-3 sentences. Be specific.]

Detail-Environment:
[Setting, time of day, composition, spatial arrangement. Aspect ratio.]

Detail-Style:
[Style reference, mood, lighting, color palette.]

Anchor: [≤20-word aesthetic summary].
Negative: [2-5 specific exclusions].
```

After generating with the fallback, suggest the closest matching template(s)
for the user's next attempt.

---

## Section 6: Quality Check & Retry

After every generation, perform a quality check based on the template category:

### Quality Criteria by Category

| Category | Critical checks |
|----------|----------------|
| A (Stylization) | Face identity preserved? Target style accurately applied? No artifacts? |
| B (Portrait) | Face identity preserved? Professional quality? Appropriate composition? |
| C (Pets/Babies) | Pet/baby features preserved? Style consistent? Appealing result? |
| D (Editing) | ONLY target area changed? Everything else pixel-identical? Natural transitions? |
| E (Creative) | All text spelled correctly? Layout professional? Visual hierarchy clear? |
| F (Design) | Professional quality? Text accurate? Style appropriate for use case? |

### Retry Protocol

If the quality check identifies issues:

1. **Identify the specific failing element** (face, text, background, style, etc.)
2. **Construct a surgical edit prompt** targeting ONLY the failing element:
   ```
   "Keep everything exactly the same in this image, but fix [specific issue].
   Do not change [list of elements to preserve]."
   ```
3. **Re-generate** using the previous output as reference image + the edit prompt
4. **Maximum 2 retries** — if still failing after 2 retries, show the best result
   and explain what could be improved

### Text Accuracy Special Handling

For templates with text rendering (E01, E02, E04, F04):
- After generation, carefully verify ALL text character by character
- If any text is misspelled or malformed, always retry with emphasis:
  ```
  "Render the text EXACTLY as: '[correct text]'. Each letter must be
  perfect and clearly legible. No misspellings, no text warping."
  ```

---

## Section 7: Prompt Optimization Rules (apply to ALL templates)

These rules override any conflicting template defaults:

1. **Always English prompts** — even if user speaks Chinese, the prompt to the model must be in English
2. **Identity preservation** — for any photo-based template, always include "preserve the subject's exact facial identity" or equivalent
3. **Aspect ratio** — always state explicitly in the prompt
4. **No text unless requested** — append "No text, no watermark" unless the template specifically includes text
5. **Style anchoring** — every prompt ends with a ≤20-word style summary sentence
6. **Negative constraints** — every prompt includes 2-5 specific exclusions at the end

---

## Conversational Guidelines

- **One generation at a time** — do not batch multiple templates
- **Show, don't tell** — generate first, explain after
- **Suggest next steps** — always recommend 2-3 related templates after showing a result
- **Prefer editing over re-rolling** — if the user wants changes, upload the generated image as reference and make surgical edits
- **Respect user preferences** — if the user specifies parameters that differ from template defaults, use the user's values
