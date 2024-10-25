# Ürün sınıfı tanımı
class urun:
    def __init__(self, urun_id, ad, fiyat, stok_adedi):
        # Ürün özellikleri tanımlandı
        self.urun_id = urun_id
        self.ad = ad
        self.fiyat = fiyat
        self.stok_adedi = stok_adedi  # stok_adedi şeklinde doğru yazıldı
    
    def bilgileri_goster(self):
        # Ürünün bilgilerini ekrana yazdıran fonksiyon
        print(f"Urun ID : {self.urun_id}")
        print(f"Urun adi : {self.ad}")
        print(f"Fiyat : {self.fiyat}")
        print(f"Stok adedi : {self.stok_adedi}")
        print("-" * 20)  # Bilgiler arasında ayrım yapılması için çizgi çekildi

# Kullanıcı sınıfı tanımı
class kullanici:
    def __init__(self, kullanici_id, ad, soyad, email):
        # Kullanıcı özellikleri tanımlandı
        self.kullanici_id = kullanici_id
        self.ad = ad
        self.soyad = soyad
        self.email = email
        self.siparisler = []  # Siparişler için boş bir liste

    def siparis_ver(self, urunler):
        # Sipariş verme fonksiyonu; yeni siparişi sipariş listesine ekler
        siparis = Siparis(self, urunler)
        self.siparisler.append(siparis)

    def bilgileri_goster(self):
        # Kullanıcı bilgilerini ve siparişlerini ekrana yazdıran fonksiyon
        print(f"Kullanici Id: {self.kullanici_id}")
        print(f"Ad : {self.ad}")
        print(f"Soyadi : {self.soyad}")
        print(f"email : {self.email}")
        print("Siparisler:")
        for siparis in self.siparisler:
            siparis.detaylari_goster()  # Sipariş detaylarını göster
            print("=" * 20)

# Sipariş sınıfı tanımı
class Siparis:
    def __init__(self, kullanici, urunler):
        # Sipariş özellikleri tanımlandı
        self.siparis_id = len(kullanici.siparisler) + 1  # Sipariş ID’si, kullanıcının sipariş sayısına göre belirlenir
        self.kullanici = kullanici
        self.urunler = urunler
        self.toplam_tutar = sum(urun.fiyat for urun in urunler)  # Ürünlerin fiyatlarının toplamını hesapla

        for urun in urunler:
            if urun.stok_adedi == 0:  # Stok adedi sıfır olan ürün varsa hata verir
                raise ValueError(f"{urun.ad} stokta bulunmamaktadır")
            urun.stok_adedi -= 1  # Stoktan bir adet düşer

    def detaylari_goster(self):
        # Sipariş detaylarını gösteren fonksiyon
        print(f"Siparis id : {self.siparis_id}")
        print("Urunler:")
        for urun in self.urunler:
            urun.bilgileri_goster()
        print(f"Toplam tutar : {self.toplam_tutar}")
        print("=" * 20)

# Envanter sınıfı tanımı
class envanter:
    def __init__(self):
        # Envanterdeki ürünleri tutmak için boş bir liste oluşturuldu
        self.urunler = []

    def urun_ekle(self, urun):
        # Envantere ürün ekleyen fonksiyon
        self.urunler.append(urun)

    def envanter_durumu_goster(self):
        # Envanterdeki tüm ürünleri ekrana yazdıran fonksiyon
        print("Envanter durumu:")
        for urun in self.urunler:
            urun.bilgileri_goster()
        print("=" * 20)

# Envanter ve Ürün örnekleri oluşturuluyor
envanter = envanter()
urun1 = urun(1, "Akilli Telefon", 1200, 10)
urun2 = urun(2, "Tablet", 1500, 5)
urun3 = urun(3, "Bilgisayar", 1600, 8)

# Ürünler envantere ekleniyor
envanter.urun_ekle(urun1)
envanter.urun_ekle(urun2)
envanter.urun_ekle(urun3)

# Kullanıcı örnekleri oluşturuluyor
kullanici1 = kullanici(101, "berke", "korkut", "berkekorkt1907@gmail.com")
kullanici2 = kullanici(102, "ahmet", "yilmaz", "ahmetyilmaz@gmail.com")

# Kullanıcılar sipariş veriyor
kullanici1.siparis_ver([urun1, urun2])
kullanici2.siparis_ver([urun2, urun3])

# Kullanıcı bilgileri ve siparişleri ekrana yazdırılıyor
kullanici1.bilgileri_goster()
kullanici2.bilgileri_goster()

# Envanter durumu ekrana yazdırılıyor
envanter.envanter_durumu_goster()


