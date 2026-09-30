/* Orla — the AI Control Architecture guide. Floating chat widget, no dependencies.
   Served at /orla/orla.js; talks to /api/orla. Transcript kept in sessionStorage for the tab only. */
(function () {
  if (window.__orla) return;
  window.__orla = true;

  var API = "/api/orla";
  var STORE = "orla.chat.v1";
  var OWL = "/orla/orla.svg";
  var GREETING = "Hoo, hello! I'm Orla, your guide to the AI Control Architecture. Ask me about the ten pillars, risk tiers, RCDM, the Action Fabric, or how to get started.";
  var SUGGEST = [
    "What is AI Control Architecture?",
    "How do I decide a use case's risk tier?",
    "What is RCDM and Shadow Mode?",
    "What does the Action Fabric do?",
    "Is there an open-source implementation?"
  ];

  var css = [
    "#orla-btn{position:fixed;right:20px;bottom:20px;z-index:9999;width:60px;height:60px;border-radius:50%;border:1px solid rgba(59,130,246,.55);background:#0b0c10;box-shadow:0 8px 28px rgba(0,0,0,.45);cursor:pointer;padding:6px;transition:transform .15s}",
    "#orla-btn:hover{transform:translateY(-2px) scale(1.04)}",
    "#orla-btn img{width:100%;height:100%;display:block}",
    "#orla-tip{position:fixed;right:88px;bottom:34px;z-index:9999;background:#111827;color:#e5e7eb;border:1px solid #1f2937;border-radius:10px;padding:7px 11px;font:13px/1.3 system-ui,-apple-system,Segoe UI,sans-serif;box-shadow:0 6px 20px rgba(0,0,0,.35)}",
    "#orla-panel{position:fixed;right:20px;bottom:92px;z-index:9999;width:380px;max-width:calc(100vw - 24px);height:560px;max-height:calc(100vh - 120px);display:none;flex-direction:column;background:#0b0c10;color:#e5e7eb;border:1px solid #1f2937;border-radius:16px;box-shadow:0 18px 50px rgba(0,0,0,.55);overflow:hidden;font:14px/1.5 system-ui,-apple-system,Segoe UI,sans-serif}",
    "#orla-panel.open{display:flex}",
    ".orla-hd{display:flex;align-items:center;gap:10px;padding:12px 14px;border-bottom:1px solid #1f2937;background:linear-gradient(180deg,#0f172a,#0b0c10)}",
    ".orla-hd img{width:34px;height:34px}",
    ".orla-hd b{display:block;font-size:15px;color:#f8fafc}",
    ".orla-hd small{color:#94a3b8;font-size:12px}",
    ".orla-hd .sp{flex:1}",
    ".orla-hd button{background:none;border:0;color:#94a3b8;cursor:pointer;font-size:12px;padding:4px 6px;border-radius:6px}",
    ".orla-hd button:hover{color:#f8fafc;background:#1f2937}",
    ".orla-log{flex:1;overflow-y:auto;padding:14px;display:flex;flex-direction:column;gap:10px}",
    ".orla-m{max-width:88%;padding:9px 12px;border-radius:12px;white-space:pre-wrap;word-wrap:break-word}",
    ".orla-m.u{align-self:flex-end;background:#1d4ed8;color:#fff;border-bottom-right-radius:4px}",
    ".orla-m.a{align-self:flex-start;background:#111827;border:1px solid #1f2937;border-bottom-left-radius:4px}",
    ".orla-m a{color:#93c5fd;text-decoration:underline}",
    ".orla-m.u a{color:#fff}",
    ".orla-src{margin-top:6px;font-size:12px;color:#94a3b8}",
    ".orla-src a{display:inline-block;margin:3px 6px 0 0;padding:2px 8px;border:1px solid #1e3a8a;border-radius:999px;text-decoration:none;color:#93c5fd}",
    ".orla-sug{display:flex;flex-wrap:wrap;gap:6px}",
    ".orla-sug button{background:#0f172a;color:#cbd5e1;border:1px solid #1e3a8a;border-radius:999px;padding:5px 10px;font-size:12.5px;cursor:pointer}",
    ".orla-sug button:hover{border-color:#3b82f6;color:#fff}",
    ".orla-typing{align-self:flex-start;color:#94a3b8;font-size:13px}",
    ".orla-ft{border-top:1px solid #1f2937;padding:10px;display:flex;gap:8px}",
    ".orla-ft textarea{flex:1;resize:none;height:42px;max-height:110px;background:#111827;color:#f8fafc;border:1px solid #1f2937;border-radius:10px;padding:10px;font:inherit;outline:none}",
    ".orla-ft textarea:focus{border-color:#3b82f6}",
    ".orla-ft button{background:#3b82f6;color:#fff;border:0;border-radius:10px;padding:0 14px;font-weight:600;cursor:pointer}",
    ".orla-ft button:disabled{opacity:.5;cursor:default}",
    ".orla-note{padding:0 12px 10px;color:#64748b;font-size:11px;text-align:center}",
    "@media (max-width:480px){#orla-panel{right:8px;left:8px;width:auto;bottom:86px;height:calc(100vh - 110px)}}"
  ].join("\n");

  var style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);

  var btn = document.createElement("button");
  btn.id = "orla-btn";
  btn.setAttribute("aria-label", "Ask Orla, the AI Control Architecture guide");
  btn.innerHTML = '<img src="' + OWL + '" alt="">';

  var panel = document.createElement("div");
  panel.id = "orla-panel";
  panel.setAttribute("role", "dialog");
  panel.setAttribute("aria-label", "Orla chat");
  panel.innerHTML =
    '<div class="orla-hd"><img src="' + OWL + '" alt=""><div><b>Orla</b><small>Your guide to ACA and RCDM</small></div><div class="sp"></div>' +
    '<button type="button" data-act="new" title="Start a new conversation">New</button><button type="button" data-act="close" aria-label="Close">✕</button></div>' +
    '<div class="orla-log" aria-live="polite"></div>' +
    '<form class="orla-ft"><textarea placeholder="Ask Orla about the framework…" maxlength="1500" aria-label="Your question"></textarea><button type="submit">Ask</button></form>' +
    '<div class="orla-note">Orla is an AI guide and can be wrong. Check the linked pages. Please don\'t share confidential information.</div>';

  function mount() {
    document.body.appendChild(btn);
    document.body.appendChild(panel);
    try {
      if (!sessionStorage.getItem("orla.tip")) {
        var tip = document.createElement("div");
        tip.id = "orla-tip";
        tip.textContent = "Questions? Ask Orla 🦉";
        document.body.appendChild(tip);
        setTimeout(function () { tip.remove(); }, 6000);
        sessionStorage.setItem("orla.tip", "1");
      }
    } catch (e) {}
  }
  if (document.body) mount(); else document.addEventListener("DOMContentLoaded", mount);

  var log = panel.querySelector(".orla-log");
  var form = panel.querySelector("form");
  var ta = panel.querySelector("textarea");
  var send = panel.querySelector(".orla-ft button");
  var msgs = load();
  var busy = false;

  function load() { try { return JSON.parse(sessionStorage.getItem(STORE) || "[]"); } catch (e) { return []; } }
  function save() { try { sessionStorage.setItem(STORE, JSON.stringify(msgs.slice(-30))); } catch (e) {} }

  function esc(s) { return s.replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function safeUrl(u) {
    if (/^\/(?!\/)[^\s]*$/.test(u)) return u;
    if (/^https:\/\/(aicontrolarchitecture\.org|neocontrol\.ai|github\.com)(\/|$)/i.test(u)) return u;
    return null;
  }
  function md(text) {
    var h = esc(text);
    h = h.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, function (m, t, u) {
      var ok = safeUrl(u.replace(/&amp;/g, "&"));
      if (!ok) return t;
      var ext = /^https?:/.test(ok);
      return '<a href="' + esc(ok) + '"' + (ext ? ' target="_blank" rel="noopener"' : "") + ">" + t + "</a>";
    });
    h = h.replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>");
    h = h.replace(/(^|\n)[-*] /g, "$1• ");
    return h;
  }

  function bubble(role, text, sources) {
    var d = document.createElement("div");
    d.className = "orla-m " + (role === "user" ? "u" : "a");
    d.innerHTML = role === "user" ? esc(text) : md(text);
    if (sources && sources.length) {
      var s = document.createElement("div");
      s.className = "orla-src";
      s.innerHTML = "Read more: " + sources.map(function (x) {
        var u = safeUrl(x.url); return u ? '<a href="' + esc(u) + '">' + esc(x.title) + "</a>" : "";
      }).join("");
      d.appendChild(s);
    }
    log.appendChild(d);
    log.scrollTop = log.scrollHeight;
  }

  function render() {
    log.innerHTML = "";
    bubble("assistant", GREETING);
    if (!msgs.length) {
      var sg = document.createElement("div");
      sg.className = "orla-sug";
      SUGGEST.forEach(function (q) {
        var b = document.createElement("button");
        b.type = "button"; b.textContent = q;
        b.onclick = function () { ask(q); };
        sg.appendChild(b);
      });
      log.appendChild(sg);
    }
    msgs.forEach(function (m) { bubble(m.role, m.content, m.sources); });
  }

  function ask(q) {
    q = (q || "").trim();
    if (!q || busy) return;
    var sg = log.querySelector(".orla-sug"); if (sg) sg.remove();
    msgs.push({ role: "user", content: q.slice(0, 1500) });
    bubble("user", q);
    ta.value = "";
    busy = true; send.disabled = true;
    var t = document.createElement("div");
    t.className = "orla-typing"; t.textContent = "Orla is thinking…";
    log.appendChild(t); log.scrollTop = log.scrollHeight;
    fetch(API, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ messages: msgs.map(function (m) { return { role: m.role, content: m.content }; }) })
    })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; }); })
      .then(function (x) {
        t.remove();
        if (!x.ok || !x.j.reply) {
          msgs.pop();
          bubble("assistant", (x.j && x.j.error) || "Sorry, I couldn't answer that just now. Please try again.");
          return;
        }
        msgs.push({ role: "assistant", content: x.j.reply, sources: x.j.sources || [] });
        bubble("assistant", x.j.reply, x.j.sources);
        save();
      })
      .catch(function () {
        t.remove(); msgs.pop();
        bubble("assistant", "I couldn't connect. Check your connection and try again.");
      })
      .then(function () { busy = false; send.disabled = false; ta.focus(); });
  }

  function open() { panel.classList.add("open"); render(); setTimeout(function () { ta.focus(); }, 50); var tip = document.getElementById("orla-tip"); if (tip) tip.remove(); }
  function close() { panel.classList.remove("open"); btn.focus(); }

  btn.addEventListener("click", function () { panel.classList.contains("open") ? close() : open(); });
  panel.addEventListener("click", function (e) {
    var a = e.target.getAttribute && e.target.getAttribute("data-act");
    if (a === "close") close();
    if (a === "new") { msgs = []; save(); render(); }
  });
  form.addEventListener("submit", function (e) { e.preventDefault(); ask(ta.value); });
  ta.addEventListener("keydown", function (e) { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); ask(ta.value); } });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && panel.classList.contains("open")) close(); });
})();
