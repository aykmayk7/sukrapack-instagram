"""Hafta 47 (16-22 Kas 2026) içerikleri. HTML -> Playwright -> PNG / MP4.
Çalıştır: python3 gen/week47.py   (depo kökünden)
"""
import os, subprocess, shutil, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
GEN = ROOT / "gen"
FONTS = (GEN / "fonts.css").read_text()

C = dict(cream="#F6F0E4", dark="#2A1B10", gold="#B07A3A", lgold="#E3B877", green="#2F7A4C")

def logo(dark_bg=True, h=1.0):
    leaf = "#6FBF8A" if dark_bg else C["green"]
    bar = C["lgold"] if dark_bg else C["gold"]
    return (f'<svg viewBox="28 12 64 98" style="height:{h}em;width:auto;display:inline-block;vertical-align:-0.12em">'
            f'<path fill="{leaf}" d="M90 18 C70 12 40 20 30 50 C52 50 78 40 90 18 Z"/>'
            f'<path fill="{leaf}" d="M30 102 C50 108 80 100 90 70 C68 70 42 80 30 102 Z"/>'
            f'<path fill="{bar}" d="M36.79 51.56 L84.79 58.56 A5.5 5.5 0 0 1 83.21 69.44 L35.21 62.44 A5.5 5.5 0 0 1 36.79 51.56 Z"/></svg>')

def wordmark(dark_bg=True, size=64):
    col = C["cream"] if dark_bg else C["dark"]
    # S yerine logo; logo ile "u" arası harf aralığı kadar (≈0.04em)
    return (f'<span class="wm" style="font-size:{size}px;color:{col}">{logo(dark_bg, 0.92)}'
            f'<span style="margin-left:0.04em">ukra</span></span>')

BASE_CSS = f"""
{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:var(--w);height:var(--h);overflow:hidden}}
body{{font-family:'Figtree',sans-serif;-webkit-font-smoothing:antialiased}}
.wm{{font-family:'Baloo 2';font-weight:700;letter-spacing:0.01em;line-height:1;white-space:nowrap}}
h1,h2,.num{{font-family:'Baloo 2';font-weight:800;line-height:1.02;letter-spacing:-0.01em}}
.kicker{{font-family:'Figtree';font-weight:700;letter-spacing:0.18em;text-transform:uppercase;font-size:26px}}
.page{{position:relative;width:100%;height:100%;padding:96px 88px}}
.dark{{background:{C['dark']};color:{C['cream']}}}
.light{{background:{C['cream']};color:{C['dark']}}}
.rule{{width:120px;height:6px;background:{C['gold']};border-radius:3px}}
.foot{{position:absolute;left:88px;right:88px;bottom:80px;display:flex;justify-content:space-between;align-items:center}}
.handle{{font-weight:600;font-size:26px;opacity:.75}}
"""

def doc(body, w=1080, h=1350, extra=""):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>:root{{--w:{w}px;--h:{h}px}}{BASE_CSS}{extra}</style></head><body>{body}</body></html>"

# ---------- A) Carousel: Paketi kapatmadan önce 4 kontrol ----------
def kontrol():
    out = []
    cover = f"""<div class="page dark">
      <div class="kicker" style="color:{C['lgold']}">Paket servis · Kaydedin</div>
      <h1 style="font-size:128px;margin-top:64px">Paketi<br>kapatmadan<br>önce <span style="color:{C['lgold']}">4 kontrol.</span></h1>
      <div class="rule" style="margin:56px 0 40px"></div>
      <p style="font-size:40px;line-height:1.35;max-width:820px;opacity:.9">Beş saniye sürer. Müşteriniz farkı ilk lokmadan önce görür.</p>
      <div class="foot">{wordmark(True,60)}<span class="handle">Kaydırın →</span></div></div>"""
    out.append(("Sukra_v2_22_Kontrol_1.png", doc(cover)))
    items = [
        ("01", "Sos ayrı kapta.", "Sosu yemeğin üstüne değil, yanına koyun. Kızartma çıtır, salata diri kalır; müşteri sosu kendi ayarlar."),
        ("02", "Sıcak ile soğuk ayrı.", "Sıcak ana yemek ile soğuk meze aynı gözde durmasın. Buhar soğuğu ılıtır, soğuk sıcağı söndürür."),
        ("03", "Peçete ve çatal en üstte.", "Poşeti açan müşterinin eli ilk neye gidecekse o hazır olsun. Aramak, ilk izlenimi bozar."),
        ("04", "Kapak kapandı, imza atıldı.", "Logolu etiket ya da mühür bandı. Paketin yolda açılmadığını ve kimden geldiğini tek bakışta söyler."),
    ]
    for i, (n, t, d) in enumerate(items, start=2):
        last = i == 5
        foot = (f'<div class="foot">{wordmark(False,60)}<span class="handle">Ekibinizle paylaşın</span></div>' if last
                else f'<div class="foot">{wordmark(False,60)}<span class="handle">{i-1} / 4</span></div>')
        body = f"""<div class="page light">
          <div class="kicker" style="color:{C['gold']}">Paketi kapatmadan önce</div>
          <div class="num" style="font-size:300px;color:{C['gold']};margin-top:60px;line-height:.9">{n}</div>
          <h2 style="font-size:96px;margin-top:40px;max-width:900px">{t}</h2>
          <div class="rule" style="margin:48px 0 36px;background:{C['green']}"></div>
          <p style="font-size:42px;line-height:1.4;max-width:880px">{d}</p>
          {foot}</div>"""
        out.append((f"Sukra_v2_22_Kontrol_{i}.png", doc(body)))
    return out

# ---------- C) Bir koli yeter ----------
def koli():
    chips = "".join(f'<span style="display:inline-block;border:3px solid {C["gold"]};border-radius:60px;padding:18px 34px;margin:0 18px 22px 0;font-size:36px;font-weight:600">{c}</span>'
                    for c in ["Minimum sipariş yok", "Koli bazında", "Havale / EFT", "Antalya içi aynı gün teslimat"])
    body = f"""<div class="page light">
      <div class="kicker" style="color:{C['gold']}">Yeni açılan işletmeler için</div>
      <h1 style="font-size:190px;margin-top:70px">Bir koli<br><span style="color:{C['green']}">yeter.</span></h1>
      <p style="font-size:44px;line-height:1.38;max-width:880px;margin:56px 0 64px">Yeni kafe, küçük mutfak, deneme menüsü. Depo doldurmadan, ihtiyacınız kadar başlayın.</p>
      <div>{chips}</div>
      <div class="foot">{wordmark(False,60)}<span class="handle">DM · @sukrapack</span></div></div>"""
    return [("Sukra_v2_24_Bir_Koli.png", doc(body))]

# ---------- D) Yerinde sunum (teklif) ----------
def sunum():
    body = f"""<div class="page dark" style="display:flex;flex-direction:column">
      <div class="kicker" style="color:{C['lgold']}">Antalya · Yerinde sunum</div>
      <h1 style="font-size:150px;margin-top:80px">Kutuları<br>masanızda<br><span style="color:{C['lgold']}">görün.</span></h1>
      <div class="rule" style="margin:60px 0 44px"></div>
      <p style="font-size:44px;line-height:1.38;max-width:860px;opacity:.92">Restoranınıza gelelim. Ürünleri kendi masanızda, menünüzün yanında birlikte inceleyelim; hangi kutunun hangi yemeğe yakıştığına beraber karar verelim.</p>
      <div class="foot">{wordmark(True,60)}<span class="handle" style="opacity:.9">Randevu için DM</span></div></div>"""
    return [("Sukra_v2_25_Yerinde_Sunum.png", doc(body))]

# ---------- B) Reels: En kalabalık şubeniz ----------
REEL_LINES = [  # (başlangıç sn, metin, stil)
    (0.3, "Salonunuzda ışık var,<br>müzik var, garson var.", "s"),
    (3.0, "Paket servis müşterinizin evinde ise", "s"),
    (5.2, "yalnızca <span class='g'>paketiniz</span> var.", "b"),
    (8.0, "En kalabalık şubeniz,<br><span class='g'>müşterinizin evi.</span>", "b"),
]
REEL_T = 13.0

def reel_html():
    lines = "".join(f'<div class="ln {s}" data-t="{t}">{txt}</div>' for t, txt, s in REEL_LINES)
    extra = f"""
    .stage{{position:absolute;inset:0;padding:0 96px;display:flex;flex-direction:column;justify-content:center}}
    .ln{{opacity:0;transform:translateY(40px);margin:18px 0}}
    .ln.s{{font-family:'Figtree';font-weight:600;font-size:64px;line-height:1.25}}
    .ln.b{{font-family:'Baloo 2';font-weight:800;font-size:112px;line-height:1.05}}
    .g{{color:{C['lgold']}}}
    #end{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;opacity:0;background:{C['dark']}}}
    #end p{{font-size:46px;margin-top:44px;opacity:.9;text-align:center;line-height:1.35}}
    #bar{{position:absolute;left:96px;top:420px;height:6px;width:0;background:{C['gold']};border-radius:3px}}
    """
    body = f"""<div class="dark" style="position:absolute;inset:0">
      <div id="bar"></div>
      <div class="stage">{lines}</div>
      <div id="end">{wordmark(True,150)}<p>Şeker kamışı lifinden.<br>Restoranınızın imzası.</p></div></div>
    <script>
    const ease=x=>1-Math.pow(1-Math.min(Math.max(x,0),1),3);
    window.setT=t=>{{
      document.querySelectorAll('.ln').forEach(el=>{{
        const s=+el.dataset.t; let a=ease((t-s)/0.6);
        if(t>10.0) a*=1-ease((t-10.0)/0.5);
        el.style.opacity=a; el.style.transform=`translateY(${{(1-a)*40}}px)`;
      }});
      document.getElementById('bar').style.width=(ease(t/1.2)*160)+'px';
      document.getElementById('end').style.opacity=ease((t-10.3)/0.7);
    }};
    setT(0);
    </script>"""
    return doc(body, 1080, 1920, extra)

def render():
    out_png = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        for name, html in kontrol() + koli() + sunum():
            f = GEN / "_tmp.html"; f.write_text(html)
            pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(150)
            sh = pg.evaluate("[document.body.scrollHeight, document.body.scrollWidth, Math.max(...[...document.querySelectorAll('.page *')].map(e=>e.getBoundingClientRect().bottom))]")
            print(name, "scroll", sh)
            pg.screenshot(path=str(ROOT / name)); out_png.append(name)
        # reel
        pg2 = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        f = GEN / "_tmp.html"; f.write_text(reel_html())
        pg2.goto(f.as_uri()); pg2.evaluate("document.fonts.ready"); pg2.wait_for_timeout(200)
        fr = GEN / "_frames"; shutil.rmtree(fr, ignore_errors=True); fr.mkdir()
        fps = 30
        for i in range(int(REEL_T * fps)):
            pg2.evaluate(f"setT({i/fps})")
            pg2.screenshot(path=str(fr / f"{i:04d}.png"))
        pg2.evaluate("setT(9.2); [...document.querySelectorAll('.ln')].slice(0,3).forEach(e=>e.style.display='none')"); pg2.screenshot(path=str(ROOT / "Sukra_v2_23_Sube_Kapak.png"))
        b.close()
    (ROOT / "reels").mkdir(exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", "30", "-i", str(fr / "%04d.png"),
                    "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-crf", "20",
                    str(ROOT / "reels" / "Sukra_Reels_Sube.mp4")], check=True)
    shutil.rmtree(fr); (GEN / "_tmp.html").unlink()

if __name__ == "__main__":
    render()
