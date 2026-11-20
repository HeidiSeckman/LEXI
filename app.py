ST_OPEN = "<" + "style>"
ST_CLOSE = "<" + "/style>"

css_1 = (
    "@import url('https://googleapis.com');"
    "html,body,.stApp,[data-testid='stAppViewContainer'],[data-testid='stMain']{"
    " background:#F6F7F9!important;color:#0F172A!important;"
    " font-family:'Plus Jakarta Sans',sans-serif!important}"
    "#MainMenu,footer,header,[data-testid='stHeader'],[data-testid='stToolbar']{"
    " display:none!important}"
    "[data-testid='stBottom'],[data-testid='stBottom']>div,"
    "[data-testid='stBottomBlockContainer']{background:#F6F7F9!important}"
    "@keyframes floatAv{0%,100%{transform:translateY(0px)}50%{transform:translateY(-4px)}}"
    "@keyframes auraPulse{"
    " 0%,100%{box-shadow:0 6px 20px rgba(249,168,212,.35)}"
    " 50%{box-shadow:0 10px 28px rgba(249,168,212,.60)}}"
    ".block-container{position:relative;z-index:2;max-width:780px!important}"
    ".card{display:flex;align-items:center;gap:20px;padding:20px 24px;border-radius:18px;"
    " background:linear-gradient(135deg,#3D0E27 0%,#6D1A45 55%,#882257 100%);"
    " border:1px solid rgba(255,255,255,.16);box-shadow:0 12px 28px rgba(61,14,39,.16);margin-bottom:14px}"
    ".card img{width:104px;height:128px;object-fit:cover;border-radius:14px;"
    " border:2px solid #F9A8D4;animation:floatAv 3.4s ease-in-out infinite,"
    " auraPulse 2.4s ease-in-out infinite;transition:transform .15s ease,box-shadow .15s ease}"
)

css_2 = (
    "div.stButton>button{width:100%;border-radius:12px!important;"
    " background:#FFFFFF!important;border:1px solid #E2E8F0!important;"
    " color:#0F172A!important;font-weight:600!important;box-shadow:0 2px 6px rgba(15,23,42,.04)!important}"
    "div.stButton>button:hover{border-color:#BE185D!important;color:#BE185D!important}"
    "[data-testid='stExpander']{background:#FFFFFF!important;border:1px solid #E2E8F0!important;border-radius:14px!important}"
    "[data-testid='stAudioInput']{background:#FFFFFF!important;"
    " border:1px solid rgba(157,23,77,.28)!important;border-radius:14px!important;padding:8px!important}"
    "[data-testid='stChatMessage']{background:#FFFFFF!important;"
    " border:1px solid #E2E8F0!important;border-radius:14px!important;box-shadow:0 2px 8px rgba(15,23,42,.03)!important}"
    "[data-testid='stChatMessage'] p,[data-testid='stChatMessage'] li{color:#0F172A!important}"
    "[data-testid='stChatInput']{background:#FFFFFF!important;border:1.5px solid #BE185D!important;"
    " border-radius:14px!important}"
    "[data-testid='stChatInput'] textarea{color:#0F172A!important}"
    ".status{font-size:12px;color:#475569;font-weight:500;margin:4px 0 12px}"
)

avatar_html = f'<img id="lexi-av" src="{avatar_data}">' if avatar_data else ""
header_html = (
    ST_OPEN + css_1 + css_2 + ST_CLOSE
    + f'<div class="card">{avatar_html}<div>'
    + '<div style="font:700 11px JetBrains Mono,monospace;letter-spacing:1.2px;color:#F9A8D4">LEXITECH // LEGAL &amp; TAX INTELLIGENCE</div>'
    + '<h3 style="margin:4px 0;font-size:24px;font-weight:800;color:#FFFFFF">LEXI</h3>'
    + '<p style="margin:0;font-size:14px;color:rgba(255,245,250,.90)">'
    + 'Forensic legal, tax &amp; execution partner built for you.</p>'
    + '</div></div>'
)
st.markdown(header_html, unsafe_allow_html=True)
