# Python101

🌍 **Languages:** [English](#welcome) | [Türkçe](./README.md)

---

### Hoş Geldiniz

**Python101** reposuna hoş geldiniz!  
Bu repo, üniversitede verilen Python101 dersi için hazırlanmıştır. Ders boyunca kullanılan notlar, örnekler ve küçük otomasyon araçları tek bir yerde toplanmıştır. Dersleri takip ederken, konuları tekrar ederken veya ek örnekleri incelerken bu repo size yardımcı olacaktır.

### Ders Hakkında

**Python101**, Python programlamaya giriş niteliğinde bir derstir.  

Dersin amacı yalnızca Python sözdizimini öğretmek değil; aynı zamanda problem çözme becerisi, programlama bakış açısı ve programlama dilinden bağımsız yazılım geliştirme yetkinliği kazandırmaktır.

### Klasör Açıklamaları

- [**assets/**](./assets)
  Dokümantasyon ve ders materyallerinde kullanılan görseller.

- [**resources/**](./resources)
  Dersler için hazırlanan kaynaklar.  
  Bu klasör şunları içerir:
  - Ham Markdown ders notları  
  - Derlenmiş PDF dosyaları  
  - Sunum dosyaları (PPTX)

- [**src/**](./src)
  Derste kullanılan otomasyon araçları, örnek programlar ve projeler.
  
  - [**Pytracker/**](./src/Pytracker)
    Ders kapsamında geliştirilen, öğrenci yoklama kayıtlarını tutan web tabanlı bir uygulamadır.  
    Uygulama **Python**, **HTML** ve **CSS** kullanılarak yazılmıştır ve arka uç mantığı ile basit ön yüz bileşenlerinin birlikte nasıl çalıştığını göstermektedir.
    - `app.py`: Yönlendirme ve uygulama mantığını içeren ana dosya  
    - `config.py`: Uygulama yapılandırma ayarları  
    - `requirements.txt`: Gerekli Python kütüphaneleri  
    - `data/`: Öğrenci yoklama kayıtları ve veri dosyaları  
    - `scripts/`: Yardımcı ve çalıştırma betikleri  
    - `static/` & `templates/`: Web arayüzü için kullanılan ön yüz dosyaları ve HTML şablonları  

### Repo Nasıl Kullanılır?

- Öğrenciler dersleri `resources/` klasöründen takip edebilir  
- Kod örnekleri ve projeler `src/` altında incelenebilir ve çalıştırılabilir  
- Ders ilerledikçe repo güncellenecektir

İyi çalışmalar!

---

### Welcome

Welcome to the **Python101** repository!  
This repository is designed to support the Python101 course taught at the university level. It serves as a central place for lecture materials, examples, and small automation tools used throughout the course. Whether you are reviewing concepts, following along with lectures, or exploring additional examples, this repo is here to help you build a strong foundation in Python.

### About the Course

**Python101** is an introductory programming course focused on teaching the fundamentals of Python.

The goal of the course is not only to teach Python syntax, but also to develop problem-solving skills, a programming mindset, and language-independent programming skills that can be applied to future courses and projects.

### Directory Descriptions

- [**assets/**](./assets)
  Contains images and visual assets used in documentation and course materials.

- [**resources/**](./resources)
  Lecture resources for the course.  
  This directory includes:
  - Raw Markdown lecture notes  
  - Compiled PDF files  
  - Presentation files (PPTX)

- [**src/**](./src)
  Contains automation tools, example programs, and course-related projects.
  
  - [**Pytracker/**](./src/Pytracker)  
    A web-based student attendance tracking application developed as a practical course project.  
    It is written using **Python**, **HTML**, and **CSS**, and demonstrates how backend logic and simple frontend components work together.
    - `app.py`: Main application file handling routing and logic  
    - `config.py`: Application configuration settings  
    - `requirements.txt`: Python dependencies  
    - `data/`: Student attendance records and datasets  
    - `scripts/`: Helper and run scripts  
    - `static/` & `templates/`: Frontend assets and HTML templates for the web interface

### How to Use This Repository

- Students can follow lectures using the files in `resources/`  
- Code examples and projects can be explored and run from `src/`  
- The repository will grow as the course progresses

Happy coding!
