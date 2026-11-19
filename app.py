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
""", unsafe_allow_html=True)

# --- 3 WORKING FORENSIC AUDIT TRIGGERS ---
quick_prompt = None
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("01 // Contract Clause Audit"):
        quick_prompt = "Run a forensic contract audit checklist: what are the most dangerous indemnification, IP ownership, and auto-renewal clauses signers miss?"
with c2:
    if st.button("02 // Dual-Corpus Tax Trap"):
        quick_prompt = "Explain the top IRS tax traps when classifying independent contractors vs. employees and deducting home-office or software expenses."
with c3:
    if st.button("03 // Worst-Case Stress-Test"):
        quick_prompt = "Stress-test a standard service contract against a worst-case life event (medical emergency, sudden income loss, or force majeure). What protections should I demand?"

st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

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
    clean_text = text.replace("*", "").replace("#", "").replace("`", "")[:600]
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

# --- RESILIENT GEMINI ENGINE WITH AUTOMATIC 503 RETRY & FAILOVER ---
def ask_lexi_brain(api_key, prompt_text):
    client = genai.Client(api_key=api_key)
    models_to_try = [
        "gemini-3.6-flash",
        "gemini-3.5-flash-lite",
        "gemini-3.7-flash"
    ]
    last_error = ""
    for model_name in models_to_try:
        for attempt in range(2):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt_text
                )
                if response.text:
                    return response.text
            except Exception as e:
                last_error = str(e)
                if "503" in last_error or "UNAVAILABLE" in last_error or "429" in last_error:
                    time.sleep(1.2)
                    continue
                break
    return f"⚠️ **Temporary Model Traffic Spike:** `{last_error}` — please hit send again in a moment."

# --- CHAT HISTORY & EXECUTION ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "LEXI Neural Core online. Paste a contract clause to audit, ask an IRS tax question, or tap one of the three forensic engines above."}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

sys_prompt = (
    "You are LEXI, the holographic AI assistant for LexiTech Legal & Tax AI Studio, founded by Heidi Seckman. "
    "Be sharp, structured, concise, and authoritative on contract red flags, IRS tax publications, and risk mitigation. "
    "Include a brief closing note that insights are informational and not formal legal or tax representation."
)

typed_prompt = st.chat_input("Ask LEXI about contract traps, IRS rules, or paste a clause...")
active_prompt = quick_prompt or typed_prompt

if active_prompt:
    st.session_state.messages.append({"role": "user", "content": active_prompt})
    with st.chat_message("user"):
        st.markdown(active_prompt)

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
                reply = ask_lexi_brain(api_key, full_prompt)

            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

            audio_bytes = speak_paige(reply)
            if audio_bytes:
                st.audio(audio_bytes, format="audio/mp3", autoplay=True)
