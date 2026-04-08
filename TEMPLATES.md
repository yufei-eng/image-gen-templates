# High-Heat Template Prompt Library

50 curated prompt templates for Gemini 3.1 Flash Image (Nano Banana 2).
Each template provides a ready-to-use prompt pattern with `{placeholder}` slots for user customization.

---

## Category A: Stylization (风格化) — P0

### A01 — Chibi Cartoon

**Keywords:** chibi, Q版, 卡通, cute cartoon, mini me, SD character
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Transform the uploaded photo into an adorable chibi-style 3D character. The character should have an oversized round head (approximately 1:1 head-to-body ratio), large sparkling anime eyes with highlight reflections, tiny blushing cheeks, and a cheerful smile. Preserve the subject's exact hairstyle, hair color, and distinguishing facial features for clear identity recognition.

The character wears a miniaturized, stylized version of {outfit_description, default: "their original clothing"}, rendered with soft matte textures and rounded edges as if sculpted from premium vinyl. Pose: {pose, default: "standing with one hand waving, slight head tilt"}.

Background: clean solid {bg_color, default: "pastel pink"} gradient. Lighting: soft studio front light with gentle rim highlight for depth separation. Render style: high-end 3D chibi figure, glossy eyes, smooth skin shading, subtle ambient occlusion at joints. No text, no watermark. Aspect ratio 1:1.

The overall style is a premium collectible chibi figure with Pixar-quality rendering and heart-melting kawaii appeal.
```

**Quality Checklist:**
- [ ] Face identity clearly preserved (hairstyle, key features)
- [ ] Correct chibi proportions (large head, small body)
- [ ] Clean background, no artifacts
- [ ] Cute, appealing aesthetic

---

### A02 — 3D Pixar Animation

**Keywords:** 3D, Pixar, 皮克斯, animated, Disney style, 3D动画
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 4:5

**Prompt Pattern:**

```
Transform the uploaded photo into a Pixar/Disney-style 3D animated character portrait. Maintain 100% facial identity accuracy — preserve exact bone structure, jawline, eye shape, nose, hairstyle, and all distinguishing features.

The character has smooth, slightly stylized skin with subtle subsurface scattering, large expressive eyes with detailed iris reflections, and naturally styled {hair_description, default: "hair matching the original photo"}. Expression: {expression, default: "warm, confident smile with a hint of playfulness"}.

Outfit: {outfit, default: "modern casual — clean crew-neck sweater in warm earth tones"}. The clothing has soft fabric folds and realistic texture.

Background: {background, default: "soft bokeh gradient in warm golden tones, suggesting a cozy indoor setting"}. Lighting: cinematic three-point studio setup — warm key light from upper-left, cool fill from right, subtle rim light separating subject from background.

Render: ultra-detailed Pixar-quality 3D, global illumination, soft shadows, 8K resolution. Head-and-shoulders portrait with clean breathing space. Aspect ratio 4:5. No text, no watermark.

The overall style is a premium animated movie character portrait with cinematic warmth and emotional depth.
```

**Quality Checklist:**
- [ ] Strong facial identity match
- [ ] Pixar/Disney aesthetic (not uncanny valley)
- [ ] Cinematic lighting quality
- [ ] Clean composition, no artifacts

---

### A03 — Comic / Manga

**Keywords:** comic, manga, 漫画, 漫画风格, anime, 动漫
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 3:4

**Prompt Pattern:**

```
Transform the uploaded photo into a stylish manga/comic illustration. Preserve the subject's facial identity, hairstyle, and key distinguishing features while applying bold comic art stylization.

Style: {style, default: "modern shonen manga with clean linework"} — strong black ink outlines of varying thickness, dynamic cross-hatching for shadows, and flat color fills with selective gradient shading. Eyes are slightly enlarged and expressive with detailed highlights. Hair has flowing, dynamic strands with sharp highlights.

Expression: {expression, default: "determined and confident, with a slight smirk"}.
Outfit: {outfit, default: "the subject's original clothing, rendered with comic-style fabric folds and bold shadow shapes"}.

Background: {background, default: "dynamic speed lines radiating from behind the subject with scattered manga-style effect particles (sparkles, small geometric shapes)"}. A subtle halftone dot pattern overlays parts of the background.

Composition: head-and-shoulders portrait, slightly low angle for a heroic feel. Aspect ratio 3:4.

The overall style is a high-quality manga cover illustration with professional-grade inking, vivid colors, and dynamic energy. No text, no watermark.
```

**Quality Checklist:**
- [ ] Recognizable identity from original photo
- [ ] Authentic manga/comic linework style
- [ ] Dynamic composition and energy
- [ ] Clean, professional finish

---

### A04 — Sketch / Pencil Drawing

**Keywords:** sketch, pencil, 素描, 铅笔画, drawing, hand-drawn
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Transform the uploaded photo into a masterful graphite pencil sketch on textured cream drawing paper. Preserve the subject's complete facial identity with precise anatomical accuracy — every facial proportion, bone structure detail, and distinguishing feature must be faithfully reproduced.

Technique: realistic academic pencil portraiture using a full tonal range from deep 8B graphite darks to delicate HB highlights. Employ layered cross-hatching for mid-tones, smooth blending with tortillon for skin surfaces, and crisp directional hatching for hair texture. Leave strategic areas of bare paper for highlights on the forehead, nose bridge, and cheekbones.

The drawing shows {composition, default: "a three-quarter view head-and-shoulders portrait"}. Hair is rendered with individual strand groupings showing natural flow and volume. Eyes have detailed iris patterns and precise catch-light dots.

Background: minimal — soft, loose gestural strokes fading to blank paper at the edges, creating a vignette effect. A subtle graphite smudge in one corner adds authenticity.

The overall style is a museum-quality graphite portrait combining photorealistic accuracy with visible artistic handcraft. Aspect ratio 1:1. No color, no watermark.
```

**Quality Checklist:**
- [ ] Strong facial likeness to original
- [ ] Authentic pencil/graphite texture (not digital filter look)
- [ ] Full tonal range with visible drawing technique
- [ ] Paper texture visible

---

### A05 — Clay / Claymation

**Keywords:** clay, claymation, 黏土, 粘土, stop-motion, plasticine
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Transform the uploaded photo into a charming claymation-style character. Preserve key facial features and identity while rendering the entire subject as if hand-sculpted from colorful modeling clay.

The character has smooth, rounded clay surfaces with visible hand-molded textures — subtle fingerprint impressions, gentle surface undulations, and soft edges where clay pieces join. Skin is warm-toned clay with slight color variations. Eyes are large, expressive spheres with glossy black pupils. Hair is sculpted from {hair_color, default: "matching-color"} clay in thick, stylized strands.

Outfit: {outfit, default: "a miniaturized version of the original clothing"}, crafted from clay with simplified details — tiny buttons formed from clay balls, fabric folds rendered as smooth clay ridges.

Pose: {pose, default: "standing with a friendly wave and tilted head"}.

Background: a simple {bg, default: "pastel-colored"} clay backdrop with soft, even studio lighting typical of professional stop-motion animation sets. Two-point lighting: warm key light from left, soft fill from right creating gentle shadows that reveal clay surface texture.

The overall style is a premium Aardman/Laika-quality claymation character with heartwarming tactile appeal. Aspect ratio 1:1. No text, no watermark.
```

**Quality Checklist:**
- [ ] Recognizable identity preserved
- [ ] Authentic clay/plasticine texture (fingerprints, imperfections)
- [ ] Warm, appealing lighting
- [ ] Professional stop-motion aesthetic

---

### A06 — 80s Retro Animation

**Keywords:** 80s, retro, 80年代, retro animation, vintage cartoon, synthwave
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 4:5

**Prompt Pattern:**

```
Transform the uploaded photo into a stylish 1980s retro animation character portrait. Preserve the subject's facial identity and key features while applying the distinct visual language of 80s Japanese/American animation.

Style: bold, clean cel-animation look with strong black outlines, flat color fills with hard-edged shadow shapes (no gradients), and vibrant saturated colors. Eyes are large and sparkly with multiple highlight reflections in the classic 80s anime style. Hair has dramatic volume and flow with sharp highlight streaks in {highlight_color, default: "electric blue"}.

Outfit: {outfit, default: "a stylish 80s ensemble — oversized pastel blazer with rolled sleeves, bold geometric-print t-shirt underneath"}.

Background: a synthwave-inspired sunset gradient — deep purple at the top transitioning through hot magenta to neon orange at the bottom. A chrome grid recedes toward a glowing horizon line. Lens flares and star sparkles scatter across the composition.

Lighting: dramatic rim lighting in neon pink/cyan, with warm frontal fill. Film grain overlay for authentic vintage feel.

Composition: head-and-shoulders, slightly heroic low angle. Aspect ratio 4:5.

The overall style is a premium 80s animation cel portrait blending City Pop aesthetics with synthwave neon drama. No text, no watermark.
```

**Quality Checklist:**
- [ ] Identity recognizable from original
- [ ] Authentic 80s animation style (not modern anime)
- [ ] Vibrant neon/synthwave color palette
- [ ] Clean cel-animation look

---

### A07 — Retro-Futurism

**Keywords:** retro-futurism, 未来复古, retro sci-fi, space age, vintage future
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 3:4

**Prompt Pattern:**

```
Transform the uploaded photo into a retro-futuristic portrait in the style of 1960s space-age illustration art. Preserve the subject's facial identity while placing them in a sleek, optimistic vision of the future as imagined in the mid-20th century.

The subject wears {outfit, default: "a streamlined silver space suit with orange accent panels, a transparent dome helmet resting beside them"}. Their pose is {pose, default: "confident and forward-looking, chin slightly raised"}.

Background: a sweeping vista of a retro-futuristic cityscape — gleaming chrome towers with rounded edges, flying cars with tail-fins, monorail tracks curving through the sky, and a massive ringed planet visible on the horizon. The sky transitions from teal to warm coral.

Style: painted illustration with visible brushwork, reminiscent of Syd Mead or Robert McCall. Colors are saturated but slightly muted with a warm film-stock quality. Strong directional lighting creates dramatic shadows and metallic reflections.

Composition: three-quarter portrait with the cityscape visible behind. Aspect ratio 3:4.

The overall style is a premium retro-futuristic painted illustration evoking the optimistic space-age dreams of the 1960s. No text, no watermark.
```

**Quality Checklist:**
- [ ] Identity preserved from photo
- [ ] Authentic retro-futuristic aesthetic (not modern sci-fi)
- [ ] Painted illustration quality
- [ ] Optimistic, aspirational mood

---

### A08 — Ukiyo-e / Chinese Painting

**Keywords:** ukiyo-e, 浮世绘, Chinese painting, 国画, 国风, 古风, Japanese woodblock, ink wash
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 3:4

**Prompt Pattern:**

```
Transform the uploaded photo into an exquisite East Asian traditional art portrait. Preserve the subject's facial identity and features while rendering them in {style, default: "Japanese Ukiyo-e woodblock print"} style.

The subject is depicted wearing {outfit, default: "an elegant traditional kimono with intricate floral patterns in indigo blue and vermilion red"}. Expression is serene and dignified, maintaining the original person's likeness.

Technique: {technique, default: "Ukiyo-e woodblock print — bold hand-carved ink outlines of varying thickness, flat areas of color from traditional mineral pigments (Prussian blue, vermilion, yellow ochre, soft green), visible wood-grain texture throughout"}. Skin is rendered with smooth, flat warm tones. Hair is depicted as flowing black ink strokes with fine individual strand details.

Background: {background, default: "stylized clouds in the upper portion, a distant mountainscape with Mt. Fuji silhouette, cherry blossom branches framing one side"}. The composition uses traditional flattened perspective with no vanishing point.

Include: subtle paper fiber texture, slight pigment bleeding at color boundaries for authenticity, and a small red artist seal stamp in one corner.

Composition: portrait from chest up. Aspect ratio 3:4.

The overall style is a museum-quality traditional East Asian art portrait with authentic period craftsmanship. No modern elements, no watermark.
```

**Quality Checklist:**
- [ ] Facial identity recognizable
- [ ] Authentic traditional art technique (not digital filter)
- [ ] Correct use of traditional color palette
- [ ] Paper/woodblock texture present

---

### A09 — Watercolor Portrait

**Keywords:** watercolor, 水彩, 水彩画, aquarelle, painting
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Transform the uploaded photo into a luminous watercolor portrait painting on cold-pressed watercolor paper. Preserve the subject's facial identity with artistic interpretation — key features, bone structure, and expression must remain recognizable.

Technique: professional watercolor portraiture with wet-on-wet blending for skin tones creating beautiful color bleeds and soft edges. Use a limited but harmonious palette: warm skin tones mixed from raw sienna, cadmium red, and yellow ochre; cool shadows in cerulean blue and light violet; hair in {hair_colors, default: "burnt umber with raw sienna highlights"}.

Key watercolor effects: visible paper grain showing through transparent washes, deliberate areas where pigment pools and granulates at edges, controlled blooms where wet colors merge organically, and crisp dry-brush strokes for hair texture and clothing details. White of the paper serves as the brightest highlights on nose tip, brow ridge, and lower lip.

Background: loose, suggestive washes in {bg_colors, default: "complementary cool blues and soft greens"} that bleed and fade toward the paper edges, leaving generous white margins.

Composition: head-and-shoulders portrait with slightly off-center placement. Aspect ratio 1:1.

The overall style is a gallery-quality watercolor portrait with the luminous transparency and spontaneous beauty unique to the watercolor medium. No text, no watermark.
```

**Quality Checklist:**
- [ ] Facial likeness preserved
- [ ] Authentic watercolor look (transparency, bleeds, granulation)
- [ ] Visible paper texture
- [ ] Beautiful color harmony

---

### A10 — K-Pop Star

**Keywords:** K-Pop, kpop, 韩风, Korean idol, 明星, idol photo
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 3:4

**Prompt Pattern:**

```
Transform the uploaded photo into a stunning K-Pop idol concept photo. Preserve 100% facial identity — exact facial structure, eye shape, nose, and lips — while elevating the styling to top-tier K-Pop visual standards.

Styling: {styling, default: "flawless, dewy glass skin with subtle highlight on cheekbones and nose bridge. Soft gradient lip tint in rose pink. Eyes enhanced with subtle smoky liner and natural lashes. Brows groomed to a clean, natural arch"}.

Hair: {hair, default: "styled in the latest K-Pop trend — fluffy, textured layers with a center part, in a trendy ash brown tone with subtle highlights"}.

Outfit: {outfit, default: "designer oversized blazer in cream white over a thin chain necklace and minimal black turtleneck"}.

Background: {background, default: "clean studio setting with soft, dreamy haze and lens flares in pastel tones — reminiscent of a high-budget music video concept photo"}. Lighting: beauty-focused setup — large softbox from front-left for flawless skin rendering, subtle rim light in cool blue from behind for ethereal glow, and butterfly lighting for defined cheekbone shadows.

Camera: 85mm portrait lens, f/2.0, shallow depth of field. Color grading: slightly desaturated with lifted blacks and a cool-toned shadow shift, characteristic of modern K-Pop photography.

Aspect ratio 3:4. Head-to-waist framing.

The overall style is an official K-Pop idol concept photo worthy of a debut album photobook. No text, no watermark.
```

**Quality Checklist:**
- [ ] Strong facial identity match
- [ ] Polished K-Pop beauty standard (skin, hair, styling)
- [ ] Professional studio lighting
- [ ] Album-quality color grading

---

### A11 — Imperial / Royal

**Keywords:** imperial, royal, 帝王, 皇帝, 王室, king, queen, emperor, 帝王范
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 3:4

**Prompt Pattern:**

```
Transform the uploaded photo into a grand royal portrait in the style of {era, default: "European Renaissance oil painting, reminiscent of Hans Holbein or Hyacinthe Rigaud"}.

Preserve the subject's complete facial identity — exact bone structure, features, and expression — while draping them in magnificent {royal_attire, default: "crimson velvet royal robes with ermine fur trim, intricate gold embroidery featuring heraldic motifs, and a jewel-encrusted crown resting slightly askew"}.

The subject sits or stands in a {pose, default: "regal three-quarter pose on an ornate gilded throne, one hand resting on the armrest, the other holding a golden scepter"}.

Background: a palatial interior — {bg, default: "deep burgundy drapes with gold tassels frame the composition, a marble column is partially visible, and warm candlelight illuminates a tapestry depicting a coat of arms"}.

Painting technique: rich oil paint with visible impasto brushwork on highlights, smooth glazing layers for skin, and meticulous detail on fabrics and jewelry. Lighting: dramatic chiaroscuro — warm golden key light from upper left, deep shadows on the opposite side, candlelight reflections on metallic elements.

Composition: formal royal portrait, three-quarter body. Aspect ratio 3:4.

The overall style is a museum-worthy classical royal portrait with the gravitas and grandeur of old-master painting. No modern elements, no watermark.
```

**Quality Checklist:**
- [ ] Facial identity clearly preserved
- [ ] Authentic historical royal aesthetic
- [ ] Rich oil painting technique visible
- [ ] Dramatic, regal atmosphere

---

### A12 — 90s Yearbook

**Keywords:** 90s, yearbook, 毕业照, 90年代, high school, retro photo
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Transform this selfie into a 1990s American high school yearbook photo. Preserve the subject's complete facial identity — exact face, features, and expression.

Style: classic 90s yearbook portrait — head-and-shoulders framed shot, soft diffused studio lighting from dual umbrella flashes, gentle catch-lights in the eyes. Background: {background, default: "iconic 90s laser-beam gradient — cyan and magenta rays radiating against deep cobalt blue"}.

The subject wears {outfit, default: "a navy crew-neck sweater with a plaid button-up collar visible underneath, era-appropriate and neatly pressed"}.

Film: Kodak Gold 200 — warm color shift, subtle grain, slightly desaturated reds. Skin has the characteristic soft-focus portrait look of 90s school photography — smooth but not over-retouched. Hair is styled naturally, period-appropriate.

Composition: centered subject, tight head-and-shoulders crop with even breathing space on all sides. Square format (1:1 aspect ratio).

The overall style is an authentic 1990s American high school yearbook page photo that perfectly captures the era's portrait conventions. No modern elements, no digital artifacts.
```

**Quality Checklist:**
- [ ] Face strongly resembles the input
- [ ] Period-accurate backdrop (laser beams or mottled gradient)
- [ ] Era-appropriate outfit and styling
- [ ] Authentic film grain and color grading

---

### A13 — High Fashion

**Keywords:** high fashion, 高级时尚, vogue, editorial, fashion photography, 时尚大片
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 3:4

**Prompt Pattern:**

```
Transform the uploaded photo into a high-fashion editorial portrait. Preserve the subject's facial identity with 100% accuracy while elevating the visual presentation to top-tier fashion magazine standards.

Styling: {styling, default: "dramatic, editorial makeup — bold sculpted cheekbones, smoky eye with metallic copper accents, perfectly defined brows, matte nude lip. Skin: luminous, dewy, with strategic highlighter on high points"}.

Hair: {hair, default: "sleek, sculptural updo with a few loose face-framing tendrils, polished to a high-gloss finish"}.

Outfit: {outfit, default: "an avant-garde structured shoulder piece in black with metallic thread detailing, paired with a sheer high-neck underlayer"}.

Lighting: dramatic Vogue-style setup — hard key light from 45° upper-left creating strong shadow geometry on the face, large reflector fill from below for jaw definition, subtle color-gelled hair light in {accent_color, default: "deep amber"}. The interplay creates sharp, architectural shadows.

Background: {background, default: "seamless gradient from charcoal to black"}. Camera: 100mm telephoto, f/2.8, razor-thin depth of field isolating the subject. Color grading: rich contrast, deep blacks, skin tones slightly warm.

Composition: tight portrait from chest up, subject looking {direction, default: "directly into camera with an intense, captivating gaze"}. Aspect ratio 3:4.

The overall style is a cover-worthy high-fashion editorial portrait with dramatic lighting and commanding presence. No text, no watermark.
```

**Quality Checklist:**
- [ ] Facial identity preserved
- [ ] Fashion-editorial quality lighting
- [ ] Professional styling and makeup render
- [ ] Magazine-grade color and contrast

---

### A14 — Cyberpunk Portrait

**Keywords:** cyberpunk, 赛博朋克, neon, cyber, futuristic, sci-fi portrait
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 9:16

**Prompt Pattern:**

```
Transform the uploaded photo into a stunning cyberpunk portrait. Preserve the subject's facial identity while immersing them in a neon-drenched dystopian future.

The subject has {cyberwear, default: "sleek chrome cybernetic augmentations — a thin LED-lit strip running along the jawline, a glowing cyan optical implant replacing one eye's iris, and micro-circuit tattoos visible on the neck in faint bioluminescent blue"}.

Outfit: {outfit, default: "a weathered black tactical jacket with holographic patches, high collar, and subtle fiber-optic threading in the seams that pulses with soft violet light"}.

Environment: {environment, default: "a rain-slicked alley in a neon-lit megacity — towering buildings with holographic advertisements in the background, steam rising from street grates, reflections of pink and cyan neon on every wet surface"}.

Lighting: dramatic multi-source neon — hot magenta from a sign to the left, electric cyan from the right, warm amber from a distant street lamp behind. Rain droplets catch and scatter the neon light. Volumetric fog/haze adds depth layers.

Camera: 50mm at f/1.4 — subject tack-sharp, background dissolving into a colorful bokeh of neon circles. Aspect ratio 9:16 vertical.

The overall style is a cinematic cyberpunk portrait blending Blade Runner atmosphere with modern photo-real quality. No text, no watermark.
```

**Quality Checklist:**
- [ ] Facial identity recognizable
- [ ] Authentic cyberpunk neon aesthetic
- [ ] Detailed environment and atmosphere
- [ ] Cinematic depth and bokeh

---

## Category B: Portrait (写真/人像) — P0

### B01 — Studio Photoshoot

**Keywords:** photoshoot, portrait, 写真, 棚拍, studio photo, professional portrait
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 3:4

**Prompt Pattern:**

```
Transform the uploaded photo into a high-end studio portrait photoshoot. Preserve the subject's complete facial identity, expression nuance, and natural skin texture.

Setting: {setting, default: "a professional photography studio with a seamless paper backdrop in warm taupe"}.

Outfit: {outfit, default: "elegant, camera-ready — tailored blazer in soft camel over a simple white t-shirt, creating a clean, editorial look"}.

Pose: {pose, default: "natural three-quarter body angle, one shoulder slightly forward, head tilted 10 degrees with a genuine, relaxed expression"}.

Lighting: professional three-point setup — large octabox key light at 45° camera-left producing soft, wrapping illumination with gentle shadow falloff on the face. Silver reflector fill from camera-right lifting shadows to a 2:1 ratio. Subtle strip light from behind for hair separation and rim highlight. Color temperature: 5500K daylight balanced.

Camera: 85mm portrait lens at f/2.0, shallow depth of field with subject's eyes tack-sharp. Film simulation: Fuji Pro 400H — slightly lifted shadows, creamy skin tones, understated pastel palette.

Composition: three-quarter body with generous headroom. Aspect ratio 3:4.

The overall style is a premium studio portrait with magazine-grade lighting, natural skin rendering, and timeless elegance. No text, no watermark.
```

**Quality Checklist:**
- [ ] Strong facial identity match
- [ ] Professional studio lighting quality
- [ ] Natural skin texture (not over-smoothed)
- [ ] Clean, elegant composition

---

### B02 — ID Photo

**Keywords:** ID photo, passport photo, 证件照, 一寸照, headshot, visa photo
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 3:4

**Prompt Pattern:**

```
Transform the uploaded photo into a professional ID/passport-style headshot. Preserve the subject's facial identity with absolute accuracy — no alterations to facial features whatsoever.

Requirements: formal head-and-shoulders portrait against a solid {background, default: "white"} background with no texture, shadows, or gradients. Subject faces the camera directly with a {expression, default: "neutral, calm expression with mouth closed, eyes open and looking straight at the lens"}.

Lighting: flat, even illumination from dual front lights eliminating harsh shadows. No shadow on the background, no shadow under chin. Color temperature: neutral 5500K.

Outfit: {outfit, default: "clean, dark-colored formal shirt or blouse with a simple collar"}.

Standards: ears visible, forehead clear, no hair covering eyes. No glasses glare. Skin rendered naturally — no beauty filter, no smoothing, faithful skin tone reproduction. Head centered in frame, face occupying approximately 70% of the vertical space.

Aspect ratio 3:4 (standard ID photo proportions). Resolution sharp and clear.

The overall style is a regulation-compliant ID photograph with professional studio quality and neutral presentation. No text, no watermark, no border.
```

**Quality Checklist:**
- [ ] Exact facial identity preserved
- [ ] Solid, even background
- [ ] Compliant composition (centered, proper face-to-frame ratio)
- [ ] Natural skin (no beauty filter artifacts)

---

### B03 — Pet Humanization

**Keywords:** pet humanization, 宠物拟人化, pet portrait, pet as human, anthropomorphic
**Input:** User pet photo
**Aspect Ratio:** 3:4

**Prompt Pattern:**

```
Transform the uploaded pet photo into a sophisticated anthropomorphic portrait. The pet becomes a dignified humanoid character while preserving their exact species, breed characteristics, fur color/pattern, facial features, and expression.

The pet character stands upright in a human pose, wearing {outfit, default: "a tailored three-piece suit in charcoal gray with a burgundy silk pocket square and gold cufflinks"}. They have human-like posture and proportions (bipedal, arms at sides) while retaining their animal head, fur, ears, and distinctive features.

Expression: {expression, default: "dignified and slightly amused, as if posing for an official corporate headshot"}.

Background: {background, default: "a rich, dark wood-paneled study with leather-bound books and a warm desk lamp"}.

Lighting: classic portrait studio setup — warm key light from the left creating soft Rembrandt lighting on the furred face, fill light from the right, subtle backlight for fur edge definition.

Style: hyper-realistic digital painting with attention to individual fur strands, fabric texture on the clothing, and accurate pet breed anatomy. The fusion of animal and human elements must feel natural, not grotesque.

Composition: three-quarter body portrait. Aspect ratio 3:4.

The overall style is a premium anthropomorphic pet portrait with the elegance of a Victorian gentleman's painting and the realism of modern digital art. No text, no watermark.
```

**Quality Checklist:**
- [ ] Pet's breed, colors, and features preserved
- [ ] Natural-looking anthropomorphic fusion
- [ ] Clothing rendered realistically on animal body
- [ ] Dignified, appealing result

---

### B04 — Emoji / Sticker Pack

**Keywords:** emoji, sticker, 表情包, 贴纸, emoticon, reaction
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Create a 3x3 grid sticker set (9 stickers total) based on the uploaded photo. Each sticker is a stylized portrait of the same person in a different expression/pose, designed as premium digital stickers.

Character style: Pixar-quality 3D with slightly exaggerated proportions — head slightly larger than realistic, big expressive eyes, smooth rounded features. Preserve the subject's exact hairstyle, hair color, and key facial features for clear identity recognition across all 9 stickers.

9 expressions (one per grid cell):
1. Happy smile with squinted eyes
2. Laughing with open mouth
3. Cool (wearing sunglasses, finger guns)
4. Surprised (wide eyes, open mouth, hands on cheeks)
5. Thinking (chin on hand, looking up)
6. Winking (one eye closed, tongue out playfully)
7. Heart eyes (cartoonish hearts replacing pupils, hand heart gesture)
8. Angry (puffed cheeks, furrowed brows, comedic steam lines)
9. Thumbs up (big grin, exaggerated thumbs up)

Each sticker: head-and-shoulders only, different casual outfit per sticker, bold clean outline, subtle drop shadow. Background: clean white for each cell. Clear spacing between stickers.

Final layout: 3x3 grid, cream background, 1:1 aspect ratio, ultra-high resolution (8K).

The overall style is a highly engaging, cute, and expressive premium sticker pack optimized for messaging platforms. No text labels.
```

**Quality Checklist:**
- [ ] All 9 stickers present in grid
- [ ] Consistent identity across all stickers
- [ ] Each expression clearly distinct
- [ ] Clean white backgrounds, proper spacing

---

### B05 — Avatar / Profile Picture

**Keywords:** avatar, profile, 头像, profile picture, pfp, icon
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Transform the uploaded photo into a stunning stylized avatar/profile picture. Preserve the subject's facial identity while creating a visually striking, icon-worthy portrait optimized for social media profiles.

Style: {style, default: "8K stylized digital portrait illustration — semi-realistic blending editorial portrait art with graphic novel aesthetics. Strong sketch-like linework with expressive strokes, visible textured brushwork and painterly shading, dry brush effects around the shoulders where the image softly dissolves"}.

Face accuracy (critical): match 100% — preserve exact facial structure, bone anatomy, grooming details, jawline, cheekbones, forehead proportions. Natural skin texture with varied tones (subtle reds, neutral hues). No beautification — preserve raw realism and imperfections.

Hair: {hair, default: "natural-length hair, slightly naturally messy, with textured strands highlighted to add depth and volume"}.

Outfit: {outfit, default: "a dark green and brown plaid jacket with a painterly pattern, muted beige button-down shirt underneath"}.

Composition: head-and-shoulders portrait, perfectly centered. Shoulders must not touch edges — clean breathing space. Bottom fades into soft, rough painterly edge (subtle cut-out feel). Background: {background, default: "minimal cream with a bold orange square behind the head creating contrast and halo-like framing"}.

Lighting: soft directional from upper left, gentle highlights on forehead and nose bridge. Aspect ratio 1:1.

The overall style is an ultra-detailed premium illustration portrait that functions as a distinctive, recognizable social media avatar. No text.
```

**Quality Checklist:**
- [ ] Strong facial identity match
- [ ] Visually distinctive and "avatar-ready"
- [ ] Clean 1:1 composition
- [ ] Artistic style consistent throughout

---

## Category C: Pets & Babies (萌宠/宝宝) — P0

### C01 — Pet Stylization

**Keywords:** pet, cute, 萌宠, 宠物, 宠物造型, furry friend
**Input:** User pet photo
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Transform the uploaded pet photo into an adorable stylized portrait. Preserve the pet's exact breed characteristics, fur color/pattern, eye color, and distinguishing features while applying a {style, default: "kawaii needle-felted plush"} aesthetic.

The pet is rendered as if crafted from {material, default: "soft needle-felted wool — fluffy texture with visible fine stitching and fuzzy edges, like a premium handmade plush toy"}. Features: big sparkling eyes with detailed reflections, tiny blushing cheeks (subtle pink circles), and a {expression, default: "happy, heart-melting smile"}.

Scene: {scene, default: "sitting among colorful flowers, tiny sparkles floating around, warm gentle lighting creating a dreamy glow"}.

Accessories: {accessories, default: "a tiny flower crown or bow on the head, matching the color palette"}.

Color palette: warm pastels with {accent, default: "soft pink, lavender, and mint green"} accents. Lighting: warm, soft, slightly golden — like a magical golden hour moment. Subtle lens flare or bokeh sparkles add whimsy.

Composition: centered pet portrait. Aspect ratio 1:1.

The overall style is a heart-melting kawaii pet portrait with ultra-detailed texture and professional plush photography aesthetics. No text, no watermark.
```

**Quality Checklist:**
- [ ] Pet's identity clearly preserved (breed, colors, markings)
- [ ] Adorable, appealing aesthetic
- [ ] Consistent stylization
- [ ] Warm, inviting color palette

---

### C02 — Baby Comic Grid

**Keywords:** baby, 宝宝, comic grid, 宫格漫画, baby expressions, four panel
**Input:** User baby photo
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Transform the uploaded baby photo into a delightful 2x2 comic-style grid showing four different expressions/moments of the same baby. Preserve the baby's exact facial features, skin tone, and any distinguishing characteristics across all four panels.

Style: vibrant hand-drawn manga/comic aesthetic with bold outlines, bright colors, and playful manga special effects.

Four panels:
1. TOP-LEFT: Surprised face — wide eyes, open mouth "O" shape. Manga effect: large exclamation marks "!!" and speed lines radiating outward.
2. TOP-RIGHT: Pouty/angry face — puffed cheeks, furrowed tiny brows. Manga effect: comedic anger veins and small flame symbols.
3. BOTTOM-LEFT: Laughing — big open-mouth giggle, squished happy eyes. Manga effect: musical notes and sparkle stars floating around.
4. BOTTOM-RIGHT: Cute/shy — head tilted, finger near mouth, blushing cheeks. Manga effect: floating hearts and flower petals.

Each panel has a different colorful background (pastel yellow, pastel pink, pastel blue, pastel green). Baby wears {outfit, default: "adorable animal-themed onesies — different one per panel (bear, rabbit, duck, cat)"}.

Center intersection: a heart-shaped frame containing a cute miniature version of the baby waving. Panels have clean white borders between them.

Composition: 2x2 grid. Aspect ratio 1:1.

The overall style is a vibrant baby comic page bursting with personality and kawaii charm. No readable text except manga sound effects.
```

**Quality Checklist:**
- [ ] Baby's features consistent across all 4 panels
- [ ] Four distinct expressions clearly shown
- [ ] Manga effects and decorations present
- [ ] Clean grid layout with proper spacing

---

### C03 — Pet VOGUE Magazine Cover

**Keywords:** pet magazine, 宠物杂志, VOGUE pet, pet cover, magazine cover
**Input:** User pet photo
**Aspect Ratio:** 3:4

**Prompt Pattern:**

```
Transform the uploaded pet photo into a glamorous fashion magazine cover featuring the pet as the star model. Preserve the pet's exact breed, fur color/pattern, and distinctive features.

The pet poses as a confident fashion model: {pose, default: "wearing designer sunglasses pushed up on the head, draped in a luxurious bathrobe, leaning back on a velvet chaise lounge with effortless attitude"}.

Magazine layout: large masthead text "VOGUE" at the top in classic Didot serif font, white with subtle shadow. Cover lines on the left side in elegant small serif type: {coverlines, default: "'THE PET ISSUE', 'Best Dressed Fur Babies 2026', 'Luxury Life: Inside Their $10M Doghouse'"}.

Photography style: high-end fashion editorial — soft beauty dish lighting from above-right creating flattering catchlights in the pet's eyes, subtle fill from a large reflector, rim light for fur separation. Film stock: medium format, Kodak Portra 400 — creamy skin tones, subtle grain, soft pastel palette.

Background: {background, default: "luxurious setting — marble floor, velvet drapes, vintage gold frame partially visible"}.

Composition: classic fashion magazine cover layout with text placement. Aspect ratio 3:4.

The overall style is a premium, high-fashion pet magazine cover indistinguishable from a real Vogue publication. Text must be spelled correctly and clearly legible.
```

**Quality Checklist:**
- [ ] Pet's identity preserved
- [ ] "VOGUE" text correctly spelled and prominent
- [ ] Fashion magazine composition and typography
- [ ] Luxurious, editorial aesthetic

---

## Category D: Try-on & Editing (换装/编辑) — P1

### D01 — Outfit Change

**Keywords:** outfit, clothing, change clothes, 换装, 换衣服, try on, wardrobe
**Input:** User photo + outfit description
**Aspect Ratio:** (preserve original)

**Prompt Pattern:**

```
A precise local image edit replacing only the clothing on the subject while keeping every other element of the photograph pixel-identical.

Target Change:
Replace the current outfit with {new_outfit, default: "a tailored navy blue blazer over a crisp white dress shirt, top button undone, creating a smart-casual professional look"}. The new clothing has {fabric_details, default: "fine wool texture with subtle herringbone pattern, natural fabric draping and wrinkles at the elbow bend, properly proportioned lapels"}.

Absolute Preservation (do NOT change any of these):
- Face: exact expression, skin tone, every facial feature, hair, brows, glasses if present
- Body: exact pose, hand positions, body proportions, body language
- Accessories: existing jewelry, watch, bag — keep or naturally adjust for new outfit
- Background: every single background element, colors, textures, depth of field
- Camera: identical angle, focal length, perspective, color grading, white balance

Transition:
Clothing edges blend seamlessly with the neck, wrists, and waist. Shadows from the new garment follow the existing lighting direction and intensity. Fabric naturally interacts with the body's pose — no floating or stiff appearance.

Do not change the aspect ratio. Do not alter the face in any way.

The result is a seamless, photorealistic outfit swap indistinguishable from an original photograph.
```

**Quality Checklist:**
- [ ] Only clothing changed, nothing else
- [ ] Background completely preserved
- [ ] Face and expression unchanged
- [ ] New outfit looks natural and realistic

---

### D02 — Hairstyle Change

**Keywords:** hairstyle, hair, 发型, 换发型, haircut, hair color, 改发型
**Input:** User photo + hairstyle description
**Aspect Ratio:** (preserve original)

**Prompt Pattern:**

```
A precise local image edit changing only the hairstyle of the subject while keeping every other element of the photograph pixel-identical.

Target Change:
Transform the hair to {new_hairstyle, default: "a short, textured pixie cut with side-swept bangs, in a warm honey blonde color with darker roots for dimension"}. The new hair has {hair_details, default: "natural movement and texture, individual strand detail, realistic shine highlights matching the scene's lighting"}.

Absolute Preservation (do NOT change any of these):
- Face: exact expression, skin tone, every facial feature, eyebrows, makeup, facial hair
- Body: exact pose, clothing, every fabric detail, hand positions
- Accessories: earrings, necklace, glasses — adjust naturally if hair length changes interaction
- Background: every single pixel of background unchanged
- Camera: identical angle, focal length, perspective, color grading

Transition:
The hairline blends naturally with the forehead and temples. Any newly exposed areas (ears, neck) have natural skin tone matching the face. Hair shadows on the face and shoulders follow the existing lighting direction.

Do not change the aspect ratio. Do not alter the face in any way.

The result is a seamless, photorealistic hairstyle change indistinguishable from an original photograph.
```

**Quality Checklist:**
- [ ] Only hair changed
- [ ] Face and background completely preserved
- [ ] New hairstyle looks natural
- [ ] Lighting and shadows consistent

---

### D03 — Background Change

**Keywords:** background, 背景, 换背景, remove background, change background, 抠图
**Input:** User photo + background description
**Aspect Ratio:** (preserve original)

**Prompt Pattern:**

```
A precise image edit replacing only the background while keeping the subject completely unchanged.

Target Change:
Replace the entire background with {new_background, default: "a serene Japanese zen garden — raked white sand patterns, smooth gray stones, a small bamboo water fountain, and a few carefully placed moss-covered rocks, with soft morning mist and warm golden hour sunlight filtering through distant bamboo groves"}.

Absolute Preservation (do NOT change any of these):
- Subject: every detail — face, expression, hair, clothing, pose, accessories, skin tone
- Lighting on subject: attempt to re-light the subject to match the new environment naturally
- Edge quality: the subject's outline must have natural, anti-aliased edges — no harsh cutout appearance

New Background Details:
{bg_details, default: "The background has natural depth of field — sharp detail in the mid-ground elements nearest the subject, softening to gentle bokeh further back. Lighting: warm directional sunlight from the right, matching any existing subject lighting where possible. Color palette: muted earth tones with pops of green"}.

Transition:
The subject's feet/base connects naturally with the new ground surface. Reflected light from the new environment subtly influences the subject's shadow areas. Cast shadows appear on the new ground surface matching the lighting.

Do not change the aspect ratio.

The result is a seamless composite where the subject appears to have been genuinely photographed in the new location.
```

**Quality Checklist:**
- [ ] Subject completely unchanged
- [ ] Background fully replaced
- [ ] Natural edge quality (no cutout artifacts)
- [ ] Consistent lighting between subject and background

---

## Category E: Social Media & Creative (自媒体/创意) — P1

### E01 — Social Media Post

**Keywords:** social media, Instagram, 配图, social post, quote card, 名言卡
**Input:** Text content (quote, caption) + optional photo
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Create a visually stunning social media post card for {platform, default: "Instagram"}.

Content: {content_type, default: "an inspirational quote card"}.

Text to render (EXACT, letter-perfect):
- Main text: "{main_text, default: "Stay Hungry, Stay Foolish"}" — large, {font_style, default: "light-gold elegant serif"} font, centered, with generous letter-spacing
- Attribution: "{attribution, default: "— Steve Jobs"}" — smaller text below, same font family

Visual design: {design, default: "a large, subtle decorative quotation mark watermark behind the text. If a portrait photo is included, place it on the left third with a slight gradient transition effect, text occupying the right two-thirds. If no photo, center the text on the card"}.

Background: {background, default: "rich warm brown gradient, slightly textured like premium paper"}.

Typography: sharp, perfectly rendered text with no misspellings, no text warping, no artifacts. Each character must be crisp and legible.

Color palette: {colors, default: "warm browns and golds — cohesive, sophisticated, and readable"}.

Composition: clean, balanced layout with professional graphic design spacing. Aspect ratio {ratio, default: "1:1"}.

The overall style is a premium social media graphic that looks professionally designed, ready for immediate posting. No watermark.
```

**Quality Checklist:**
- [ ] All text correctly spelled and rendered
- [ ] Professional graphic design layout
- [ ] Color palette cohesive and appealing
- [ ] Platform-appropriate aspect ratio

---

### E02 — Poster Design

**Keywords:** poster, flyer, 海报, banner, event poster, 宣传海报
**Input:** Event/content details (text)
**Aspect Ratio:** 3:4

**Prompt Pattern:**

```
Create a {style, default: "high-contrast, bold graphic design"} poster for {event, default: "a creative event"}.

Text to render (EXACT — render every character letter-perfect, no misspellings):
Line 1 (top, hero text): "{title}" — {title_style, default: "extra bold sans-serif, all caps, white, largest text on poster"}
Line 2 (middle): "{subtitle}" — {subtitle_style, default: "medium weight, sentence case, 60% size of title"}
Line 3 (details): "{details}" — {detail_style, default: "light weight, smaller, arranged in a clean row with bullet separators"}

Visual design:
Color palette: {colors, default: "bold primary colors — deep navy background, bright coral accents, white text"}.
Decorative elements: {elements, default: "abstract geometric shapes (circles, triangles) in accent colors, arranged asymmetrically to guide the eye from title to details"}.
Composition hierarchy: title draws the eye first (largest, brightest), subtitle second, details third.

Layout: clean, modern poster with generous whitespace and clear visual hierarchy. No clutter. Text must be perfectly legible against the background.

Aspect ratio {ratio, default: "3:4 portrait"}.

The overall style is a professional, print-ready event poster with striking typography and clean, contemporary graphic design. No spelling errors, no text warping.
```

**Quality Checklist:**
- [ ] All text present, correctly spelled, readable
- [ ] Clear visual hierarchy
- [ ] Professional graphic design quality
- [ ] Print-ready resolution

---

### E03 — Storyboard / Comic Strip

**Keywords:** storyboard, comic strip, 分镜图, 漫画条, 动画分镜, panels
**Input:** Scene description + optional photo
**Aspect Ratio:** 16:9

**Prompt Pattern:**

```
Create a {panels, default: "4-panel"} horizontal comic strip / storyboard depicting: {story, default: "a day in the life of a character"}.

Layout: {panels, default: "4"} evenly-spaced panels arranged left-to-right in a single horizontal row, each panel clearly bordered with clean black lines and white gutters between them.

Panel descriptions:
Panel 1: {panel1, default: "Character waking up, alarm clock ringing, messy hair, morning light through window"}
Panel 2: {panel2, default: "Character drinking coffee, looking at phone, kitchen setting, warm lighting"}
Panel 3: {panel3, default: "Character at work/desk, focused expression, computer screen glow"}
Panel 4: {panel4, default: "Character relaxing at sunset, happy and satisfied, beautiful sky colors"}

Art style: {art_style, default: "clean, modern comic illustration with bold outlines, flat colors with cel-shading, expressive character design. Consistent character appearance across all panels"}.

Character consistency: the main character must look identical across all panels — same face, same body type, same hair. Only expression, pose, outfit, and environment change.

Composition: widescreen storyboard format. Aspect ratio 16:9.

The overall style is a professional storyboard/comic strip with clear narrative progression and consistent character design. Minimal text — story told through visuals.
```

**Quality Checklist:**
- [ ] All panels present and properly laid out
- [ ] Character consistent across panels
- [ ] Clear narrative progression
- [ ] Clean borders and spacing

---

### E04 — Handwritten Poster

**Keywords:** handwritten poster, 手抄报, bulletin, class poster, notice board
**Input:** Topic/content text
**Aspect Ratio:** 3:4

**Prompt Pattern:**

```
Create a beautiful hand-drawn educational poster / bulletin board on the topic of "{topic, default: "Environmental Protection"}".

Layout: a large poster divided into visually distinct sections with hand-drawn borders and decorative elements. Title at the top in {title_style, default: "large, colorful hand-lettered text with decorative doodles around it"}.

Content sections (3-4 sections):
{sections, default:
"Section 1: 'Key Facts' — 3-4 bullet points with small illustrative icons
Section 2: 'What We Can Do' — action items with checkboxes and cute doodles
Section 3: 'Did You Know?' — fun fact with a hand-drawn illustration
Section 4: 'Our Pledge' — a framed commitment statement"}

Style: charming hand-drawn aesthetic as if created with {media, default: "colored markers, crayons, and colored pencils on white poster board"}. Include:
- Hand-lettered text in various sizes and colors (not computer fonts)
- Cute doodles and illustrations in the margins
- Decorative borders made of vines, stars, or themed shapes
- Small stickers, tape, or pinned elements for added charm

Colors: bright, cheerful palette with {palette, default: "primary and secondary colors — red, blue, green, yellow, orange, purple"}.

Composition: portrait orientation with balanced section layout. Aspect ratio 3:4.

The overall style is a heartwarming, creative class poster that looks genuinely hand-made by a talented student. All text must be legible.
```

**Quality Checklist:**
- [ ] Authentic hand-drawn appearance
- [ ] Text legible and relevant to topic
- [ ] Multiple organized sections
- [ ] Colorful and visually appealing

---

### E05 — Illustration

**Keywords:** illustration, 插画, artwork, digital art, 绘画, drawing
**Input:** Scene/subject description
**Aspect Ratio:** 3:4

**Prompt Pattern:**

```
Create a stunning {style, default: "digital illustration"} depicting: {scene, default: "a magical scene"}.

Subject: {subject, default: "a young adventurer standing at the edge of a floating island, looking out at a sky filled with whales swimming among the clouds"}.

Art style: {art_style, default: "Studio Ghibli-inspired watercolor illustration — soft, dreamy palette with warm golden undertones, delicate linework visible beneath transparent washes, whimsical and fantastical yet grounded in emotional authenticity"}.

Environment details: {environment, default: "lush green grass and wildflowers on the floating island, ancient stone ruins with ivy, clouds at eye level, distant floating islands in the background, a gentle sunset painting the sky in peach and lavender"}.

Lighting: {lighting, default: "golden hour back-lighting creating a warm silhouette effect on the character, god-rays piercing through the clouds, gentle ambient glow from below the clouds"}.

Color palette: {colors, default: "warm golds and peaches for the sky, rich greens for vegetation, soft blues and purples for distance, white and cream for clouds"}.

Mood: {mood, default: "wonder, serenity, and the excitement of discovery"}.

Composition: {composition, default: "character positioned at the left-third, looking right toward the expansive sky, creating a sense of scale and adventure"}. Aspect ratio {ratio, default: "3:4"}.

The overall style is a breathtaking illustration worthy of a children's book cover or concept art gallery. No text, no watermark.
```

**Quality Checklist:**
- [ ] Subject clearly depicted as described
- [ ] Art style consistent and appealing
- [ ] Strong mood and atmosphere
- [ ] Professional illustration quality

---

## Category F: Professional Design (专业设计) — P1

### F01 — E-commerce Main Image

**Keywords:** e-commerce, product, 电商, 头图, product photo, Amazon, shop listing
**Input:** Product photo or description
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Create an ultra-realistic cinematic product photograph for {product, default: "a premium product"}.

Product: {product_details, default: "a transparent glass jar filled with luminous deep golden honey, topped with a satin bronze metallic lid and narrow cream seal strip"}.

Staging: {staging, default: "placed inside a shallow wooden hollow surrounded by tall wild wheat and tiny yellow meadow flowers"}. Surface: {surface, default: "natural wood with visible grain and warm patina"}.

Supporting elements: {props, default: "thin climbing ivy strands lightly touching the jar, one realistic honeybee hovering near the front glass surface, another resting on a wheat stem behind the jar, scattered pollen particles catching the light"}.

Environment: {environment, default: "quiet countryside field during late afternoon, warm sunlight filtering through wheat stalks from behind"}.

Lighting: warm directional backlight creating glowing translucency through the product. Soft halo edges around the jar. Foreground: blurred wheat tips and soft natural bokeh. Background: fading into creamy green and amber tones.

Camera: {camera, default: "90mm macro lens, f/2.2, intimate low-angle perspective"}. Extreme sharpness on product textures, shallow depth of field with everything behind product melting into beautiful bokeh.

Aspect ratio {ratio, default: "1:1"}.

The overall style is a cinematic luxury advertising product shot with premium organic campaign aesthetics. No text, no watermark.
```

**Quality Checklist:**
- [ ] Product is the clear hero of the image
- [ ] Professional commercial lighting
- [ ] Sharp product, beautiful bokeh background
- [ ] Premium, aspirational mood

---

### F02 — Sticker Set Design

**Keywords:** sticker set, art design, 贴纸集, 美术设计, sticker sheet, character stickers
**Input:** User photo or character description
**Aspect Ratio:** 4:5

**Prompt Pattern:**

```
Create a premium {style, default: "Pixar-style 3D character"} sticker set that is clearly recognizable as the same person/character.

Identity source: {identity, default: "use the uploaded image as the facial reference"}.

Output: 3x3 grid layout (9 stickers total). Final aspect ratio 4:5, ultra-high resolution (8K). Clean cream background. Each sticker separated with clear spacing. Subtle drop shadow under each sticker for depth.

Character identity (CRITICAL): preserve exact facial structure, hairstyle, grooming details, and unique features. Maintain high likeness accuracy. Do NOT over-beautify or alter identity.

Style: {render_style, default: "Pixar-style 3D animation — glossy, high-end rendering, soft global illumination, smooth shading, high-detail facial textures"}.

Framing: all stickers head-and-shoulders (portrait close-up) only. Focus tightly on face and upper shoulders.

Each sticker has a different outfit (no repetition) — modern, casual, visually appealing.

9 expressions:
1. Happy smile  2. Laughing  3. Cool (sunglasses)
4. Angry/serious  5. Surprised  6. Thinking
7. Wink  8. Love (heart gesture)  9. Thumbs up

Sticker design: bold clean outline, slightly exaggerated proportions, strong emphasis on facial expressions. Smooth rounded bottom cutout on each sticker.

The overall style is a premium collectible sticker pack with consistent character identity and expressive range. No text labels.
```

**Quality Checklist:**
- [ ] 9 stickers in 3x3 grid
- [ ] Consistent identity across all
- [ ] Distinct expressions per sticker
- [ ] Professional sticker design quality

---

### F03 — Interior Design

**Keywords:** interior, room design, 家装, 室内设计, 装修, redesign room, home decor
**Input:** Room photo + style description
**Aspect Ratio:** 16:9

**Prompt Pattern:**

```
Redesign the room in the uploaded photo in a {style, default: "modern Scandinavian minimalist"} style while preserving the room's exact layout, dimensions, and architectural features (windows, doors, ceiling height).

Design specifications:
- Furniture: {furniture, default: "clean-lined oak furniture — a low-profile platform sofa in natural linen, a minimalist round coffee table, a slim bookshelf with curated objects"}
- Color palette: {colors, default: "warm whites and light grays for walls, natural wood tones for furniture, soft sage green and dusty rose accents in textiles"}
- Flooring: {floor, default: "light oak hardwood in a herringbone pattern with a large hand-woven wool area rug in cream"}
- Textiles: {textiles, default: "linen curtains in off-white, chunky knit throw blanket, assorted cushions in complementary muted tones"}
- Lighting: {lighting, default: "a sculptural pendant light over the seating area, warm-toned (2700K) ambient lighting, natural daylight from existing windows enhanced"}
- Plants & decor: {decor, default: "2-3 potted plants (fiddle leaf fig, trailing pothos), ceramic vases, a few curated books, minimal wall art"}

Rendering: photorealistic architectural visualization quality. Natural daylight rendering with accurate shadow casting. Materials have realistic textures — visible wood grain, fabric weave, ceramic glaze.

Camera: {camera, default: "wide-angle interior photography, 16mm equivalent, room-level perspective"}. Aspect ratio 16:9.

The overall style is a magazine-quality interior design visualization ready for a client presentation. No text, no watermark.
```

**Quality Checklist:**
- [ ] Room layout preserved from original
- [ ] Target design style accurately represented
- [ ] Photorealistic material rendering
- [ ] Professional interior photography quality

---

### F04 — Logo Design

**Keywords:** logo, brand, 标志, Logo设计, brand identity, icon design
**Input:** Brand name + style description
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Design a professional logo for {brand, default: "a brand"} named "{brand_name, default: "BRAND"}".

Logo type: {type, default: "combination mark (icon + wordmark)"}.

Icon: {icon_description, default: "a minimalist, geometric representation of a mountain peak with a rising sun, constructed from clean geometric shapes — triangle for the mountain, circle for the sun, with negative space creating the horizon line"}.

Wordmark: the text "{brand_name}" rendered in {font_style, default: "a clean, modern sans-serif typeface — medium weight, generous letter-spacing, all caps"}. Spell the name EXACTLY as provided — no variations, no misspellings.

Color palette: {colors, default: "primary: deep navy blue (#1B365D). Accent: warm gold (#D4A855). The icon uses both colors, the wordmark is in the primary color"}.

Style: {style, default: "modern, clean, timeless — could work equally well at 16px favicon size and on a billboard. No gradients, no shadows, no 3D effects — flat, vector-clean design"}.

Layout: icon centered above the wordmark, balanced vertical stacking. Generous padding around the logo. Background: solid white.

Composition: centered, square format. Aspect ratio 1:1.

The overall style is a premium, professionally designed brand logo that communicates {values, default: "trust, innovation, and quality"}. Must work in single-color reproduction.
```

**Quality Checklist:**
- [ ] Brand name spelled correctly
- [ ] Clean, professional design
- [ ] Scalable (looks good small and large)
- [ ] Cohesive color palette

---

### F05 — Merchandise / Keychain Design

**Keywords:** merchandise, keychain, 钥匙扣, figure, 手办, 实物设计, figurine
**Input:** User photo or character description
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Design a {type, default: "1/7 scale collectible figure"} based on {character, default: "the uploaded photo"}.

Figure design: {design, default: "a premium chibi-style collectible figure with a slightly oversized head, expressive face preserving the subject's key features, dynamic action pose"}. Material appearance: {material, default: "high-quality PVC figure with smooth matte finish, subtle metallic paint accents, clean paint application typical of premium Japanese figure brands"}.

Pose: {pose, default: "dynamic stance — one foot forward, arm outstretched with an energy effect, slight twist at the waist for visual dynamism"}.

Outfit: {outfit, default: "a stylized version of the subject's clothing with added fantasy elements — detailed texture work, miniature accessories, flowing cloth elements frozen in dynamic motion"}.

Base: {base, default: "a sleek circular black acrylic display base with the character's name engraved in small silver text"}.

Presentation: product photography style — the figure is centered on a clean {background, default: "gradient gray"} backdrop. Lighting: professional product photography setup — soft, even illumination highlighting the figure's paint job and sculpt details, subtle rim light for edge definition.

Camera: slightly low angle looking up at the figure for a heroic perspective. Aspect ratio 1:1.

The overall style is a premium collectible figure product photo ready for pre-order announcement. No text overlay, no watermark.
```

**Quality Checklist:**
- [ ] Character identity recognizable
- [ ] Authentic collectible figure appearance
- [ ] Professional product photography
- [ ] Dynamic, appealing pose

---

### F06 — Coloring Book Page

**Keywords:** coloring, coloring book, 涂色, 涂色线稿, line art, coloring page
**Input:** Subject description or photo
**Aspect Ratio:** 3:4

**Prompt Pattern:**

```
Create a detailed coloring book page featuring {subject, default: "an enchanted garden scene with a fairy sitting on a mushroom, surrounded by flowers, butterflies, and a small cottage in the background"}.

Style: professional coloring book illustration — clean, crisp black line art on a pure white background. Lines are {line_weight, default: "medium weight (varying between 1-3pt), with thicker outlines for main subjects and thinner lines for details and textures"}.

Details: {details, default: "the scene is rich with fillable areas of varying sizes — large simple areas for young colorists and intricate pattern-filled sections (mandalas, zentangle-inspired fills, decorative borders) for advanced colorists. Flowers have detailed petal structures. Leaves show vein patterns. Background includes decorative swirls and dot patterns"}.

Composition: {composition, default: "the main subject is centered and prominent. Supporting elements frame the scene without overcrowding. Generous border around the edges"}.

Technical requirements:
- Pure black lines on pure white background — NO gray tones, NO gradients, NO fills
- All areas are fully enclosed (no broken outlines) for clean coloring
- Sufficient detail to be engaging but not overwhelming
- Lines are clean and precise, not sketchy

Aspect ratio 3:4 portrait.

The overall style is a premium adult/family coloring book page with intricate detail and satisfying patterns to color. No pre-filled colors, no gray shading.
```

**Quality Checklist:**
- [ ] Clean black lines on white only
- [ ] All areas properly enclosed
- [ ] Mix of simple and detailed areas
- [ ] Engaging subject and composition

---

### A15 — Oil Painting / Classical Art

**Keywords:** oil painting, 油画, classical, 古典, impressionist, 印象派, renaissance
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 3:4

**Prompt Pattern:**

```
Convert the uploaded photo into a classical oil painting on stretched linen canvas. Preserve the subject's complete facial identity — exact bone structure, features, and expression — while rendering the entire portrait with rich, layered oil paint technique.

Technique: {technique, default: "old-master classical realism in the manner of Rembrandt or Vermeer"}. Build the painting from a warm umber ground layer, with transparent glazing for luminous skin tones, opaque impasto highlights on the forehead, nose bridge, and lower lip, and soft lost-and-found edges where the figure dissolves into the background. Visible palette-knife work on clothing textures. Color palette: rich earth tones — raw sienna, burnt umber, cadmium yellow deep, alizarin crimson — with strategic touches of vermilion and ultramarine blue.

Subject wears {outfit, default: "period-appropriate attire — a rich velvet garment with intricate fabric folds catching the light"}.

Background: {background, default: "dark, atmospheric chiaroscuro — a deep umber-to-black gradient with subtle warm undertones, reminiscent of a Dutch Golden Age interior"}.

Lighting: dramatic Rembrandt lighting — strong warm key light from upper-left illuminating three-quarters of the face, deep shadow on the far side with a subtle reflected warm bounce, creating the classic triangle of light on the shadowed cheek.

Composition: three-quarter view, head-and-shoulders. Aspect ratio 3:4. Include subtle canvas weave texture and minor craquelure at edges for authenticity.

The overall style is a museum-worthy oil portrait combining photographic identity accuracy with masterful classical painting technique. No modern elements, no watermark.
```

**Quality Checklist:**
- [ ] Facial identity clearly preserved
- [ ] Authentic oil painting texture (visible brushwork, impasto)
- [ ] Rich, warm color palette with dramatic lighting
- [ ] Canvas texture visible

---

### A16 — Pixel Art

**Keywords:** pixel art, 像素, 8-bit, retro game, 像素风, pixel, 16-bit
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Transform the uploaded photo into a charming retro pixel art portrait. Preserve the subject's key facial features, hairstyle, and distinguishing characteristics while rendering entirely in a {style, default: "16-bit era pixel art style, reminiscent of classic SNES/Genesis RPG character portraits"}.

Pixel specifications: limited color palette of {colors, default: "32 carefully selected colors"}, each pixel clearly defined as a discrete square block. No anti-aliasing, no gradients — all shading achieved through dithering patterns and strategic color placement. Each pixel must be intentional and contribute to the overall likeness.

The subject is depicted as a {character_type, default: "RPG hero character — expressive large eyes with pixel-perfect highlight dots, simplified but recognizable facial features, stylized hair rendered in distinct pixel clusters"}.

Outfit: {outfit, default: "fantasy RPG armor or adventurer clothing in vibrant pixel colors"}.

Background: {background, default: "a simple, clean solid color or a minimal pixel-art scene — a castle wall, starry night, or grassy field — all in matching pixel resolution"}.

Frame the portrait as a {frame, default: "classic RPG dialogue box portrait — square format with a thin pixel border"}.

Composition: centered head-and-shoulders pixel portrait. Aspect ratio 1:1.

The overall style is a nostalgic, professionally crafted pixel art portrait worthy of a beloved retro video game's character select screen. No text, no watermark.
```

**Quality Checklist:**
- [ ] Recognizable identity from original photo
- [ ] Authentic pixel art style (visible individual pixels)
- [ ] Limited color palette, no gradients
- [ ] Nostalgic retro game aesthetic

---

### A17 — Flat / Vector Illustration

**Keywords:** flat illustration, vector, 平面插画, 扁平风, flat design, minimalist illustration
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Transform the uploaded photo into a clean, modern flat vector illustration portrait. Preserve the subject's facial identity — hairstyle, face shape, and key distinguishing features — while applying bold geometric simplification.

Style: {style, default: "contemporary flat design illustration — crisp geometric shapes, zero gradients, flat solid color fills with hard edges, minimal detail that still captures personality. Influenced by modern editorial illustration and tech company avatar art"}.

Colors: {palette, default: "a curated palette of 5-7 harmonious flat colors — warm skin tones, bold accent colors for clothing, and a complementary background"} with zero texture, zero grain. Each area is a clean, unbroken color block.

Face: simplified to essential shapes — geometric eye forms with flat color fills, a simple nose shape, clean mouth line. Despite simplification, the overall face shape, hairstyle silhouette, and proportions must clearly match the original person.

Hair: rendered as {hair_style, default: "bold, flowing shapes with clean silhouette edges — no individual strands, just elegant mass forms"}.

Outfit: {outfit, default: "simplified version of the original clothing in bold flat colors"}.

Background: {background, default: "solid pastel or complementary color — single flat tone"}.

Composition: centered portrait from shoulders up. Clean breathing space around the subject. Aspect ratio 1:1.

The overall style is a premium flat vector illustration portrait suitable for a modern tech profile avatar or editorial magazine spot illustration. No outlines, no texture, no watermark.
```

**Quality Checklist:**
- [ ] Identity recognizable through simplified forms
- [ ] True flat/vector aesthetic (no gradients, no textures)
- [ ] Clean geometric shapes and edges
- [ ] Harmonious limited color palette

---

### A18 — Anime / 二次元

**Keywords:** anime, 二次元, 动漫, Japanese animation, light novel, アニメ, otaku
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 3:4

**Prompt Pattern:**

```
Transform the uploaded photo into a beautiful anime/二次元 character portrait in the style of {style, default: "a modern high-budget anime series like Violet Evergarden or Makoto Shinkai's films"}. Preserve the subject's facial identity — face shape, eye characteristics, hairstyle, and distinguishing features — while applying authentic Japanese animation aesthetics.

Character rendering: large, detailed anime eyes with {eye_detail, default: "multiple layers of color, light reflections, and subtle gradient irises — deep, expressive, with small star-shaped catch-lights"}. Skin: smooth, luminous, with anime-style shading — hard shadow edges on the neck and under the hair, soft blush on cheeks. Hair: {hair, default: "flowing, dynamic strands with rich color depth, individual highlight streaks in a lighter tone, and wispy flyaway hairs at the edges"}.

Expression: {expression, default: "gentle smile with warm, inviting eyes — the kind of expression that makes viewers feel connected to the character"}.

Outfit: {outfit, default: "stylish modern Japanese fashion — a cozy oversized knit sweater in soft pastel colors, or a fashionable school uniform blazer"}.

Background: {background, default: "a dreamy golden hour scene — cherry blossom petals drifting lazily through warm sunlight, with a soft bokeh of city lights or a scenic sky in the distance"}. Lens flares and floating light particles add magical atmosphere.

Lighting: {lighting, default: "warm golden back-lighting creating a glowing halo around the hair, soft fill light on the face, dramatic rim light separating subject from background — classic anime 'magic hour' look"}.

Composition: three-quarter portrait, slightly upward angle. Aspect ratio 3:4.

The overall style is a breathtaking anime character portrait worthy of a light novel cover illustration or key visual. No text, no watermark.
```

**Quality Checklist:**
- [ ] Facial identity recognizable from original
- [ ] Authentic high-quality anime aesthetic
- [ ] Beautiful, detailed eyes with reflections
- [ ] Atmospheric lighting and background

---

### A19 — Wool Felt / Needle Felt

**Keywords:** wool felt, needle felt, 羊毛毡, felt craft, felted, plush, handmade
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Transform the uploaded photo into an adorable needle-felted wool character. Preserve the subject's key facial features, hairstyle, and identity while rendering them as if hand-crafted from soft wool roving using the needle-felting technique.

Material: the entire character is made from {wool_type, default: "premium merino wool roving — soft, fluffy fibers with visible fine wisps and fuzzy edges"}. Surface shows the characteristic slightly fuzzy, uneven texture of hand-poked needle felting — tiny fiber ends poking out, gentle dimples from repeated needle pokes, and a soft matte finish.

Face: round and simplified, with {face_details, default: "tiny black bead eyes with a sparkle reflection, a small pink needle-felted nose, and rosy felt circles for cheeks. Despite simplification, the overall face shape and expression match the original"}.

Hair: sculpted from {hair_color, default: "matching-color"} wool in soft, thick tufts — not individual strands but gentle wool formations that capture the original hairstyle's silhouette and character.

Outfit: {outfit, default: "a miniature version of the original clothing, crafted from tiny felt pieces with visible hand-stitching details — a small knitted scarf or wool sweater"}.

Scene: {scene, default: "placed on a rustic wooden surface with a few tiny felted flowers and miniature props around it, warm natural daylight from a window"}.

Photography: macro product photography style — sharp focus on the felt character, shallow depth of field for a dreamy background, warm natural lighting emphasizing the wool texture.

Composition: centered character. Aspect ratio 1:1.

The overall style is a premium handmade needle-felted wool art portrait with heartwarming craft authenticity and tiny, adorable charm. No text, no watermark.
```

**Quality Checklist:**
- [ ] Identity recognizable in simplified form
- [ ] Authentic wool felt texture (fuzzy fibers, dimples)
- [ ] Warm, handcrafted aesthetic
- [ ] Adorable and appealing

---

### A20 — Colored Pencil Drawing

**Keywords:** colored pencil, 彩铅, 彩铅画, crayon, Prismacolor, colored drawing
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Transform the uploaded photo into a stunning colored pencil portrait on heavyweight drawing paper. Preserve the subject's complete facial identity with precise detail while showcasing masterful colored pencil technique.

Medium: {medium, default: "premium wax-based colored pencils (Prismacolor or Faber-Castell Polychromos) on smooth Bristol board"}. Technique: multiple layers of colored pencil built up from light to dark — visible directional strokes following the contours of the face, burnished smooth areas on skin highlights, and looser hatching in shadow areas.

Skin: built from layered warm tones — {skin_tones, default: "peach, light carmine, raw sienna, and touches of light cerulean for cool shadows. The layered strokes create a luminous, dimensional quality"}.

Hair: {hair, default: "rendered with flowing directional strokes — individual strand groupings visible, building from dark base colors to bright highlights, with the paper tooth creating subtle texture breaks"}.

Eyes: the most detailed area — precise iris patterns with multiple color layers, bright white paper showing through for catch-lights, delicate lash detail.

Outfit: {outfit, default: "the original clothing, rendered with appropriate colored pencil strokes and fabric texture"}.

Background: {background, default: "soft, loosely rendered color washes that gradually fade to bare paper at the edges, creating an elegant vignette"}.

Paper texture: visible throughout — the tooth of the paper shows through the colored pencil, creating the characteristic grainy texture that defines the medium.

Composition: head-and-shoulders portrait. Aspect ratio 1:1.

The overall style is a gallery-quality colored pencil portrait demonstrating exceptional technique and faithful identity reproduction. No digital effects, no watermark.
```

**Quality Checklist:**
- [ ] Strong facial likeness
- [ ] Authentic colored pencil strokes visible
- [ ] Paper texture showing through
- [ ] Rich, layered color work

---

### A21 — Pop Art

**Keywords:** pop art, 波普, Warhol, 波普艺术, Lichtenstein, 名画风, art movement
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Transform the uploaded photo into a bold Pop Art portrait in the style of {artist, default: "Andy Warhol's iconic silkscreen prints"}. Preserve the subject's facial identity — recognizable features, hairstyle, and expression — while applying dramatic Pop Art visual treatment.

Style: {style, default: "Warhol-style screen print — the photograph is reduced to high-contrast flat areas of bold, saturated color. The image is divided into a 2x2 grid of four identical portraits, each rendered in a different striking color scheme"}.

Color schemes (one per quadrant):
{colors, default:
"Top-left: hot pink face, electric blue hair, canary yellow background
Top-right: lime green face, orange hair, magenta background
Bottom-left: bright cyan face, red hair, purple background
Bottom-right: golden yellow face, teal hair, coral background"}

Technique: screen-printed aesthetic — flat color fills with slightly offset registration (subtle misalignment between color layers for authenticity). Bold black outlines defining major facial features. Halftone dot pattern visible in mid-tone areas. High contrast with no subtle gradients — everything reduced to 3-4 tonal values per color channel.

Each quadrant is identical in composition — same head-and-shoulders portrait, same expression — only the color palette changes.

Composition: 2x2 grid, square format. Aspect ratio 1:1.

The overall style is an authentic Warhol-inspired Pop Art silkscreen that transforms the subject into a cultural icon. No text, no watermark.
```

**Quality Checklist:**
- [ ] Identity recognizable across all quadrants
- [ ] Authentic Pop Art / Warhol aesthetic
- [ ] Bold, contrasting color schemes
- [ ] Screen-print texture (halftone, registration offset)

---

### A22 — Miniature / Diorama

**Keywords:** miniature, diorama, 微缩景观, tilt-shift, small world, tiny world, 微缩
**Input:** User photo (portrait or scene)
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Transform the uploaded photo into a hyper-detailed miniature diorama scene. The subject from the photo becomes a {scale, default: "1/6 scale collectible figurine"} placed inside a meticulously crafted tabletop miniature world.

Figurine: the subject is rendered as a highly detailed miniature figure — {figure_style, default: "realistic hand-painted figure with visible brushstroke texture on clothing, glossy eye details, and a stable base"}. Preserve the subject's facial features, hairstyle, and outfit at miniature scale.

Diorama environment: {environment, default: "a cozy miniature coffee shop interior — tiny tables with real-looking wooden grain, miniature coffee cups with glossy liquid surface, tiny potted plants with individually sculpted leaves, warm Edison bulb string lights (actual tiny LEDs), checkered tile floor"}.

Craft materials visible: {materials, default: "balsa wood structures, hand-painted plaster walls, real moss for miniature greenery, tiny paper posters on walls, sculpted polymer clay accessories"}.

Photography: extreme macro photography style — {camera, default: "shot with a macro lens at f/4, creating natural miniature depth of field where the foreground and background blur beautifully while the subject stays sharp. Warm, directional lighting from a small LED panel simulating golden hour sunlight through a tiny window"}.

Scale indicators: include elements that sell the miniature scale — {scale_cues, default: "a real coin or pencil tip visible at the edge of frame for scale reference, slightly visible table surface the diorama sits on"}.

Composition: eye-level view into the diorama. Aspect ratio 1:1.

The overall style is a professionally photographed miniature diorama that sparks wonder at its incredible tiny-world detail. No text, no watermark.
```

**Quality Checklist:**
- [ ] Subject recognizable as miniature figurine
- [ ] Convincing miniature scale and materials
- [ ] Beautiful macro-style depth of field
- [ ] Detailed, charming diorama environment

---

### A23 — Children's Drawing

**Keywords:** children drawing, kid art, 儿童绘画, 儿童画, crayon drawing, child style
**Input:** User photo (portrait or scene)
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Transform the uploaded photo into an endearing children's drawing style artwork, as if drawn by a {age, default: "creative and talented 6-year-old child"}.

Drawing style: {medium, default: "thick wax crayons and colorful markers on white construction paper"}. The drawing captures the subject's key identity features — hairstyle, clothing colors, and distinctive characteristics — through the charming lens of a child's artistic interpretation.

Character: the subject is drawn with {proportions, default: "a large round head (roughly 1/3 of total body), simple circle eyes with dot pupils, a wide U-shaped smile, stick-like arms and legs with mitten hands, and a triangular or rectangular body for the torso"}. Despite the childlike simplification, the hair color, style, and clothing should reference the original photo.

Colors: {colors, default: "bold, fully saturated crayon colors — pressing hard for maximum vibrancy. Slightly going outside the lines in places. Color choices are enthusiastic and sometimes unexpected (green skin tones, purple hair are OK)"}.

Scene: {scene, default: "the character standing on a strip of green grass at the bottom, with a bright yellow sun with radiating lines in the upper corner, a few V-shaped birds in the blue sky, and a simple house or tree in the background"}.

Details that sell authenticity:
- Uneven line pressure (thicker in some spots, thinner in others)
- Slight wobbliness to all lines
- Paper texture visible beneath the crayon
- A few spots where colors overlap messily
- {extra, default: "The child's 'signature' — a few backwards letters or a small heart in one corner"}

Composition: centered character with surrounding scene elements. Aspect ratio 1:1.

The overall style is a genuine, heartwarming children's artwork that makes viewers smile at its innocent charm and creative energy. No digital perfection — embrace the beautiful imperfection.
```

**Quality Checklist:**
- [ ] Subject features referenced (hair, clothing)
- [ ] Authentic children's drawing style (not adult mimicking child)
- [ ] Crayon/marker texture visible
- [ ] Charming and heartwarming

---

## Category B: Portrait (写真/人像) — P0 (continued)

### B06 — Film / Cinematic Portrait

**Keywords:** film photography, cinematic, 电影写真, movie still, film grain, 胶片, cinematic portrait
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 3:4

**Prompt Pattern:**

```
Transform the uploaded photo into a cinematic film portrait that looks like a still frame from a {film_style, default: "Wong Kar-wai arthouse film — moody, intimate, and dripping with nostalgia"}. Preserve the subject's complete facial identity, expression, and natural features.

Film stock: {film, default: "Kodak Vision3 500T tungsten motion picture film — distinctive warm-to-cool color crossover, pronounced but elegant grain structure, slightly lifted blacks with a subtle cyan cast in the shadows, warm golden skin tones"}.

Mood: {mood, default: "melancholic beauty — the subject gazes slightly off-camera with a contemplative expression, as if lost in a private memory"}.

Environment: {environment, default: "a dimly lit urban setting at night — neon signs reflecting off rain-wet surfaces, the warm glow of a nearby streetlamp mixing with cool blue ambient light. The subject is positioned near a window or doorway, creating natural framing"}.

Lighting: {lighting, default: "motivated practical lighting from available sources — a neon sign casting a warm red-orange glow on one side of the face, cool blue ambient from the night sky on the other. No fill light. Let the shadows be rich and mysterious. A slight lens flare from a distant light source"}.

Camera: {camera, default: "35mm anamorphic lens (Panavision C-series), wide open at T1.4. The shallow depth of field creates beautiful oval bokeh of city lights behind the subject. Slight anamorphic lens breathing and horizontal flare streaks"}.

Aspect ratio {ratio, default: "3:4"}. Frame the subject with cinematic negative space — they occupy roughly one-third of the frame, with the atmospheric environment filling the rest.

The overall style is a hauntingly beautiful cinematic portrait that tells a story in a single frame, with the emotional depth of festival-circuit arthouse cinema. No text, no watermark.
```

**Quality Checklist:**
- [ ] Facial identity preserved
- [ ] Authentic film grain and color science
- [ ] Cinematic composition with negative space
- [ ] Atmospheric mood and lighting

---

### B07 — Dreamy / Hazy Portrait

**Keywords:** dreamy, hazy, soft focus, 朦胧, 朦胧肖像, ethereal, gauze, romantic
**Input:** User photo (selfie / portrait)
**Aspect Ratio:** 3:4

**Prompt Pattern:**

```
Transform the uploaded photo into an ethereal, dreamlike portrait with a soft, hazy quality. Preserve the subject's facial identity while wrapping them in a romantic, otherworldly atmosphere.

Technique: {technique, default: "shot through vintage soft-focus glass or a light gauze diffusion filter — the entire image has a luminous, bloom-like glow where highlights spread softly into surrounding areas"}.

The subject's face is {face_quality, default: "gently softened but still clearly identifiable — like seeing someone through a thin layer of morning mist. Eyes remain the sharpest element, drawing the viewer in. Skin has a luminous, almost translucent quality with a warm inner glow"}.

Hair: {hair, default: "catches and scatters the light — individual strands create a glowing halo effect around the head, with warm backlighting turning flyaway hairs into golden threads"}.

Environment: {environment, default: "drenched in soft, diffused golden light — as if the subject is standing in a sunlit meadow at the most magical moment of golden hour. Light particles and tiny dust motes float in the warm air, catching the sunlight"}.

Lighting: {lighting, default: "intense warm backlight creating a full-body glow and light wrap. Soft fill from a reflector or bounce light keeps the face luminous without harsh shadows. The light has a dreamy, almost liquid quality — it wraps around the subject rather than hitting them directly"}.

Color palette: {colors, default: "warm golden tones dominate — honey, amber, soft peach. Shadows are lifted to a warm brown. No pure blacks anywhere — everything bathed in light"}.

Camera: {camera, default: "vintage 85mm lens (Helios 44-2 or similar) wide open at f/1.5 — distinctive swirly bokeh in the background, natural optical imperfections adding to the dreamy quality"}.

Composition: intimate head-and-shoulders portrait. Aspect ratio 3:4.

The overall style is an impossibly romantic and ethereal portrait that looks like a beautiful memory or a scene from a dream. No text, no watermark.
```

**Quality Checklist:**
- [ ] Identity still recognizable through soft effect
- [ ] Authentic dreamy/hazy quality (not just blur)
- [ ] Luminous, warm glow throughout
- [ ] Romantic, ethereal atmosphere

---

## Category C: Pets & Babies (萌宠/宝宝) — P0 (continued)

### C04 — Pet Costume Play / Mugshot

**Keywords:** pet costume, 宠物入狱, pet mugshot, 萌宠打工, pet dress-up, 宠物变装, pet job
**Input:** User pet photo
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Transform the uploaded pet photo into a hilarious {scenario, default: "police mugshot"} scene. Preserve the pet's exact breed, fur color/pattern, facial features, and expression while placing them in the comedic scenario.

Scenario options (pick one):
{scene_details, default: "MUGSHOT — The pet stands facing the camera in front of a height-measurement wall chart. They hold a booking placard/nameplate with '{pet_name, default: THE SUSPECT}' and a case number. The pet has a perfectly guilty expression — slightly shifty eyes, ears back. They wear an orange prison jumpsuit collar. The mugshot board behind shows measurements in both cm and inches. Harsh overhead fluorescent lighting casts unflattering shadows, like a real police station photograph"}.

Alternative scenarios:
- "CORPORATE JOB" — pet in a business suit at a tiny desk with a laptop, coffee mug, and stack of papers. Nameplate reads "CEO"
- "DOCTOR" — pet in a white lab coat with a stethoscope, examining a chart
- "CHEF" — pet in a chef's hat and apron, stirring a tiny pot in a kitchen
- "TEACHER" — pet wearing glasses, standing at a small chalkboard

The pet retains their natural animal proportions — they are NOT humanoid. The costume and props are humorously fitted onto the actual animal body. The comedy comes from the contrast between the serious scenario and the adorable animal.

Style: {style, default: "photorealistic with comedic staging — the scenario elements (costume, props, environment) are rendered with realistic detail, making the absurd situation even funnier"}.

Composition: centered, front-facing. Aspect ratio 1:1.

The overall style is a viral-worthy comedic pet photo that makes everyone laugh while showcasing the pet's natural charm and personality. No text except for in-scene props (nameplate, signs).
```

**Quality Checklist:**
- [ ] Pet identity preserved (breed, colors, features)
- [ ] Comedic scenario clearly staged
- [ ] Costume/props realistically rendered on animal
- [ ] Funny and shareable result

---

## Category E: Social Media & Creative (自媒体/创意) — P1 (continued)

### E06 — YouTube Thumbnail

**Keywords:** YouTube thumbnail, thumbnail, 缩略图, video cover, 封面, clickbait
**Input:** Text description + optional photo
**Aspect Ratio:** 16:9

**Prompt Pattern:**

```
Create a high-impact YouTube video thumbnail for a video about: "{topic, default: "an amazing discovery"}".

Layout: {layout, default: "the classic high-performing YouTube thumbnail formula — a subject with an exaggerated expression on the left 60% of the frame, a bold visual element or reveal on the right side, with text overlaid"}.

Subject: {subject, default: "a person with a dramatically exaggerated surprised/excited expression — wide eyes, open mouth, hands on cheeks. The reaction is slightly over-the-top for maximum click appeal"}.

Text to render (EXACT, letter-perfect):
{text, default: "Main text: 'THIS IS INSANE' — ultra-bold white Impact font with thick black outline and neon yellow drop shadow, angled slightly for dynamic feel. Smaller text: 'You Won't Believe...' in clean white"}.

Visual design:
- Background: {background, default: "vibrant gradient or dramatic scene relevant to the video topic — high saturation, high contrast"}
- Key visual element: {visual, default: "the main subject/object of the video, enlarged and highlighted with a glowing edge or arrow pointing to it"}
- Color saturation: cranked to maximum — YouTube thumbnails need to pop at tiny sizes
- Contrast: extreme — everything reads clearly even at 120px width

Technical requirements:
- Resolution: ultra-sharp, every element legible at thumbnail size
- Text: bold, high-contrast with outlines/shadows — readable on any background
- Faces: clear and expressive, immediately readable emotion
- No small details — everything is bold, big, and graphic

Composition: landscape, tightly packed with visual information. Aspect ratio 16:9.

The overall style is a professional, high-CTR YouTube thumbnail optimized for maximum click-through — eye-catching, emotionally engaging, and instantly communicating the video's value. All text must be perfectly spelled.
```

**Quality Checklist:**
- [ ] All text correctly rendered and readable at small size
- [ ] High contrast, vibrant colors
- [ ] Clear, expressive subject
- [ ] Professional YouTube thumbnail composition

---

### E07 — Educational Visual / Infographic

**Keywords:** educational, infographic, 教育, 知识图, diagram, visual learning, 教育类视觉图
**Input:** Topic/content description
**Aspect Ratio:** 3:4

**Prompt Pattern:**

```
Create a visually engaging educational infographic on the topic of: "{topic, default: "How Photosynthesis Works"}".

Layout: {layout, default: "clean, structured infographic with a clear visual hierarchy — title at top, main diagram in the center, supporting facts around the edges"}.

Title: "{title, default: "How Photosynthesis Works"}" — {title_style, default: "bold, large, friendly sans-serif font in dark blue, centered at the top with a subtle colored underline"}.

Main visual: {main_visual, default: "a clear, beautifully illustrated diagram showing the photosynthesis process — a stylized cross-section of a leaf with labeled parts: sunlight arrows coming from above, water arrows from below, CO2 entering, O2 releasing. Each element uses a different color for clarity"}.

Supporting elements:
{elements, default:
"- 3-4 key fact boxes arranged around the main diagram, each with an icon and short text
- Color-coded arrows showing the flow/process
- Small illustrative icons for each concept (sun, water drop, molecule)
- A 'Did You Know?' callout box with an interesting fact"}

Style: {style, default: "modern, clean educational illustration — friendly and approachable, using a consistent color palette of 4-5 colors. Flat design with subtle shadows. Icons are simple and universally understandable. All text is clear, legible, and well-spaced"}.

Color palette: {colors, default: "primary: deep teal blue. Accents: leaf green, sunlight yellow, sky blue, warm orange. Background: clean white or very light gray"}.

Typography: all text must be {text_quality, default: "perfectly legible, well-spaced, using a clean sans-serif font. Headers bold, body text regular weight. No text smaller than readable size"}.

Composition: portrait infographic with generous white space. Aspect ratio 3:4.

The overall style is a premium educational infographic worthy of a classroom wall poster or a high-quality textbook illustration. All text must be spelled correctly and factually accurate.
```

**Quality Checklist:**
- [ ] All text correct and legible
- [ ] Clear visual hierarchy
- [ ] Accurate and educational content
- [ ] Professional infographic design

---

### E08 — Picture Book / Storybook Illustration

**Keywords:** picture book, storybook, 绘本, children's book, 童话, bedtime story
**Input:** Scene/story description
**Aspect Ratio:** 16:9

**Prompt Pattern:**

```
Create a stunning picture book illustration depicting: {scene, default: "a magical scene from a bedtime story"}.

Story moment: {story, default: "a small fox wearing a red scarf discovers a hidden door in an ancient oak tree. The door glows with warm golden light, and tiny fireflies float around the entrance. The fox looks up with wonder and curiosity, one paw reaching toward the door handle"}.

Art style: {style, default: "classic children's book illustration — soft watercolor and gouache on textured paper. Warm, inviting colors with a hand-painted quality. Influenced by the gentle, detailed style of Beatrix Potter meets Studio Ghibli — realistic enough to be immersive, stylized enough to be magical"}.

Environment: {environment, default: "an enchanted forest at twilight — tall, gnarled trees with lush canopies, dappled moonlight filtering through leaves, mushrooms glowing softly on mossy logs, ferns and wildflowers covering the forest floor"}.

Lighting: {lighting, default: "warm golden glow from the tree door serving as the main light source, cool blue-purple twilight ambient from the sky above, tiny points of warm firefly light scattered throughout, creating a magical contrast between warm and cool"}.

Color palette: {colors, default: "rich, warm earth tones for the forest — deep greens, warm browns, mossy golds. Cool blues and purples for the sky and shadows. Warm amber and gold for the magical light source"}.

Character design: {character, default: "the fox is expressive and endearing — large, intelligent eyes, fluffy red-orange fur with white chest marking, wearing a simple but charming red scarf. Small enough in the frame to emphasize the wonder of the environment"}.

Composition: {composition, default: "wide establishing shot with the character positioned in the lower-left third, looking toward the glowing door on the right. The ancient tree dominates the center of the frame. The eye travels from character → door → up into the magical canopy"}. Aspect ratio 16:9.

The overall style is a breathtaking picture book double-page spread that makes both children and adults pause in wonder. No text, no watermark.
```

**Quality Checklist:**
- [ ] Scene clearly tells a story moment
- [ ] Authentic picture book art style
- [ ] Warm, inviting atmosphere
- [ ] Character expressive and appealing

---

## Category F: Professional Design (专业设计) — P1 (continued)

### F07 — Game Asset / Character Design

**Keywords:** game asset, game character, 游戏, 游戏资产, game design, character sheet, concept art
**Input:** Character description or photo
**Aspect Ratio:** 1:1

**Prompt Pattern:**

```
Create a professional game character design sheet for a {genre, default: "fantasy RPG"} character: {character, default: "a powerful mage warrior"}.

Character design: {design, default: "a mystical battle mage — athletic build wrapped in a combination of enchanted armor plates and flowing sorcerer robes. The armor is dark steel with glowing blue runic engravings along the edges. The robe underneath is deep indigo with golden thread patterns that pulse with magical energy. A hooded cloak flows from the shoulders, tattered at the edges from countless battles"}.

Layout: {layout, default: "a professional character concept sheet with multiple views and details:
- CENTER: full-body front-facing pose (T-pose or action stance), largest element
- LEFT: three-quarter view of the same character in a dynamic action pose
- RIGHT: back view showing cloak and weapon details
- CORNERS: close-up detail callouts — weapon, armor ornament, magical effects, face/helmet"}.

Art style: {art_style, default: "AAA game concept art — semi-realistic digital painting with clean rendering, strong silhouette, and readable shapes at any scale. The style balances visual spectacle with practical game design considerations"}.

Color palette: {colors, default: "primary: dark steel gray and deep indigo. Accent: glowing cyan-blue for magical elements. Secondary: gold for ornamental details. The palette is cohesive and tells the character's story"}.

Background: clean {background, default: "neutral gray gradient"} — standard concept art presentation background that doesn't compete with the character design.

Technical: include subtle {annotations, default: "design notes — material callouts, scale reference bar, color palette swatches along the bottom edge"}.

Composition: character sheet layout. Aspect ratio 1:1.

The overall style is a professional AAA game studio character concept sheet ready for a production art bible. No watermark.
```

**Quality Checklist:**
- [ ] Multiple views/angles present
- [ ] Professional concept art quality
- [ ] Clear character design with readable silhouette
- [ ] Detail callouts and annotations

---

### F08 — Product Marketing Design

**Keywords:** marketing, campaign, 营销, 广告, promotion, ad creative, 产品营销
**Input:** Product/service description + text
**Aspect Ratio:** 9:16

**Prompt Pattern:**

```
Create a premium product marketing visual for: {product, default: "a new product launch campaign"}.

Product: {product_details, default: "a sleek wireless noise-canceling headphone in matte black with brushed copper accents, the 'AURA Pro Max'"}.

Layout: {layout, default: "modern vertical social media ad format — product hero shot in the upper two-thirds, marketing copy in the lower third"}.

Product photography: {photography, default: "the headphone floats at a dramatic three-quarter angle against a rich dark gradient background. Volumetric light beams in warm copper tones slice through subtle atmospheric haze behind the product. The product surface catches light perfectly — matte areas absorb softly, copper accents reflect with precision"}.

Text to render (EXACT):
{text, default:
"Headline: 'AURA Pro Max' — large, ultra-modern geometric sans-serif, white, tracking wide
Tagline: 'Silence. Reimagined.' — elegant light-weight font, copper color
CTA: 'Pre-order Now →' — clean, medium weight, white with subtle glow"}.

Visual effects: {effects, default: "abstract sound wave visualizations floating around the product in translucent copper light, suggesting the noise-canceling technology. Tiny particle effects catching the light for premium atmosphere"}.

Color palette: {colors, default: "background: near-black to dark charcoal gradient. Accent: brushed copper/rose gold. Text: white and copper. The palette communicates premium, sophisticated technology"}.

Typography: {typography, default: "modern, geometric sans-serif family (like Montserrat or Gilroy). Strong hierarchy — headline largest, tagline medium, CTA smaller but prominent. All text razor-sharp and perfectly aligned"}.

Composition: vertical ad format optimized for Instagram Stories / TikTok. Aspect ratio 9:16.

The overall style is a premium brand campaign visual worthy of an Apple or Sony product launch — clean, sophisticated, and aspirational. All text must be perfectly spelled and rendered.
```

**Quality Checklist:**
- [ ] Product rendered with premium quality
- [ ] All text correctly spelled and properly styled
- [ ] Professional marketing design layout
- [ ] Aspirational, brand-worthy aesthetic

---

## Template Index (Quick Reference)

| ID | Name | Category | Input | Priority |
|----|------|----------|-------|----------|
| A01 | Chibi Cartoon | Stylization | Photo | P0 |
| A02 | 3D Pixar Animation | Stylization | Photo | P0 |
| A03 | Comic / Manga | Stylization | Photo | P0 |
| A04 | Sketch / Pencil | Stylization | Photo | P0 |
| A05 | Clay / Claymation | Stylization | Photo | P0 |
| A06 | 80s Retro Animation | Stylization | Photo | P0 |
| A07 | Retro-Futurism | Stylization | Photo | P0 |
| A08 | Ukiyo-e / Chinese Painting | Stylization | Photo | P0 |
| A09 | Watercolor Portrait | Stylization | Photo | P0 |
| A10 | K-Pop Star | Stylization | Photo | P0 |
| A11 | Imperial / Royal | Stylization | Photo | P0 |
| A12 | 90s Yearbook | Stylization | Photo | P0 |
| A13 | High Fashion | Stylization | Photo | P0 |
| A14 | Cyberpunk Portrait | Stylization | Photo | P0 |
| A15 | Oil Painting / Classical | Stylization | Photo | P0 |
| A16 | Pixel Art | Stylization | Photo | P0 |
| A17 | Flat / Vector Illustration | Stylization | Photo | P0 |
| A18 | Anime / 二次元 | Stylization | Photo | P0 |
| A19 | Wool Felt / Needle Felt | Stylization | Photo | P0 |
| A20 | Colored Pencil | Stylization | Photo | P0 |
| A21 | Pop Art | Stylization | Photo | P0 |
| A22 | Miniature / Diorama | Stylization | Photo | P0 |
| A23 | Children's Drawing | Stylization | Photo | P0 |
| B01 | Studio Photoshoot | Portrait | Photo | P0 |
| B02 | ID Photo | Portrait | Photo | P0 |
| B03 | Pet Humanization | Portrait | Pet photo | P0 |
| B04 | Emoji / Sticker Pack | Portrait | Photo | P0 |
| B05 | Avatar / Profile Picture | Portrait | Photo | P0 |
| B06 | Film / Cinematic Portrait | Portrait | Photo | P0 |
| B07 | Dreamy / Hazy Portrait | Portrait | Photo | P0 |
| C01 | Pet Stylization | Pets & Babies | Pet photo | P0 |
| C02 | Baby Comic Grid | Pets & Babies | Baby photo | P0 |
| C03 | Pet VOGUE Magazine | Pets & Babies | Pet photo | P0 |
| C04 | Pet Costume Play | Pets & Babies | Pet photo | P0 |
| D01 | Outfit Change | Editing | Photo + text | P1 |
| D02 | Hairstyle Change | Editing | Photo + text | P1 |
| D03 | Background Change | Editing | Photo + text | P1 |
| E01 | Social Media Post | Creative | Text (+ photo) | P1 |
| E02 | Poster Design | Creative | Text | P1 |
| E03 | Storyboard / Comic Strip | Creative | Text (+ photo) | P1 |
| E04 | Handwritten Poster | Creative | Text | P1 |
| E05 | Illustration | Creative | Text | P1 |
| E06 | YouTube Thumbnail | Creative | Text (+ photo) | P2 |
| E07 | Educational Visual | Creative | Text | P2 |
| E08 | Picture Book Illustration | Creative | Text | P1 |
| F01 | E-commerce Main Image | Design | Product photo/text | P1 |
| F02 | Sticker Set Design | Design | Photo | P1 |
| F03 | Interior Design | Design | Room photo | P1 |
| F04 | Logo Design | Design | Text | P1 |
| F05 | Merchandise / Keychain | Design | Photo/text | P1 |
| F06 | Coloring Book Page | Design | Text (+ photo) | P1 |
| F07 | Game Asset Design | Design | Text/photo | P2 |
| F08 | Product Marketing Design | Design | Product + text | P2 |
