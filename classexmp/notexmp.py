class ogrenci():
    def __init__(self,ad,soyad,ogrenci_no,notlar=None):
        self.ad=ad
        self.soyad=soyad
        self.ogrenci_no=ogrenci_no
        self.notlar= notlar if notlar is not None else{}
        
    def not_ekle(self,ders,not_degeri):
        if ders not in self.notlar:
            self.notlar[ders] = [] #not girisi daha once yoksa ilk once olusturup alt satirda da ekleme olayini yapiyoruz
        self.notlar[ders].append(not_degeri)
        
    def not_ortalama(self,ders):
        if ders in self.notlar:
            return sum(self.notlar[ders]/len(self.notlar[ders]))
        
        else:
            return None
    
    def genel_not_ortalamasi(self):
        notlar_toplam= 0
        notlar_adet = 0
        
        for ders,notlar in self.notlar.items():
            if notlar and all(isinstance(not_,(int,float)) for not_ in notlar):
                notlar_toplam += sum(notlar)
                notlar_adet += len(notlar)
        return notlar_toplam/notlar_adet if notlar_adet > 0 else None
    
    def durum(self):
        genel_ortalama = self.genel_not_ortalamasi()
        return "Gecti" if genel_ortalama is not None and genel_ortalama >= 50 else "Kaldi"
    
    def ogrenci_bilgilerini_goster(self):
        print(f"Ogrenci no : {self.ogrenci_no}")
        print(f"Ad : {self.ad} Soyad: {self.soyad}")
        print("Notlar :")
        for ders,notlar in self.notlar.items():
            print(f" - {ders} : {','.join(map(str,notlar))}")
        print(f"Genel not ortalamasi : {self.genel_not_ortalamasi()}")
        print(f"Durumu : {self.durum}")
    
ogrenci1=ogrenci("Berke","Korkut","123456",{"Matematik" : [80,90,100],"Fizik" : [70,75,80]})
ogrenci2=ogrenci("Yusuf","Kaya","123457",{"Matematik" : [70,60,100],"Fizik" : [60,85,70]})

ogrenci1.not_ekle("Kimya ", [75,80,90])
ogrenci2.not_ekle("Kimya",[60,70,90])

ogrenci1.ogrenci_bilgilerini_goster()
print("--------------")
ogrenci2.ogrenci_bilgilerini_goster()