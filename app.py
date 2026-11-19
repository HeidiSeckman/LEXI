import streamlit as st
from google import genai
from google.genai import types
import requests
import base64
import os

st.set_page_config(page_title="LEXI // Holographic AI", page_icon="✨", layout="centered")

PAIGE_VOICE_ID = "yM93hbw8Qtvdma2wCnJG"

def get_avatar_b64():
    if os.path.exists("LEXI_avatar.png"):
        with open("LEXI_avatar.png", "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode()
    return ""

AVATAR_DATA = get_avatar_b64()

st.markdown("""
<style>
.stApp, [data-testid="stAppViewContainer"], [data-testid="stBottom"], [data-testid="stBottom"] > div {
    background: #12050D !important;
    color: #FFF5FA !important;
}
.stApp {
    background: radial-gradient(circle at 50% 18%, #2E0E22 0%, #12050D 60%, #070205 100%) !important;
}
header, footer, #MainMenu { visibility: hidden; }
.holo-box { text-align: center; padding: 6px 0 10px; }
.holo-img {
    width: 220px; height: 265px; object-fit: contain;
    mix-blend-mode: screen;
    filter: drop-shadow(0 0 22px rgba(255, 42, 133, 0.85));
    animation: floatHolo 4s ease-in-out infinite;
}
@keyframes floatHolo { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-8px); } }
.holo-badge {
    display: inline-block; font-family: monospace; font-size: 11px; font-weight: 700;
    color: #F9A8D4; background: rgba(255, 42, 133, 0.2);
    border: 1px solid #FF2A85; border-radius: 999px; padding: 4px 14px; margin-bottom: 8px;
}
[data-testid="stChatMessage"] {
    background: rgba(34, 14, 27, 0.94) !important;
    border: 1px solid rgba(255, 42, 133, 0.45) !important;
    border-radius: 16px !important;
}
[data-testid="stChatMessage"] p, [data-testid="stChatMessage"] div, .stMarkdown p {
    color: #FFF5FA !important;
    font-size: 15px !important;
}
[data-testid="stChatInput"] textarea {
    background: #1E0C18 !important;
    color: #FFF5FA !important;
    border: 1.5px solid #FF2A85 !important;
}
.stLinkButton a {
    background: linear-gradient(135deg, #E11D74 0%, #88134D 100%) !important;
    color: #FFF !important; border: 1px solid #F9A8D4 !important; border-radius: 999px !important; font-weight: 700 !important;
}
</style>
""", unsafe_allow_html=True)

if AVATAR_DATA:
    st.markdown(f"""
    <div class="holo-box">
        <div class="holo-badge">LEXI // HOLOGRAPHIC AI CORE</div><br/>
        <img class="holo-img" src="{AVATAR_DATA}" alt="LEXI" />
    </div>
    """, unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
c1.link_button("Module 01", "https://streamlit.app", use_container_width=True)
c2.link_button("Module 02", "https://streamlit.app", use_container_width=True)
c3.link_button("Module 03", "https://streamlit.app", use_container_width=True)
c4.link_button("Cloud Vault", "https://streamlit.app", use_container_width=True)

def speak_paige(text: str):
    el_key = st.secrets.get("ELEVENLABS_API_KEY", "")
    if not el_key:
        st.warning("ELEVENLABS_API_KEY missing in Secrets.")
        return
    try:
        r = requests.post(
            f"https://elevenlabs.io{PAIGE_VOICE_ID}",
            headers={"xi-api-key": el_key, "Content-Type": "application/json"},
            json={"text": text, "model_id": "eleven_multilingual_v2", "voice_settings": {"stability": 0.42, "similarity_boost": 0.85}},
            timeout=15
        )
        if r.status_code == 200:
            b64 = base64.b64encode(r.content).decode()
            st.markdown(f'<audio autoplay><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>', unsafe_allow_html=True)
        else:
            st.warning(f"ElevenLabs Error {r.status_code}: {r.text}")
    except Exception as e:
        st.warning(f"Voice error: {e}")
if "lexi_chat" not in st.session_state:
    st.session_state.lexi_chat = [
        {"role": "assistant", "content": "Hi, I'm Lexi. Ask me anything, talk to me with the mic below, or jump straight into any of your four studio engines."}
    ]

for msg in st.session_state.lexi_chat:
    with st.chat_message(msg["role"], avatar="✨" if msg["role"] == "assistant" else "👤"):
        st.write(msg["content"])

voice_audio = st.audio_input("🎙 Speak to Lexi")
typed_text = st.chat_input("Ask Lexi anything...")

user_prompt = None
if typed_text:
    user_prompt = typed_text
elif voice_audio and voice_audio != st.session_state.get("last_audio"):
    st.session_state.last_audio = voice_audio
    user_prompt = ("audio", voice_audio.getvalue())

if user_prompt:
    gemini_key = st.secrets.get("GEMINI_API_KEY", "")
    if not gemini_key:
        st.error("Add GEMINI_API_KEY in Streamlit Cloud Secrets.")
        st.stop()

    client = genai.Client(api_key=gemini_key)
    sys_prompt = (
        "You are Lexi, a sharp, warm, witty, and deeply intelligent conversational AI partner created by Heidi Seckman "
        "for LexiTech Legal & Tax AI Studio. Talk naturally like a real person in 2 to 4 clear sentences. "
        "Never use markdown symbols like asterisks or bullet points because your replies are spoken aloud."
    )

    if isinstance(user_prompt, tuple):
        transcribe = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=["Transcribe exactly what the user said in this audio clip. Return only the words spoken.", types.Part.from_bytes(data=user_prompt, mime_type="audio/wav")]
        )
        user_text = (transcribe.text or "").strip()
    else:
        user_text = user_prompt

    if user_text:
        st.session_state.lexi_chat.append({"role": "user", "content": user_text})
        with st.chat_message("user", avatar="👤"):
            st.write(user_text)

        history_text = "\n".join([f"{m['role'].upper()}: {m['content']}" for m in st.session_state.lexi_chat[-12:]])
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{sys_prompt}\n\nConversation so far:\n{history_text}\n\nRespond naturally as Lexi:"
        )
        reply = (response.text or "Say that again?").replace("*", "").replace("#", "").strip()
        st.session_state.lexi_chat.append({"role": "assistant", "content": reply})

        with st.chat_message("assistant", avatar="✨"):
            st.write(reply)
            speak_paige(reply)
