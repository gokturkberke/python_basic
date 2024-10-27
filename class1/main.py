from datetime import datetime

suan = datetime.now() #veya datetime.today de kullanabiliriz ayni kullanim
print(suan)
#sadece yil istiyosak print(suan.year) ayi istiyosak month vs

tarih = datetime.ctime(suan) # ekim 27 pazar ve saat seklinde yazar
print(tarih)

#tarih 18 ocak 2024 saat 13:45:46 saatini olusturma
tarih1 = datetime(2024,1,18,13,45,46) #seklinde olusturulur
bugun = datetime.now()
fark = bugun - tarih1
print(fark)