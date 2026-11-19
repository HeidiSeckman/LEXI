<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>LEXI // LexiTech AI Assistant</title>
<link href="https://googleapis.com" rel="stylesheet" />
<style>
 :root { --card:rgba(30,12,24,0.88); --pink:#FF2A85; --rose:#F9A8D4; --cyan:#38BDF8; --border:rgba(255,42,133,0.38); --text:#FFF5FA; --muted:#E5C1D3; }
 * { box-sizing:border-box; margin:0; padding:0; }
 body { background:radial-gradient(circle at 50% 24%, #2E0E22 0%, #12050D 58%, #070205 100%); color:var(--text); font-family:'Plus Jakarta Sans',sans-serif; min-height:100vh; display:flex; flex-direction:column; align-items:center; padding:22px 18px 40px; }
 .topbar { width:100%; max-width:960px; display:flex; justify-content:space-between; align-items:center; background:var(--card); border:1px solid var(--border); border-radius:16px; padding:12px 20px; margin-bottom:24px; flex-wrap:wrap; gap:10px; position:relative; z-index:2; }
 .brand { font-weight:800; font-size:21px; letter-spacing:1px; }
 .brand span { color:var(--pink); }
 .pill { font-family:'JetBrains Mono',monospace; font-size:11px; font-weight:700; color:var(--rose); border:1px solid var(--border); background:rgba(255,42,133,0.12); padding:6px 14px; border-radius:999px; text-decoration:none; cursor:pointer; }
 .core-stage { width:100%; max-width:960px; background:var(--card); border:1.5px solid var(--border); border-radius:24px; padding:26px 24px 30px; display:flex; flex-direction:column; align-items:center; text-align:center; box-shadow:0 0 50px rgba(255,42,133,0.18); position:relative; z-index:2; }
 .holo-stage { position:relative; width:260px; height:310px; display:flex; flex-direction:column; align-items:center; justify-content:center; margin:6px 0 8px; cursor:pointer; }
 .holo-avatar { width:245px; height:295px; object-fit:contain; mix-blend-mode:screen; animation:holoFloat 4.2s ease-in-out infinite, holoFlicker 7s infinite; filter:drop-shadow(0 0 18px rgba(255,42,133,0.65)); transition:filter 0.3s ease; pointer-events:none; }
 .listening .holo-avatar { filter:hue-rotate(155deg) saturate(1.4) drop-shadow(0 0 26px rgba(56,189,248,0.95)); }
 .speaking .holo-avatar { animation:holoSpeak 0.42s ease-in-out infinite alternate; filter:brightness(1.12) saturate(1.25) drop-shadow(0 0 32px rgba(255,42,133,1)); }
 @keyframes holoFloat { 0%, 100% { transform:translateY(0px); } 50% { transform:translateY(-8px); } }
 @keyframes holoSpeak { from { transform:translateY(-3px) scale(1.0); } to { transform:translateY(-7px) scale(1.028); } }
 @keyframes holoFlicker { 0%, 96%, 100% { opacity:0.98; } 97% { opacity:0.84; } 98% { opacity:0.99; } 99% { opacity:0.88; } }
 .holo-tag { font-family:'JetBrains Mono',monospace; font-size:10px; font-weight:700; letter-spacing:1.5px; color:#FFF; background:rgba(255,42,133,0.22); border:1px solid var(--pink); padding:4px 14px; border-radius:999px; margin-top:-6px; }
 .status-bar { font-family:'JetBrains Mono',monospace; font-size:12px; color:var(--rose); margin:10px 0 14px; letter-spacing:0.5px; }
 .controls { display:flex; gap:10px; flex-wrap:wrap; justify-content:center; align-items:center; margin-bottom:12px; }
 .quick-chips { display:flex; gap:8px; flex-wrap:wrap; justify-content:center; margin-bottom:16px; }
 .chip { font-family:'JetBrains Mono',monospace; font-size:11px; color:#FCE7F3; background:rgba(255,42,133,0.14); border:1px solid var(--border); padding:5px 12px; border-radius:999px; cursor:pointer; }
 .chip:hover { background:rgba(255,42,133,0.32); border-color:var(--pink); }
 .btn { display:inline-block; text-decoration:none; background:linear-gradient(135deg,#E11D74 0%,#88134D 100%); color:#FFF; font-weight:700; font-size:13.5px; padding:11px 22px; border-radius:999px; border:1px solid #F9A8D4; cursor:pointer; box-shadow:0 6px 20px rgba(225,29,116,0.35); }
 .btn-ghost { background:transparent; border:1.5px solid var(--rose); color:var(--rose); box-shadow:none; }
 .chat-box { width:100%; max-width:760px; background:rgba(12,4,9,0.75); border:1px solid var(--border); border-radius:16px; padding:16px; text-align:left; max-height:260px; overflow-y:auto; margin-bottom:14px; display:flex; flex-direction:column; gap:10px; }
 .msg { font-size:13.8px; line-height:1.55; padding:10px 14px; border-radius:12px; }
 .msg-lexi { background:rgba(255,42,133,0.14); border-left:3px solid var(--pink); color:#FFF5FA; }
 .msg-user { background:rgba(255,255,255,0.07); border-right:3px solid var(--rose); color:#E5C1D3; align-self:flex-end; }
 .launch-link { display:inline-block; margin-top:8px; padding:7px 16px; border-radius:999px; background:linear-gradient(135deg,#FF2A85 0%,#9D174D 100%); color:#FFF; font-weight:700; font-size:12.5px; text-decoration:none; border:1px solid #F9A8D4; }
 .input-row { width:100%; max-width:760px; display:flex; gap:10px; }
 .txt-in { flex:1; background:rgba(255,255,255,0.08); border:1.5px solid var(--border); color:#FFF; border-radius:999px; padding:12px 18px; font-size:14px; font-family:inherit; outline:none; }
 .key-drawer { width:100%; max-width:760px; margin-top:16px; padding:16px 18px; background:rgba(255,42,133,0.08); border:1px dashed var(--border); border-radius:14px; display:none; flex-direction:column; gap:10px; text-align:left; }
 .key-drawer.open { display:flex; }
 .key-row { display:flex; gap:10px; flex-wrap:wrap; align-items:center; }
</style>
</head>
<body>
<div class="topbar">
  <div class="brand">LEXI<span> // HOLOGRAPHIC AI</span></div>
  <div style="display:flex;gap:10px;flex-wrap:wrap;">
    <button type="button" class="pill" onclick="toggleKeyDrawer()">⚙ AI &amp; VOICE KEYS</button>
    <a class="pill" id="studioBackLink" href="#">← BACK TO STUDIO</a>
  </div>
</div>

<div class="core-stage">
  <div class="pill">LEXITECH AI ASSISTANT // ENGINEERED BY HEIDI SECKMAN</div>
  <div class="holo-stage" id="holoWrap" onclick="testVoice()" title="Click Lexi to hear her">
    <img class="holo-avatar" src="LEXI_avatar.png" alt="LEXI Hologram" />
    <div class="holo-tag" id="coreState">LEXI // STANDBY</div>
  </div>
  <div class="status-bar" id="statusText">READY — TAP A QUICK COMMAND, SPEAK, OR ASK ANY QUESTION</div>

  <div class="controls">
    <button type="button" class="btn" id="micBtn" onclick="startListening()">🎙 Talk to Lexi</button>
    <button type="button" class="btn btn-ghost" id="wakeBtn" onclick="toggleWakeMode()">👂 Wake Word: OFF</button>
    <button type="button" class="btn btn-ghost" onclick="stopSpeech()">⏹ Mute</button>
  </div>

  <div class="quick-chips">
    <button type="button" class="chip" onclick="processQuery('Open Legal & Tax Assistant')">Open Module 01</button>
    <button type="button" class="chip" onclick="processQuery('Open Tax-Trap Scanner')">Open Module 02</button>
    <button type="button" class="chip" onclick="processQuery('Open Life Event Simulator')">Open Module 03</button>
    <button type="button" class="chip" onclick="processQuery('Open Cloud Workspace')">Open Cloud Workspace</button>
    <button type="button" class="chip" onclick="processQuery('What can each LexiTech engine do?')">Explain All 4 Engines</button>
  </div>

  <div class="chat-box" id="chatLog">
    <div class="msg msg-lexi"><strong>LEXI:</strong> Hi, I'm Lexi, your AI assistant. Ask any question—I'm here to help.</div>
  </div>

  <form class="input-row" id="chatForm">
    <input class="txt-in" id="userInput" type="text" placeholder="Ask about contracts, IRS rules, or say 'Open Tax-Trap Scanner'..." autocomplete="off" />
    <button type="submit" id="sendBtn" class="btn">Send →</button>
  </form>

  <div class="key-drawer" id="keyDrawer">
    <div style="font-size:12.5px;color:#F9A8D4;font-weight:700;">Connect Full AI Brain &amp; Realistic Human Voice (saved privately on this device only):</div>
    <div class="key-row">
      <input class="txt-in" id="apiKeyInput" type="password" placeholder="Gemini API Key (AIzaSy...) for full AI answers" style="min-width:220px;" />
      <input class="txt-in" id="elevenKeyInput" type="password" placeholder="Optional ElevenLabs Key (sk_...) for real human voice" style="min-width:220px;" />
      <select class="txt-in" id="elevenVoiceSelect" style="max-width:200px;">
        <option value="EXAVITQu4vr4xnSDxMaL">Voice: Bella (Youthful &amp; Warm)</option>
        <option value="MF3mGyEYCl7XYWbV9V6O">Voice: Elli (Young &amp; Clear)</option>
        <option value="21m00Tcm4TlvDq8ikWAM">Voice: Rachel (Calm &amp; Poised)</option>
      </select>
      <button type="button" class="btn" onclick="saveKeys()">Save Keys</button>
    </div>
  </div>
</div>
<canvas id="lexiRain" style="position:fixed;inset:0;width:100%;height:100%;z-index:0;pointer-events:none;opacity:0.24;"></canvas>
<script>
const STUDIO_HOME = 'https://' + 'heidiseckman' + '.github.io';
document.getElementById('studioBackLink').href = STUDIO_HOME;

const MODULES = {
  assistant: { name: "Module 01: Legal & Tax Document AI Assistant", url: 'https://' + 'legal-tax-ai-assistant-8vttj8mpyeo3dlaoxzunac' + '.streamlit.app' },
  tax: { name: "Module 02: Tax-Trap Contract Scanner", url: 'https://' + 'lexitech-tax-trap-contract-scanner-kzkf4rappq6fesyv2gy7kgs' + '.streamlit.app' },
  life: { name: "Module 03: Worst-Case Life Event Simulator", url: 'https://' + 'lexitech-life-event-simulator-ml2f72eoad2ytnngjurwat' + '.streamlit.app' },
  workplace: { name: "Module 04: LexiTech Pro Cloud Workspace", url: 'https://' + 'lexitech-workplace-jqfg2cjffckrfphhyyzrca' + '.streamlit.app' },
  studio: { name: "LexiTech Main Studio Landing Page", url: STUDIO_HOME }
};

let wakeMode = false;
let recognition = null;
let currentAudio = null;
let chatHistory = Array.of();

function setVisualState(state, label) {
  const wrap = document.getElementById('holoWrap');
  wrap.classList.remove('listening', 'speaking');
  if (state) wrap.classList.add(state);
  document.getElementById('coreState').textContent = 'LEXI // ' + label;
}

function addMessage(sender, text, actionUrl, actionLabel) {
  const log = document.getElementById('chatLog');
  const div = document.createElement('div');
  div.className = sender === 'LEXI' ? 'msg msg-lexi' : 'msg msg-user';
  div.innerHTML = `<strong>${sender}:</strong> ${text}`;
  if (actionUrl) {
    const link = document.createElement('a');
    link.className = 'launch-link';
    link.href = actionUrl;
    link.target = '_blank';
    link.rel = 'noopener';
    link.textContent = `Launch ${actionLabel} →`;
    div.appendChild(document.createElement('br'));
    div.appendChild(link);
  }
  log.appendChild(div);
  log.scrollTop = log.scrollHeight;
}

function stopSpeech() {
  if (currentAudio) { currentAudio.pause(); currentAudio = null; }
  if ('speechSynthesis' in window) window.speechSynthesis.cancel();
  setVisualState('', 'STANDBY');
}

async function speak(text) {
  stopSpeech();
  const elevenKey = localStorage.getItem('lexi_eleven_key');
  const elevenVoice = localStorage.getItem('lexi_eleven_voice') || 'EXAVITQu4vr4xnSDxMaL';

  if (elevenKey) {
    try {
      setVisualState('speaking', 'SPEAKING');
      const res = await fetch(`https://elevenlabs.io{elevenVoice}`, {
        method: 'POST',
        headers: { 'xi-api-key': elevenKey, 'Content-Type': 'application/json' },
        body: JSON.stringify({
          text,
          model_id: 'eleven_turbo_v2_5',
          voice_settings: { stability: 0.45, similarity_boost: 0.80 }
        })
      });
      if (res.ok) {
        const blob = await res.blob();
        const url = URL.createObjectURL(blob);
        currentAudio = new Audio(url);
        currentAudio.onended = () => {
          setVisualState('', 'STANDBY');
          if (wakeMode) startListening(true);
        };
        await currentAudio.play();
        return;
      }
    } catch (e) {}
  }

  if (!('speechSynthesis' in window)) return;
  const utter = new SpeechSynthesisUtterance(text);
  const voices = window.speechSynthesis.getVoices().filter(v => v.lang && v.lang.startsWith('en'));
  const preferred = Array.of('Karen', 'Zoe', 'Ava', 'Nicky', 'Samantha', 'Google UK English Female');
  const match = preferred.map(name => voices.find(v => v.name.includes(name))).find(Boolean);
  if (match) utter.voice = match;
  utter.rate = 0.92;
  utter.pitch = 1.08;
  utter.onstart = () => setVisualState('speaking', 'SPEAKING');
  utter.onend = () => {
    setVisualState('', 'STANDBY');
    if (wakeMode) startListening(true);
  };
  window.speechSynthesis.speak(utter);
}

function testVoice() {
  speak("Hi, I'm Lexi, your AI assistant. Ask any question—I'm here to help.");
}

function toggleKeyDrawer() {
  document.getElementById('keyDrawer').classList.toggle('open');
  document.getElementById('apiKeyInput').value = localStorage.getItem('lexi_gemini_key') || '';
  document.getElementById('elevenKeyInput').value = localStorage.getItem('lexi_eleven_key') || '';
  const savedVoice = localStorage.getItem('lexi_eleven_voice');
  if (savedVoice) document.getElementById('elevenVoiceSelect').value = savedVoice;
}

function saveKeys() {
  const gVal = document.getElementById('apiKeyInput').value.trim();
  const eVal = document.getElementById('elevenKeyInput').value.trim();
  const vVal = document.getElementById('elevenVoiceSelect').value;
  if (gVal) localStorage.setItem('lexi_gemini_key', gVal);
  else localStorage.removeItem('lexi_gemini_key');
  if (eVal) localStorage.setItem('lexi_eleven_key', eVal);
  else localStorage.removeItem('lexi_eleven_key');
  localStorage.setItem('lexi_eleven_voice', vVal);
  document.getElementById('keyDrawer').classList.remove('open');
  const msg = "Your settings are saved. I'm ready whenever you are.";
  addMessage('LEXI', msg);
  speak(msg);
}

function detectModuleIntent(q) {
  const s = q.toLowerCase();
  const wantsNav = /(open|launch|start|go to|take me|show|visit|load|bring up|use)/.test(s);
  if (!wantsNav) return null;
  if (/(tax|trap|scanner|8332|module 2|module two|02)/.test(s)) return MODULES.tax;
  if (/(life|event|simulator|crisis|emergency|layoff|module 3|module three|03)/.test(s)) return MODULES.life;
  if (/(workplace|workspace|vault|cloud|login|account|folder|module 4|module four|04)/.test(s)) return MODULES.workplace;
  if (/(assistant|document|audit|contract|module 1|module one|01)/.test(s)) return MODULES.assistant;
  if (/(home|landing|studio|main page)/.test(s)) return MODULES.studio;
  return null;
}

function builtInBrain(q) {
  const s = q.toLowerCase();
  if (/^(hi|hello|hey|yo|sup|good morning|good evening)/.test(s)) {
    return { text: "Hey! I'm ready whenever you are. Ask me how any of our four legal and tax engines work, ask a tax or contract question, or tell me which module to open." };
  }
  if (/(who made|who created|who built|heidi)/.test(s)) {
    return { text: "I was engineered by Heidi Seckman as the central AI interface for LexiTech Legal and Tax AI Studio—designed around strict, closed-book extraction with zero hallucinations." };
  }
  if (/(4 engines|four engines|what can|capabilities|modules|explain)/.test(s)) {
    return { text: "LexiTech runs four specialized engines: Module 01 audits contracts and IRS manuals with exact page citations; Module 02 cross-checks agreements against IRS rules for tax traps; Module 03 stress-tests contracts against emergencies like layoffs or illness; and Module 04 is your Pro Cloud Workspace with saved case folders.", url: MODULES.workplace.url, label: "Pro Cloud Workspace" };
  }
  if (/(8332|divorce|child|dependent|custody)/.test(s)) {
    return { text: "Under IRS rules, a divorce decree alone does not override federal tax law—the custodial parent must sign Form 8332 to release a dependency exemption. Module 02 scans agreements specifically for Form 8332 collisions and drafts protective redlines.", url: MODULES.tax.url, label: "Tax-Trap Scanner" };
  }
  if (/(1099|contractor|w-2|w2|classification|employee)/.test(s)) {
    return { text: "Misclassifying a W-2 employee as a 1099 independent contractor triggers back payroll taxes and IRS penalties based on behavioral and financial control tests. You can upload any contractor agreement into Module 02 to flag classification traps.", url: MODULES.tax.url, label: "Tax-Trap Scanner" };
  }
  if (/(layoff|disability|medical|emergency|force majeure|crisis|simulator)/.test(s)) {
    return { text: "Module 03 simulates worst-case events—like sudden job loss, medical emergencies, or co-founder default—against your lease or contract to calculate financial exposure and draft protective escape clauses.", url: MODULES.life.url, label: "Life Event Simulator" };
  }
  if (/(vault|cloud|login|save|account|supabase)/.test(s)) {
    return { text: "Your LexiTech Pro Cloud Workspace uses Supabase authentication so you can create persistent case folders, run all four AI engines in one place, and keep audit memos permanently on file.", url: MODULES.workplace.url, label: "Cloud Workspace" };
  }
  if (/(4012|4491|irs|manual|citation|grounded|hallucination)/.test(s)) {
    return { text: "Every LexiTech engine uses closed-book grounding verified on 90-plus megabytes of IRS Publication 4012 and Publication 4491 manuals—meaning answers are strictly anchored to uploaded documents with exact tab and page citations.", url: MODULES.assistant.url, label: "Document Assistant" };
  }
  return { text: "I can help you audit a contract, check IRS tax rules like Form 8332 or 1099 classification, or launch any of your four studio modules. For open-ended questions outside LexiTech, tap AI & Voice Keys at the top right to connect your Gemini key." };
}

async function processQuery(rawText) {
  const text = rawText.trim();
  if (!text) return;
  addMessage('YOU', text);

  const navTarget = detectModuleIntent(text);
  if (navTarget) {
    const reply = `Opening ${navTarget.name} for you now. If your browser blocks popups, tap the button below.`;
    addMessage('LEXI', reply, navTarget.url, navTarget.name);
    speak(reply);
    const win = window.open(navTarget.url, '_blank', 'noopener');
    if (!win) window.location.href = navTarget.url;
    return;
  }

  const apiKey = localStorage.getItem('lexi_gemini_key');
  if (!apiKey) {
    const localAns = builtInBrain(text);
    addMessage('LEXI', localAns.text, localAns.url, localAns.label);
    speak(localAns.text);
    return;
  }

  document.getElementById('statusText').textContent = 'THINKING...';
  chatHistory.push({ role: 'user', parts: Array.of({ text }) });
  if (chatHistory.length > 10) chatHistory = chatHistory.slice(-10);

  try {
    const payload = {
