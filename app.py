import streamlit as st
import base64
import os
import random
import re
import requests

from google import genai
from google.genai import types

# ------------------------------------------------------------
# LEXI // LexiTech — Gemini primary + Groq backup
# Existing Streamlit design, chat, memory pin, and ElevenLabs
# voice are preserved. All providers are optional and use
# user-supplied API keys stored in Streamlit Secrets.
# ------------------------------------------------------------

st.set_page_config(
    page_title="LEXI // LexiTech",
    page_icon="✨",
    layout="centered",
)

# ---------- Secrets ----------
def get_secret(name, fallback=""):
    try:
        value = st.secrets.get(name, fallback)
        return str(value).strip() if value else fallback
    except Exception:
        return fallback

GEMINI_KEY = get_secret("GEMINI_API_KEY") or get_secret("GOOGLE_API_KEY")
GROQ_KEY = get_secret("GROQ_API_KEY")
ELEVEN_KEY = get_secret("ELEVENLABS_API_KEY")

# ---------- Avatar ----------
avatar_path = "LEXI_avatar.png"
avatar_data = ""
if os.path.exists(avatar_path):
    try:
        with open(avatar_path, "rb") as avatar_file:
            avatar_data = (
                "data:image/png;base64,"
                + base64.b64encode(avatar_file.read()).decode("utf-8")
            )
    except OSError:
        avatar_data = ""

# ---------- Background animation ----------
random.seed(7)
columns = []
for i in range(28):
    symbols = "<br>".join(random.choice("01LEXI§∆") for _ in range(25))
    columns.append(
        f'<div class="rc" style="left:{i * 3.5}%;'
        f'animation-duration:{random.randint(9, 17)}s;'
        f'animation-delay:-{random.randint(1, 15)}s">{symbols}</div>'
    )

css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&family=Orbitron:wght@700&family=JetBrains+Mono&display=swap');
html,body,.stApp,[data-testid="stAppViewContainer"],[data-testid="stMain"]{
 background:#050205!important;color:#FFF5FA!important;
 font-family:'Plus Jakarta Sans',sans-serif!important
}
#MainMenu,footer,header,[data-testid="stHeader"],[data-testid="stToolbar"]{
 display:none!important
}
[data-testid="stBottom"],[data-testid="stBottom"]>div,
[data-testid="stBottomBlockContainer"]{background:#050205!important}
.bg{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden;
 background:radial-gradient(circle at 50% 15%,rgba(255,42,133,.16),#050205 65%)}
.rc{position:absolute;top:-100%;font:12px 'JetBrains Mono',monospace;
 color:rgba(255,65,150,.28);animation:f linear infinite}
@keyframes f{to{transform:translateY(210vh)}}
@keyframes floatAv{0%,100%{transform:translateY(0px)}50%{transform:translateY(-6px)}}
@keyframes auraPulse{
 0%,100%{box-shadow:0 0 18px rgba(255,42,133,.55),0 0 36px rgba(255,42,133,.25)}
 50%{box-shadow:0 0 32px rgba(255,42,133,.95),0 0 64px rgba(249,168,212,.55)}
}
.block-container{position:relative;z-index:2;max-width:780px!important}
.card{display:flex;align-items:center;gap:20px;padding:18px;border-radius:18px;
 background:rgba(16,5,12,.82);border:1px solid rgba(255,42,133,.45);margin-bottom:14px}
.card img{width:110px;height:135px;object-fit:cover;border-radius:14px;
 border:2px solid #FF2A85;animation:floatAv 3.4s ease-in-out infinite,
 auraPulse 2.4s ease-in-out infinite;transition:transform .15s ease,box-shadow .15s ease}
.card img.speaking{border-color:#F9A8D4;
 box-shadow:0 0 42px #FF2A85,0 0 80px rgba(249,168,212,.85)!important}
div.stButton>button{width:100%;border-radius:12px!important;
 background:rgba(18,6,14,.85)!important;border:1px solid rgba(255,42,133,.45)!important;
 color:#FFF5FA!important;font-weight:600!important}
[data-testid="stAudioInput"]{background:rgba(18,6,14,.85)!important;
 border:1px solid rgba(255,42,133,.55)!important;border-radius:14px!important;padding:8px!important}
[data-testid="stChatMessage"]{background:rgba(16,5,12,.85)!important;
 border:1px solid rgba(255,42,133,.35)!important;border-radius:14px!important}
[data-testid="stChatMessage"] p{color:#FFF5FA!important}
[data-testid="stChatInput"]{background:#10050C!important;border:1px solid #FF2A85!important;
 border-radius:14px!important}
[data-testid="stChatInput"] textarea{color:#FFF5FA!important}
.status{font-size:12px;color:#FFD6E8;opacity:.9;margin:4px 0 12px}
</style>
"""

avatar_html = f'<img id="lexi-av" src="{avatar_data}">' if avatar_data else ""
header_html = (
    css
    + '<div class="bg">' + "".join(columns) + '</div>'
    + f'<div class="card">{avatar_html}<div>'
    + '<div style="font:700 13px Orbitron;color:#FF4D9A">LEXITECH // NEURAL CORE v4</div>'
    + '<h3 style="margin:4px 0;color:#FFF5FA">LEXI</h3>'
    + '<p style="margin:0;font-size:14px;color:#FFD6E8">'
    + 'Forensic legal, tax &amp; execution partner built for you.</p>'
    + '</div></div>'
)
st.markdown(header_html, unsafe_allow_html=True)

# ---------- Memory pin ----------
with st.expander(
    "🧠 Studio Memory Pin (Optional Context LEXI Always Remembers)",
    expanded=False,
):
    mem_note = st.text_input(
        "Active focus, project, or rule for LEXI:",
        value="Building LexiTech Studio AI modules & protecting contracts/tax strategy.",
        label_visibility="collapsed",
    )

# ---------- Provider status ----------
if GEMINI_KEY and GROQ_KEY:
    provider_status = "🟢 Gemini primary · Groq backup ready"
elif GEMINI_KEY:
    provider_status = "🟡 Gemini ready · Add GROQ_API_KEY for independent backup"
elif GROQ_KEY:
    provider_status = "🟡 Groq ready · Gemini key not configured"
else:
    provider_status = "🔴 Add a Gemini or Groq API key in Streamlit Secrets"
st.markdown(f'<div class="status">{provider_status}</div>', unsafe_allow_html=True)

# ---------- Quick prompts ----------
c1, c2, c3 = st.columns(3)
b1 = c1.button("⚖️ Contract Traps")
b2 = c2.button("🧾 IRS Tax Check")
b3 = c3.button("⚡ Risk Stress-Test")

quick_prompt = None
if b1:
    quick_prompt = "What are the top 3 hidden contract traps people miss, and how do I counter each?"
elif b2:
    quick_prompt = "What are the biggest IRS tax traps for 1099 contractors right now?"
elif b3:
    quick_prompt = "What 3 protective clauses save someone in a sudden life emergency?"

# ---------- Chat history ----------
if "m" not in st.session_state:
    st.session_state["m"] = [{
        "role": "assistant",
        "content": "Hey there! Neural core upgraded and locked in. What are we strategizing or building right now?",
    }]

for message in st.session_state["m"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------- Voice and text input ----------
mic = st.audio_input("🎙️ Tap to talk to LEXI")
typed = st.chat_input("Talk to LEXI...")

# ---------- Provider functions ----------
SYSTEM_PROMPT = (
    "You are LEXI, an advanced, fact-driven research and execution partner. "
    "Provide expert-level assistance across science, law, medicine, history, "
    "engineering, coding, finance, and other subjects. Prioritize verified facts "
    "from authoritative sources. Use available web search tools when current "
    "information or external verification is needed. Never fabricate facts, "
    "citations, sources, statistics, or events. Clearly distinguish established "
    "facts from theories, estimates, and opinions. If you cannot verify something, "
    "say so rather than guessing. For legal, tax, and medical topics, explain "
    "important limitations and encourage checking authoritative or professional "
    "sources. Be intelligent, analytical, direct, and thorough while remaining useful."
)

def gemini_answer(prompt, history_text, memory_text):
    """Try Gemini with Google Search grounding."""
    client = genai.Client(api_key=GEMINI_KEY)
    full_prompt = (
        f"Active Focus / Studio Memory: {memory_text}\n\n"
        f"Conversation:\n{history_text}\n\n"
        f"LEXI, respond to the latest user message."
    )
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=full_prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature=0.1,
            tools=[types.Tool(google_search=types.GoogleSearch())],
        ),
    )
    answer = (response.text or "").strip()
    if not answer:
        raise RuntimeError("Gemini returned an empty response.")
    return answer

def groq_answer(history, memory_text):
    """Independent fallback using Groq's OpenAI-compatible chat API."""
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "openai/gpt-oss-120b",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        SYSTEM_PROMPT
                        + "\n\nActive Focus / Studio Memory: "
                        + memory_text
                        + "\n\nYou are operating in backup mode. Do not claim "
                        "to have performed live web research unless a tool result "
                        "is actually provided. If the question requires current "
                        "facts, clearly say that live verification is unavailable "
                        "in this backup response."
                    ),
                },
                *history,
            ],
            "temperature": 0.2,
            "max_tokens": 1800,
        },
        timeout=60,
    )
    if response.status_code != 200:
        raise RuntimeError(
            f"Groq API error {response.status_code}: {response.text[:350]}"
        )
    data = response.json()
    answer = data["choices"][0]["message"]["content"].strip()
    if not answer:
        raise RuntimeError("Groq returned an empty response.")
    return answer

def transcribe_with_gemini(audio_bytes):
    client = genai.Client(api_key=GEMINI_KEY)
    result = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=[
            "Transcribe the spoken audio accurately. Return only the words spoken.",
            types.Part.from_bytes(data=audio_bytes, mime_type="audio/wav"),
        ],
    )
    text = (result.text or "").strip()
    if not text:
        raise RuntimeError("Gemini could not transcribe the audio.")
    return text

def transcribe_with_groq(audio_bytes):
    response = requests.post(
        "https://api.groq.com/openai/v1/audio/transcriptions",
        headers={"Authorization": f"Bearer {GROQ_KEY}"},
        files={"file": ("lexi_audio.wav", audio_bytes, "audio/wav")},
        data={"model": "whisper-large-v3-turbo", "response_format": "json"},
        timeout=60,
    )
    if response.status_code != 200:
        raise RuntimeError(
            f"Groq transcription error {response.status_code}: {response.text[:250]}"
        )
    transcript = (response.json().get("text") or "").strip()
    if not transcript:
        raise RuntimeError("Groq could not transcribe the audio.")
    return transcript

def speak_with_elevenlabs(text_to_speak):
    """Return MP3 bytes from the configured ElevenLabs voice."""
    if not ELEVEN_KEY or not text_to_speak:
        return None

    speech_text = re.sub(r"\s+", " ", text_to_speak)
    speech_text = re.sub(r"[*#`_~>|/]+", " ", speech_text).strip()[:700]
    if not speech_text:
        return None

    # Preserve the two voice IDs from the user's original app.
    voice_ids = ["cgSgspJ2msm6clMCkdW9", "9BWtsMINqrJLrRacOk9x"]
    for voice_id in voice_ids:
        try:
            result = requests.post(
                f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
                json={
                    "text": speech_text,
                    "model_id": "eleven_multilingual_v2",
                    "voice_settings": {
                        "stability": 0.42,
                        "similarity_boost": 0.82,
                    },
                },
                headers={
                    "xi-api-key": ELEVEN_KEY,
                    "Content-Type": "application/json",
                },
                timeout=30,
            )
            if result.status_code == 200:
                return result.content
            # If a voice ID is invalid or unavailable, try the next one.
        except requests.RequestException:
            continue
    return None

# ---------- Handle the current input ----------
user_prompt = quick_prompt or typed
input_error = None

if mic is not None:
    audio_bytes = mic.getvalue()
    audio_signature = base64.b64encode(audio_bytes[:64]).decode("ascii")
    if audio_bytes and audio_signature != st.session_state.get("last_mic_signature"):
        st.session_state["last_mic_signature"] = audio_signature
        with st.spinner("LEXI is listening..."):
            try:
                if GEMINI_KEY:
                    try:
                        user_prompt = transcribe_with_gemini(audio_bytes)
                    except Exception:
                        if GROQ_KEY:
                            user_prompt = transcribe_with_groq(audio_bytes)
                        else:
                            raise
                elif GROQ_KEY:
                    user_prompt = transcribe_with_groq(audio_bytes)
                else:
                    raise RuntimeError(
                        "Voice transcription needs a Gemini or Groq API key."
                    )
            except Exception as error:
                input_error = str(error)

if input_error:
    st.error(f"LEXI couldn't transcribe that audio: {input_error}")

if user_prompt:
    user_prompt = user_prompt.strip()
    if user_prompt:
        st.session_state["m"].append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.markdown(user_prompt)

        # Keep the same recent-conversation window as the original app.
        recent_messages = st.session_state["m"][-16:]
        history_text = "\n".join(
            ("Heidi: " if item["role"] == "user" else "LEXI: ")
            + item["content"]
            for item in recent_messages
        )

        # Groq uses chat-format history. The latest user message is included.
        groq_history = []
        for item in recent_messages:
            groq_history.append({
                "role": "user" if item["role"] == "user" else "assistant",
                "content": item["content"],
            })

        answer = ""
        active_provider = ""
        provider_errors = []

        with st.spinner("LEXI is thinking..."):
            if GEMINI_KEY:
                try:
                    answer = gemini_answer(
                        user_prompt,
                        history_text,
                        mem_note,
                    )
                    active_provider = "Gemini"
                except Exception as error:
                    provider_errors.append(f"Gemini: {str(error)[:260]}")

            # Independent provider failover if Gemini is unavailable or over quota.
            if not answer and GROQ_KEY:
                try:
                    answer = groq_answer(groq_history, mem_note)
                    active_provider = "Groq backup"
                except Exception as error:
                    provider_errors.append(f"Groq: {str(error)[:260]}")

        if not answer:
            detail = " | ".join(provider_errors) if provider_errors else (
                "No API key is configured."
            )
            answer = (
                "I'm here, but both intelligence connections are unavailable "
                "right now. Please check the API keys and provider limits in "
                "Streamlit Secrets.\n\n"
                f"Connection details: {detail}"
            )
            active_provider = "Connection issue"

        st.session_state["m"].append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.markdown(answer)
            st.caption(f"LEXI engine: {active_provider}")

        # ElevenLabs voice remains independent of the selected AI provider.
        if ELEVEN_KEY:
            with st.spinner("LEXI is preparing her voice..."):
                audio_output = speak_with_elevenlabs(answer)
            if audio_output:
                audio_b64 = base64.b64encode(audio_output).decode("ascii")
                audio_html = (
                    '<audio id="lexi-voice" controls autoplay '
                    f'src="data:audio/mpeg;base64,{audio_b64}" '
                    'style="width:100%;height:36px"></audio>'
                    '<script>'
                    'const a=document.getElementById("lexi-voice");'
                    'const v=document.getElementById("lexi-av");'
                    'if(a&&v){'
                    'a.onplay=()=>v.classList.add("speaking");'
                    'a.onended=()=>v.classList.remove("speaking");'
                    'a.onpause=()=>v.classList.remove("speaking");'
                    '}'
                    '</script>'
                )
                st.markdown(audio_html, unsafe_allow_html=True)
            else:
                st.caption(
                    "Text response is ready. ElevenLabs did not return audio; "
                    "check its API key, voice access, and free-tier quota."
                )
        else:
            st.caption(
                "Text response is ready. Add ELEVENLABS_API_KEY in Streamlit "
                "Secrets to enable spoken replies."
            )

# ---------- Small configuration reminder ----------
with st.expander("🔧 Connection setup"):
    st.write(
        "Add these keys under Streamlit → App → Settings → Secrets. "
        "Do not paste API keys into the chat or source code."
    )
    st.code(
        'GEMINI_API_KEY = "your-gemini-key"\n'
        'GROQ_API_KEY = "your-groq-key"\n'
        'ELEVENLABS_API_KEY = "your-elevenlabs-key"',
        language="toml",
    )
    st.caption(
        "Groq is an optional independent backup. Its free-tier limits apply. "
        "The Groq backup response does not currently perform live web search; "
        "Gemini retains Google Search grounding when Gemini is available."
    )
