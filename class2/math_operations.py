import math
import random

print(math.ceil(32.05)) # 33 yazdirir ceil fonksiyonu
#bir ust tam sayiya yuvarlar
#32.01 olsa bile 33 olur sadece 32 yi 32 yazdirir

#ayni sekilde bi altina donusturen fonksiyon da math.floor() fonksiyonu sayilarin bi altina donusturur
#math.floor(25.42) -> 25 / -12.45 -> -13 vs gibi
#-------------------------------
#copysign
import math

sonuc = math.copysign(3.5, -2)  # 3.5'in işaretini -2'nin işaretiyle değiştirir
print(sonuc)  # Çıktı: -3.5

sonuc = math.copysign(-3.5, 2)  # -3.5'in işaretini 2'nin işaretiyle değiştirir
print(sonuc)  # Çıktı: 3.5
#----------------------------------
#math.fabs mutlak degerini alir sayi1=-4.5 mutlak_deger =math.fabs(sayi1) print(mutlak_deger) = 4.5 degerini yazdirir

#math.factorial verdigimiz degerin faktoriyelini alir

import math

sonuc1 = math.fmod(9, 4)
print(sonuc1)  # Çıktı: 1.0 (çünkü 9 / 4 işlemi 2 kalanı 1 bırakır)

sonuc2 = math.fmod(-9, 4)
print(sonuc2)  # Çıktı: -1.0 (işaret -9'un işaretiyle aynı kalır)

sonuc3 = math.fmod(9.5, 4.2)
print(sonuc3)  # Çıktı: 1.1 (ondalıklı sayılarla işlem yapar)
#----------------------------------
#math.gcd
import math

sayi1 = 36
sayi2 = 60
ebob = math.gcd(sayi1, sayi2)
print(ebob)  # Çıktı: 12 (çünkü 36 ve 60'ın en büyük ortak böleni 12'dir)
#-------------------------------------
#math.trunc ise sayinin ondalikli kismini atar sonuc kisminda 15.6 ise 15 yani floattan inte donusur

#math.exp ise e kuvvetinin (e saiyisinin) kuvvetlerini almaya yarar
#log 
import math

print(math.log(10))        # Doğal logaritma (taban e)
print(math.log(100, 10))   # Taban 10'da logaritma, sonuç 2.0
#ayni sekilde log2 log10 lu fonksiyonlar da ayni islevi gorur
#------------------------------------
#math.sqrt karekok hesaplama fonksiyonu
#math.sinh() sinus degerini hesaplar girdigimzi derecenin math.cos() da ayni skeilde cosinusu
#------------------------------------
#print(random.random()) 0 ile 1 arasinda random float uretmemize yarar
#farkli bi aralikta sayi uretmek istiyosak uniform() fonksiyonu
print(random.uniform(0.5,1.5))
#random tam sayi istersek randint(a,b) fonksiyonunu kullanmamiz lazim
import random

# randint ile 1 ile 10 arasında bir sayı (1 ve 10 dahil)
sayi1 = random.randint(1, 10)

# randrange ile 1 ile 10 arasında bir sayı (10 dahil değil)
sayi2 = random.randrange(1, 10)

print("randint ile:", sayi1)
print("randrange ile:", sayi2)

#------------------------------------
#choice fonksiyonu dizi,liste siralanabilir veri yapilarindan rastgele bi deger cekmek icin kullanilir
#import random

liste = [1, 2, 3, 4, 5]
secim = random.choice(liste)
print(secim)
#listeden birden fazla oge sececeksek sample kullaniriz

liste = [1, 2, 3, 4, 5]
secimler = random.sample(liste, 3)
print(secimler)  # Listeden 3 farklı rastgele öğe

#------------------------------------
#shuffle fonksiyonu ise siralanabilir bi dize liste vs veri yapisini karistirmak icin kullanilir
#import os

# Belirli bir dizindeki dosya ve klasörleri listele
#dizin = "/path/to/directory"
#icerik = os.listdir(dizin)

#print(icerik)
#------------------------------------



