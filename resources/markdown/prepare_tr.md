# Python101 Kursuna Hoş Geldiniz

Aramıza katıldığınız için çok mutluyuz. Bu kurs, Python programlama konusunda size **güçlü ve pratik bir temel** kazandırmak için tasarlanmıştır. Bu kursta endüstri ve araştırmalarda yaygın olarak kullanılan gerçek dünya geliştirme yaklaşımlarına ve araçlarına odaklanacağız.

---

## Bu Dosyayı Neden Alıyorsunuz?

Ders süresinin sınırlı olması nedeniyle, **ilk dersten önce** bu dokümanı sizinle paylaşıyoruz. Böylece çalışma ortamınızı önceden hazırlayabilirsiniz.  
Her şeyin önceden hazır olması, ders sırasında teknik kurulumlarla zaman kaybetmek yerine Python kavramlarını öğrenmeye ve birlikte kod yazmaya odaklanmamızı sağlar.

---

## Python Yorumlayıcısı (Zorunlu)

Python programlarını çalıştırmak için bir **Python Yorumlayıcısına (Interpreter)** ihtiyacınız vardır.

* [**Python nasıl kurulur (Windows)**](https://youtu.be/gmDB2iZMwAQ?si=-Umq19pa2BLthfMm)
* [**Python 3.14 indir (Windows)**](https://www.python.org/downloads/windows/)

* [**Python nasıl kurulur (MacOS)**](https://www.youtube.com/watch?time_continue=96&v=jDTgmMlDSKg)
* [**Python 3.14 indir (MacOS)**](https://www.python.org/downloads/macos/)

---

## JetBrains Öğrenci Hesabı (Önerilir)

Bir **JetBrains Öğrenci Hesabı** oluşturmanız önerilir (öğrenciler için ücretsizdir).

**Neden?**  
JetBrains araçları (PyCharm Professional dahil) şunları sağlar:

* Güçlü kod tamamlama ve yeniden düzenleme (refactoring)
* Gelişmiş hata ayıklama (debugging) araçları
* Test, Git ve sanal ortamlar için entegre destek

Hesap oluşturmak **zorunlu değildir**, ancak bu kurs boyunca geliştirme deneyiminizi önemli ölçüde iyileştirir.

[**JetBrains hesabı oluştur**](https://sales.jetbrains.com/hc/en-gb/articles/207737419-Create-a-JetBrains-Account)

---

## IDE Kurulumu: PyCharm (Önerilir)

Bu kurs için ana IDE olarak **PyCharm Professional Edition** kullanılacaktır.

* Kurs materyalleri, canlı anlatımlar ve iş akışları **yoğun olarak PyCharm ve JetBrains araçlarına dayalıdır**
* Adım adım kurulum talimatları sizinle paylaşılacaktır
* Lütfen ilk dersten önce PyCharm’ın yüklü olduğundan ve sorunsuz çalıştığından emin olun

> İsterseniz VS Code gibi başka bir IDE kullanabilirsiniz, ancak şunu unutmayın:
> * Ders sırasında verilen destek PyCharm odaklı olacaktır
> * Bazı özellikler ve iş akışları farklılık gösterebilir

[**Pycharm Kurulumu (Windows)**](https://youtu.be/Tmu_fkFwIvw?si=wE1-GmXCP9jiowxy)  
[**Pycharm Kurulumu (MacOS)**](https://youtu.be/ZVjQFjOI49c?si=HfekgYiJn-ZBDYh4)  
[**Pycharm İndir**](https://www.jetbrains.com/help/pycharm/installation-guide.html)

---

## GitHub Hesabı (Zorunlu)

Aşağıdaki nedenlerle bir **GitHub hesabına** ihtiyacınız vardır:

* Kurs materyallerine erişmek
* Örnek kodları ve ödevleri indirmek
* Çalışmalarınızı paylaşmak ve (gerektiğinde) teslim etmek

Lütfen ilk dersten önce GitHub hesabınıza başarıyla giriş yapabildiğinizden emin olun.

[**GitHub Hesabı Oluştur**](https://github.com/signup)

---

## İlk Dersten Önce

Aşağıdaki bölümü mutlaka okuyunuz:

* Python programlama diline giriş
* Programlama ve programlama dillerinin açıklaması
* Farklı programlama dilleri
* Python programlama dilinin özellikleri ve sınırlamaları

---

![Python Kaynak Kodu](../../assets/1.jpg "Kod")

### 1. Programlama Nedir?

Programlama, bir bilgisayara belirli görevleri yerine getirmesi için talimatlar verme sürecidir. Bu talimatlar, bir problemi çözmek için mantıklı ve adım adım bir şekilde yazılır. Programlama, insanların bilgisayarlarla etkili bir şekilde iletişim kurmasını sağlar. Bir problemi analiz etmeyi, bir çözüm tasarlamayı ve ardından bunu kod kullanarak uygulamayı içerir. Bilgisayarlar programlar olmadan kendi başlarına çalışamaz. Programlama; yazılımlar, web siteleri, mobil uygulamalar ve oyunlar oluşturmak için kullanılır. Ayrıca bilim, eğitim, sağlık ve iş dünyasında önemli bir rol oynar. Programlama, mantıksal düşünme ve yaratıcılık gerektirir. Programlama öğrenmek, problem çözme ve analitik düşünme becerilerini geliştirir.

---

### 2. Programlama Dili Nedir?

Programlama dili, bilgisayara talimat yazmak için kullanılan resmi bir dildir. İnsanların bilgisayarlarla, bilgisayarların anlayabileceği bir şekilde iletişim kurmasını sağlar.

---

### 3. Derlenen (Compiled) Dil Nedir?

Derlenen bir dil, tüm programın çalıştırılmadan önce makine koduna çevrildiği bir programlama dilidir. Bu çeviri işlemi bir derleyici (compiler) tarafından yapılır.

---

### 4. Yorumlanan (Interpreted) Dil Nedir?

Yorumlanan bir dil, satır satır çalıştırılan bir programlama dilidir. Kod, çalıştırma sırasında bir yorumlayıcı (interpreter) tarafından çevrilir ve çalıştırılır. Program önceden makine koduna dönüştürülmez. Yorumlanan diller genellikle derlenen dillere göre daha yavaştır.

---

![Derlenen Dil vs. Yorumlanan Dil](../../assets/2.jpg "Karşılaştırma Görseli")

### 5. Derlenen ve Yorumlanan Diller Arasındaki Fark

| Özellik                            | Derlenen Dil                         | Yorumlanan Dil                                  |
|------------------------------------|--------------------------------------|-------------------------------------------------|
| **Çeviri yöntemi**                 | Tüm program bir defada çevrilir      | Program satır satır çevrilir                    |
| **Çalışma hızı**                   | Daha hızlı                           | Daha yavaş                                      |
| **Hata tespiti**                   | Derleme sonrası gösterilir           | Çalışma sırasında tek tek gösterilir            |
| **Çalışma anında kaynak kodu**     | Gerekli değil                        | Gereklidir                                      |
| **Taşınabilirlik**                 | Daha az (platforma bağlı)            | Daha fazla (platformdan bağımsız)               |
| **Bellek kullanımı**               | Çalışma anında genellikle daha az    | Çalışma anında genellikle daha fazla            |
| **Örnek diller**                   | C, C++, Go, Rust                     | Python, JavaScript, Ruby                        |
| **Çıktı**                          | Çalıştırılabilir dosya üretir        | Ayrı bir çalıştırılabilir dosya üretmez         |

---

### 6. Python Nedir?

Python, üst seviye (high-level), yorumlanan bir programlama dilidir. Okunması ve yazılması kolay olacak şekilde tasarlanmıştır, bu da onu yeni başlayanlar için ideal hale getirir. Prosedürel, nesne yönelimli ve fonksiyonel programlama dahil olmak üzere birden fazla programlama yaklaşımını destekler. Python; web geliştirme, veri bilimi, yapay zeka ve otomasyon alanlarında yaygın olarak kullanılır. Çok geniş bir standart kütüphaneye sahiptir ve birçok yerleşik fonksiyon sunar. Python, günümüzde en popüler programlama dillerinden biridir.

---

### 7. Python’un Avantajları ve Sınırlamaları

| **Python’un Avantajları**                | **Python’un Sınırlamaları**               |
|------------------------------------------|-------------------------------------------|
| Öğrenmesi ve okuması kolay               | Daha yavaş çalışma hızı                   |
| Basit ve temiz sözdizimi                 | Daha fazla bellek kullanımı               |
| Geniş standart kütüphane                 | Mobil uygulamalar için ideal değil        |
| Çoklu paradigmaları destekler (OOP, vb.) | Düşük seviye programlama için zayıf       |
| Platformdan bağımsız                     | Çalışma zamanı hataları oluşabilir        |
| Büyük topluluk desteği                   | Sınırlı veritabanı performansı            |
| AI, ML ve veri bilimi için uygun         | Gerçek zamanlı sistemler için uygun değil |
| Hızlı geliştirme ve prototipleme         | Yüksek performanslı işler için yavaş      |
