class hesapsahibi():
    def __init__(self,ad,soyad,tc_no):
        self.ad=ad
        self.soyad=soyad
        self.tc_no=tc_no
class hesap():
    def __init__(self,hesap_no,hesap_sahibi,bakiye=0):
        self.hesap_no=hesap_no
        self.hesap_sahibi=hesap_sahibi
        self.bakiye=bakiye
        self.hesap_hareketleri=[]
        
    def para_yatir(self,miktar):
        self.bakiye += miktar
        hareket = f"{miktar} TL yatirildi Yeni bakiye : {self.bakiye}"
        self.hesap_hareketleri.append(hareket)
        print(hareket)
        
    def para_cek(self,miktar):
        if self.bakiye >= miktar:
            self.bakiye -=miktar
            hareket=f"{miktar} Tl para cekildi Yeni bakiye {self.bakiye}"
            self.hesap_hareketleri.append(hareket)
            print(hareket)
        else:
            print("Yetersiz bakiye. Islem gerceklestirilemedi")
            
    def hesap_durumu_goster(self):
        print(f"Hesap no : {self.hesap_no}")
        print(f"Hesap sahibi {self.hesap_sahibi.ad} {self.hesap_sahibi.soyad}")
        print(f"Bakiye : {self.bakiye}")
        print("Gecmis hesap hareketleri")
        for hareket in self.hesap_hareketleri:
            print(f"- {hareket}")
            
class banka:
    def __init__(self,adi):
        self.adi=adi
        self.hesaplar={}
        
    def hesap_ac(self,hesap_sahibi):
        hesap_no= str(len(self.hesaplar) +1).zfill(8) #hesaplar adli lsitenin uzunlugunu alip 1 ekleyip 8 haneli bir str e donusturduk
        yeni_hesap=hesap(hesap_no,hesap_sahibi)
        self.hesaplar[hesap_no]=yeni_hesap
        print(f"{hesap_sahibi.ad} {hesap_sahibi.soyad}'a ait yeni hesap olusturuldu")
        
    def hesap_kapat(hesap_no):
        if hesap_no in self.hesaplar:
            del self.hesaplar[hesap_no]
            print(f"{hesap_no} numarali musteri hesabi silindi")
        else:
            print(f"hesap bulunamadi")
            

    def hesap_getir(self,hesap_no):
        return self.hesaplar.get(hesap_no)
    
    
banka = banka("ABC Bankasi")

musteri1 = hesapsahibi("berke","korkut","12345678901")
musteri2= hesapsahibi("ahmet","yilmaz","12345678902")

hesap1 = banka.hesap_ac(musteri1)
hesap2 = banka.hesap_ac(musteri2)