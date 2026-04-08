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
│  │   └─ No match → DELEGATE to image-gen skill (Section 5)
│  │
│  └─ → QUALITY CHECK (Section 6)
│       ├─ Pass → Show result + suggest related templates
│       └─ Fail → RETRY (max 2) with surgical edit
│
END
```

---

## Section 1: Template Registry

50 templates organized in 6 categories (A01-A23, B01-B07, C01-C04, D01-D03, E01-E08, F01-F08). Read `TEMPLATES.md` in the same skill directory
for the full prompt patterns.

### Category A: Stylization (23 templates) — P0

| ID | Template | Keywords (EN) | Keywords (ZH) | Input |
|----|----------|---------------|---------------|-------|
| A01 | Chibi Cartoon | chibi, Q-version, cute cartoon, mini me | Q版, 卡通, 萌版, 迷你 | Photo |
| A02 | 3D Pixar Animation | 3D, Pixar, Disney, animated | 3D, 皮克斯, 迪士尼, 动画 | Photo |
| A03 | Comic / Manga | comic, manga, graphic novel | 漫画, 日漫 | Photo |
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
| A15 | Oil Painting / Classical | oil painting, classical, renaissance | 油画, 古典, 印象派 | Photo |
| A16 | Pixel Art | pixel art, 8-bit, retro game, 16-bit | 像素, 像素风, 像素画 | Photo |
| A17 | Flat / Vector Illustration | flat, vector, minimalist illustration | 平面插画, 扁平风, 矢量 | Photo |
| A18 | Anime / 二次元 | anime, 二次元, Japanese animation | 二次元, 动漫, 番剧 | Photo |
| A19 | Wool Felt / Needle Felt | wool felt, needle felt, felted | 羊毛毡, 毛毡, 手工毡 | Photo |
| A20 | Colored Pencil | colored pencil, Prismacolor, crayon | 彩铅, 彩铅画, 彩色铅笔 | Photo |
| A21 | Pop Art | pop art, Warhol, Lichtenstein | 波普, 波普艺术, 名画风 | Photo |
| A22 | Miniature / Diorama | miniature, diorama, tilt-shift | 微缩景观, 微缩, 小人国 | Photo |
| A23 | Children's Drawing | children drawing, kid art, crayon | 儿童绘画, 儿童画, 童画 | Photo |

### Category B: Portrait (7 templates) — P0

| ID | Template | Keywords (EN) | Keywords (ZH) | Input |
|----|----------|---------------|---------------|-------|
| B01 | Studio Photoshoot | photoshoot, studio, professional portrait | 写真, 棚拍, 专业照 | Photo |
| B02 | ID Photo | ID photo, passport, headshot | 证件照, 一寸照, 登记照 | Photo |
| B03 | Pet Humanization | pet humanization, anthropomorphic | 宠物拟人, 宠物拟人化 | Pet photo |
| B04 | Emoji / Sticker Pack | emoji, sticker, emoticon | 表情包, 贴纸, 表情 | Photo |
| B05 | Avatar / Profile Picture | avatar, profile, pfp, icon | 头像, 个性头像, 头像生成 | Photo |
| B06 | Film / Cinematic Portrait | film photography, cinematic, movie still | 电影写真, 胶片, 电影感 | Photo |
| B07 | Dreamy / Hazy Portrait | dreamy, hazy, soft focus, ethereal | 朦胧, 朦胧肖像, 梦幻 | Photo |

### Category C: Pets & Babies (4 templates) — P0

| ID | Template | Keywords (EN) | Keywords (ZH) | Input |
|----|----------|---------------|---------------|-------|
| C01 | Pet Stylization | cute pet, pet portrait, kawaii pet | 萌宠, 宠物造型, 宠物 | Pet photo |
| C02 | Baby Comic Grid | baby comic, baby expressions, grid | 宝宝, 宝宝漫画, 宫格 | Baby photo |
| C03 | Pet VOGUE Magazine | pet magazine, pet cover, VOGUE | 宠物杂志, 宠物封面 | Pet photo |
| C04 | Pet Costume Play | pet costume, pet mugshot, pet dress-up | 宠物入狱, 萌宠打工, 宠物变装 | Pet photo |

### Category D: Try-on & Editing (3 templates) — P1

| ID | Template | Keywords (EN) | Keywords (ZH) | Input |
|----|----------|---------------|---------------|-------|
| D01 | Outfit Change | outfit, clothes, wardrobe, try-on | 换装, 换衣服, 试穿 | Photo + text |
| D02 | Hairstyle Change | hairstyle, haircut, hair color | 发型, 换发型, 理发 | Photo + text |
| D03 | Background Change | background, backdrop, remove bg | 换背景, 抠图, 背景 | Photo + text |

### Category E: Social Media & Creative (8 templates) — P1/P2

| ID | Template | Keywords (EN) | Keywords (ZH) | Input |
|----|----------|---------------|---------------|-------|
| E01 | Social Media Post | social media, Instagram, quote card | 配图, 朋友圈, 社交, 名言 | Text (+photo) |
| E02 | Poster Design | poster, flyer, banner, event | 海报, 传单, 横幅 | Text |
| E03 | Storyboard / Comic Strip | storyboard, comic strip, panels | 分镜, 漫画条, 故事板 | Text (+photo) |
| E04 | Handwritten Poster | handwritten, bulletin, class poster | 手抄报, 板报 | Text |
| E05 | Illustration | illustration, artwork, digital art | 插画, 插图, 绘画 | Text |
| E06 | YouTube Thumbnail | YouTube, thumbnail, video cover | YouTube缩略图, 封面, 视频封面 | Text (+photo) |
| E07 | Educational Visual | educational, infographic, diagram | 教育, 知识图, 教学图 | Text |
| E08 | Picture Book Illustration | picture book, storybook, bedtime | 绘本, 童话, 儿童读物 | Text |

### Category F: Professional Design (8 templates) — P1/P2

| ID | Template | Keywords (EN) | Keywords (ZH) | Input |
|----|----------|---------------|---------------|-------|
| F01 | E-commerce Main Image | e-commerce, product, Amazon, shop | 电商, 头图, 产品图 | Product photo/text |
| F02 | Sticker Set Design | sticker set, character stickers | 贴纸集, 表情贴纸 | Photo |
| F03 | Interior Design | interior, room design, home decor | 家装, 室内设计, 装修 | Room photo |
| F04 | Logo Design | logo, brand, identity, icon | Logo, 标志, 品牌 | Text |
| F05 | Merchandise Design | merchandise, keychain, figure | 手办, 钥匙扣, 周边 | Photo/text |
| F06 | Coloring Book Page | coloring, line art, coloring page | 涂色, 线稿, 涂色页 | Text (+photo) |
| F07 | Game Asset Design | game character, concept art, game asset | 游戏, 游戏角色, 游戏资产 | Text/photo |
| F08 | Product Marketing Design | marketing, ad creative, campaign | 营销, 广告, 产品营销 | Product + text |

---

## Section 2: Proactive Showcase

When the skill is activated and the user has NO specific image request, present this
template menu to inspire exploration. Use this EXACT format:

```
I can help you create amazing images with 50 high-quality templates! Here are the
most popular ones to try:

🎨 **STYLIZATION** (23 styles to transform your photo)
  • Chibi Cartoon — Turn yourself into an adorable Q-version character
  • 3D Pixar Animation — Become a Disney/Pixar movie character
  • Anime / 二次元 — Beautiful Japanese animation style portrait
  • Oil Painting — Classical masterpiece portrait
  • Pixel Art — Retro 8-bit/16-bit game character
  • Wool Felt — Adorable handmade needle-felted figure
  • Pop Art — Bold Warhol-style color grid
  • Miniature / Diorama — Tiny figurine in a miniature world
  • Clay, Sketch, Watercolor, Ukiyo-e, Cyberpunk, and 14 more...

📸 **PORTRAITS & IDENTITY**
  • K-Pop Star — Get the idol concept photo treatment
  • Film / Cinematic — Moody arthouse movie still portrait
  • Dreamy / Hazy — Ethereal soft-focus romantic portrait
  • 90s Yearbook, High Fashion, Studio Photoshoot, ID Photo

🐾 **PETS & BABIES**
  • Pet Humanization — Your pet in a business suit
  • Pet Costume Play — Your pet's hilarious mugshot or "working" photo
  • Pet VOGUE Magazine — Your pet on a fashion magazine cover
  • Baby Comic Grid — Adorable 4-panel baby expression comic

✏️ **EDITING**
  • Outfit Change — Try on any clothes instantly
  • Hairstyle Change — Preview a new look
  • Background Change — Teleport to any location

🎯 **CREATIVE & DESIGN**
  • YouTube Thumbnail — High-impact clickable video covers
  • Picture Book — Magical storybook illustrations
  • Educational Visual — Infographics and diagrams
  • Game Character Design — Professional concept art sheets
  • Product Marketing — Premium ad campaign visuals
  • Poster, Logo, E-commerce, Interior Design, and more...

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
| photo + "油画" / "oil painting" / "classical" / "古典" | A15 |
| photo + "像素" / "pixel" / "8-bit" / "retro game" | A16 |
| photo + "扁平" / "flat" / "vector" / "平面插画" | A17 |
| photo + "二次元" / "anime" / "动漫" / "番剧" | A18 |
| photo + "羊毛毡" / "wool felt" / "needle felt" / "毛毡" | A19 |
| photo + "彩铅" / "colored pencil" / "彩色铅笔" | A20 |
| photo + "波普" / "pop art" / "Warhol" / "名画风" | A21 |
| photo + "微缩" / "miniature" / "diorama" / "小人国" | A22 |
| photo + "儿童画" / "children drawing" / "kid art" / "童画" | A23 |
| photo + "写真" / "portrait" / "photoshoot" | B01 |
| photo + "证件照" / "ID photo" / "passport" | B02 |
| pet photo + "拟人" / "humanize" / "as human" | B03 |
| photo + "表情包" / "sticker" / "emoji" | B04 |
| photo + "头像" / "avatar" / "profile" | B05 |
| photo + "电影" / "cinematic" / "film photography" / "胶片" | B06 |
| photo + "朦胧" / "dreamy" / "hazy" / "梦幻" / "soft focus" | B07 |
| pet photo + styling keywords | C01 |
| baby photo + "漫画" / "comic" / "grid" | C02 |
| pet photo + "杂志" / "magazine" / "VOGUE" | C03 |
| pet photo + "入狱" / "mugshot" / "打工" / "costume" / "变装" | C04 |
| photo + "换装" / "换衣服" / "try on" / "outfit" | D01 |
| photo + "发型" / "hairstyle" / "hair" | D02 |
| photo + "背景" / "background" | D03 |
| text about social media / quotes / cards | E01 |
| text about events / posters / flyers | E02 |
| text about stories / panels / storyboard | E03 |
| text about 手抄报 / bulletin | E04 |
| text about illustration / artwork / scene | E05 |
| text about YouTube / thumbnail / 缩略图 / video cover | E06 |
| text about educational / infographic / 教育 / diagram | E07 |
| text about picture book / 绘本 / storybook / 童话 | E08 |
| product + "电商" / "e-commerce" / "product shot" | F01 |
| photo + "贴纸集" / "sticker set" | F02 |
| room photo + "设计" / "design" / "装修" | F03 |
| text about logo / brand / identity | F04 |
| photo/text + "手办" / "钥匙扣" / "figure" | F05 |
| text about coloring / 涂色 / line art | F06 |
| text about game / 游戏 / character design / concept art | F07 |
| text/product about marketing / 营销 / ad / campaign / 广告 | F08 |

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

## Section 5: Fallback — Delegate to image-gen Skill

When NO template in this skill matches the user's request, **delegate to the
`image-gen` skill** (https://github.com/yufei-eng/image_gen) for prompt rewriting
and image generation. That skill is a general-purpose prompt optimizer covering
ANY image generation task.

### When to Delegate

- User's request is a valid image generation/editing task, BUT does not match any
  of the 33 templates in Section 1
- User explicitly asks for something outside the template categories (e.g., food
  photography, landscape, architecture, abstract art, custom character design)
- User's intent is ambiguous after Step 3 (Section 3) and none of the top candidates
  feel like a good fit

### How to Delegate

Read the `image-gen` skill's `SKILL.md` and follow its workflow:

1. **Classify the user's request** into one of the `image-gen` skill's 6 scenarios:
   - Avatar / Style Transfer
   - Local Edit
   - Poster / Typography
   - Character Design
   - Product / Object
   - General Scene (catch-all)
2. **Rewrite the prompt** using the matched scenario template and the skill's
   10 Core Rewrite Principles (GDG structure, narrative prose, camera/lighting
   language, material specificity, film stock, aspect ratio, negative constraints,
   style anchoring)
3. **Generate the image** using the same dual-mode approach (Mode A: MCP tool /
   Mode B: script — see "Image Generation — Dual Mode" above)
4. **Run Quality Check** (Section 6 of THIS skill still applies)

### After Fallback Generation

- Show the result to the user
- Suggest the 2-3 closest matching templates from THIS skill for their next attempt
- Example: "I generated this using a general prompt. Next time, you might also like
  template A14 (Cyberpunk Portrait) or E05 (Illustration) for similar vibes!"

### Skill Location

The `image-gen` skill should be installed alongside this skill. Common paths:
- `~/.cursor/skills/image-gen/SKILL.md`
- `~/.claude/skills/image-gen/SKILL.md`
- Or read directly from: https://github.com/yufei-eng/image_gen

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
