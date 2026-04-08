# Image Generation — High-Heat Template Skill

33 curated high-quality prompt templates for one-click image generation via **Gemini 3.1 Flash Image** (Nano Banana 2). Covers stylization, portraits, pets, editing, social media, and professional design — everything users need to discover what AI image generation can do.

## Results

**33/33 templates** generated successfully. Average quality score: **4.73/5.0**

| Category | Templates | Avg Score | Highlights |
|----------|-----------|-----------|------------|
| A: Stylization | 14 | 4.74 | Chibi, Clay, Ukiyo-e, Cyberpunk scored 4.9+ |
| B: Portrait | 5 | 4.74 | Pet Humanization and Sticker Pack scored 5.0 |
| C: Pets & Babies | 3 | 4.67 | Pet VOGUE Magazine scored 5.0 |
| D: Try-on & Editing | 3 | 4.37 | Pixel-level editing is a known model limitation |
| E: Social Media & Creative | 5 | 4.80 | Poster, Quote Card, Illustration scored 5.0 |
| F: Professional Design | 6 | 4.75 | Logo, E-commerce, Coloring Book scored 5.0 |

**10 templates scored perfect 5.0/5.0:** 90s Yearbook, Pet Humanization, Sticker Pack, Pet VOGUE, Social Media Post, Poster Design, Illustration, E-commerce, Logo Design, Coloring Book Page.

## What It Does

This skill provides two workflows:

### 1. User-Initiated: Query → Template Match → Generate

```
User: "Turn my photo into a Q-version cartoon" + uploads selfie
  → Matches A01 (Chibi Cartoon)
  → Fills template prompt with user's image
  → Generates high-quality chibi character
  → Suggests related templates (3D Pixar, Clay, Comic)
```

### 2. Proactive: Skill showcases template menu on install

When activated without a specific request, the skill presents all 33 templates organized by category, inspiring users to explore what's possible.

## Template Coverage

Covers **all P0-P1 scenarios** from competitive analysis:

| Source | Scenarios Covered |
|--------|-------------------|
| **P0 — Stylization** | 14 style templates (Chibi, 3D, Manga, Sketch, Clay, 80s, Retro-Future, Ukiyo-e, Watercolor, K-Pop, Imperial, 90s, Fashion, Cyberpunk) |
| **P0 — Portraits** | Studio photoshoot, ID photo, pet humanization, sticker pack, avatar |
| **P0 — Pets & Babies** | Pet stylization, baby comic grid, pet magazine cover |
| **P1 — Editing** | Outfit change, hairstyle change, background change |
| **P1 — Social Media** | Quote cards, posters, storyboards, handwritten posters, illustrations |
| **P1 — Professional Design** | E-commerce, sticker sets, interior design, logos, merchandise, coloring books |
| **ChatGPT features** | Style transformation, pet humanization, try-on, comic/storyboard, keychain design, e-commerce, room redesign |
| **Grok features** | All portrait styles (Chibi, 3D, Manga, 80s, Cyberpunk, High Fashion, etc.) |
| **Doubao AI创作** | 写真, 萌宠, 宝宝, 头像, 海报, 手抄报, 插画, Logo |

## Prompt Methodology

Each template uses the **General-Detail-General** prompt structure:

1. **Overview** — one-sentence transformation description
2. **Detail-Primary** — subject specifics (identity, clothing, materials)
3. **Detail-Secondary** — environment, lighting, camera, film stock
4. **Anchor** — ≤20-word style summary sentence
5. **Negative** — specific exclusions

Key techniques fused from multiple sources:
- **Identity Lock** from awesome-nano-banana-pro-prompts (10.7k stars)
- **Material Specificity** — "needle-felted wool", "matte obsidian with metallic flake"
- **Camera Language** — focal length, aperture, film stock
- **Text-First Hack** — specify all text before design elements
- **Per-Category Preservation** — exhaustive lists for editing templates

## Installation

### Claude Code

```bash
# Clone the repo
git clone https://github.com/yufei-eng/image-gen-templates.git

# Install the skill
mkdir -p ~/.claude/skills/image-gen-templates
cp image-gen-templates/SKILL.md ~/.claude/skills/image-gen-templates/
cp image-gen-templates/TEMPLATES.md ~/.claude/skills/image-gen-templates/
```

### Cursor

```bash
mkdir -p ~/.cursor/skills/image-gen-templates
cp SKILL.md ~/.cursor/skills/image-gen-templates/
cp TEMPLATES.md ~/.cursor/skills/image-gen-templates/
```

## Requirements

- Python 3.10+
- `google-genai` package
- Compass LLM Proxy access (client_token)

### Setup

```bash
# Option 1: Environment variable
export COMPASS_CLIENT_TOKEN="your_token"

# Option 2: Config file
cp config.json.example config.json
# Edit and fill in your client_token
```

## Evaluation

Run the evaluation suite:

```bash
# Generate all templates (requires API token)
python scripts/eval_templates.py

# Generate a specific category
python scripts/eval_templates.py --category A

# Generate a single template
python scripts/eval_templates.py --template A01

# Score interactively
python scripts/eval_templates.py --score

# Build HTML report
python scripts/build_report.py
```

## Project Structure

```
├── SKILL.md                     # Main skill file (workflow + intent matching + quality checks)
├── TEMPLATES.md                 # 33 prompt templates with patterns and quality checklists
├── README.md                    # This file
├── scripts/
│   ├── generate.py              # Gemini API client via Compass LLM Proxy
│   ├── eval_templates.py        # Batch evaluation runner
│   └── build_report.py          # HTML report generator
├── test/
│   ├── samples/                 # Test input images
│   └── results/                 # Per-template generation results + scores.json
├── report/
│   ├── template-report.html     # Self-contained HTML report (72MB with embedded images)
│   └── template-inventory.json  # Machine-readable template inventory
└── config.json.example          # API configuration template
```

## Key Features

- **33 curated templates** covering all major image generation use cases
- **Bilingual keyword matching** (English + Chinese) for intent classification
- **Quality self-check + retry** — per-category verification with surgical edit retry (max 2)
- **Proactive template showcase** — organized menu for discovery when no specific request
- **Fallback generation** — General-Detail-General rewrite for unmatched queries
- **Objective evaluation** — 5-dimension scoring with reproducible benchmarks

## License

MIT
