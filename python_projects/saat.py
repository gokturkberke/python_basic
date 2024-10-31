from tkinter import *  # tkinter modülündeki tüm sınıfları ve fonksiyonları içe aktarır
import time  # Saat ve zaman işlemleri için time modülünü içe aktarır

# Pencere oluşturma
pencere = Tk()  # tkinter'de ana pencere oluşturmak için Tk() sınıfını kullanıyoruz
pencere.title("Saatim")  # Pencere başlığını "Saatim" olarak ayarlıyoruz

# Saat etiketi (Label) oluşturma
zaman1 = ''  # Bir önceki zamanı saklamak için boş bir değişken tanımlıyoruz
tiktak = Label(pencere, font=('times', 100, "bold"), bg='yellow')  # Saat gösterecek etiketi ayarlıyoruz
# Label ayarları:
# - font: 'times' yazı tipi, 100 boyutu ve kalın (bold)
# - bg: arka plan rengi sarı (yellow)

tiktak.grid()  # Label öğesini pencereye yerleştiriyoruz

# Saat fonksiyonunu tanımlama
def saat():
    global zaman1  # zaman1 değişkenini global olarak tanımlıyoruz, böylece fonksiyon dışında da erişilebilir

    zaman2 = time.strftime('%H:%M:%S')  # Şu anki saati 'HH:MM:SS' formatında alıyoruz
    
    if zaman1 != zaman2:  # Eğer zaman1 bir önceki zamandan farklıysa
        zaman1 = zaman2  # zaman1'i güncel saat ile güncelliyoruz
        tiktak.config(text=zaman2)  # Label'ın (tiktak) metin ayarını güncel saati gösterecek şekilde değiştiriyoruz

    tiktak.after(50, saat)  # 50 milisaniye sonra 'saat' fonksiyonunu tekrar çağırıyoruz
    
# Saat fonksiyonunu başlatma
saat()  # İlk kez çalıştırıyoruz

# Pencere döngüsü
pencere.mainloop()  # Pencerenin sürekli açık kalması için ana döngüyü başlatıyoruz
