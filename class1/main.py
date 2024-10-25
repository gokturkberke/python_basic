# class calisan():
#     personel_listesi=[]   #self olmadigi icin kisiye ozgu degildir
#     def __init__(self):
#         self.unvani=''
#         self.bildigi_diller = []
#         self.isim=''
#         self.soyisim=''
#         self.yas=None

# ahmet = calisan()
# calisan.personel_listesi.append('ahmet')
# ahmet.unvani='Python gelistirici'
# ahmet.isim='ahmet'
# ahmet.soyisim='Can'
# ahmet.bildigi_diller.append('python')
# ahmet.yas=40

# berke=calisan()
# calisan.personel_listesi.append('berke')
# berke.isim='berke'
# berke.soyisim='korkut'
# berke.yas=21
# berke.bildigi_diller.append('Java')
# berke.unvani='Java Gelistirici'

# print(berke.bildigi_diller) #hem java hem python gelir burda
# #sinifa ozgu calisiyoruz burda aslinda kisiye ozgu degil

# #eger kisiye ozgu istiyorsak self init kullanmaliyiz yukarda

# print(calisan.personel_listesi)

#-----------------------------------------------------

class calisan():
    personel_listesi=[]
    
    def __init__(self,isim):
        self.isim=isim
        self.kabiliyetleri=[]
        self.personel_ekle()
    
    def personel_ekle(self):
        self.personel_listesi.append(self.isim)
        print(f"{self.isim} isimli personel listesine eklendi. ")
    
    def personel_listesi_goruntule(self):
        print("------- Personel Listesi -------")
        for personel in self.personel_listesi:
            print(personel)
            
    def kabiliyet_ekle(self,kabiliyet):
        self.kabiliyetleri.append(kabiliyet)
    
    def  kabiliyetleri_goruntule(self):
        print(f"{self.isim} isimli personelin kabiliyetleri :")
        for kabiliyet in self.kabiliyetleri:
            print(kabiliyet)

ahmet= calisan('Ahmet')
berke=calisan('berke')
gokce=calisan('gokce')
ahmet.kabiliyet_ekle("Python")
ahmet.kabiliyet_ekle("Java")
berke.kabiliyet_ekle("Python")
gokce.kabiliyet_ekle("JavaScript")
ahmet.kabiliyetleri_goruntule()

#----------------------------------------------------------
#nesneye ozguler self yapi da kullanirken
#sinifa ozgu yapilari cls methodu yani class methoduyla kullanicaz
class Kitap:
    def __init__(self, ad, yazar, sayfa_sayisi):
        self.ad = ad
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi

    @classmethod
    def tanimla_string_ile(cls, kitap_str):
        ad, yazar, sayfa_sayisi = kitap_str.split(',')
        return cls(ad, yazar, int(sayfa_sayisi))

# Normal bir nesne oluşturma
kitap1 = Kitap("Suç ve Ceza", "Dostoyevski", 500)

# Class method kullanarak nesne oluşturma
kitap_str = "Savaş ve Barış,Tolstoy,1200"
kitap2 = Kitap.tanimla_string_ile(kitap_str)

print(kitap1.ad)   # Suç ve Ceza
print(kitap2.ad)   # Savaş ve Barış

#------------------------------------------------------------
class bilgisayar():
    tum_bilgisayarlar=[] #class degiskeni
    
    def __init__(self,marka,model,ram,depolama):
        self.marka= marka
        self.model= model
        self.ram= ram
        self.depolama = depolama
        
        bilgisayar.tum_bilgisayarlar.append(self)
    
    @classmethod
    def toplam_ram(cls):
        return sum(bilgisayar.ram for bilgisayar in cls.tum_bilgisayarlar)
#class methodumuz tum bilgisayarlarin ram toplamlarini verir
    def ozellikleri_goster(self):
        print(f"{self.marka} {self.model} - RAM : {self.ram} GB , Depolama : {self.depolama} GB ")
        
    @staticmethod #konudan bagimsiz ikisini de ilgilendirmeyen bi calisma yapiyoruz static ile
    def en_yuksek_depolama():
        en_yuksek_depolama = max(bilgisayar.tum_bilgisayarlar,key = lambda bilgisayar : bilgisayar.depolama)
        return f"En yuksek depolama : {en_yuksek_depolama.marka} {en_yuksek_depolama.model}"
    
 

#iki tane bilgisayar olusturalim
bilgisayar1 = bilgisayar("lenovo","IdeaPad",8,512)
bilgisayar2 = bilgisayar("Dell","Inspiron",16,256)

print(f"Toplam RAM : {bilgisayar.toplam_ram()} GB ")  

bilgisayar1.ozellikleri_goster()
bilgisayar2.ozellikleri_goster()

en_yuksek_depolama_bilgisayar = bilgisayar.en_yuksek_depolama()
print(en_yuksek_depolama_bilgisayar)