# Exception
# ValueError
# TypeError
# ZeroDivisionError
# IndexError
# FileNotFoundError
# KeyError

try:
    dosya=open("dosya.txt","r")
    veri = dosya.read()
    sayi=int(veri)
    
except (ValueError,FileNotFoundError) as e:
    print("Hata olustu ", str(e))
    #normalde kodu durdururdu fakat boyle kodu durdurmasin hata olustu mesaji versin devam etsin amacimiz
    
#Raising exceptions (istisnalarin ayiklanmasi)

def bolme(a,b):
    if b == 0:
        raise ValueError("Sifira bolunme hatasi")
    return a/b

try:
    sonuc = bolme(10,0)
    
except ValueError as e:
    print("Hata olustu.",str(e))
#--------------------------------------
def asal_mi(sayi):
    if sayi<2:
        return False
    for i in range(2,int(sayi**0.5)+1):
        if sayi % i == 0:
            return False
    return True

def asal_sayilari_bul(baslangic,bitis):
    asal_sayilar = []
    for sayi in range(baslangic,bitis +1):
        if asal_mi(sayi):
            asal_sayilar.append(sayi)
            
        return asal_sayilar

while True:
    try:
        baslangic = int(input("Lutfen baslangic deferini giriniz"))
        bitis= int(input("Lutfen bitis deferini giriniz"))
        
        if baslangic >= 0 and bitis >= baslangic:
            asal_liste = asal_sayilari_bul(baslangic,bitis)
            print("asal sayilar :",asal_liste)
            break
        
        else:
            print("Hatali giris. Baslngic degeri sifirdan buyuk olmali ve bitis degeri baslangic degerinden buyuk olmali")
            
    except ValueError:
        print("Hatali giris. Lutfen sayisal degerler girin")
#--------------------------------------
def not_hesapla():
    
    while True:
        
        try:
            
            vize1 = float(input("Lutfen birinci vize notunuzu giriniz"))
            vize2 = float(input("Lutfen ikinci vize notunuzu giriniz "))
            final1 = float(input("Lutfen final notunuzu giriniz "))
            if (0<=vize1<=100) and (0<=vize2<=100) and (0<=final1<=100):
                ortalama = vize1 *0.3 + vize2 *0.3 + final1 *0.4
                
                if ortalama>=90:
                    return "AA"
                elif ortalama >= 80:
                    return "BA"
                elif ortalama >=70:
                    return "BB"
                elif ortalama >=60:
                    return "CB"
                elif ortalama >=50:
                    return "CC"
                elif ortalama >=40:
                    return "DC"
                else:
                    return "Kaldiniz."
                
            else:
                print("Hatali veri girisi , notlariniz 0 100 araliginda olmalidir")
            
        except ValueError:
            print("Hatali giris lutfen sayisal deger giriniz")
            
print(f"Sinav sonucu : {not_hesapla()}")

#-------------------------------------------------------
def oyuncu_bilgisi():
    oyuncu_listesi = []
    
    while True:
        
        try:
            
            ad=input("Oyuncu adini girin : ")
            soyad=input("Oyuncu soyadini girin :")
            yas=int(input("oyuncu yasini giriniz"))
            takim= input("oyuncu takimini giriniz :")
            yeni_oyuncu = {"Ad" : ad, "Soyad " : soyad, "Yas" : yas, "Takim" :takim}
            oyuncu_listesi.append(yeni_oyuncu)
            
        except ValueError:
            print("Lutfen yas degerini sayisal bir formatta giriniz.")
            
        except Exception as e:
            print("Hata olustu",str(e))
            
            
        finally:
            while True:
                devam = input("Yeni oyuncu eklemek istiyor musunuz ? (E/H) :")
                
                if devam.lower() == "e":
                    break
                elif devam.lower() == "h":
                    return oyuncu_listesi
                else:
                    print("Lutfen E veya H degeri giriniz")
                    
oyuncular = oyuncu_bilgisi()
print("Oyuncu bilgileri : ")
print("-"*10)
for oyuncu in oyuncular:
    print(oyuncu)
                    
#---------------------------------------------------
def kira_hesapla(gun_sayisi,araba_turu):
    if araba_turu == "ekonomik" :
        kira_bedeli = gun_sayisi *100
    elif araba_turu== "orta":
        kira_bedeli == gun_sayisi*150
    elif araba_turu == "luks":
        kira_bedeli == gun_sayisi *200
    else:
        raise ValueError("Gecersiz araba turu!, ekonomik orta veya luks degerlerinden birini girin")
    
    return kira_bedeli

while True:
    try:
        gun_sayisi = int(input("Lutfen araci kac gunluk kiralamak istediginizi giriniz"))
        araba_turu = input("Lutfen araba turunu seciniz(ekonomik/orta/luks)").lower()
        kira_bedeli = kira_hesapla(gun_sayisi,araba_turu)
        print(f"Toplam kira bedeli : {kira_bedeli} TL ")
        break
    except ValueError as e:
        print("Hata olustu",str(e))
    #----------------------------------
                        


