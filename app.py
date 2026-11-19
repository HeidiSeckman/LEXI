import streamlit as st
import base64
import os
import random
import time
import requests
from google import genai

st.set_page_config(page_title="LEXI // LexiTech Neural Core", page_icon="✨", layout="centered", initial_sidebar_state="collapsed")

avatar_src = ("data:image/png;base64," + base64.b64encode(open("LEXI_avatar.png", "rb").read()).decode()) if os.path.exists("LEXI_avatar.png") else ""

random.seed(7)
glyphs = "01011001ABCDEF01§∆011001"
cols = [f'<div class="rain-col" style="left:{round(i*3.1+0.5,1)}%;animation-duration:{round(random.uniform(9.0,18.0),1)}s;animation-delay:{round(random.uniform(-16.0,0.0),1)}s;">' + "".join("<span>" + random.choice(glyphs) + "</span>" for _ in range(28)) + "</div>" for i in range(32)]

css_rules = [
    "@import url('https://googleapis.com');",
    "html, body { background-color: #050205 !important; color: #FFF5FA !important; font-family: 'Plus Jakarta Sans', sans-serif !important; overflow-x: hidden; }",
    ".stApp, [data-testid='stAppViewContainer'], [data-testid='stMain'], section.main { background: transparent !important; }",
    "#MainMenu, footer, header, [data-testid='stHeader'], [data-testid='stToolbar'], [data-testid='stDecoration'] { display: none !important; }",
    "[data-testid='stBottom'], [data-testid='stBottom'] > div, [data-testid='stBottomBlockContainer'], .stChatFloatingInputContainer { background: linear-gradient(180deg, rgba(5,2,5,0) 0%, #050205 30%) !important; border-top: none !important; }",
    ".cyber-bg { position: fixed; inset: 0; z-index: 0; pointer-events: none; overflow: hidden; background: radial-gradient(circle at 50% 14%, rgba(255,42,133,0.16) 0%, rgba(18,5,13,0.85) 45%, #050205 100%); }",
    ".cyber-grid { position: absolute; inset: 0; background-image: linear-gradient(to right, rgba(255,42,133,0.045) 1px, transparent 1px), linear-gradient(to bottom, rgba(255,42,133,0.045) 1px, transparent 1px); background-size: 44px 44px; }",
    ".rain-col { position: absolute; top: -100%; display: flex; flex-direction: column; font-family: 'JetBrains Mono', monospace; font-size: 12px; line-height: 18px; color: rgba(255,65,150,0.28); text-shadow: 0 0 6px rgba(255,42,133,0.35); user-select: none; animation: digitalFall linear infinite; }",
    ".rain-col span:nth-child(4n) { color: rgba(255,150,200,0.42); }",
    "@keyframes digitalFall { 0% { transform: translateY(-10vh); opacity: 0; } 10% { opacity: 1; } 90% { opacity: 0.9; } 100% { transform: translateY(210vh); opacity: 0; } }",
    ".block-container { position: relative; z-index: 2; padding-top: 1.2rem !important; padding-bottom: 6.5rem !important; max-width: 820px !important; }",
    ".studio-navbar { display: flex; justify-content: space-between; align-items: center; padding: 12px 20px; margin-bottom: 18px; border-radius: 16px; background: rgba(16,5,12,0.78); border: 1px solid rgba(255,42,133,0.35); backdrop-filter: blur(14px); }",
    ".studio-brand { font-family: 'Orbitron', sans-serif; font-size: 0.9rem; font-weight: 800; letter-spacing: 2.5px; color: #FF4D9A; }",
    ".nav-pills { display: flex; gap: 10px; align-items: center; }",
    ".nav-btn-primary { padding: 6px 15px; border-radius: 999px; background: linear-gradient(90deg, #FF2A85, #D81B6B); color: #FFF5FA !important; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; font-weight: 600; }",
    ".nav-btn-outline { padding: 6px 14px; border-radius: 999px; background: rgba(255,42,133,0.08); border: 1px solid rgba(255,42,133,0.45); color: #FFD6E8 !important; text-decoration: none !important; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; }",
    ".lexi-hero-card { display: flex; align-items: center; gap: 22px; padding: 20px 24px; margin-bottom: 16px; border-radius: 20px; background: rgba(16,5,12,0.76); border: 1px solid rgba(255,42,133,0.42); box-shadow: 0 0 34px rgba(255,42,133,0.16); backdrop-filter: blur(16px); }",
    ".lexi-avatar-box { flex-shrink: 0; width: 120px; height: 145px; border-radius: 16px; padding: 2px; background: linear-gradient(145deg, #FF2A85, #4B0D2C, #FF7EB6); box-shadow: 0 0 26px rgba(255,42,133,0.45); }",
    ".lexi-avatar-box img { width: 100%; height: 100%; object-fit: cover; object-position: top center; border-radius: 14px; display: block; }",
    ".eyebrow-pill { display: inline-block; padding: 4px 12px; border-radius: 999px; background: rgba(255,42,133,0.14); border: 1px solid rgba(255,42,133,0.45); font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; letter-spacing: 1.5px; color: #FF85B8; margin-bottom: 8px; }",
    ".lexi-hero-title { font-size: 1.5rem; font-weight: 700; color: #FFF5FA; margin: 0 0 6px 0; }",
    ".lexi-hero-desc { font-size: 0.88rem; color: rgba(255,235,245,0.78); line-height: 1.5; margin: 0; }",
    "div.stButton > button { width: 100%; border-radius: 14px !important; background: rgba(18,6,14,0.82) !important; border: 1px solid rgba(255,42,133,0.42) !important; color: #FFF5FA !important; font-size: 0.8rem !important; font-weight: 600 !important; padding: 0.65rem 0.85rem !important; backdrop-filter: blur(12px) !important; }",
    "div.stButton > button:hover { background: linear-gradient(90deg, rgba(255,42,133,0.28), rgba(184,20,91,0.35)) !important; border-color: #FF2A85 !important; }",
    "[data-testid='stChatMessage'] { background: rgba(16,5,12,0.8) !important; border: 1px solid rgba(255,42,133,0.32) !important; border-radius: 16px !important; padding: 14px 18px !important; margin-bottom: 12px !important; backdrop-filter: blur(14px) !important; }",
    "[data-testid='stChatMessage'] p, [data-testid='stChatMessage'] li, [data-testid='stChatMessage'] span { color: #FFF5FA !important; font-size: 0.94rem !important; line-height: 1.6 !important; }",
    "[data-testid='stChatInput'] { background: rgba(16,5,12,0.94) !important; border: 1px solid rgba(255,42,133,0.72) !important; border-radius: 16px !important; box-shadow: 0 0 28px rgba(255,42,133,0.28) !important; }",
    "[data-testid='stChatInput'] textarea { color: #FFF5FA !important; background: transparent !important; }",
    "[data-testid='stChatInputSubmitButton'] { background: #FF2A85 !important; color: #FFF5FA !important; border-radius: 10px !important; }"
]

st.markdown("<style>" + "\n".join(css_rules) + "</style>" + '<div class="cyber-bg"><div class="cyber-grid"></div>' + "".join(cols) + "</div>", unsafe_allow_html=True)

img_tag = f'<img src="{avatar_src}" alt="LEXI">' if avatar_src else '<div style="color:#FF2A85;padding-top:55px;text-align:center;font-weight:700;">LEXI</div>'
hero_html = (
    '<div class="studio-navbar"><div class="studio-brand">LEXITECH</div>'
    '<div class="nav-pills"><span class="nav-btn-primary">● LEXI NEURAL CORE</span>'
    '<a class="nav-btn-outline" href="https://github.io" target="_blank">STUDIO HOME ↗</a>'
    '<a class="nav-btn-outline" href="https://github.com" target="_blank">GITHUB ↗</a></div></div>'
    f'<div class="lexi-hero-card"><div class="lexi-avatar-box">{img_tag}</div>'
    '<div class="lexi-hero-copy"><div class="eyebrow-pill">CLOSED-BOOK LEGAL &amp; TAX AI CONCIERGE</div>'
    '<div class="lexi-hero-title">LEXI // Forensic AI Core</div>'
    '<p class="lexi-hero-desc">Interactive AI strategist engineered by Heidi Seckman to flag hidden contract traps, cross-check IRS publication rules, and simulate worst-case life event risks.</p></div></div>'
)
st.markdown(hero_html, unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
b1 = c1.button("01 // Contract Clause Audit")
b2 = c2.button("02 // Dual-Corpus Tax Trap")
b3 = c3.button("03 // Worst-Case Stress-Test")

quick_prompt = "Run a forensic contract audit checklist: what are the most dangerous indemnification, IP ownership, and auto-renewal clauses signers miss?" if b1 else ("Explain the top IRS tax traps when classifying independent contractors vs. employees and deducting home-office or software expenses." if b2 else ("Stress-test a standard service contract against a worst-case life event (medical emergency, sudden income loss, or force majeure). What protections should I demand?" if b3 else None))

st.session_state.setdefault("messages", [{"role": "assistant", "content": "LEXI Neural Core online. Paste a contract clause to audit, ask an IRS tax question, or tap one of the three forensic engines above."}])

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).markdown(msg["content"])

typed = st.chat_input("Ask LEXI about contract traps, IRS rules, or paste a clause...")
active = quick_prompt or typed

def try_gemini(key, prompt_text):
    client = genai.Client(api_key=key)
    for m in ["gemini-3.6-flash", "gemini-3.5-flash-lite", "gemini-3.7-flash"]:
        try:
            res = client.models.generate_content(model=m, contents=prompt_text)
            if res and res.text:
                return res.text
        except Exception as e:
            err = str(e)
            time.sleep(1.0)
    return f"⚠️ **Temporary Model Traffic Spike:** `{err}` — hit send again in a moment."

def try_paige(text):
    el_key = st.secrets.get("ELEVENLABS_API_KEY", "")
    if not el_key:
        return None
    clean = text.replace("*", "").replace("#", "").replace("`", "")[:600]
    try:
        r = requests.post("https://elevenlabs.io", json={"text": clean, "model_id": "eleven_multilingual_v2", "voice_settings": {"stability": 0.45, "similarity_boost": 0.78}}, headers={"xi-api-key": el_key, "Content-Type": "application/json"}, timeout=15)
        return r.content if r.status_code == 200 else None
    except Exception:
        return None

if active:
    st.session_state["messages"].append({"role": "user", "content": active})
    st.chat_message("user").markdown(active)
    key = st.secrets.get("GEMINI_API_KEY", "") or st.secrets.get("GOOGLE_API_KEY", "")
