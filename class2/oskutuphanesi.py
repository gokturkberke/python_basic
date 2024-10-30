import os #dizin ve dosya islemleri icin kullanilir

# Geçerli çalışma dizinini tam yol olarak döndürür
print(os.getcwd())  # Örnek çıktı: "/Users/gokturkberkekorkut/python_projects"

# curdir sabiti '.' döndürür
print(os.curdir)  # Çıktı: .
#------------------------------
# 1. Geçerli Çalışma Dizinini Al
current_directory = os.getcwd()
print("Geçerli çalışma dizini:", current_directory)

# 2. Çalışma Dizinini Değiştir
# Yeni bir dizine geçiş yapmak için aşağıdaki gibi kullanılabilir
# os.chdir("/path/to/new/directory")
# print("Yeni çalışma dizini:", os.getcwd())

# 3. Bir Dizindeki Dosyaları ve Klasörleri Listele
# Burada geçerli dizini listeledik
contents = os.listdir(current_directory)
print("Geçerli dizindeki dosya ve klasörler:", contents)

# 4. Yeni Bir Klasör Oluştur
# Yeni bir klasör oluşturmak için örnek
# os.mkdir("yeni_klasor")
# print("yeni_klasor klasörü oluşturuldu.")

# 5. Dosya Silme
# Belirli bir dosyayı silmek için kullanılır (dikkatli olun!)
# os.remove("dosya_ismi.txt")
# print("dosya_ismi.txt silindi.")

# 6. Klasör Silme (boş olmalı)
# os.rmdir("yeni_klasor")
# print("yeni_klasor klasörü silindi.")

# 7. Çevresel Değişkenleri Listeleme
environment_vars = os.environ
print("Çevresel değişkenler:", environment_vars)

# 8. Belirli Bir Çevresel Değişkeni Alma
path_var = os.getenv("PATH")
print("PATH çevresel değişkeni:", path_var)

# 9. Çevresel Değişken Ayarlama
# os.putenv("YENI_VAR", "deger")
# print("YENI_VAR çevresel değişkeni ayarlandı.")

# 10. Dosya ve Klasör Yolunu Birleştirme
full_path = os.path.join(current_directory, "yeni_klasor", "dosya.txt")
print("Birleştirilmiş yol:", full_path)

# 11. Yolun Varlığını Kontrol Etme
path_exists = os.path.exists(full_path)
print(f"{full_path} var mı?", path_exists)

# 12. Yolun Bir Dosya Olup Olmadığını Kontrol Etme
is_file = os.path.isfile(full_path)
print(f"{full_path} bir dosya mı?", is_file)

# 13. Yolun Bir Dizin Olup Olmadığını Kontrol Etme
is_dir = os.path.isdir(current_directory)
print(f"{current_directory} bir dizin mi?", is_dir)

# 14. İşletim Sisteminin Türünü Öğrenme
os_type = os.name
print("İşletim sistemi türü:", os_type)

# 15. Sistem Komutu Çalıştırma
# Örneğin, 'ls' komutunu çalıştırır (Linux/macOS) veya 'dir' (Windows)
# os.system("ls")  # veya Windows için os.system("dir")

# 16. Dosya veya Klasör Yeniden Adlandırma
# os.rename("eski_dosya_adi.txt", "yeni_dosya_adi.txt")
# print("Dosya yeniden adlandırıldı.")
#------------------------------
