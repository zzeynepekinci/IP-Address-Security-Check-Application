# IP-Address-Security-Check-Application

## Proje Açıklaması  
Bu uygulama, IP adreslerini güvenlik açısından kontrol etmek için geliştirilmiştir. Uygulama, IP adreslerinin şüpheli aktiviteler içerip içermediğini tespit eder ve kullanıcıya güvenli veya tehlikeli olup olmadığı hakkında bilgi verir. IP adreslerinin kara listeye alınıp alınmadığını kontrol etmek için bir API kullanarak tehdit analizi yapar.

## Özellikler  
- IP adreslerinin güvenliğini kontrol etme  
- IP adreslerinin şüpheli aktiviteler içerip içermediğini belirleme  
- Kötü amaçlı IP'ler hakkında bilgi edinme  
- Kullanıcı dostu bir arayüz ile güvenlik değerlendirmesi sağlama  

## Kullanılan Teknolojiler  
- **Python** – Uygulamanın temel programlama dili  
- **Flask** – Web framework  
- **Requests** – HTTP isteklerini yapmak için kullanıldı  
- **AbuseIPDB API** – IP güvenlik verilerini almak için kullanıldı  
- **HTML/CSS** – Basit bir kullanıcı arayüzü için kullanıldı  

## Kurulum  

Öncelikle, **Python 3.x** sürümünün sisteminizde yüklü olduğundan emin olun. Ardından aşağıdaki adımları takip edin:

1. Repository’yi klonlayın:  
   ```bash
   git clone https://github.com/username/repository-name.git
   ```

2. Gerekli bağımlılıkları yükleyin:  
   ```bash
   pip install -r requirements.txt
   ```

3. Flask uygulamasını başlatın:  
   ```bash
   python app.py
   ```

4. Tarayıcınızda aşağıdaki adrese giderek uygulamayı çalıştırabilirsiniz:  
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Kullanım  
Uygulama çalıştırıldığında, ana sayfada bir IP adresi girmeniz için bir alan görünecektir. Girdiğiniz IP adresinin güvenli olup olmadığı hakkında anında geri bildirim alırsınız. Eğer IP adresi kötü amaçlı aktiviteler içeriyorsa, uygulama size uyarı verecektir.  

