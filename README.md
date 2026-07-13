<svg width="1180" height="610" viewBox="0 0 1180 610" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" font-family="'SFMono-Regular','Consolas','Menlo',monospace">
<title>Umesh Sai Hanuma Prasad Syamala — Profile Banner (light)</title>
<defs>
  <clipPath id="cardClip-light"><rect x="0" y="0" width="1180" height="610" rx="26"/></clipPath>
  <clipPath id="leftClip-light"><rect x="24" y="24" width="424" height="562" rx="18"/></clipPath>
  <clipPath id="rightClip-light"><rect x="468" y="24" width="688" height="562" rx="18"/></clipPath>

  <linearGradient id="accentGrad-light" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#2563EB"/>
    <stop offset="50%" stop-color="#06B6D4"/>
    <stop offset="100%" stop-color="#10B981"/>
    <animate attributeName="x1" values="0%;100%;0%" dur="8s" repeatCount="indefinite"/>
    <animate attributeName="x2" values="100%;0%;100%" dur="8s" repeatCount="indefinite"/>
  </linearGradient>

  <linearGradient id="asciiGrad-light" x1="0%" y1="0%" x2="100%" y2="100%" gradientUnits="objectBoundingBox">
    <stop offset="0%" stop-color="#06B6D4"/>
    <stop offset="100%" stop-color="#2563EB"/>
    <animateTransform attributeName="gradientTransform" type="translate" values="-0.3 0; 0.3 0; -0.3 0" dur="6s" repeatCount="indefinite"/>
  </linearGradient>

  <radialGradient id="blobPurple-light" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#2563EB" stop-opacity="0.28"/>
    <stop offset="100%" stop-color="#2563EB" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="blobCyan-light" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#06B6D4" stop-opacity="0.28"/>
    <stop offset="100%" stop-color="#06B6D4" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="blobEmerald-light" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#10B981" stop-opacity="0.28"/>
    <stop offset="100%" stop-color="#10B981" stop-opacity="0"/>
  </radialGradient>

  <filter id="softGlow-light" x="-60%" y="-60%" width="220%" height="220%">
    <feGaussianBlur stdDeviation="6" result="blur"/>
    <feMerge>
      <feMergeNode in="blur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>

  <filter id="bigBlur-light" x="-100%" y="-100%" width="300%" height="300%">
    <feGaussianBlur stdDeviation="40"/>
  </filter>

  <filter id="noiseFilter-light">
    <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" stitchTiles="stitch" result="noise"/>
    <feColorMatrix in="noise" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 0.05 0"/>
  </filter>

  <style>
    .pill { transition: none; }
    .pill:hover .pillRect { filter: url(#softGlow-light); }
    .pill:hover { transform: scale(1.06); }
    .social:hover { filter: url(#softGlow-light); }
    .social { transform-box: fill-box; transform-origin: center; }
    .pill { transform-box: fill-box; transform-origin: center; }
  </style>
</defs>

<g clip-path="url(#cardClip-light)">
  <rect x="0" y="0" width="1180" height="610" fill="#FFFFFF"/>

  <!-- floating ambient blobs -->
  <circle cx="150" cy="120" r="220" fill="url(#blobPurple-light)">
    <animateTransform attributeName="transform" type="translate" values="0 0; 30 20; 0 0" dur="14s" repeatCount="indefinite"/>
  </circle>
  <circle cx="950" cy="480" r="260" fill="url(#blobCyan-light)">
    <animateTransform attributeName="transform" type="translate" values="0 0; -25 -15; 0 0" dur="16s" repeatCount="indefinite"/>
  </circle>
  <circle cx="820" cy="80" r="180" fill="url(#blobEmerald-light)">
    <animateTransform attributeName="transform" type="translate" values="0 0; 15 25; 0 0" dur="11s" repeatCount="indefinite"/>
  </circle>

  <!-- noise overlay -->
  <rect x="0" y="0" width="1180" height="610" filter="url(#noiseFilter-light)" opacity="0.025"/>

  <!-- outer border shimmer -->
  <rect x="1" y="1" width="1178" height="608" rx="25" fill="none" stroke="url(#accentGrad-light)" stroke-width="1.5" opacity="0.55"/>

  <!-- LEFT PANEL : terminal ascii portrait -->
  <g clip-path="url(#leftClip-light)">
    <rect x="24" y="24" width="424" height="562" rx="18" fill="#F8FAFC" fill-opacity="0.55"/>
    <rect x="24" y="24" width="424" height="562" rx="18" fill="none" stroke="rgba(15,23,42,.14)" stroke-width="1"/>
    <rect x="25" y="25" width="422" height="560" rx="17" fill="none" stroke="url(#accentGrad-light)" stroke-width="1" stroke-dasharray="6 10" opacity="0.6">
      <animate attributeName="stroke-dashoffset" from="0" to="32" dur="3s" repeatCount="indefinite"/>
    </rect>

    <!-- terminal top bar -->
    <rect x="24" y="24" width="424" height="34" rx="18" fill="rgba(15,23,42,0.05)"/>
    <rect x="24" y="42" width="424" height="16" fill="rgba(15,23,42,0.05)"/>
    <circle cx="46" cy="41" r="5" fill="#FF5F56"/>
    <circle cx="64" cy="41" r="5" fill="#FFBD2E"/>
    <circle cx="82" cy="41" r="5" fill="#27C93F"/>
    <text x="236" y="45" text-anchor="middle" font-size="11" fill="#475569">umesh@profile ~ ascii</text>

    <text x="38" y="78.0" font-size="8.6" xml:space="preserve" fill="url(#asciiGrad-light)" opacity="0">                            I-{(|)}-+l"'<animate attributeName="opacity" from="0" to="1" begin="0.0s" dur="0.35s" fill="freeze"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -1.5;0 0" dur="5s" begin="1.0s" repeatCount="indefinite"/></text>
    <text x="38" y="93.5" font-size="8.6" xml:space="preserve" fill="url(#asciiGrad-light)" opacity="0">                          lnwbbbqQJLZOUcvt&gt;<animate attributeName="opacity" from="0" to="1" begin="0.11s" dur="0.35s" fill="freeze"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -1.5;0 0" dur="6s" begin="1.11s" repeatCount="indefinite"/></text>
    <text x="38" y="109.0" font-size="8.6" xml:space="preserve" fill="url(#asciiGrad-light)" opacity="0">                        ~rbB%&amp;MohahM*aMahkpu~.<animate attributeName="opacity" from="0" to="1" begin="0.22s" dur="0.35s" fill="freeze"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -1.5;0 0" dur="7s" begin="1.22s" repeatCount="indefinite"/></text>
    <text x="38" y="124.5" font-size="8.6" xml:space="preserve" fill="url(#asciiGrad-light)" opacity="0">                      "npM$B8%%%$$$$$$%&amp;MMWWaJ/`<animate attributeName="opacity" from="0" to="1" begin="0.33s" dur="0.35s" fill="freeze"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -1.5;0 0" dur="5s" begin="1.33s" repeatCount="indefinite"/></text>
    <text x="38" y="140.0" font-size="8.6" xml:space="preserve" fill="url(#asciiGrad-light)" opacity="0">                     :J8$B@BWhpkao*##M8$$$BWWW&amp;Q;<animate attributeName="opacity" from="0" to="1" begin="0.44s" dur="0.35s" fill="freeze"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -1.5;0 0" dur="6s" begin="1.44s" repeatCount="indefinite"/></text>
    <text x="38" y="155.5" font-size="8.6" xml:space="preserve" fill="url(#asciiGrad-light)" opacity="0">                     Y$$$@&amp;Qr\()))(\tjv0a&amp;%BB$$$n<animate attributeName="opacity" from="0" to="1" begin="0.55s" dur="0.35s" fill="freeze"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -1.5;0 0" dur="7s" begin="1.55s" repeatCount="indefinite"/></text>
    <text x="38" y="171.0" font-size="8.6" xml:space="preserve" fill="url(#asciiGrad-light)" opacity="0">                     Y$$$$Z]+-_+~+++___?{/vb$$$$r<animate attributeName="opacity" from="0" to="1" begin="0.66s" dur="0.35s" fill="freeze"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -1.5;0 0" dur="5s" begin="1.6600000000000001s" repeatCount="indefinite"/></text>
    <text x="38" y="186.5" font-size="8.6" xml:space="preserve" fill="url(#asciiGrad-light)" opacity="0">                     !M$$W\_(fjf)]--?{fxnxtc%$@X:<animate attributeName="opacity" from="0" to="1" begin="0.77s" dur="0.35s" fill="freeze"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -1.5;0 0" dur="6s" begin="1.77s" repeatCount="indefinite"/></text>
    <text x="38" y="202.0" font-size="8.6" xml:space="preserve" fill="url(#asciiGrad-light)" opacity="0">                      r@$ci)nzL0Lu(1rCmZQYv|b$q.<animate attributeName="opacity" from="0" to="1" begin="0.88s" dur="0.35s" fill="freeze"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -1.5;0 0" dur="7s" begin="1.88s" repeatCount="indefinite"/></text>
    <text x="38" y="217.5" font-size="8.6" xml:space="preserve" fill="url(#asciiGrad-light)" opacity="0">                      :vk]!1trJrnt_~\vxcYux[cq]<animate attributeName="opacity" from="0" to="1" begin="0.99s" dur="0.35s" fill="freeze"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -1.5;0 0" dur="5s" begin="1.99s" repeatCount="indefinite"/></text>
    <text x="38" y="233.0" font-size="8.6" xml:space="preserve" fill="url(#asciiGrad-light)" opacity="0">                      ?[|&lt;I&gt;~-_--&gt;l!_[]]]?__(t?<animate attributeName="opacity" from="0" to="1" begin="1.1s" dur="0.35s" fill="freeze"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -1.5;0 0" dur="6s" begin="2.1s" repeatCount="indefinite"/></text>
    <text x="38" y="248.5" font-size="8.6" xml:space="preserve" fill="url(#asciiGrad-light)" opacity="0">                      l}1-~++~+-_[]?({]+_-[}t\;<animate attributeName="opacity" from="0" to="1" begin="1.21s" dur="0.35s" fill="freeze"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -1.5;0 0" dur="7s" begin="2.21s" repeatCount="indefinite"/></text>
    <text x="38" y="264.0" font-size="8.6" xml:space="preserve" fill="url(#asciiGrad-light)" opacity="0">                       i{\?]}{|/zpmQhQj\1)(tz[.<animate attributeName="opacity" from="0" to="1" begin="1.32s" dur="0.35s" fill="freeze"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -1.5;0 0" dur="5s" begin="2.3200000000000003s" repeatCount="indefinite"/></text>
    <text x="38" y="279.5" font-size="8.6" xml:space="preserve" fill="url(#asciiGrad-light)" opacity="0">                       .!\x/)tmZJUXXLOqpujXO(^<animate attributeName="opacity" from="0" to="1" begin="1.43s" dur="0.35s" fill="freeze"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -1.5;0 0" dur="6s" begin="2.4299999999999997s" repeatCount="indefinite"/></text>
    <text x="38" y="295.0" font-size="8.6" xml:space="preserve" fill="url(#asciiGrad-light)" opacity="0">                         ;JCvnJjfxnuunxYzCdU'<animate attributeName="opacity" from="0" to="1" begin="1.54s" dur="0.35s" fill="freeze"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -1.5;0 0" dur="7s" begin="2.54s" repeatCount="indefinite"/></text>
    <text x="38" y="310.5" font-size="8.6" xml:space="preserve" fill="url(#asciiGrad-light)" opacity="0">                          ~QOLwCzJwwCY0wObO:<animate attributeName="opacity" from="0" to="1" begin="1.65s" dur="0.35s" fill="freeze"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -1.5;0 0" dur="5s" begin="2.65s" repeatCount="indefinite"/></text>
    <text x="38" y="326.0" font-size="8.6" xml:space="preserve" fill="url(#asciiGrad-light)" opacity="0">                           {wo*haao#MW&amp;Woq[<animate attributeName="opacity" from="0" to="1" begin="1.76s" dur="0.35s" fill="freeze"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -1.5;0 0" dur="6s" begin="2.76s" repeatCount="indefinite"/></text>
    <text x="38" y="341.5" font-size="8.6" xml:space="preserve" fill="url(#asciiGrad-light)" opacity="0">                          -1\Yqa&amp;%B$B&amp;#pUjx?<animate attributeName="opacity" from="0" to="1" begin="1.87s" dur="0.35s" fill="freeze"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -1.5;0 0" dur="7s" begin="2.87s" repeatCount="indefinite"/></text>
    <text x="38" y="357.0" font-size="8.6" xml:space="preserve" fill="url(#asciiGrad-light)" opacity="0">                         ^nr{\trcXXJUXvrf/UuI<animate attributeName="opacity" from="0" to="1" begin="1.98s" dur="0.35s" fill="freeze"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -1.5;0 0" dur="5s" begin="2.98s" repeatCount="indefinite"/></text>
    <text x="38" y="372.5" font-size="8.6" xml:space="preserve" fill="url(#asciiGrad-light)" opacity="0">                        ^+-vt((\/tffrrfttrC|1"<animate attributeName="opacity" from="0" to="1" begin="2.09s" dur="0.35s" fill="freeze"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -1.5;0 0" dur="6s" begin="3.09s" repeatCount="indefinite"/></text>

    <!-- scanline sweep -->
    <rect x="24" y="78" width="424" height="2" fill="url(#accentGrad-light)" opacity="0.4">
      <animate attributeName="y" values="78;408.0;78" dur="4s" repeatCount="indefinite"/>
    </rect>

    <!-- blinking cursor under ascii -->
    <text x="38" y="428.0" font-size="12" fill="#0F172A">&gt; <tspan fill="url(#accentGrad-light)">_</tspan></text>
    <rect x="52" y="417.0" width="7" height="13" fill="url(#accentGrad-light)">
      <animate attributeName="opacity" values="1;1;0;0;1" keyTimes="0;0.4;0.5;0.9;1" dur="1.1s" repeatCount="indefinite"/>
    </rect>

    <text x="38" y="456.0" font-size="12.5" fill="#475569">B.Tech CSE (AI &amp; ML) · Vishnu IoT</text>
    <text x="38" y="478.0" font-size="12.5" fill="#475569">CGPA 9.59/10 · Bhimavaram, AP</text>
  </g>

  <!-- RIGHT PANEL : profile terminal -->
  <g clip-path="url(#rightClip-light)">
    <rect x="468" y="24" width="688" height="562" rx="18" fill="#F8FAFC" fill-opacity="0.55"/>
    <rect x="468" y="24" width="688" height="562" rx="18" fill="none" stroke="rgba(15,23,42,.14)" stroke-width="1"/>
    <rect x="469" y="25" width="686" height="560" rx="17" fill="none" stroke="url(#accentGrad-light)" stroke-width="1" stroke-dasharray="6 10" opacity="0.6">
      <animate attributeName="stroke-dashoffset" from="32" to="0" dur="3s" repeatCount="indefinite"/>
    </rect>

    <rect x="468" y="24" width="688" height="34" rx="18" fill="rgba(15,23,42,0.05)"/>
    <rect x="468" y="42" width="688" height="16" fill="rgba(15,23,42,0.05)"/>
    <circle cx="490" cy="41" r="5" fill="#FF5F56"/>
    <circle cx="508" cy="41" r="5" fill="#FFBD2E"/>
    <circle cx="526" cy="41" r="5" fill="#27C93F"/>
    <text x="812" y="45" text-anchor="middle" font-size="11" fill="#475569">umesh@portfolio: ~</text>

    <text x="500" y="100" font-size="26" font-weight="700" fill="#0F172A" opacity="0">
      Hi 👋
      <animate attributeName="opacity" from="0" to="1" begin="0.2s" dur="0.5s" fill="freeze"/>
    </text>
    <text x="500" y="136" font-size="21" font-weight="600" fill="#0F172A" opacity="0">
      I'm Umesh Sai Hanuma Prasad Syamala
      <animate attributeName="opacity" from="0" to="1" begin="0.6s" dur="0.5s" fill="freeze"/>
    </text>
    <text x="500" y="168" font-size="15.5" fill="url(#accentGrad-light)" opacity="0">Building AI agents that ship<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.05;0.85;1" dur="12s" begin="0s" repeatCount="indefinite"/></text>
    <text x="500" y="168" font-size="15.5" fill="url(#accentGrad-light)" opacity="0">GenAI / RAG Engineer<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.05;0.85;1" dur="12s" begin="3s" repeatCount="indefinite"/></text>
    <text x="500" y="168" font-size="15.5" fill="url(#accentGrad-light)" opacity="0">Full Stack + LLM Systems<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.05;0.85;1" dur="12s" begin="6s" repeatCount="indefinite"/></text>
    <text x="500" y="168" font-size="15.5" fill="url(#accentGrad-light)" opacity="0">Open Source Contributor<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.05;0.85;1" dur="12s" begin="9s" repeatCount="indefinite"/></text>
    <rect x="500" y="157" width="8" height="15" fill="url(#accentGrad-light)">
      <animate attributeName="opacity" values="1;1;0;0;1" keyTimes="0;0.4;0.5;0.9;1" dur="1s" repeatCount="indefinite"/>
    </rect>
    <g opacity="0" transform="translate(-12,0)">
      <animate attributeName="opacity" from="0" to="1" begin="1.0s" dur="0.4s" fill="freeze"/>
      <animateTransform attributeName="transform" type="translate" from="-12 0" to="0 0" begin="1.0s" dur="0.4s" fill="freeze"/>
      <text x="500" y="210" font-size="14" fill="#0F172A">📍</text>
      <text x="524" y="210" font-size="12.5" fill="#475569">Location:</text>
      <text x="600" y="210" font-size="12.5" fill="#0F172A">Bhimavaram, Andhra Pradesh, India</text>
    </g>
    <g opacity="0" transform="translate(-12,0)">
      <animate attributeName="opacity" from="0" to="1" begin="1.25s" dur="0.4s" fill="freeze"/>
      <animateTransform attributeName="transform" type="translate" from="-12 0" to="0 0" begin="1.25s" dur="0.4s" fill="freeze"/>
      <text x="500" y="236" font-size="14" fill="#0F172A">🎓</text>
      <text x="524" y="236" font-size="12.5" fill="#475569">Education:</text>
      <text x="600" y="236" font-size="12.5" fill="#0F172A">B.Tech CSE (AI &amp; ML), CGPA 9.59/10</text>
    </g>
    <g opacity="0" transform="translate(-12,0)">
      <animate attributeName="opacity" from="0" to="1" begin="1.5s" dur="0.4s" fill="freeze"/>
      <animateTransform attributeName="transform" type="translate" from="-12 0" to="0 0" begin="1.5s" dur="0.4s" fill="freeze"/>
      <text x="500" y="262" font-size="14" fill="#0F172A">🎯</text>
      <text x="524" y="262" font-size="12.5" fill="#475569">Focus:</text>
      <text x="600" y="262" font-size="12.5" fill="#0F172A">AI Agents, RAG Systems, Full-Stack GenAI</text>
    </g>
    <g opacity="0" transform="translate(-12,0)">
      <animate attributeName="opacity" from="0" to="1" begin="1.75s" dur="0.4s" fill="freeze"/>
      <animateTransform attributeName="transform" type="translate" from="-12 0" to="0 0" begin="1.75s" dur="0.4s" fill="freeze"/>
      <text x="500" y="288" font-size="14" fill="#0F172A">🌐</text>
      <text x="524" y="288" font-size="12.5" fill="#475569">Portfolio:</text>
      <text x="600" y="288" font-size="12.5" fill="#0F172A">github.com/Umesh-369</text>
    </g>
    <g opacity="0" transform="translate(-12,0)">
      <animate attributeName="opacity" from="0" to="1" begin="2.0s" dur="0.4s" fill="freeze"/>
      <animateTransform attributeName="transform" type="translate" from="-12 0" to="0 0" begin="2.0s" dur="0.4s" fill="freeze"/>
      <text x="500" y="314" font-size="14" fill="#0F172A">✉</text>
      <text x="524" y="314" font-size="12.5" fill="#475569">Email:</text>
      <text x="600" y="314" font-size="12.5" fill="#0F172A">s.umeshsaihanumaprasad@gmail.com</text>
    </g>
    <text x="500" y="358" font-size="12.5" font-weight="700" fill="#475569">SKILLS</text>
    <g class="pill" opacity="0">
      <animate attributeName="opacity" from="0" to="1" begin="2.2s" dur="0.35s" fill="freeze"/>
      <rect class="pillRect" x="500.0" y="359.0" width="60.2" height="24" rx="12" fill="rgba(37,99,235,0.08)" stroke="rgba(6,182,212,0.35)" stroke-width="1"/>
      <text x="530.1" y="375.0" text-anchor="middle" font-size="11.5" fill="#0F172A">Python</text>
    </g>
    <g class="pill" opacity="0">
      <animate attributeName="opacity" from="0" to="1" begin="2.2800000000000002s" dur="0.35s" fill="freeze"/>
      <rect class="pillRect" x="570.2" y="359.0" width="81.8" height="24" rx="12" fill="rgba(37,99,235,0.08)" stroke="rgba(6,182,212,0.35)" stroke-width="1"/>
      <text x="611.1" y="375.0" text-anchor="middle" font-size="11.5" fill="#0F172A">LangChain</text>
    </g>
    <g class="pill" opacity="0">
      <animate attributeName="opacity" from="0" to="1" begin="2.3600000000000003s" dur="0.35s" fill="freeze"/>
      <rect class="pillRect" x="662.0" y="359.0" width="89.0" height="24" rx="12" fill="rgba(37,99,235,0.08)" stroke="rgba(6,182,212,0.35)" stroke-width="1"/>
      <text x="706.5" y="375.0" text-anchor="middle" font-size="11.5" fill="#0F172A">Gemini API</text>
    </g>
    <g class="pill" opacity="0">
      <animate attributeName="opacity" from="0" to="1" begin="2.4400000000000004s" dur="0.35s" fill="freeze"/>
      <rect class="pillRect" x="761.0" y="359.0" width="67.4" height="24" rx="12" fill="rgba(37,99,235,0.08)" stroke="rgba(6,182,212,0.35)" stroke-width="1"/>
      <text x="794.7" y="375.0" text-anchor="middle" font-size="11.5" fill="#0F172A">FastAPI</text>
    </g>
    <g class="pill" opacity="0">
      <animate attributeName="opacity" from="0" to="1" begin="2.52s" dur="0.35s" fill="freeze"/>
      <rect class="pillRect" x="838.4" y="359.0" width="53.0" height="24" rx="12" fill="rgba(37,99,235,0.08)" stroke="rgba(6,182,212,0.35)" stroke-width="1"/>
      <text x="864.9" y="375.0" text-anchor="middle" font-size="11.5" fill="#0F172A">React</text>
    </g>
    <g class="pill" opacity="0">
      <animate attributeName="opacity" from="0" to="1" begin="2.6s" dur="0.35s" fill="freeze"/>
      <rect class="pillRect" x="901.4" y="359.0" width="67.4" height="24" rx="12" fill="rgba(37,99,235,0.08)" stroke="rgba(6,182,212,0.35)" stroke-width="1"/>
      <text x="935.1" y="375.0" text-anchor="middle" font-size="11.5" fill="#0F172A">Next.js</text>
    </g>
    <g class="pill" opacity="0">
      <animate attributeName="opacity" from="0" to="1" begin="2.68s" dur="0.35s" fill="freeze"/>
      <rect class="pillRect" x="978.8" y="359.0" width="89.0" height="24" rx="12" fill="rgba(37,99,235,0.08)" stroke="rgba(6,182,212,0.35)" stroke-width="1"/>
      <text x="1023.3" y="375.0" text-anchor="middle" font-size="11.5" fill="#0F172A">TypeScript</text>
    </g>
    <g class="pill" opacity="0">
      <animate attributeName="opacity" from="0" to="1" begin="2.7600000000000002s" dur="0.35s" fill="freeze"/>
      <rect class="pillRect" x="1077.8" y="359.0" width="53.0" height="24" rx="12" fill="rgba(37,99,235,0.08)" stroke="rgba(6,182,212,0.35)" stroke-width="1"/>
      <text x="1104.3" y="375.0" text-anchor="middle" font-size="11.5" fill="#0F172A">FAISS</text>
    </g>
    <g class="pill" opacity="0">
      <animate attributeName="opacity" from="0" to="1" begin="2.8400000000000003s" dur="0.35s" fill="freeze"/>
      <rect class="pillRect" x="500.0" y="393.0" width="60.2" height="24" rx="12" fill="rgba(37,99,235,0.08)" stroke="rgba(6,182,212,0.35)" stroke-width="1"/>
      <text x="530.1" y="409.0" text-anchor="middle" font-size="11.5" fill="#0F172A">Ollama</text>
    </g>
    <g class="pill" opacity="0">
      <animate attributeName="opacity" from="0" to="1" begin="2.92s" dur="0.35s" fill="freeze"/>
      <rect class="pillRect" x="570.2" y="393.0" width="67.4" height="24" rx="12" fill="rgba(37,99,235,0.08)" stroke="rgba(6,182,212,0.35)" stroke-width="1"/>
      <text x="603.9" y="409.0" text-anchor="middle" font-size="11.5" fill="#0F172A">MongoDB</text>
    </g>
    <g class="pill" opacity="0">
      <animate attributeName="opacity" from="0" to="1" begin="3.0s" dur="0.35s" fill="freeze"/>
      <rect class="pillRect" x="647.6" y="393.0" width="38.6" height="24" rx="12" fill="rgba(37,99,235,0.08)" stroke="rgba(6,182,212,0.35)" stroke-width="1"/>
      <text x="666.9" y="409.0" text-anchor="middle" font-size="11.5" fill="#0F172A">Git</text>
    </g>
    <g class="pill" opacity="0">
      <animate attributeName="opacity" from="0" to="1" begin="3.08s" dur="0.35s" fill="freeze"/>
      <rect class="pillRect" x="696.2" y="393.0" width="60.2" height="24" rx="12" fill="rgba(37,99,235,0.08)" stroke="rgba(6,182,212,0.35)" stroke-width="1"/>
      <text x="726.3" y="409.0" text-anchor="middle" font-size="11.5" fill="#0F172A">OpenCV</text>
    </g>
    <line x1="500" y1="440" x2="1136" y2="440" stroke="rgba(15,23,42,.08)" stroke-width="1"/>
    <a xlink:href="https://github.com/Umesh-369" target="_blank">
    <g class="social" opacity="0">
      <animate attributeName="opacity" from="0" to="1" begin="2.6s" dur="0.4s" fill="freeze"/>
      <circle cx="518" cy="464" r="18" fill="rgba(37,99,235,0.08)" stroke="rgba(6,182,212,0.35)" stroke-width="1"/>
      <text x="518" y="468" text-anchor="middle" font-size="12" font-weight="700" fill="#0F172A">GH</text>
      <animateTransform attributeName="transform" type="scale" additive="sum" values="1;1.04;1" dur="3s" begin="2.6s" repeatCount="indefinite"/>
    </g>
    </a>
    <a xlink:href="https://linkedin.com/in/umeshsaihanumaprasad" target="_blank">
    <g class="social" opacity="0">
      <animate attributeName="opacity" from="0" to="1" begin="2.72s" dur="0.4s" fill="freeze"/>
      <circle cx="564" cy="464" r="18" fill="rgba(37,99,235,0.08)" stroke="rgba(6,182,212,0.35)" stroke-width="1"/>
      <text x="564" y="468" text-anchor="middle" font-size="12" font-weight="700" fill="#0F172A">in</text>
      <animateTransform attributeName="transform" type="scale" additive="sum" values="1;1.04;1" dur="3s" begin="2.72s" repeatCount="indefinite"/>
    </g>
    </a>
    <a xlink:href="mailto:s.umeshsaihanumaprasad@gmail.com" target="_blank">
    <g class="social" opacity="0">
      <animate attributeName="opacity" from="0" to="1" begin="2.84s" dur="0.4s" fill="freeze"/>
      <circle cx="610" cy="464" r="18" fill="rgba(37,99,235,0.08)" stroke="rgba(6,182,212,0.35)" stroke-width="1"/>
      <text x="610" y="468" text-anchor="middle" font-size="12" font-weight="700" fill="#0F172A">✉</text>
      <animateTransform attributeName="transform" type="scale" additive="sum" values="1;1.04;1" dur="3s" begin="2.84s" repeatCount="indefinite"/>
    </g>
    </a>
    <a xlink:href="https://github.com/Umesh-369" target="_blank">
    <g class="social" opacity="0">
      <animate attributeName="opacity" from="0" to="1" begin="2.96s" dur="0.4s" fill="freeze"/>
      <circle cx="656" cy="464" r="18" fill="rgba(37,99,235,0.08)" stroke="rgba(6,182,212,0.35)" stroke-width="1"/>
      <text x="656" y="468" text-anchor="middle" font-size="12" font-weight="700" fill="#0F172A">W</text>
      <animateTransform attributeName="transform" type="scale" additive="sum" values="1;1.04;1" dur="3s" begin="2.96s" repeatCount="indefinite"/>
    </g>
    </a>
  </g>
</g>
</svg>
