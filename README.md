# People Photo Prompt Maker US

People Photo Prompt Maker US is a browser-based prompt builder for US small businesses that need realistic people-centered marketing images for hiring, local customer acquisition, and consultation requests.

It helps non-designers create structured, copy-ready prompts for image generators without having to understand prompt engineering, ad photography direction, or AI-specific image constraints.

The interface is designed to feel clean, responsive, and practical: the user can scan the available choices, see the generated prompt immediately, and copy it without setup.

## Live Demo

https://singtur-lab.github.io/people-photo-prompt-maker-us/

## Why This Exists

Small businesses often need trustworthy people photos for flyers, social posts, hiring campaigns, and local service pages. But prompt writing is hard when the owner has to decide the audience, business context, subject, background, aspect ratio, photo style, and generator-specific constraints all at once.

This tool turns that work into a guided workflow:

1. Pick the business goal.
2. Pick the channel.
3. Choose an industry preset.
4. Adjust the people, scene, style, and size.
5. Copy a clean English prompt that avoids text, logos, signs, and watermarks inside the generated image.

## Features

- Outcome-first prompt flow for hiring, lead generation, and trust-building visuals
- US-focused industry presets:
  - hair salon
  - real estate agency
  - medical clinic
  - professional services
  - tutoring center
  - home contractor
- People, audience, relationship, scene, framing, light, and aspect-ratio controls
- Generator-aware background handling for ChatGPT, Gemini, and Google Flow
- Transparent-background mode for subject-only cutout prompts
- Solid-background mode for generators where a flat background is easier to control
- Polished responsive interface for desktop and mobile use
- Copy-ready prompt output
- No build step, no server, no dependencies

## How To Run

Open `index.html` directly in any modern browser.

```bash
open index.html
```

You can also serve it locally:

```bash
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

## Example Output

```text
Act as a professional advertising photo director for US small business marketing.
Goal: increase new customer inquiries
Channel: local direct mail flyer
People and location context: Americans in the United States
Industry: hair salon
Audience: nearby new customers
Main subject: a happy salon customer
People count and relationship: one person, staff and customer conversation
Person detail: no gender specified
Scene: clean and welcoming salon interior
Framing and light: upper body visible, bright natural light
Style: bright advertising photo
Aspect ratio: 4:5 vertical
Do not include any text, numbers, logos, signs, trademarks, watermarks, or UI elements inside the image.
Create a natural, trustworthy, high-quality people photo that works clearly as local advertising.
```

## Built With

- HTML
- CSS
- JavaScript
- Codex
- GPT-5.6

## How Codex And GPT-5.6 Were Used

Codex and GPT-5.6 were used as the primary product-building partner for the project.

- Scoped the tool around a real audience: US small businesses that need practical advertising images.
- Compared broader prompt-maker ideas and narrowed the product to people-centered marketing photos because that had the clearest problem, audience, and workflow.
- Designed the UI structure around business outcomes instead of generic prompt tokens.
- Created English-first industry presets and prompt language for the US market.
- Implemented the standalone HTML/CSS/JavaScript app.
- Added generator-aware decisions for transparent backgrounds and solid-background control.
- Refined the visual design into a cleaner, more focused interface with stronger selected states and mobile-friendly layout.
- Wrote submission-ready project documentation and demo materials.
- Validated that the app is dependency-free and can be run by judges from a static file.

## Design Decisions

- The app does not ask image generators to place text, logos, or contact information inside the image. Those are added later in tools like Canva, PowerPoint, or Illustrator because image models can make text errors.
- The prompt starts with the business goal because small businesses care about the marketing outcome, not prompt mechanics.
- Presets are intentionally practical and local: hiring, direct mail, Facebook/Instagram, consultations, and storefront trust.
- The app runs as a static file so judges and small business users can test it immediately.
- The interface avoids decorative complexity and uses clear selected states, readable spacing, and responsive layout so the workflow stays fast.

## Devpost Track

Recommended category: **Work & Productivity**

Reason: the project helps small businesses move faster and produce better marketing assets with a guided workflow.

## License

MIT
