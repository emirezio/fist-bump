# Fist-Bump

Fist-Bump, Huawei'nin el hareketleriyle dosya paylaşım özelliğinden ilham alınarak geliştirilmiş bir Python tabanlı uygulamadır. Bu projenin amacı, bir webcam veya video kaynağı üzerinden algılanan el hareketleri kullanılarak dosya paylaşımını mümkün kılmaktır. Son güncellemeler, gelişmiş dizin yönetimi, daha iyi bir modüler yapı ve dosya gönderme/alma işlemleri için daha sağlam bir çoklu iş parçacığı uygulamasını içermektedir. Bu projeyi daha da geliştirmek için katkılarınızı ve fikirlerinizi bekliyoruz.

---

## Özellikler

- **El Hareketi Algılama**: OpenCV ve MediaPipe kullanarak elin açık mı kapalı mı olduğunu algılar.
- **Dosya Paylaşımı**:
  - **Dosya Gönderimi**: Belirli bir hareket (kapalı yumruk) algılandığında otomatik olarak ekran görüntüsü alır ve gönderir.
  - **Dosya Alma**: Başka bir hareket (açık el) algılandığında gelen dosyaları dinler.
- **Dizin Yönetimi**: Ekran görüntülerini ve alınan dosyaları kaydetmek için otomatik olarak dizinler oluşturur.
- **Çoklu İş Parçacığı Tasarımı**: Dosya gönderme ve alma işlemleri verimlilik için ayrı iş parçacıklarında çalışır.
- **Loglama**: Uygulama davranışını ve hataları izlemek için yapılandırılabilir loglama sistemi.

---

## Gereksinimler

- Python 3.7+
- OpenCV
- PyAutoGUI
- MediaPipe

### Gereksinimlerin Kurulumu
Gerekli bağımlılıkları kurmak için şu komutu çalıştırın:
```bash
pip install -r requirements.txt
```

---

## Kullanım

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/emirezio/fist-bump.git
   cd fist-bump
   ```

2. Ana scripti çalıştırın:
   ```bash
   python main.py
   ```

3. Varsayılan olarak, script birincil web kameranızı kullanır. Farklı bir video kaynağı kullanmak için `FistBump` sınıfındaki `cam` parametresini değiştirebilirsiniz.

---

## Nasıl Çalışır?

- Program, `HandTracker` sınıfını kullanarak el işaretlerini algılar ve elin açık mı kapalı mı olduğunu belirler.
- Algılanan hareketlere göre:
  - **Kapalı yumruk**, ekran görüntüsü alır ve önceden belirlenmiş bir alıcıya gönderir.
  - **Açık el**, gelen dosyaları dinler.
- `NetworkHandler`, dosyaların yerel ağ üzerinden gönderilmesi ve alınmasını yönetir.
- Daha iyi modülerlik ve hata ayıklama için loglama ve dizin yönetimi `Config` sınıfı ile sağlanır.

---

## Zorluklar ve Gelecek Hedefler

Mevcut işlevsellik çalışıyor olsa da, bu projede geliştirilebilecek birçok alan var:

### Güvenlik
- **Şifreleme**: Şu anda dosya transferleri şifreleme içermiyor. Güvenli protokoller (ör. TLS veya dosya şifreleme) uygulanması kritik öneme sahiptir.
- **Kimlik Doğrulama**: Dosyaların yalnızca güvenilir taraflar arasında paylaşılmasını sağlamak için mekanizmalar eklenmeli.

### Güvenilirlik
- **Hata Yönetimi**: Ağ sorunları, dosya sistemi hataları vb. için hata yönetimini geliştirin.
- **Gelişmiş Hareket Algılama**: Yanlış pozitifleri azaltmak için doğruluk artırılmalı.

### Genişletilebilirlik
- **Yeni Özellikler**: Ek hareketler ekleyin veya sesli komutları içerecek şekilde işlevselliği genişletin.
- **Çapraz Platform Uyumluluğu**: Farklı işletim sistemleri ve donanım yapılandırmalarında sorunsuz çalışma sağlayın.

---

## Katkı Sağlama

Katkılarınızı memnuniyetle karşılıyoruz! İşte nasıl yardımcı olabilirsiniz:

1. Depoyu çatallayın (fork).
2. Özellik veya düzeltmeniz için bir dal oluşturun.
3. Değişikliklerinizi yapın ve çatallanmış depoya gönderin.
4. Detaylı bir açıklama ile bir çekme isteği (pull request) gönderin.

---

## İletişim

Herhangi bir sorunuz veya fikriniz varsa, bir sorun (issue) açmaktan veya doğrudan benimle iletişime geçmekten çekinmeyin. Fist-Bump'ı birlikte daha iyi hale getirelim!

---

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakın.

---

## Teşekkür

Açık kaynak topluluğuna ve bu projeye ilham veren herkese özel teşekkürler. Hareket algılama ve dosya paylaşımı teknolojilerine katkıda bulunan herkesin katkısı değerlidir!

