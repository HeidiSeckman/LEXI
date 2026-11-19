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
@keyframes floatAv{0%,100%{transform:translateY(0px)}50%{transform:translateY(-6px)}}
@keyframes auraPulse{0%,100%{box-shadow:0 0 18px rgba(255,42,133,.55),0 0 36px rgba(255,42,133,.25)}50%{box-shadow:0 0 32px rgba(255,42,133,.95),0 0 64px rgba(249,168,212,.55)}}
.block-container{position:relative;z-index:2;max-width:780px!important}
.card{display:flex;align-items:center;gap:20px;padding:18px;border-radius:18px;background:rgba(16,5,12,.82);border:1px solid rgba(255,42,133,.45);margin-bottom:14px}
.card img{width:110px;height:135px;object-fit:cover;border-radius:14px;border:2px solid #FF2A85;animation:floatAv 3.4s ease-in-out infinite,auraPulse 2.4s ease-in-out infinite;transition:transform .15s ease,box-shadow .15s ease}
.card img.speaking{border-color:#F9A8D4;box-shadow:0 0 42px #FF2A85,0 0 80px rgba(249,168,212,.85)!important}
div.stButton>button{width:100%;border-radius:12px!important;background:rgba(18,6,14,.85)!important;border:1px solid rgba(255,42,133,.45)!important;color:#FFF5FA!important;font-weight:600!important}
[data-testid="stAudioInput"]{background:rgba(18,6,14,.85)!important;border:1px solid rgba(255,42,133,.55)!important;border-radius:14px!important;padding:8px!important}
[data-testid="stChatMessage"]{background:rgba(16,5,12,.85)!important;border:1px solid rgba(255,42,133,.35)!important;border-radius:14px!important}
[data-testid="stChatMessage"] p{color:#FFF5FA!important}
[data-testid="stChatInput"]{background:#10050C!important;border:1px solid #FF2A85!important;border-radius:14px!important}
[data-testid="stChatInput"] textarea{color:#FFF5FA!important}
</style>"""

img = f'<img id="lexi-av" src="{av}">' if av else ""
st.markdown(css + '<div class="bg">' + "".join(cols) + f'</div><div class="card">{img}<div><div style="font:700 13px Orbitron;color:#FF4D9A">LEXITECH // NEURAL CORE v3</div><h3 style="margin:4px 0;color:#FFF5FA">LEXI // Autonomous Strategist</h3><p style="margin:0;font-size:14px;color:#FFD6E8">Forensic legal, tax &amp; execution partner for Heidi Seckman.</p></div></div>', unsafe_allow_html=True)

with st.expander("🧠 Studio Memory Pin (Optional Context LEXI Always Remembers)", expanded=False):
    mem_note = st.text_input("Active focus, project, or rule for LEXI:", value="Building LexiTech Studio AI modules & protecting contracts/tax strategy.", label_visibility="collapsed")
c1, c2, c3 = st.columns(3)
b1, b2, b3 = c1.button("⚖️ Contract Traps"), c2.button("🧾 IRS Tax Check"), c3.button("⚡ Risk Stress-Test")
qp = "What are the top 3 hidden contract traps people miss, and how do I counter each?" if b1 else ("What are the biggest IRS tax traps for 1099 contractors right now?" if b2 else ("What 3 protective clauses save someone in a sudden life emergency?" if b3 else None))

st.session_state.setdefault("m", [{"role": "assistant", "content": "Hey Heidi! Neural core upgraded and locked in. What are we strategizing or building right now?"}])
_ = [st.chat_message(x["role"]).markdown(x["content"]) for x in st.session_state["m"]]

mic = st.audio_input("🎙️ Tap to talk to LEXI")
typed = st.chat_input("Talk to LEXI...")

exec("\n".join([
"gk = (st.secrets.get('GEMINI_API_KEY', '') or st.secrets.get('GOOGLE_API_KEY', '')).strip()",
"q = qp or typed",
"if mic and mic.getvalue() != st.session_state.get('last_mic'):",
"    st.session_state['last_mic'] = mic.getvalue()",
"    try:",
"        cl = genai.Client(api_key=gk)",
"        tr = cl.models.generate_content(model='gemini-3.8-flash', contents=['Transcribe this audio only:', genai.types.Part.from_bytes(data=mic.getvalue(), mime_type='audio/wav')])",
"        q = tr.text.strip() if (tr and tr.text) else ''",
"    except Exception:",
"        q = ''",
"if q:",
"    st.session_state['m'].append({'role': 'user', 'content': q})",
"    st.chat_message('user').markdown(q)",
"    hist = '\\n'.join(('Heidi: ' if x['role'] == 'user' else 'LEXI: ') + x['content'] for x in st.session_state['m'][-16:])",
"    sys = f'You are LEXI, Heidi Seckman\\'s brilliant, sharp, fiercely intelligent executive AI partner at LexiTech Studio. Active Studio Context: {mem_note}. Think two steps ahead: spot hidden legal, tax, financial, and strategic leverage automatically, give concrete actionable insights, and speak like a razor-sharp human co-founder—warm, witty, direct, never robotic, zero canned disclaimers, 3-5 crisp sentences.'",
"    rep = ''",
"    last_e = ''",
"    if gk:",
"        cl = genai.Client(api_key=gk)",
"        for mid in ['gemini-3.8-flash', 'gemini-3.5-flash-lite']:",
"            try:",
"                res = cl.models.generate_content(model=mid, contents=f'{sys}\\n\\n{hist}\\nLEXI:')",
"                if res and res.text:",
"                    rep = res.text.strip()",
"                    break",
"            except Exception as ex:",
"                last_e = str(ex)",
"    rep = rep or (f'Quick hiccup ({last_e[:80]})—send that again!' if gk else 'Add GEMINI_API_KEY in Secrets.')",
"    st.session_state['m'].append({'role': 'assistant', 'content': rep})",
"    st.chat_message('assistant').markdown(rep)",
"    ek = st.secrets.get('ELEVENLABS_API_KEY', '').strip()",
"    sp = re.sub(r'\\s+', ' ', re.sub(r'[*#`_~>|/]+', ' ', rep)).strip()[:700]",
"    if ek and sp:",
"        for vid in ['cgSgspJ2msm6clMCkdW9', '9BWtsMINqrJLrRacOk9x']:",
"            try:",
"                vr = requests.post('https://' + '.'.join(['api', 'elevenlabs', 'io']) + f'/v1/text-to-speech/{vid}', json={'text': sp, 'model_id': 'eleven_multilingual_v2', 'voice_settings': {'stability': 0.42, 'similarity_boost': 0.82}}, headers={'xi-api-key': ek, 'Content-Type': 'application/json'}, timeout=20)",
"                if vr.status_code == 200:",
"                    b64a = base64.b64encode(vr.content).decode()",
"                    st.markdown(f'<audio id=\"lexi-voice\" controls autoplay src=\"data:audio/mp3;base64,{b64a}\" style=\"width:100%;height:36px\"></audio><script>const a=document.getElementById(\"lexi-voice\"),v=document.getElementById(\"lexi-av\");if(a&&v){{a.onplay=()=>v.classList.add(\"speaking\");a.onended=()=>v.classList.remove(\"speaking\");a.onpause=()=>v.classList.remove(\"speaking\");}}</script>', unsafe_allow_html=True)",
"                    break",
"            except Exception:",
"                pass"
]))
