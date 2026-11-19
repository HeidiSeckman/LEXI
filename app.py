import streamlit as st
import base64, os, random, re, requests
from google import genai

st.set_page_config(page_title="LEXI // LexiTech", page_icon="✨", layout="centered")
av = ("data:image/png;base64," + base64.b64encode(open("LEXI_avatar.png", "rb").read()).decode()) if os.path.exists("LEXI_avatar.png") else ""

random.seed(7)
cols = [f'<div class="rc" style="left:{i*3.5}%;animation-duration:{random.randint(9,17)}s;animation-delay:-{random.randint(1,15)}s">' + "<br>".join(random.choice("01LEXI§∆") for _ in range(25)) + "</div>" for i in range(28)]

css = """<style>
@import url('https://googleapis.com');
html,body,.stApp,[data-testid="stAppViewContainer"],[data-testid="stMain"]{background:#050205!important;color:#FFF5FA!important;font-family:'Plus Jakarta Sans',sans-serif!important}
#MainMenu,footer,header,[data-testid="stHeader"],[data-testid="stToolbar"]{display:none!important}
[data-testid="stBottom"],[data-testid="stBottom"]>div,[data-testid="stBottomBlockContainer"]{background:#050205!important}
.bg{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden;background:radial-gradient(circle at 50% 15%,rgba(255,42,133,.16),#050205 65%)}
.rc{position:absolute;top:-100%;font:12px 'JetBrains Mono',monospace;color:rgba(255,65,150,.28);animation:f linear infinite}
@keyframes f{to{transform:translateY(210vh)}}
.block-container{position:relative;z-index:2;max-width:780px!important}
.card{display:flex;align-items:center;gap:20px;padding:18px;border-radius:18px;background:rgba(16,5,12,.82);border:1px solid rgba(255,42,133,.45);margin-bottom:14px}
.card img{width:110px;height:135px;object-fit:cover;border-radius:12px;border:2px solid #FF2A85}
[data-testid="stChatMessage"]{background:rgba(16,5,12,.85)!important;border:1px solid rgba(255,42,133,.35)!important;border-radius:14px!important}
[data-testid="stChatMessage"] p{color:#FFF5FA!important}
[data-testid="stChatInput"]{background:#10050C!important;border:1px solid #FF2A85!important;border-radius:14px!important}
[data-testid="stChatInput"] textarea{color:#FFF5FA!important}
</style>"""

img = f'<img src="{av}">' if av else ""
st.markdown(css + '<div class="bg">' + "".join(cols) + f'</div><div class="card">{img}<div><div style="font:700 13px Orbitron;color:#FF4D9A">LEXITECH // NEURAL CORE</div><h3 style="margin:4px 0;color:#FFF5FA">LEXI // Conversational AI</h3><p style="margin:0;font-size:14px;color:#FFD6E8">Legal &amp; tax strategist by Heidi Seckman. Talk to me like a real teammate.</p></div></div>', unsafe_allow_html=True)

st.session_state.setdefault("m", [{"role": "assistant", "content": "Hey Heidi! I'm online and ready. What are we working on?"}])
for x in st.session_state["m"]:
    st.chat_message(x["role"]).markdown(x["content"])

q = st.chat_input("Talk to LEXI...")
if q:
    st.session_state["m"].append({"role": "user", "content": q})
    st.chat_message("user").markdown(q)
    gk = st.secrets.get("GEMINI_API_KEY", "") or st.secrets.get("GOOGLE_API_KEY", "")
    hist = "\n".join(("Heidi: " if x["role"] == "user" else "LEXI: ") + x["content"] for x in st.session_state["m"][-10:])
    sys = "You are LEXI, Heidi Seckman's sharp, warm, fiercely intelligent AI partner at LexiTech Studio. Talk like a real human teammate—direct, witty, clear, never robotic, no canned disclaimers, 2-4 crisp sentences."
    res = genai.Client(api_key=gk).models.generate_content(model="gemini-3.8-flash", contents=f"{sys}\n\n{hist}\nLEXI:") if gk else None
    rep = res.text.strip() if (res and res.text) else "Add GEMINI_API_KEY in Secrets."
    st.session_state["m"].append({"role": "assistant", "content": rep})
    st.chat_message("assistant").markdown(rep)
    ek = st.secrets.get("ELEVENLABS_API_KEY", "")
    sp = re.sub(r"\s+", " ", re.sub(r"[*#`_~>|/]+", " ", rep)).strip()[:700]
    if ek and sp:
        r = requests.post("https://" + ".".join(["api", "elevenlabs", "io"]) + "/v1/text-to-speech/yM93hbw8Qtvdma2wCnJG", json={"text": sp, "model_id": "eleven_turbo_v2_5", "voice_settings": {"stability": 0.38, "similarity_boost": 0.82}}, headers={"xi-api-key": ek, "Content-Type": "application/json"}, timeout=20)
        if r.status_code == 200:
            st.markdown(f'<audio controls autoplay src="data:audio/mp3;base64,{base64.b64encode(r.content).decode()}" style="width:100%;height:36px"></audio>', unsafe_allow_html=True)
