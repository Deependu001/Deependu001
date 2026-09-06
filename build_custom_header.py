import os
from PIL import Image, ImageDraw, ImageFont

# ==============================================================================
# RESOLUTION: 2x Supersampled (1920x700 -> 960x350)
# ==============================================================================
W2, H2 = 1920, 700
W1, H1 = 960, 350

# Colors (Strictly matching prompt: Pure White, Black/Charcoal, One Muted Green)
BG = (255, 255, 255)              # Pure White
FG_HERO = (15, 23, 42)            # Slate 900 / Deep Charcoal
FG_CMD = (31, 41, 55)             # Gray 800
FG_MUTED = (100, 116, 139)        # Slate 500
FG_LIGHT = (156, 163, 175)        # Gray 400
ACCENT_GREEN = (16, 185, 129)     # Emerald 500 (Terminal Green)
ACCENT_DARK_GREEN = (5, 150, 105) # Emerald 600

# Fonts (Crisp, modern, readable)
font_hero = ImageFont.truetype("C:\\Windows\\Fonts\\segoeuib.ttf", 56)
font_intro = ImageFont.truetype("C:\\Windows\\Fonts\\CascadiaMono.ttf", 26)
font_role = ImageFont.truetype("C:\\Windows\\Fonts\\CascadiaMono.ttf", 24)
font_sub = ImageFont.truetype("C:\\Windows\\Fonts\\CascadiaMono.ttf", 22)
font_cmd = ImageFont.truetype("C:\\Windows\\Fonts\\CascadiaMono.ttf", 24)
font_small = ImageFont.truetype("C:\\Windows\\Fonts\\CascadiaMono.ttf", 21)

X = 140  # 70px in 1x scale

def new_canvas():
    img = Image.new("RGB", (W2, H2), BG)
    draw = ImageDraw.Draw(img)
    return img, draw

def draw_prompt(draw, x, y):
    """Draws: $ """
    draw.text((x, y), "$ ", fill=ACCENT_DARK_GREEN, font=font_cmd)
    bbox = font_cmd.getbbox("$ ")
    return x + (bbox[2] - bbox[0])

frames_2x = []
durations = []

def add_frame(img, dur):
    frames_2x.append(img)
    durations.append(dur)

# ==============================================================================
# SCENE 1: Blank white screen. Small blinking terminal cursor.
# ==============================================================================
img, draw = new_canvas()
px = draw_prompt(draw, X, 60)
draw.text((px, 60), "_", fill=ACCENT_DARK_GREEN, font=font_cmd)
add_frame(img, 450)

img, draw = new_canvas()
px = draw_prompt(draw, X, 60)
add_frame(img, 280)

img, draw = new_canvas()
px = draw_prompt(draw, X, 60)
draw.text((px, 60), "_", fill=ACCENT_DARK_GREEN, font=font_cmd)
add_frame(img, 350)

# ==============================================================================
# SCENE 2: Terminal types: $ whoami
# ==============================================================================
cmd_whoami = "whoami"
for i in range(1, len(cmd_whoami) + 1):
    sub = cmd_whoami[:i]
    img, draw = new_canvas()
    px = draw_prompt(draw, X, 60)
    draw.text((px, 60), sub + " _", fill=FG_CMD, font=font_cmd)
    add_frame(img, 65)

# Hold typed command
img, draw = new_canvas()
px = draw_prompt(draw, X, 60)
draw.text((px, 60), cmd_whoami, fill=FG_CMD, font=font_cmd)
add_frame(img, 260)

# ==============================================================================
# SCENE 3: Answer: deependu
# ==============================================================================
img, draw = new_canvas()
px = draw_prompt(draw, X, 60)
draw.text((px, 60), cmd_whoami, fill=FG_CMD, font=font_cmd)
draw.text((X, 96), "deependu", fill=FG_MUTED, font=font_cmd)
add_frame(img, 500)

# ==============================================================================
# SCENE 4: Large introduction: Hi, I'm / DEEPENDU MONDAL (kinetic letter entrance)
# ==============================================================================
# "Hi, I'm" appears
img, draw = new_canvas()
px = draw_prompt(draw, X, 60)
draw.text((px, 60), cmd_whoami, fill=FG_CMD, font=font_cmd)
draw.text((X, 96), "deependu", fill=FG_MUTED, font=font_cmd)
draw.text((X, 150), "Hi, I'm", fill=FG_MUTED, font=font_intro)
add_frame(img, 300)

# "DEEPENDU MONDAL" types out with commanding presence
hero_name = "DEEPENDU MONDAL"
for i in range(1, len(hero_name) + 1):
    sub_name = hero_name[:i]
    img, draw = new_canvas()
    px = draw_prompt(draw, X, 60)
    draw.text((px, 60), cmd_whoami, fill=FG_CMD, font=font_cmd)
    draw.text((X, 96), "deependu", fill=FG_MUTED, font=font_cmd)
    draw.text((X, 150), "Hi, I'm", fill=FG_MUTED, font=font_intro)
    draw.text((X, 194), sub_name, fill=FG_HERO, font=font_hero)
    add_frame(img, 45)

# Hold on full name
img, draw = new_canvas()
px = draw_prompt(draw, X, 60)
draw.text((px, 60), cmd_whoami, fill=FG_CMD, font=font_cmd)
draw.text((X, 96), "deependu", fill=FG_MUTED, font=font_cmd)
draw.text((X, 150), "Hi, I'm", fill=FG_MUTED, font=font_intro)
draw.text((X, 194), hero_name, fill=FG_HERO, font=font_hero)
add_frame(img, 350)

# ==============================================================================
# SCENE 5: Subtitle: CYBERSECURITY ENGINEER
# ==============================================================================
img, draw = new_canvas()
px = draw_prompt(draw, X, 60)
draw.text((px, 60), cmd_whoami, fill=FG_CMD, font=font_cmd)
draw.text((X, 96), "deependu", fill=FG_MUTED, font=font_cmd)
draw.text((X, 150), "Hi, I'm", fill=FG_MUTED, font=font_intro)
draw.text((X, 194), hero_name, fill=FG_HERO, font=font_hero)
draw.text((X, 268), "CYBERSECURITY ENGINEER", fill=ACCENT_DARK_GREEN, font=font_role)
add_frame(img, 380)

# ==============================================================================
# SCENE 6: Specializations appear: OFFENSIVE SECURITY · APPSEC · SECURITY ENGINEERING
# ==============================================================================
def draw_base_intro():
    img, draw = new_canvas()
    px = draw_prompt(draw, X, 60)
    draw.text((px, 60), cmd_whoami, fill=FG_CMD, font=font_cmd)
    draw.text((X, 96), "deependu", fill=FG_MUTED, font=font_cmd)
    draw.text((X, 150), "Hi, I'm", fill=FG_MUTED, font=font_intro)
    draw.text((X, 194), hero_name, fill=FG_HERO, font=font_hero)
    draw.text((X, 268), "CYBERSECURITY ENGINEER", fill=ACCENT_DARK_GREEN, font=font_role)
    draw.text((X, 306), "OFFENSIVE SECURITY  ·  APPSEC  ·  SECURITY ENGINEERING", fill=FG_MUTED, font=font_sub)
    return img

add_frame(draw_base_intro(), 500)

# ==============================================================================
# SCENE 7: Terminal appears subtly:
# $ ./current_focus
# [+] security tooling
# [+] web & API security
# [+] offensive security
# ==============================================================================
cmd_focus = "./current_focus"
for i in range(1, len(cmd_focus) + 1):
    sub = cmd_focus[:i]
    img = draw_base_intro()
    draw = ImageDraw.Draw(img)
    px = draw_prompt(draw, X, 368)
    draw.text((px, 368), sub + " _", fill=FG_CMD, font=font_cmd)
    add_frame(img, 50)

# Hold command
img = draw_base_intro()
draw = ImageDraw.Draw(img)
px = draw_prompt(draw, X, 368)
draw.text((px, 368), cmd_focus, fill=FG_CMD, font=font_cmd)
add_frame(img, 240)

# Focus lines reveal
focus_items = [
    "[+] security tooling",
    "[+] web & API security",
    "[+] offensive security"
]

def draw_with_focus(count=3):
    img = draw_base_intro()
    draw = ImageDraw.Draw(img)
    px = draw_prompt(draw, X, 368)
    draw.text((px, 368), cmd_focus, fill=FG_CMD, font=font_cmd)

    y_pos = 412
    for idx in range(count):
        item = focus_items[idx]
        draw.text((X, y_pos), "[+]", fill=ACCENT_GREEN, font=font_small)
        draw.text((X + 44, y_pos), item[4:], fill=FG_MUTED, font=font_small)
        y_pos += 34
    return img

add_frame(draw_with_focus(1), 220)
add_frame(draw_with_focus(2), 220)
add_frame(draw_with_focus(3), 600)

# ==============================================================================
# SCENE 8: Tiny security visualization appears for 1.5 seconds:
# target
#  ├── /api
#  ├── /auth
#  └── /admin
# Then it disappears.
# ==============================================================================
def draw_with_tree():
    img = draw_with_focus(3)
    draw = ImageDraw.Draw(img)
    
    # Attack surface tree positioned cleanly to the right
    tree_x = 960
    draw.ellipse([tree_x - 14, 419, tree_x - 4, 429], fill=ACCENT_GREEN)
    draw.text((tree_x, 412), "target", fill=FG_HERO, font=font_small)
    draw.text((tree_x, 446), " ├── /api", fill=FG_MUTED, font=font_small)
    draw.text((tree_x, 480), " ├── /auth", fill=FG_MUTED, font=font_small)
    draw.text((tree_x, 514), " └── /admin", fill=FG_MUTED, font=font_small)
    return img

add_frame(draw_with_tree(), 1500)

# Brief return to Scene 7 state (tree disappears)
add_frame(draw_with_focus(3), 400)

# ==============================================================================
# SCENE 9: Final command:
# $ ./build_security_tools.sh
# [+] ready_
# Blinking cursor. Then smoothly loop.
# ==============================================================================
cmd_build = "./build_security_tools.sh"
for i in range(1, len(cmd_build) + 1):
    sub = cmd_build[:i]
    img = draw_with_focus(3)
    draw = ImageDraw.Draw(img)
    px = draw_prompt(draw, X, 540)
    draw.text((px, 540), sub + " _", fill=FG_CMD, font=font_cmd)
    add_frame(img, 45)

# Hold final command
img = draw_with_focus(3)
draw = ImageDraw.Draw(img)
px = draw_prompt(draw, X, 540)
draw.text((px, 540), cmd_build, fill=FG_CMD, font=font_cmd)
add_frame(img, 280)

# Reveal "[+] ready" with blinking cursor
def draw_final(cursor_on=True):
    img = draw_with_focus(3)
    draw = ImageDraw.Draw(img)
    px = draw_prompt(draw, X, 540)
    draw.text((px, 540), cmd_build, fill=FG_CMD, font=font_cmd)

    draw.text((X, 582), "[+]", fill=ACCENT_GREEN, font=font_cmd)
    draw.text((X + 44, 582), "ready", fill=FG_MUTED, font=font_cmd)
    if cursor_on:
        draw.text((X + 130, 582), "_", fill=ACCENT_DARK_GREEN, font=font_cmd)
    return img

# Cursor blinks 4 times
for _ in range(4):
    add_frame(draw_final(cursor_on=True), 450)
    add_frame(draw_final(cursor_on=False), 320)

# Final hold before seamless loop restart
add_frame(draw_final(cursor_on=True), 2000)

print(f"Total 2x frames: {len(frames_2x)}")

# Downsample to 1x with Lanczos antialiasing
final_frames = []
for f in frames_2x:
    f_1x = f.resize((W1, H1), Image.Resampling.LANCZOS)
    p_img = f_1x.convert("P", palette=Image.Palette.ADAPTIVE, colors=64)
    final_frames.append(p_img)

output_path = "e:\\GITHUB\\Deependu001\\assets\\header.gif"
final_frames[0].save(
    output_path,
    save_all=True,
    append_images=final_frames[1:],
    duration=durations,
    loop=0,
    optimize=True
)

kb = os.path.getsize(output_path) / 1024
print(f"Successfully created custom animated header GIF: {output_path} ({kb:.1f} KB, {len(final_frames)} frames)")
