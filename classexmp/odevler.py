#2 sayi tanimla Kullanıcının girdiği iki birbirine eşit ise ekrana “5” sonucu yazdıracak, eşit değil ise 25 defa “eşit değil” sonucunu ekrana yazdıran python kodlarını yazınız? (while döngüsü ile yapılacaktır)
a=int(input("birinci sayiyi giriniz"))
b=int(input("ikinci sayiyi giriniz"))

if a == b:
    print(5)
else:
    i = 0
    while i < 25:
        print("eşit değil")
        i += 1
#-------------------------------
#Kullanıcın girdiği 5 basamaklı bir sayının, basamaklarının toplamını ekrana yazdıran python kodlarını yazınız
sayi = input("5 basamaklı bir sayı girin: ")

if len(sayi) == 5 and sayi.isdigit():
    toplam = sum(int(basamak) for basamak in sayi)
    print("Basamakların toplamı:", toplam)
else:
    print("Lütfen 5 basamaklı bir sayı girin.")
    #------------------------------------
#Klavyeden kullanıcının girdiği 3 adet integer türünde ki sayıyı büyükten küçüğe sıralayarak ortadaki sayı ile olan sayının arasındaki farkı ve yine ortadaki sayı ile küçük olan sayı ile arasındaki farkı ekrana yazdıran python kodlarını yazınız.
sayi1=int(input("Birinci sayiyi girin"))
sayi2=int(input("Ikinci sayiyi girin"))
sayi3=int(input("Ucuncu sayiyi girin"))

sayilar = [sayi1,sayi2,sayi3]
sayilar.sort(reverse=True) #buyukten kucuge siraladik

buyuk=sayilar[0]
kucuk=sayilar[2]
orta=sayilar[1]

fark_buyuk = buyuk-orta
fark_kucuk = orta-kucuk

print(f"Buyuk sayi ile ortadaki sayi arasindaki fark {fark_buyuk}")
print(f"Ortadaki sayi ile kucuk sayi arasindaki fark {fark_kucuk}")
#-------------------------------------------------------------------
#Rastgele 600 adet 0 ile 1000 arasında sayı oluşturup bir liste içerisine aktaran ve 100’den küçük olan sayıların adedini ekrana yazdıran python kodlarını yazınız.
import random
sayilar=[]

for i in range(600):
    rastgele_sayi=random.randint(0,1000)
    
    sayilar.append(rastgele_sayi)

kucuk_sayilar_adedi=0
for sayi in sayilar:
    if sayi <100:
        kucuk_sayilar_adedi +=1

print("100den kucuk olan sayi adedi : " ,kucuk_sayilar_adedi)
#---------------------------------------------
sayi1=int(input("Birinci sayiyi girin"))
sayi2=int(input("Ikinci sayiyi girin"))

if sayi1 + sayi2 > 40 and sayi1+sayi2 <50:
    print("Python")
else:
    print("Girdiginiz iki sayinin toplami istenilen aralikta degildir")
#-----------------------------------
sayi=int(input("Lutfen 4 basamakli bir sayi girin"))

rakamlar=[]
toplam=0

if len(sayi) == 4:
    for i in sayi:
        rakamlar.append(i)
        toplam = toplam + i
        print("Rakamlar :" ,rakamlar)
        print("Rakamlarin toplami :", toplam)
else:
    print("Lutfen 4 basamakli bir sayi girin")