import re

BASE = "/Users/Doni/EnterpriseAssistant/Library/dashboards/npi-duo-snapshot"
src = open(f"{BASE}/index.html", encoding="utf-8").read()

override = """
<style id="render-overrides">
html, body {
  width: 1920px !important;
  height: 1080px !important;
  overflow: hidden !important;
  padding: 0 !important;
  margin: 0 !important;
  scroll-snap-type: none !important;
  background: #0b0b0d !important;
}
.slide {
  width: 1920px !important;
  height: 1080px !important;
  min-height: 1080px !important;
  max-height: 1080px !important;
  margin: 0 !important;
  border: none !important;
  border-radius: 0 !important;
  box-shadow: none !important;
  scroll-snap-align: none !important;
  overflow: hidden !important;
  background: linear-gradient(180deg, rgba(255,255,255,0.015), transparent 40%), #0b0b0d !important;
}
.nav-dots, .scroll-cue, .keynote-download { display: none !important; }
</style>
</head>"""

out = src.replace("</head>", override, 1)
dest = f"{BASE}/_slides_render.html"
open(dest, "w", encoding="utf-8").write(out)
print("wrote", dest)
print("slides:", len(re.findall(r'class="slide"', src)))
