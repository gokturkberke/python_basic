#mutlak deger -> abs
print(abs(-30)) #30 yazdirir

#round fonksiyonu(yuvarlama)
print(round(1.5)) #2

#all fonksiyonu -> verilen liste tuple veya kume de tum elemanlar true is true
#herhangi bir eleman false ise false doner
sayilar = [1, 2, 3, 4, 5]
sonuc = all(sayi > 0 for sayi in sayilar)
print(sonuc)  # Çıktı: True

#------------------------------
#any fonksiyonu da herhangi bir eleman true olsa dahi true degeri doner
sayilar = [-1, -2, 3, -4, -5]
sonuc = any(sayi > 0 for sayi in sayilar)
print(sonuc)  # Çıktı: True

degerler = [0, None, False, ""]
print(any(degerler))  # Çıktı: False
#----------------------------
#bool
#print(bool(0)),print(bool[]) bunlar false doner
#print(bool(1)),print(bool(-2)) bunlar true doner
#-----------------------------
#farkli tipteki verileri listeye donusturebiliyoruz
notlar = { "yusuf" : 50 , "ayse " : 40 , "berke" : 100}

print(list(notlar)) # yusuf ayse berke
print(list(notlar.values())) #50 40 100
#------------------------------
#callable o fonksiyonunu cagrilip cagrilamayacagini kontrol eder
#sinif fonksiyonlar vs cagrilabilirken 
#temel veri turleri callable degildir
sayi = 5
print(callable(sayi))  # Çıktı: False

metin = "Merhaba"
print(callable(metin)) # Çıktı: False
#-------------------------------
#eval fonksiyonu
liste = [1, 2, 3, 4, 5]
ifade = "liste[2] * 10"
sonuc = eval(ifade)
print(sonuc)  # Çıktı: 30
#-------------------------------
x = 10  # Global değişken

def fonksiyon():
    x = 5  # Yerel değişken
    print("Fonksiyon içindeki x:", x)

fonksiyon()
print("Global x:", x)

# Çıktı:
# Fonksiyon içindeki x: 5
# Global x: 10

x = 10  # Global değişken

def fonksiyon():
    global x  # x'in global olduğunu belirtir
    x = 5
    print("Fonksiyon içindeki x:", x)

fonksiyon()
print("Global x:", x)

# Çıktı:
# Fonksiyon içindeki x: 5
# Global x: 5
#-------------------------------
#divmod
a=15
b=7
sonuc = divmod(a,b) #bolumu ve kalani verir divmod 
print(sonuc)
#-------------------------------
#enumerate

numaralandirma = enumerate("berke")
print(list(numaralandirma)) #her indexi ve yanindaki harfi yazdirir
#-------------------------------
#format
isim = "Ahmet"
yas = 25
meslek = "Mühendis"

# Basit bir cümlede format kullanımı
metin = "Benim adım {}, yaşım {} ve mesleğim {}.".format(isim, yas, meslek)
print(metin)
# Çıktı: Benim adım Ahmet, yaşım 25 ve mesleğim Mühendis.
metin = "Benim adım {isim}, yaşım {yas} ve mesleğim {meslek}.".format(isim="Ayşe", yas=30, meslek="Doktor")
print(metin)
# Çıktı: Benim adım Ayşe, yaşım 30 ve mesleğim Doktor.
#-------------------------------
#filter kullanimi
kelimeler = ["elma", "armut", "çilek", "kavun", "karpuz", "muz"]
uzun_kelime = filter(lambda kelime: len(kelime) > 5, kelimeler)
print(list(uzun_kelime))
# Çıktı: ['karpuz']

sayilar = [1, 2, 3, 4, 5]
cift_sayilar = list(filter(lambda x: x % 2 == 0, sayilar))  # Listeye dönüştürme
print(cift_sayilar)
# Çıktı: [2, 4]
#-------------------------------
#map(islem_fonksiyonu, veri_kumesi)
sayilar = [1, 2, 3, 4, 5]
sonuc = map(lambda x: x * 2, sayilar)
print(list(sonuc))
# Çıktı: [2, 4, 6, 8, 10]

sayilar = [1, 2, 3, 4, 5]
sonuc = map(lambda x: x * 2, sayilar)
print(list(sonuc))
# Çıktı: [2, 4, 6, 8, 10]
#-------------------------------
#range
sayilar = list(range(5))
print(sayilar)
# Çıktı: [0, 1, 2, 3, 4]

for i in range(10, 0, -2):
    print(i)
# Çıktı:
# 10
# 8
# 6
# 4
# 2
#-------------------------------
#sorted
notlar = [("Ali", 85), ("Ayşe", 95), ("Mehmet", 75)]
sirali_notlar = sorted(notlar, key=lambda x: x[1])  # Notlara göre sıralama
print(sirali_notlar)
# Çıktı: [('Mehmet', 75), ('Ali', 85), ('Ayşe', 95)]

kelimeler = ["elma", "armut", "çilek", "kavun"]
sirali_kelimeler = sorted(kelimeler, key=len)
print(sirali_kelimeler)
# Çıktı: ['elma', 'armut', 'kavun', 'çilek']
#-------------------------------
#slice
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
s = slice(2, 7)  # 2. indeksten 7. indekse kadar
print(liste[s])
# Çıktı: [2, 3, 4, 5, 6]

metin = "Python Programlama"
s = slice(0, 6)  # İlk 6 karakter
print(metin[s])
# Çıktı: Python

liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
s = slice(-5, None)  # Son 5 eleman
print(liste[s])
# Çıktı: [5, 6, 7, 8, 9]
#-------------------------------
#zip iki farkli listeyi ayni indexleri esleme islemi yapar
liste1 = [1, 2, 3]
liste2 = ['a', 'b', 'c']

birlesik = zip(liste1, liste2)
print(list(birlesik))
# Çıktı: [(1, 'a'), (2, 'b'), (3, 'c')]
#-------------------------------

