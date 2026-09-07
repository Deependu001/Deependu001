"""
build_custom_header.py
======================
Generates an authentic Kali Linux animated terminal header GIF for Deependu Mondal's
GitHub profile (https://github.com/Deependu001/Deependu001).

Visual Identity:
  - Real Kali Linux workstation terminal session
  - Dark slate/charcoal background (#0d1117 / #161b22)
  - Realistic Kali window chrome: '>_ deependu@kali: ~' & window controls (— □ ✕)
  - Crisp Cascadia Mono typography with 2x supersampling (1920x1000 -> 960x500)
  - Semantic color palette:
      * Kali Blue (#388bfd): Shell prompt identity and highlight
      * Terminal Green (#3fb950): Successful operations [+] and ready state
      * Analysis Yellow (#e3b341): Reconnaissance status [*]
      * Bright White (#ffffff): Hero name and primary accents
      * Crisp Slate (#94a3b8): Standard terminal output
  - Realistic typing cadence and command execution storytelling:
      Scene 1: Prompt opens with blinking cursor
      Scene 2: Typing 'whoami' -> 'deependu'
      Scene 3: Typing 'cat profile.txt' -> Deependu Mondal, Cybersecurity Engineer
      Scene 4: Typing './current-focus.sh' -> Offensive Security, AppSec, Vuln Research, Tooling
      Scene 5: Typing './recon.sh' -> Target reconnaissance sequence [lab.local]
      Scene 6: Typing './build_security_tools.sh' -> '[+] ready_' with blinking cursor
      Seamless loop (~11-13 seconds total duration)
"""

import os
from PIL import Image, ImageDraw, ImageFont

# ==============================================================================
# RESOLUTION: 2x Supersampled (1920x1000 -> 960x500)
# ==============================================================================
W2, H2 = 1920, 1000
W1, H1 = 960, 500

# Palette
BG_DARK = (13, 17, 23)           # Kali Dark Slate / Charcoal
TITLE_BG = (22, 27, 34)          # Terminal Window Header
BORDER_COL = (48, 54, 61)        # Subtle Border
BTN_CLOSE = (248, 113, 113)      # Close (Red)
BTN_MUTED = (148, 163, 184)      # Window Buttons Muted Slate

C_PROMPT_USER = (56, 139, 253)   # Kali Blue
C_PROMPT_SEP = (113, 128, 150)   # Slate Separator
C_PROMPT_PATH = (56, 189, 248)   # Cyan Path
C_PROMPT_CHAR = (240, 246, 252)  # White '$'
C_CMD = (240, 246, 252)          # Off-white Command
C_OUT = (148, 163, 184)          # Crisp Slate Output
C_HERO = (255, 255, 255)         # Hero Bold White
C_ROLE = (88, 166, 255)          # Kali Bright Blue
C_GREEN = (63, 185, 80)          # Terminal Green [+]
C_YELLOW = (227, 179, 65)        # Analysis Yellow [*]
C_CURSOR = (56, 189, 248)        # Cyan/Blue Terminal Cursor

# Monospace Fonts
font_title = ImageFont.truetype("C:\\Windows\\Fonts\\CascadiaMono.ttf", 24)
font_term = ImageFont.truetype("C:\\Windows\\Fonts\\CascadiaMono.ttf", 28)
font_bold = ImageFont.truetype("C:\\Windows\\Fonts\\CascadiaCode.ttf", 29)
font_hero = ImageFont.truetype("C:\\Windows\\Fonts\\CascadiaCode.ttf", 36)
font_role = ImageFont.truetype("C:\\Windows\\Fonts\\CascadiaCode.ttf", 29)

# Spacing & Coordinates
X = 52
Y_START = 96
LH = 43

frames_2x = []
durations = []

def add_frame(img, duration_ms):
    frames_2x.append(img)
    durations.append(duration_ms)

def new_canvas():
    img = Image.new("RGB", (W2, H2), BG_DARK)
    draw = ImageDraw.Draw(img)
    
    # Title bar
    draw.rectangle([0, 0, W2, 66], fill=TITLE_BG)
    draw.line([0, 66, W2, 66], fill=BORDER_COL, width=2)
    
    # Top-Left: Terminal icon & window title
    draw.text((36, 19), ">_", fill=C_PROMPT_PATH, font=font_bold)
    draw.text((80, 19), "deependu@kali: ~", fill=C_CMD, font=font_title)
    
    # Top-Right: Authentic Kali / Linux XFCE window buttons: minimize, maximize, close
    # Minimize: horizontal line
    draw.rectangle([W2 - 140, 35, W2 - 120, 37], fill=BTN_MUTED)
    # Maximize: square outline
    draw.rectangle([W2 - 100, 24, W2 - 82, 42], outline=BTN_MUTED, width=2)
    # Close: X symbol
    draw.line([W2 - 58, 24, W2 - 40, 42], fill=BTN_CLOSE, width=2)
    draw.line([W2 - 40, 24, W2 - 58, 42], fill=BTN_CLOSE, width=2)
    
    # Terminal bottom border
    draw.line([0, H2 - 1, W2, H2 - 1], fill=BORDER_COL, width=1)
    return img, draw

def draw_prompt(draw, x, y, cmd="", show_cursor=False, cursor_char="_"):
    draw.text((x, y), "deependu@kali", fill=C_PROMPT_USER, font=font_bold)
    w1 = font_bold.getbbox("deependu@kali")[2]
    draw.text((x + w1, y), ":", fill=C_PROMPT_SEP, font=font_term)
    w2 = font_term.getbbox(":")[2]
    draw.text((x + w1 + w2, y), "~", fill=C_PROMPT_PATH, font=font_term)
    w3 = font_term.getbbox("~")[2]
    draw.text((x + w1 + w2 + w3, y), "$ ", fill=C_PROMPT_CHAR, font=font_term)
    w4 = font_term.getbbox("$ ")[2]
    
    px = x + w1 + w2 + w3 + w4
    if cmd:
        draw.text((px, y), cmd, fill=C_CMD, font=font_term)
        w_cmd = font_term.getbbox(cmd)[2]
        px += w_cmd
    
    if show_cursor:
        draw.text((px, y), cursor_char, fill=C_CURSOR, font=font_term)
    return px

def render_state(
    cmd1=None, s1_cursor=False,
    out1=False,
    cmd2=None, s2_cursor=False,
    profile_stage=0, # 1: name, 2: role, 3: domains
    cmd3=None, s3_cursor=False,
    focus_count=0, # 1..4
    cmd4=None, s4_cursor=False,
    recon_stage=0, # 1..5
    cmd5=None, s5_cursor=False,
    ready_state=False, ready_cursor=False
):
    img, draw = new_canvas()
    y = Y_START
    
    # 1. Scene 1 & 2: whoami
    if cmd1 is not None or s1_cursor:
        draw_prompt(draw, X, y, cmd=cmd1 or "", show_cursor=s1_cursor)
    y += LH
    
    if out1:
        draw.text((X, y), "deependu", fill=C_OUT, font=font_term)
    y += LH
    
    # 2. Scene 3: cat profile.txt
    if cmd2 is not None or s2_cursor:
        draw_prompt(draw, X, y, cmd=cmd2 or "", show_cursor=s2_cursor)
    y += LH
    
    if profile_stage >= 1:
        draw.text((X, y), "Deependu Mondal", fill=C_HERO, font=font_hero)
    y += LH
    
    if profile_stage >= 2:
        draw.text((X, y), "Cybersecurity Engineer", fill=C_ROLE, font=font_role)
    y += LH - 3
    
    if profile_stage >= 3:
        draw.text((X, y), "Offensive Security", fill=C_OUT, font=font_term)
        y += 37
        draw.text((X, y), "Application Security", fill=C_OUT, font=font_term)
        y += 37
        draw.text((X, y), "Security Tooling", fill=C_OUT, font=font_term)
        y += LH
    else:
        y += 37 * 2 + LH
        
    # 3. Scene 4: ./current-focus.sh
    if cmd3 is not None or s3_cursor:
        draw_prompt(draw, X, y, cmd=cmd3 or "", show_cursor=s3_cursor)
    y += LH
    
    focus_items = [
        "Offensive Security",
        "Web & API Security",
        "Vulnerability Research",
        "Security Tooling"
    ]
    for idx in range(focus_count):
        draw.text((X, y), "[+]", fill=C_GREEN, font=font_term)
        draw.text((X + 58, y), focus_items[idx], fill=C_OUT, font=font_term)
        y += 37
    if focus_count < 4:
        y += 37 * (4 - focus_count)
    y += 6
    
    # 4. Scene 5: ./recon.sh
    if cmd4 is not None or s4_cursor:
        draw_prompt(draw, X, y, cmd=cmd4 or "", show_cursor=s4_cursor)
    y += LH
    
    if recon_stage >= 1:
        draw.text((X, y), "[*]", fill=C_YELLOW, font=font_term)
        draw.text((X + 58, y), "initializing reconnaissance [lab.local]...", fill=C_OUT, font=font_term)
    y += 37
    
    recon_items = [
        "attack surface mapped",
        "web endpoints discovered",
        "API surface identified",
        "analysis complete"
    ]
    for idx in range(max(0, recon_stage - 1)):
        draw.text((X, y), "[+]", fill=C_GREEN, font=font_term)
        draw.text((X + 58, y), recon_items[idx], fill=C_OUT, font=font_term)
        y += 37
    if recon_stage < 5:
        y += 37 * (5 - max(1, recon_stage))
    y += 6
    
    # 5. Scene 6: ./build_security_tools.sh
    if cmd5 is not None or s5_cursor:
        draw_prompt(draw, X, y, cmd=cmd5 or "", show_cursor=s5_cursor)
    y += LH
    
    if ready_state:
        draw.text((X, y), "[+]", fill=C_GREEN, font=font_term)
        draw.text((X + 58, y), "ready", fill=C_OUT, font=font_term)
        w_ready = font_term.getbbox("ready")[2]
        if ready_cursor:
            draw.text((X + 58 + w_ready, y), "_", fill=C_GREEN, font=font_term)
            
    return img

print("Generating Kali Linux terminal animation frames...")

# ==============================================================================
# SCENE 1: Terminal opens. Prompt: deependu@kali:~$ Cursor blinks.
# ==============================================================================
add_frame(render_state(cmd1="", s1_cursor=True), 420)
add_frame(render_state(cmd1="", s1_cursor=False), 280)
add_frame(render_state(cmd1="", s1_cursor=True), 380)

# ==============================================================================
# SCENE 2: Type: whoami -> Output: deependu
# ==============================================================================
typed_whoami = "whoami"
for i in range(1, len(typed_whoami) + 1):
    add_frame(render_state(cmd1=typed_whoami[:i], s1_cursor=True), 70)

# Hold typed command with cursor
add_frame(render_state(cmd1=typed_whoami, s1_cursor=False), 220)

# Execute: show 'deependu'
add_frame(render_state(cmd1=typed_whoami, out1=True, s2_cursor=False), 450)

# ==============================================================================
# SCENE 3: Type: cat profile.txt -> Show Profile Output
# ==============================================================================
# Next prompt with cursor appears
add_frame(render_state(cmd1=typed_whoami, out1=True, cmd2="", s2_cursor=True), 250)

# Typing cat profile.txt with realistic shell tab completion
typing_seq_profile = ["c", "ca", "cat", "cat ", "cat p", "cat pr", "cat profile.txt"]
for sub in typing_seq_profile:
    add_frame(render_state(cmd1=typed_whoami, out1=True, cmd2=sub, s2_cursor=True), 75)

# Hold command
add_frame(render_state(cmd1=typed_whoami, out1=True, cmd2="cat profile.txt", s2_cursor=False), 220)

# Output reveals
add_frame(render_state(cmd1=typed_whoami, out1=True, cmd2="cat profile.txt", profile_stage=1), 280)
add_frame(render_state(cmd1=typed_whoami, out1=True, cmd2="cat profile.txt", profile_stage=2), 280)
add_frame(render_state(cmd1=typed_whoami, out1=True, cmd2="cat profile.txt", profile_stage=3), 650)

# ==============================================================================
# SCENE 4: Type: ./current-focus.sh -> Show Focus Output
# ==============================================================================
# Prompt appears
add_frame(render_state(
    cmd1=typed_whoami, out1=True, cmd2="cat profile.txt", profile_stage=3,
    cmd3="", s3_cursor=True
), 260)

# Typing ./current-focus.sh
typing_seq_focus = [".", "./", "./c", "./cur", "./current-focus.sh"]
for sub in typing_seq_focus:
    add_frame(render_state(
        cmd1=typed_whoami, out1=True, cmd2="cat profile.txt", profile_stage=3,
        cmd3=sub, s3_cursor=True
    ), 80)

add_frame(render_state(
    cmd1=typed_whoami, out1=True, cmd2="cat profile.txt", profile_stage=3,
    cmd3="./current-focus.sh", s3_cursor=False
), 220)

# Focus lines reveal
for count in range(1, 5):
    add_frame(render_state(
        cmd1=typed_whoami, out1=True, cmd2="cat profile.txt", profile_stage=3,
        cmd3="./current-focus.sh", focus_count=count
    ), 220 if count < 4 else 550)

# ==============================================================================
# SCENE 5: Type: ./recon.sh -> Recon Sequence Output
# ==============================================================================
add_frame(render_state(
    cmd1=typed_whoami, out1=True, cmd2="cat profile.txt", profile_stage=3,
    cmd3="./current-focus.sh", focus_count=4,
    cmd4="", s4_cursor=True
), 260)

# Typing ./recon.sh
typing_seq_recon = [".", "./", "./r", "./rec", "./recon.sh"]
for sub in typing_seq_recon:
    add_frame(render_state(
        cmd1=typed_whoami, out1=True, cmd2="cat profile.txt", profile_stage=3,
        cmd3="./current-focus.sh", focus_count=4,
        cmd4=sub, s4_cursor=True
    ), 80)

add_frame(render_state(
    cmd1=typed_whoami, out1=True, cmd2="cat profile.txt", profile_stage=3,
    cmd3="./current-focus.sh", focus_count=4,
    cmd4="./recon.sh", s4_cursor=False
), 220)

# Recon stages reveal
for stage in range(1, 6):
    add_frame(render_state(
        cmd1=typed_whoami, out1=True, cmd2="cat profile.txt", profile_stage=3,
        cmd3="./current-focus.sh", focus_count=4,
        cmd4="./recon.sh", recon_stage=stage
    ), 240 if stage < 5 else 600)

# ==============================================================================
# SCENE 6: Type: ./build_security_tools.sh -> [+] ready_
# ==============================================================================
add_frame(render_state(
    cmd1=typed_whoami, out1=True, cmd2="cat profile.txt", profile_stage=3,
    cmd3="./current-focus.sh", focus_count=4,
    cmd4="./recon.sh", recon_stage=5,
    cmd5="", s5_cursor=True
), 260)

# Typing ./build_security_tools.sh
typing_seq_build = [".", "./", "./b", "./build", "./build_security_tools.sh"]
for sub in typing_seq_build:
    add_frame(render_state(
        cmd1=typed_whoami, out1=True, cmd2="cat profile.txt", profile_stage=3,
        cmd3="./current-focus.sh", focus_count=4,
        cmd4="./recon.sh", recon_stage=5,
        cmd5=sub, s5_cursor=True
    ), 80)

add_frame(render_state(
    cmd1=typed_whoami, out1=True, cmd2="cat profile.txt", profile_stage=3,
    cmd3="./current-focus.sh", focus_count=4,
    cmd4="./recon.sh", recon_stage=5,
    cmd5="./build_security_tools.sh", s5_cursor=False
), 250)

# Reveal [+] ready with blinking cursor
for _ in range(3):
    add_frame(render_state(
        cmd1=typed_whoami, out1=True, cmd2="cat profile.txt", profile_stage=3,
        cmd3="./current-focus.sh", focus_count=4,
        cmd4="./recon.sh", recon_stage=5,
        cmd5="./build_security_tools.sh",
        ready_state=True, ready_cursor=True
    ), 420)
    add_frame(render_state(
        cmd1=typed_whoami, out1=True, cmd2="cat profile.txt", profile_stage=3,
        cmd3="./current-focus.sh", focus_count=4,
        cmd4="./recon.sh", recon_stage=5,
        cmd5="./build_security_tools.sh",
        ready_state=True, ready_cursor=False
    ), 300)

# Final hold before seamless restart
add_frame(render_state(
    cmd1=typed_whoami, out1=True, cmd2="cat profile.txt", profile_stage=3,
    cmd3="./current-focus.sh", focus_count=4,
    cmd4="./recon.sh", recon_stage=5,
    cmd5="./build_security_tools.sh",
    ready_state=True, ready_cursor=True
), 1600)

total_ms = sum(durations)
print(f"Total 2x frames: {len(frames_2x)}, Total duration: {total_ms / 1000.0:.2f}s")

# Downsample to 1x with Lanczos antialiasing and optimize palette
print("Downsampling to 1x and generating optimized GIF palette...")
final_frames = []
for f in frames_2x:
    f_1x = f.resize((W1, H1), Image.Resampling.LANCZOS)
    p_img = f_1x.convert("P", palette=Image.Palette.ADAPTIVE, colors=128)
    final_frames.append(p_img)

output_path = os.path.join(os.path.dirname(__file__), "assets", "header.gif")
final_frames[0].save(
    output_path,
    save_all=True,
    append_images=final_frames[1:],
    duration=durations,
    loop=0,
    optimize=True
)

kb = os.path.getsize(output_path) / 1024
print(f"Successfully generated Kali Linux animated header GIF: {output_path} ({kb:.1f} KB, {len(final_frames)} frames)")
