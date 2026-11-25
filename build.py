# cresell.html 을 배포용 index.html 로 감싼다
import pathlib
here=pathlib.Path(__file__).parent
src=here.parent/"크레셀 프로토타입"/"cresell.html"
head="""<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="#0f6b55">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="크레셀">
<link rel="icon" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
</head><body>
"""
tail="""
<script>if('serviceWorker' in navigator)addEventListener('load',()=>navigator.serviceWorker.register('sw.js').catch(()=>{}));</script>
</body></html>
"""
(here/"index.html").write_text(head+src.read_text(encoding="utf-8")+tail,encoding="utf-8")
print("index.html", (here/"index.html").stat().st_size)
