from pathlib import Path
import html
import subprocess
import textwrap

from PIL import Image, ImageDraw, ImageFont
from moviepy import AudioFileClip, ImageClip, concatenate_videoclips


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "demo-assets"
SHOTS = OUT / "screenshots"
FRAMES = OUT / "frames"
CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
PY = Path("/Users/taka_imac27/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3")


SCENES = [
    {
        "name": "01-default",
        "title": "People Photo Prompt Maker US",
        "body": "A guided prompt builder for small businesses that need trustworthy people photos.",
        "actions": [],
        "duration": 18,
    },
    {
        "name": "02-preset",
        "title": "Start From A Real Business Goal",
        "body": "Industry presets turn local marketing needs into structured image prompts.",
        "actions": ["document.querySelector(\"[data-preset='real estate agency']\").click();"],
        "duration": 22,
    },
    {
        "name": "03-details",
        "title": "Control The People And Scene",
        "body": "Details define the subject, relationship, scene, framing, and lighting without prompt-engineering jargon.",
        "actions": [
            "document.querySelector(\"[data-preset='real estate agency']\").click();",
            "document.getElementById('detailsToggle').click();",
        ],
        "duration": 22,
    },
    {
        "name": "04-transparent",
        "title": "Generator-Aware Backgrounds",
        "body": "ChatGPT mode can request a transparent subject-only cutout for later design work.",
        "actions": [
            "document.querySelector(\"[data-preset='medical clinic']\").click();",
            "document.getElementById('backgroundToggle').click();",
        ],
        "duration": 20,
    },
    {
        "name": "05-solid",
        "title": "Solid Background Mode",
        "body": "Gemini and Google Flow modes switch to a flat solid-background instruction to reduce messy outputs.",
        "actions": [
            "document.querySelector(\"[data-preset='home contractor']\").click();",
            "document.querySelector(\"[data-key='generator'] [data-value='Gemini']\").click();",
        ],
        "duration": 20,
    },
    {
        "name": "06-submit",
        "title": "Built With Codex And GPT-5.6",
        "body": "Codex helped narrow the idea, design the workflow, implement the app, write US presets, and prepare this submission.",
        "actions": [
            "document.querySelector(\"[data-preset='professional services']\").click();",
            "document.getElementById('detailsToggle').click();",
        ],
        "duration": 24,
    },
]


NARRATION = """
People Photo Prompt Maker US is a guided prompt builder for small businesses that need realistic people-centered marketing photos.

The problem is simple. Local businesses need trustworthy visuals for hiring flyers, social posts, direct mail, and consultation pages, but prompt writing is hard. Owners have to decide the audience, subject, scene, style, aspect ratio, and model-specific constraints all at once.

This app turns that into a workflow. First, the user chooses a business goal, such as increasing job applications or increasing new customer inquiries. Then they choose the channel, the AI tool, and a people region for the United States market.

Industry presets make the tool practical. A real estate agency preset sets a family-focused audience, an agent helping a family, and a home interior scene. A medical clinic or contractor preset changes the prompt for hiring and trust-building.

The details panel gives more control over people count, relationship, person detail, scene, framing, and light. The prompt updates live on the right, so the user can copy it immediately.

The app also handles generator-specific background choices. In ChatGPT mode, it can request a transparent, subject-only cutout. In Gemini or Google Flow mode, it switches to a flat solid-background instruction, which is easier for those generators to control.

The prompt always avoids text, logos, signs, trademarks, watermarks, and interface elements inside the image. Those should be added later in Canva or another design tool.

Codex and GPT-5.6 were used as the main product-building partner. They helped narrow the idea from a broad prompt maker into a focused tool for US small business people photos, design the workflow, implement the standalone HTML, CSS, and JavaScript app, write the US presets, and prepare the Devpost submission.

The final project is a single static HTML file with no setup, no server, and no dependencies. Judges can open it directly, test the workflow, and copy a usable prompt.
""".strip()


def write_variant(scene):
    source = (ROOT / "index.html").read_text()
    actions = "\n".join(scene["actions"])
    injection = f"""
<script>
window.addEventListener('load', () => {{
  setTimeout(() => {{
    {actions}
  }}, 250);
}});
</script>
"""
    variant = OUT / f"{scene['name']}.html"
    variant.write_text(source.replace("</body>", injection + "\n</body>"))
    return variant


def screenshot(scene, variant):
    target = SHOTS / f"{scene['name']}.png"
    subprocess.run(
        [
            str(CHROME),
            "--headless",
            "--disable-gpu",
            "--hide-scrollbars",
            "--window-size=1440,1000",
            "--virtual-time-budget=1400",
            f"--screenshot={target}",
            variant.as_uri(),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return target


def font(size, bold=False):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Helvetica.ttc",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def wrap(draw, text, font_obj, width):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        probe = f"{current} {word}".strip()
        if draw.textlength(probe, font=font_obj) <= width:
            current = probe
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def make_frame(scene, shot):
    canvas = Image.new("RGB", (1920, 1080), "#f5f5f7")
    shot_img = Image.open(shot).convert("RGB")
    shot_img.thumbnail((1320, 920), Image.Resampling.LANCZOS)
    sx = 560
    sy = 82
    canvas.paste(shot_img, (sx, sy))
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle((48, 60, 514, 1020), radius=34, fill="#1d1d1f")
    draw.rectangle((514, 60, 560, 1020), fill="#007aff")
    title_font = font(44, bold=True)
    title_y = 112
    for line in wrap(draw, scene["title"], title_font, 380):
        draw.text((86, title_y), line, fill="#fbfbfd", font=title_font)
        title_y += 54
    body_font = font(29)
    y = max(250, title_y + 56)
    for line in wrap(draw, scene["body"], body_font, 360):
        draw.text((88, y), line, fill="#e8e8ed", font=body_font)
        y += 43
    draw.text((88, 892), "OpenAI Build Week", fill="#9dccff", font=font(26, bold=True))
    draw.text((88, 935), "Codex + GPT-5.6", fill="#9dccff", font=font(26, bold=True))
    frame = FRAMES / f"{scene['name']}.png"
    canvas.save(frame, quality=95)
    return frame


def main():
    OUT.mkdir(exist_ok=True)
    SHOTS.mkdir(exist_ok=True)
    FRAMES.mkdir(exist_ok=True)
    frames = []
    for scene in SCENES:
        variant = write_variant(scene)
        shot = screenshot(scene, variant)
        frames.append(make_frame(scene, shot))

    narration_file = OUT / "narration.txt"
    narration_file.write_text(textwrap.fill(NARRATION, 90))
    audio_file = OUT / "narration.aiff"
    subprocess.run(["say", "-v", "Samantha", "-r", "178", "-o", str(audio_file), "-f", str(narration_file)], check=True)

    audio = AudioFileClip(str(audio_file))
    base_duration = audio.duration / len(frames)
    clips = [ImageClip(str(frame)).with_duration(base_duration) for frame in frames]
    video = concatenate_videoclips(clips, method="compose").with_audio(audio)
    output = ROOT / "people-photo-prompt-maker-us-demo.mp4"
    video.write_videofile(str(output), fps=6, codec="libx264", audio_codec="aac", preset="ultrafast")
    print(output)


if __name__ == "__main__":
    main()
