# Devpost Submission Draft

## Project Name

People Photo Prompt Maker US

## Tagline

A guided prompt builder for US small businesses that need realistic people photos for hiring, local marketing, and consultations.

## Category

Work & Productivity

## Submitter Type

Individual

## Country Of Residence

Japan

## Built With

HTML, CSS, JavaScript, Codex, GPT-5.6

## Project Description

People Photo Prompt Maker US is a browser-based prompt builder for US small businesses that need realistic people-centered marketing images.

Small businesses often need trustworthy visuals for hiring flyers, social media posts, direct mail, and local service pages, but writing a useful image-generation prompt is difficult. Owners have to decide the business goal, audience, subject, scene, aspect ratio, photography style, and generator-specific constraints all at once.

This project turns that into a simple guided workflow. The user starts with the business outcome, chooses a channel, selects a US small-business industry preset, adjusts the people and scene, and copies a structured English prompt. The generated prompt is designed to create usable marketing imagery while avoiding text, logos, signs, trademarks, watermarks, and UI elements inside the image.

The app includes presets for hair salons, real estate agencies, medical clinics, professional services, tutoring centers, and home contractors. It also includes ChatGPT, Gemini, and Google Flow modes, with transparent-background and solid-background handling depending on the generator.

The project is intentionally lightweight: a single static HTML file with no dependencies, no account, and no server. Judges can open the file directly in a browser and test the full workflow immediately. The interface is clean, responsive, and focused on fast decision-making rather than prompt-engineering jargon.

## What It Does

- Helps a small business owner choose the goal, channel, industry, audience, subject, people relationship, scene, framing, light, and aspect ratio.
- Generates a complete prompt for realistic people-centered marketing photos.
- Provides industry presets for common US local businesses.
- Keeps risky text/logo generation out of the image and reminds users to add those elements later in a design tool.
- Supports background-aware prompt modes for multiple image generators.
- Provides a polished single-page interface with clear selected states, readable spacing, and mobile-friendly layout.

## Recommended Gallery Images

Use these generated samples to show the practical output of the prompt maker. Recommended order:

1. `sample-images/Real Estate Agency.png`
2. `sample-images/Home Contractor.png`
3. `sample-images/Hair Salon.png`
4. `sample-images/Professional Services Firm.png`
5. `sample-images/Medical Clinic.png`

Suggested caption:

```text
Sample images generated from prompts created with People Photo Prompt Maker US. Each image uses the same structured prompt format, adjusted for a different US small-business industry.
```

## How Codex And GPT-5.6 Were Used

Codex and GPT-5.6 were used as the core product-building partner.

They helped scope the idea from a broad prompt-maker concept into a focused tool for US small business people photos. Codex helped identify that this narrower product had a stronger audience, clearer workflow, and better Devpost fit than a generic image prompt maker.

Codex then helped design and implement the interface, write the US-focused presets, structure the generated prompt language, add generator-aware background behavior, and prepare the README and submission materials. GPT-5.6 was used through Codex for product judgment, UX decisions, implementation, and documentation.

## Technical Implementation Notes

- Static HTML/CSS/JavaScript app
- No framework or build step
- State-driven prompt generation
- Industry presets are plain JavaScript objects
- UI controls update the prompt live
- Clipboard copy support
- Polished responsive layout for desktop and mobile

## Judge Testing Instructions

1. Open `index.html` in a browser.
2. Choose an industry preset, such as `real estate agency` or `medical clinic`.
3. Change the goal, channel, and AI tool.
4. Open `Details` and adjust people count, scene, framing, and light.
5. Toggle `Transparent Background` in ChatGPT mode, or switch to Gemini/Google Flow to see solid-background mode.
6. Copy the generated prompt and use it in an image generator.

## Current Submission Links

- Code repository: https://github.com/singtur-lab/people-photo-prompt-maker-us
- Devpost project: https://devpost.com/software/people-photo-prompt-maker-us
- Current public demo video: https://www.youtube.com/watch?v=CEwEI-hjw7o
- Updated local demo video: `people-photo-prompt-maker-us-demo.mp4`
- `/feedback` Codex Session ID: `019f7974-17fe-7dc3-ad51-be2dda74463f`

## Optional Judge Test Link

After the local GitHub Pages commits are pushed and Pages is enabled, the expected URL is:

```text
https://singtur-lab.github.io/people-photo-prompt-maker-us/
```

## Submission Form Answers

Use these values for the OpenAI Build Week custom submission fields.

| Field ID | Label | Value |
|---:|---|---|
| 27945 | Submitter Type | Individual |
| 27946 | Country of Residence | Japan |
| 27947 | Category | Work & Productivity |
| 27948 | Code repository URL | https://github.com/singtur-lab/people-photo-prompt-maker-us |
| 27949 | Project test link and instructions | Open `index.html` directly in a browser. No credentials, server, or build step required. If GitHub Pages is enabled, use `https://singtur-lab.github.io/people-photo-prompt-maker-us/`. |
| 27950 | `/feedback` Session ID | `019f7974-17fe-7dc3-ad51-be2dda74463f` |
| 27951 | Plugin/dev tool instructions | Not applicable. This is a static browser app, not a plugin or developer tool. |

## Demo Video

Updated local MP4 prepared:

```text
people-photo-prompt-maker-us-demo.mp4
```

Uploaded public YouTube demo:

```text
https://www.youtube.com/watch?v=CEwEI-hjw7o
```
