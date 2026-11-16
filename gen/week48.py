"""Hafta 48 (23-29 Kas 2026) içerikleri. HTML -> Playwright -> PNG / MP4.
Çalıştır: python3 gen/week48.py   (depo kökünden)
Ortak stil ve wordmark: gen/week47.py
"""
import sys, subprocess, shutil, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from week47 import C, doc, wordmark, ROOT, GEN
from playwright.sync_api import sync_playwright

# ---------- 26) Carousel: Personel yemekhanesi, bir tabağın gerçek maliyeti ----------
def yemekhane():
    out = []
    cover = f"""<div class="page dark">
      <div class="kicker" style="color:{C['lgold']}">Oteller için · Kaydedin</div>
      <h1 style="font-size:120px;margin-top:64px">Personel<br>yemekhanesinde<br>bir tabak <span style="color:{C['lgold']}">kaça<br>yıkanıyor?</span></h1>
      <div class="rule" style="margin:52px 0 36px"></div>
      <p style="font-size:40px;line-height:1.35;max-width:840px;opacity:.9">Cevap 4 kalemde saklı. Kendi rakamlarınızla hesaplayın.</p>
      <div class="foot">{wordmark(True,60)}<span class="handle">Kaydırın →</span></div></div>"""
    out.append(("Sukra_v2_26_Yemekhane_1.png", doc(cover)))
    items = [
        ("01", "Su ve elektrik.", "Bulaşık makinesinin günlük çalışma saati, saatlik su ve enerji tüketimiyle çarpılır. Yemekhane makinesi çoğu zaman en uzun çalışanıdır."),
        ("02", "Deterjan ve parlatıcı.", "Aylık kimyasal faturası. Genellikle ayrı bir kalemde durur; kimse onu tabağa bölmez."),
        ("03", "Emek.", "Tabağı toplayan, yıkayan, kurulayan ve dizen ekibin yemekhaneye ayırdığı saatler."),
        ("04", "Kırılan ve kaybolan.", "Yıl içinde yenilenen tabak, kase, bardak ve çatal. Küçük görünür, toplamı büyür."),
    ]
    for i, (n, t, d) in enumerate(items, start=2):
        body = f"""<div class="page light">
          <div class="kicker" style="color:{C['gold']}">Bir tabağın gerçek maliyeti</div>
          <div class="num" style="font-size:300px;color:{C['gold']};margin-top:60px;line-height:.9">{n}</div>
          <h2 style="font-size:96px;margin-top:40px;max-width:900px">{t}</h2>
          <div class="rule" style="margin:48px 0 36px;background:{C['green']}"></div>
          <p style="font-size:42px;line-height:1.4;max-width:880px">{d}</p>
          <div class="foot">{wordmark(False,60)}<span class="handle">{i-1} / 4</span></div></div>"""
        out.append((f"Sukra_v2_26_Yemekhane_{i}.png", doc(body)))
    box = f"border:3px solid {C['lgold']};border-radius:28px;padding:40px 44px"
    last = f"""<div class="page dark">
      <div class="kicker" style="color:{C['lgold']}">Formül</div>
      <div style="{box};margin-top:64px">
        <div style="font-size:44px;line-height:1.35">4 kalemin <b>aylık toplamı</b></div>
        <div style="height:4px;background:{C['lgold']};margin:24px 0;border-radius:2px"></div>
        <div style="font-size:44px;line-height:1.35">aylık <b>personel öğünü sayısı</b></div>
      </div>
      <h2 style="font-size:84px;margin-top:56px">= öğün başı<br><span style="color:{C['lgold']}">yıkama maliyeti.</span></h2>
      <p style="font-size:40px;line-height:1.38;max-width:860px;margin-top:44px;opacity:.92">Bu rakamı bagas kabın öğün başı fiyatıyla yan yana koyun. İsterseniz birlikte hesaplayalım.</p>
      <div class="foot">{wordmark(True,60)}<span class="handle" style="opacity:.9">DM · @sukrapack</span></div></div>"""
    out.append(("Sukra_v2_26_Yemekhane_6.png", doc(last)))
    return out

# ---------- 27) Yılbaşına 5 hafta ----------
def yilbasi():
    rows = "".join(
        f'<div style="display:flex;align-items:flex-start;margin:0 0 30px"><span style="flex:none;width:52px;height:52px;border-radius:50%;background:{C["green"]};color:{C["cream"]};font-family:\'Baloo 2\';font-weight:800;font-size:32px;display:flex;align-items:center;justify-content:center;margin-right:28px">{i}</span>'
        f'<span style="font-size:40px;line-height:1.35;padding-top:2px">{t}</span></div>'
        for i, t in enumerate(["Geçen yılbaşı haftasının paket siparişlerine bakın.",
                               "En çok çıkan 3 yemeğin kabını belirleyin.",
                               "Koli ihtiyacınızı aralık başında netleştirin."], 1))
    body = f"""<div class="page light">
      <div class="kicker" style="color:{C['gold']}">Restoran ve kafeler için</div>
      <h1 style="font-size:170px;margin-top:64px">Yılbaşına<br><span style="color:{C['green']}">5 hafta.</span></h1>
      <p style="font-size:42px;line-height:1.38;max-width:880px;margin:48px 0 52px">Yoğun gece mutfakta değil, depoda kazanılır. Paket stoğunu şimdiden planlayın:</p>
      {rows}
      <div class="foot">{wordmark(False,60)}<span class="handle">Kaydedin · DM</span></div></div>"""
    return [("Sukra_v2_27_Yilbasi.png", doc(body))]

# ---------- 28) Sahadan bir not ----------
def saha():
    body = f"""<div class="page dark">
      <div class="kicker" style="color:{C['lgold']}">Sahadan bir not</div>
      <p style="font-size:42px;line-height:1.4;margin-top:64px;opacity:.85">Bir otel yöneticisi bize şunu söyledi:</p>
      <h1 style="font-size:96px;margin-top:28px;line-height:1.08">“Misafir tabağını yıkamak bize <span style="color:{C['lgold']}">pahalı değil.</span>”</h1>
      <div class="rule" style="margin:52px 0 40px"></div>
      <h2 style="font-size:72px">Haklı.</h2>
      <p style="font-size:40px;line-height:1.4;max-width:880px;margin-top:24px;opacity:.92">Havuzda ve restoranda porselen çoğu zaman yerinde kalır. Hesabın değiştiği yer personel yemekhanesi: her gün yüzlerce öğün, ayrı bir bulaşık hattı.</p>
      <div class="foot">{wordmark(True,60)}<span class="handle" style="opacity:.9">DM · @sukrapack</span></div></div>"""
    return [("Sukra_v2_28_Sahadan_Not.png", doc(body))]

# ---------- R4) Reels: Kadrajda paketiniz var ----------
REEL_LINES = [  # (başlangıç sn, metin, stil) ; ilk satır 0. sn'de tam görünür (kanca)
    (-1.0, "Müşteriniz yemeğinizin<br><span class='g'>fotoğrafını</span> çekiyor.", "b"),
    (2.6, "Hikayesine koyuyor. Arkadaşına gönderiyor.", "s"),
    (5.0, "Kadrajda yemeğiniz kadar<br><span class='g'>paketiniz</span> da var.", "b"),
]
REEL_T = 12.0

def reel_html():
    lines = "".join(f'<div class="ln {s}" data-t="{t}">{txt}</div>' for t, txt, s in REEL_LINES)
    extra = f"""
    .stage{{position:absolute;inset:0;padding:0 96px;display:flex;flex-direction:column;justify-content:center}}
    .ln{{opacity:0;transform:translateY(40px);margin:26px 0}}
    .ln.s{{font-family:'Figtree';font-weight:600;font-size:60px;line-height:1.25}}
    .ln.b{{font-family:'Baloo 2';font-weight:800;font-size:104px;line-height:1.05}}
    .g{{color:{C['lgold']}}}
    #frame{{position:absolute;left:60px;right:60px;top:300px;bottom:300px;border:5px solid {C['lgold']};border-radius:36px;opacity:.0}}
    #end{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;opacity:0;background:{C['dark']}}}
    #end p{{font-size:46px;margin-top:44px;opacity:.9;text-align:center;line-height:1.35}}
    """
    body = f"""<div class="dark" style="position:absolute;inset:0">
      <div id="frame"></div>
      <div class="stage">{lines}</div>
      <div id="end">{wordmark(True,150)}<p>Fotoğrafa yakışan paket.<br>Şeker kamışı lifinden.</p></div></div>
    <script>
    const ease=x=>1-Math.pow(1-Math.min(Math.max(x,0),1),3);
    window.setT=t=>{{
      document.querySelectorAll('.ln').forEach(el=>{{
        const s=+el.dataset.t; let a=ease((t-s)/0.6);
        if(t>8.6) a*=1-ease((t-8.6)/0.5);
        el.style.opacity=a; el.style.transform=`translateY(${{(1-a)*40}}px)`;
      }});
      // "kadraj" çerçevesi 5. sn'de belirir (fotoğraf vizörü hissi)
      const f=document.getElementById('frame');
      const fa=ease((t-5.0)/0.5)*(1-ease((t-8.6)/0.5));
      f.style.opacity=fa; f.style.transform=`scale(${{1.06-0.06*fa}})`;
      document.getElementById('end').style.opacity=ease((t-8.9)/0.7);
    }};
    setT(0);
    </script>"""
    return doc(body, 1080, 1920, extra)

def render():
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        for name, html in yemekhane() + yilbasi() + saha():
            f = GEN / "_tmp.html"; f.write_text(html)
            pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(150)
            # taşma kontrolü: içerik altbilginin üstünde bitmeli
            r = pg.evaluate("""(()=>{const foot=document.querySelector('.foot').getBoundingClientRect().top;
              const els=[...document.querySelectorAll('.page > *:not(.foot)')];
              return [document.body.scrollHeight, Math.round(Math.max(...els.map(e=>e.getBoundingClientRect().bottom))), Math.round(foot)]})()""")
            flag = "TAŞMA!" if r[1] > r[2] - 20 or r[0] > 1350 else "ok"
            print(name, r, flag)
            pg.screenshot(path=str(ROOT / name))
        pg2 = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        f = GEN / "_tmp.html"; f.write_text(reel_html())
        pg2.goto(f.as_uri()); pg2.evaluate("document.fonts.ready"); pg2.wait_for_timeout(200)
        fr = GEN / "_frames"; shutil.rmtree(fr, ignore_errors=True); fr.mkdir()
        fps = 30
        for i in range(int(REEL_T * fps)):
            pg2.evaluate(f"setT({i/fps})")
            pg2.screenshot(path=str(fr / f"{i:04d}.png"))
        pg2.evaluate("setT(7.5)"); pg2.screenshot(path=str(ROOT / "Sukra_v2_29_Kadraj_Kapak.png"))
        b.close()
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", "30", "-i", str(fr / "%04d.png"),
                    "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-crf", "20",
                    str(ROOT / "reels" / "Sukra_Reels_Kadraj.mp4")], check=True)
    shutil.rmtree(fr); (GEN / "_tmp.html").unlink()

if __name__ == "__main__":
    render()
