import streamlit as st
import streamlit.components.v1 as components
import base64
import os
import requests
from google import genai

st.set_page_config(
    page_title="LEXI // LexiTech AI Core",
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

# --- CYBER-PLUM UI + ZERO WHITE BAR + HOLOGRAPHIC GLOW ---
st.markdown("""
<style>
@import url('https://googleapis.com');

/* Force deep cyber-plum background everywhere & kill white bars */
html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"],
[data-testid="stBottom"], [data-testid="stBottom"] > div,
[data-testid="stBottomBlockContainer"], .stChatFloatingInputContainer {
    background-color: #12050D !important;
    background: #12050D !important;
    color: #FFF5FA !important;
    font-family: 'Inter', sans-serif !important;
}

/* Hide Streamlit default chrome */
#MainMenu, footer, header, [data-testid="stToolbar"], [data-testid="stDecoration"] {
    display: none !important;
    visibility: hidden !important;
}

/* Make main container float cleanly over the falling code canvas */
.block-container {
    position: relative;
    z-index: 2;
    padding-top: 1.5rem !important;
    padding-bottom: 6rem !important;
    max-width: 780px !important;
}

/* Holographic Header Badge */
.lexi-badge {
    display: inline-block;
    padding: 6px 18px;
    border-radius: 999px;
    border: 1px solid rgba(255, 42, 133, 0.65);
    background: rgba(255, 42, 133, 0.12);
    box-shadow: 0 0 18px rgba(255, 42, 133, 0.35);
    font-family: 'Orbitron', sans-serif;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 2.5px;
    color: #FF7EB6;
    text-transform: uppercase;
    margin-bottom: 14px;
}

/* Holographic Avatar Frame */
.avatar-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-bottom: 18px;
}

.avatar-frame {
    position: relative;
    width: 195px;
    height: 245px;
    border-radius: 22px;
    padding: 3px;
    background: linear-gradient(145deg, #FF2A85, #791848, #FF2A85);
    box-shadow: 0 0 35px rgba(255, 42, 133, 0.45), inset 0 0 20px rgba(255, 42, 133, 0.3);
    overflow: hidden;
}

.avatar-frame img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 19px;
    display: block;
}

.lexi-subtitle {
    margin-top: 10px;
    font-family: 'Orbitron', sans-serif;
    font-size: 0.78rem;
    letter-spacing: 1.8px;
    color: rgba(255, 245, 250, 0.75);
}

/* Module Pill Links */
.module-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    margin: 14px 0 22px 0;
}

.module-pill {
    text-align: center;
    padding: 9px 10px;
    border-radius: 999px;
    background: rgba(34, 10, 24, 0.85);
    border: 1px solid rgba(255, 42, 133, 0.55);
    color: #FFF5FA !important;
    text-decoration: none !important;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    box-shadow: 0 0 14px rgba(255, 42, 133, 0.22);
    transition: all 0.2s ease;
    backdrop-filter: blur(8px);
}

.module-pill:hover {
    background: linear-gradient(90deg, #FF2A85, #C81964);
    border-color: #FF85B8;
    box-shadow: 0 0 22px rgba(255, 42, 133, 0.65);
    transform: translateY(-1px);
}

/* Chat Messages Styling */
[data-testid="stChatMessage"] {
    background: rgba(28, 8, 20, 0.82) !important;
    border: 1px solid rgba(255, 42, 133, 0.35) !important;
    border-radius: 16px !important;
    padding: 14px 18px !important;
    margin-bottom: 12px !important;
    backdrop-filter: blur(10px) !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.45) !important;
}

[data-testid="stChatMessage"] p, [data-testid="stChatMessage"] li, [data-testid="stChatMessage"] span {
    color: #FFF5FA !important;
    font-size: 0.95rem !important;
    line-height: 1.55 !important;
}

/* Bottom Chat Input Box - Sleek Cyber-Plum Glass */
[data-testid="stChatInput"] {
    background: rgba(26, 7, 18, 0.95) !important;
    border: 1px solid #FF2A85 !important;
    border-radius: 16px !important;
    box-shadow: 0 0 24px rgba(255, 42, 133, 0.35) !important;
}

[data-testid="stChatInput"] textarea {
    color: #FFF5FA !important;
    background: transparent !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: rgba(255, 245, 250, 0.55) !important;
}

[data-testid="stChatInputSubmitButton"] {
    background: #FF2A85 !important;
    color: #FFF5FA !important;
    border-radius: 10px !important;
}

@media (max-width: 640px) {
    .module-grid { grid-template-columns: repeat(2, 1fr); }
}
</style>
""", unsafe_allow_html=True)

# --- FAINT FALLING DIGITAL CODE RAIN BACKGROUND ---
components.html("""
<script>
const parentDoc = window.parent.document;
if (!parentDoc.getElementById('lexi-matrix-canvas')) {
    const canvas = parentDoc.createElement('canvas');
    canvas.id = 'lexi-matrix-canvas';
    canvas.style.position = 'fixed';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100vw';
    canvas.style.height = '100vh';
    canvas.style.zIndex = '0';
    canvas.style.pointerEvents = 'none';
    canvas.style.opacity = '0.22';
    parentDoc.body.prepend(canvas);

    const ctx = canvas.getContext('2d');
    const resize = () => {
        canvas.width = window.parent.innerWidth;
        canvas.height = window.parent.innerHeight;
    };
    resize();
    window.parent.addEventListener('resize', resize);

    const chars = '01LEXITECH§¶∆∑Ω10987654321ABCDEF';
    const fontSize = 14;
    let columns = Math.floor(canvas.width / fontSize);
    let drops = Array(columns).fill(1);

    setInterval(() => {
        ctx.fillStyle = 'rgba(18, 5, 13, 0.12)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#FF2A85';
        ctx.font = fontSize + 'px monospace';

        for (let i = 0; i < drops.length; i++) {
            const text = chars.charAt(Math.floor(Math.random() * chars.length));
            ctx.fillText(text, i * fontSize, drops.at(i) * fontSize);
            if (drops.at(i) * fontSize > canvas.height && Math.random() > 0.975) {
                drops.splice(i, 1, 0);
            } else {
                drops.splice(i, 1, drops.at(i) + 1);
            }
        }
    }, 55);
}
</script>
""", height=0, width=0)
# --- HOLOGRAPHIC AVATAR & STUDIO NAVIGATION ---
avatar_html = f'<img src="{avatar_src}" alt="LEXI Core">' if avatar_src else '<div style="color:#FF2A85;padding-top:100px;text-align:center;">LEXI CORE</div>'

st.markdown(f"""
<div class="avatar-wrapper">
    <div class="lexi-badge">LEXI // HOLOGRAPHIC AI CORE</div>
    <div class="avatar-frame">
        {avatar_html}
    </div>
    <div class="lexi-subtitle">LEXITECH LEGAL &amp; TAX INTELLIGENCE</div>
</div>

<div class="module-grid">
    <a class="module-pill" href="https://github.io" target="_blank">Studio Home</a>
    <a class="module-pill" href="https://streamlit.app" target="_blank">Module 01</a>
    <a class="module-pill" href="https://streamlit.app" target="_blank">Module 02</a>
    <a class="module-pill" href="https://streamlit.app" target="_blank">Module 03</a>
</div>
""", unsafe_allow_html=True)

# --- ELEVENLABS PAIGE VOICE SYNTHESIS ---
def speak_paige(text):
    el_key = st.secrets.get("ELEVENLABS_API_KEY", "")
    if not el_key:
        return None
    voice_id = "yM93hbw8Qtvdma2wCnJG"
    url = f"https://elevenlabs.io{voice_id}"
    headers = {
        "xi-api-key": el_key,
        "Content-Type": "application/json"
    }
    clean_text = text.replace("*", "").replace("#", "")[:600]
    payload = {
        "text": clean_text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.45, "similarity_boost": 0.78}
    }
    try:
        r = requests.post(url, json=payload, headers=headers, timeout=15)
        if r.status_code == 200:
            return r.content
    except Exception:
        return None
    return None

# --- CHAT HISTORY & GEMINI 2.5 FLASH ENGINE ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "LexiTech AI Core online. Ask me about contract traps, IRS tax rules, or any LexiTech module."}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

sys_prompt = (
    "You are LEXI, the holographic AI assistant for LexiTech Legal & Tax AI Studio, founded by Heidi Seckman. "
    "Be sharp, concise, helpful, and authoritative on legal concepts, contract red flags, and IRS tax guidance. "
    "Include a brief note that insights are informational and not formal legal or tax representation."
)

if prompt := st.chat_input("Ask Lexi anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("LEXI is analyzing..."):
            api_key = st.secrets.get("GEMINI_API_KEY", "") or st.secrets.get("GOOGLE_API_KEY", "")
            if not api_key:
                reply = "⚠️ `GEMINI_API_KEY` is missing in Streamlit Cloud Secrets. Add it under **App Settings → Secrets**."
            else:
                history_lines = []
                for m in st.session_state.messages[-8:]:
                    role_label = "User" if m["role"] == "user" else "LEXI"
                    history_lines.append(f"{role_label}: {m['content']}")
                full_prompt = f"{sys_prompt}\n\n" + "\n".join(history_lines) + "\nLEXI:"

                try:
                    client = genai.Client(api_key=api_key)
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=full_prompt
                    )
                    reply = response.text or "No response returned."
                except Exception as e:
                    reply = f"⚠️ **API Connection Issue:** `{str(e)}`\n\nDouble-check that your `GEMINI_API_KEY` in Streamlit Secrets has no extra quotes/spaces and is active."

            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

            audio_bytes = speak_paige(reply)
            if audio_bytes:
                st.audio(audio_bytes, format="audio/mp3", autoplay=True)
