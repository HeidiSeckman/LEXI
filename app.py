import streamlit as st
import base64
import os
import random
import time
import requests
from google import genai

st.set_page_config(
    page_title="LEXI // LexiTech Neural Core",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

avatar_b64 = get_base64_image("LEXI_avatar.png")
avatar_src = f"data:image/png;base64,{avatar_b64}" if avatar_b64 else ""

# --- FAINT FALLING DIGITAL CODE RAIN ---
random.seed(7)
code_chars = "01011001ABCDEF01§∆011001"
rain_columns = []
for i in range(36):
    left_pos = round(i * (100 / 36) + 0.5, 2)
    dur = round(random.uniform(9.0, 19.0), 2)
    del_sec = round(random.uniform(-18.0, 0.0), 2)
    strand = "".join(f"<span>{random.choice(code_chars)}</span>" for _ in range(30))
    rain_columns.append(
        f'<div class="rain-col" style="left:{left_pos}%;animation-duration:{dur}s;animation-delay:{del_sec}s;">{strand}</div>'
    )
falling_code_layer = f'<div class="cyber-bg"><div class="cyber-grid"></div>{"".join(rain_columns)}</div>'

# --- LEXITECH STUDIO CYBER-FORENSIC THEME ---
st.markdown(f"""
<style>
@import url('https://googleapis.com');

html, body {{
    background-color: #050205 !important;
    color: #FFF5FA !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    overflow-x: hidden;
}}

.stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"], section.main {{
    background: transparent !important;
    background-color: transparent !important;
}}

#MainMenu, footer, header, [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"] {{
    display: none !important;
    visibility: hidden !important;
}}

[data-testid="stBottom"], [data-testid="stBottom"] > div,
[data-testid="stBottomBlockContainer"], .stChatFloatingInputContainer {{
    background: linear-gradient(180deg, rgba(5,2,5,0) 0%, rgba(5,2,5,0.95) 28%, #050205 100%) !important;
    border-top: none !important;
}}

.cyber-bg {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 0;
    pointer-events: none;
    overflow: hidden;
    background:
        radial-gradient(circle at 50% 14%, rgba(255, 42, 133, 0.16) 0%, rgba(18, 5, 13, 0.85) 45%, #050205 100%);
}}

.cyber-grid {{
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(to right, rgba(255, 42, 133, 0.045) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 42, 133, 0.045) 1px, transparent 1px);
    background-size: 44px 44px;
}}

.rain-col {{
    position: absolute;
    top: -100%;
    display: flex;
    flex-direction: column;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    line-height: 18px;
    color: rgba(255, 65, 150, 0.28);
    text-shadow: 0 0 6px rgba(255, 42, 133, 0.35);
    user-select: none;
    animation-name: digitalFall;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
}}

.rain-col span:nth-child(4n) {{
    color: rgba(255, 150, 200, 0.42);
}}

@keyframes digitalFall {{
    0%   {{ transform: translateY(-10vh); opacity: 0; }}
    10%  {{ opacity: 1; }}
    90%  {{ opacity: 0.9; }}
    100% {{ transform: translateY(210vh); opacity: 0; }}
}}

.block-container {{
    position: relative;
    z-index: 2;
    padding-top: 1.2rem !important;
    padding-bottom: 6.5rem !important;
    max-width: 820px !important;
}}

.studio-navbar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 20px;
    margin-bottom: 18px;
    border-radius: 16px;
    background: rgba(16, 5, 12, 0.78);
    border: 1px solid rgba(255, 42, 133, 0.35);
    box-shadow: 0 0 25px rgba(255, 42, 133, 0.12);
    backdrop-filter: blur(14px);
}}

.studio-brand {{
    font-family: 'Orbitron', sans-serif;
    font-size: 0.9rem;
    font-weight: 800;
    letter-spacing: 2.5px;
    color: #FF4D9A;
    text-shadow: 0 0 12px rgba(255, 42, 133, 0.45);
}}

.nav-pills {{
    display: flex;
    gap: 10px;
    align-items: center;
}}

.nav-btn-primary {{
    padding: 6px 15px;
    border-radius: 999px;
    background: linear-gradient(90deg, #FF2A85, #D81B6B);
    color: #FFF5FA !important;
    text-decoration: none !important;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.8px;
    box-shadow: 0 0 16px rgba(255, 42, 133, 0.5);
}}

.nav-btn-outline {{
    padding: 6px 14px;
    border-radius: 999px;
    background: rgba(255, 42, 133, 0.08);
    border: 1px solid rgba(255, 42, 133, 0.45);
    color: #FFD6E8 !important;
    text-decoration: none !important;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.8px;
}}

.nav-btn-outline:hover {{
    border-color: #FF2A85;
    background: rgba(255, 42, 133, 0.22);
}}

.lexi-hero-card {{
    display: flex;
    align-items: center;
    gap: 24px;
    padding: 22px 26px;
    margin-bottom: 16px;
    border-radius: 20px;
    background: rgba(16, 5, 12, 0.76);
    border: 1px solid rgba(255, 42, 133, 0.42);
    box-shadow: 0 0 34px rgba(255, 42, 133, 0.16), inset 0 0 24px rgba(255, 42, 133, 0.08);
    backdrop-filter: blur(16px);
}}

.lexi-avatar-box {{
    flex-shrink: 0;
    width: 126px;
    height: 152px;
    border-radius: 16px;
    padding: 2px;
    background: linear-gradient(145deg, #FF2A85, #4B0D2C, #FF7EB6);
    box-shadow: 0 0 26px rgba(255, 42, 133, 0.45);
}}

.lexi-avatar-box img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top center;
    border-radius: 14px;
    display: block;
}}

.lexi-hero-copy {{
    flex: 1;
}}

.eyebrow-pill {{
    display: inline-block;
    padding: 4px 12px;
    border-radius: 999px;
    background: rgba(255, 42, 133, 0.14);
    border: 1px solid rgba(255, 42, 133, 0.45);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 1.5px;
    color: #FF85B8;
    margin-bottom: 8px;
}}

.lexi-hero-title {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 1.55rem;
    font-weight: 700;
    color: #FFF5FA;
    margin: 0 0 6px 0;
    line-height: 1.2;
}}

.lexi-hero-desc {{
    font-size: 0.88rem;
    color: rgba(255, 235, 245, 0.78);
    line-height: 1.5;
    margin: 0;
}}

div.stButton > button {{
    width: 100%;
    border-radius: 14px !important;
    background: rgba(18, 6, 14, 0.82) !important;
    border: 1px solid rgba(255, 42, 133, 0.42) !important;
    color: #FFF5FA !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 0.8rem !important;
    font-weight: 600 !important;
    padding: 0.65rem 0.85rem !important;
    box-shadow: 0 0 18px rgba(255, 42, 133, 0.12) !important;
    backdrop-filter: blur(12px) !important;
    transition: all 0.2s ease !important;
}}

div.stButton > button:hover {{
    background: linear-gradient(90deg, rgba(255, 42, 133, 0.28), rgba(184, 20, 91, 0.35)) !important;
    border-color: #FF2A85 !important;
    box-shadow: 0 0 24px rgba(255, 42, 133, 0.45) !important;
    transform: translateY(-1px);
}}

[data-testid="stChatMessage"] {{
    background: rgba(16, 5, 12, 0.8) !important;
    border: 1px solid rgba(255, 42, 133, 0.32) !important;
    border-radius: 16px !important;
    padding: 14px 18px !important;
    margin-bottom: 12px !important;
    backdrop-filter: blur(14px) !important;
    box-shadow: 0 6px 24px rgba(0, 0, 0, 0.55) !important;
}}

[data-testid="stChatMessage"] p, [data-testid="stChatMessage"] li, [data-testid="stChatMessage"] span {{
    color: #FFF5FA !important;
    font-size: 0.94rem !important;
    line-height: 1.6 !important;
}}

[data-testid="stChatInput"] {{
    background: rgba(16, 5, 12, 0.94) !important;
    border: 1px solid rgba(255, 42, 133, 0.72) !important;
    border-radius: 16px !important;
    box-shadow: 0 0 28px rgba(255, 42, 133, 0.28) !important;
    backdrop-filter: blur(16px) !important;
}}

[data-testid="stChatInput"] textarea {{
    color: #FFF5FA !important;
    background: transparent !important;
}}

[data-testid="stChatInput"] textarea::placeholder {{
    color: rgba(255, 235, 245, 0.5) !important;
}}

[data-testid="stChatInputSubmitButton"] {{
    background: #FF2A85 !important;
    color: #FFF5FA !important;
    border-radius: 10px !important;
}}

@media (max-width: 640px) {{
    .lexi-hero-card {{ flex-direction: column; text-align: center; }}
    .studio-navbar {{ flex-direction: column; gap: 10px; }}
}}
</style>
{falling_code_layer}
""", unsafe_allow_html=True)

# --- STUDIO NAVBAR + HOLOGRAPHIC LEXI HERO CARD ---
avatar_img_tag = f'<img src="{avatar_src}" alt="LEXI Core">' if avatar_src else '<div style="color:#FF2A85;padding-top:60px;text-align:center;font-weight:700;">LEXI</div>'

st.markdown(f"""
<div class="studio-navbar">
    <div class="studio-brand">LEXITECH</div>
    <div class="nav-pills">
        <span class="nav-btn-primary">● LEXI NEURAL CORE</span>
        <a class="nav-btn-outline" href="https://github.io" target="_blank">STUDIO HOME ↗</a>
        <a class="nav-btn-outline" href="https://github.com" target="_blank">GITHUB STUDIO ↗</a>
    </div>
</div>

<div class="lexi-hero-card">
    <div class="lexi-avatar-box">{avatar_img_tag}</div>
    <div class="lexi-hero-copy">
        <div class="eyebrow-pill">CLOSED-BOOK LEGAL &amp; TAX AI CONCIERGE</div>
        <div class="lexi-hero-title">LEXI // Forensic AI Core</div>
        <p class="lexi-hero-desc">
            Interactive AI strategist engineered by Heidi Seckman to flag hidden contract traps, cross-check IRS publication rules, and simulate worst-case life event risks.
        </p>
    </div>
</div>
