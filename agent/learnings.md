# Öğrenilenler (learnings.md)

Her geri bildirim ve her haftalık değerlendirmeden sonra buraya bir satır eklenir. Yeni içerik üretmeden önce okunur.

## Aykan'ın geri bildirimleri
- Rakip firmalarla ilgili içerik yok; takip listesi de rakip değil restoran/kafe (ör. Kushimoto, Siestita tarzı).
- "Sıcakta dimdik" sloganı anlamsız bulundu, kullanılmaz.
- Videolar çorba üzerinden kurgulanmaz, genel tutulur.
- Hikayelerde üstte kırmızılık olmaz.
- İçerik prestij odaklı: ürün işletmeye prestij katar.
- İstenmeden profil/hesap keşfi için tarayıcıda gezinilmez.
- Yayınlama ve programlama yalnızca Aykan açıkça istediğinde yapılır.

## Performans bulguları
- (Henüz yok. İlk haftalık değerlendirmeden sonra doldurulacak; 6 gönderiden az veriyle kural çıkarılmaz.)

## Teknik akış
- Tasarım: Python ile HTML → Playwright ile PNG (1080×1350 / 1080×1920)
- Depo: github.com/aykmayk7/sukrapack-instagram (commit sabitli raw URL)
- Yayın/programlama: Meta Business Suite (Metricool ücretsiz limiti doldu)
- Profil linki: Business Suite > Edit Instagram profile > Links (web'den değişmiyor)
- Business Suite hikayeye anket çıkartması ekleyemiyor; anket gereken hikayede ya Aykan telefondan ekler ya da DM ile oylama (A/B/C) kullanılır.
- Kapanış karelerinde "sukra" yazısının S harfi yerine logo (iki yeşil yaprak + altın kamış çubuğu) kullanılır. Canva'da vektör: viewBox 120; yaprak1 "M90 18 C70 12 40 20 30 50 C52 50 78 40 90 18 Z", yaprak2 "M30 102 C50 108 80 100 90 70 C68 70 42 80 30 102 Z", çubuk "M36.79 51.56 L84.79 58.56 A5.5 5.5 0 0 1 83.21 69.44 L35.21 62.44 A5.5 5.5 0 0 1 36.79 51.56 Z". Koyu zeminde yaprak #6FBF8A, çubuk #E3B877.
- Aykan şimdilik Canva kullanılmasını istemiyor (1 Kas 2026). Tasarım ve video kendi hattımızla (HTML→Playwright→ffmpeg) üretilir.
- Reels müziği: Business Suite Reels composer > Edit > Audio kütüphanesinden eklenir (telif kontrolü otomatik). Prestij tonu için lounge/lüks enstrümantal seç.
- (Canva kullanılırsa) ürün görselleri stok/AI değil, sukragroup.com/img/urunler/ altındaki gerçek ürün fotoğraflarıdır.
- "sukra" yazısında S yerine logo kullanılırken logonun boş payı kırpılır (viewBox "28 12 64 98"); S ile "u" arası, harfler arası mesafeyle aynı olmalı. Hazır fonksiyon: gen/ig8.py wordmark(). (Aykan geri bildirimi, 5 Kas)
