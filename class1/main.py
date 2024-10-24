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
