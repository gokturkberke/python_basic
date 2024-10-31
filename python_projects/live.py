from datetime import *  # datetime daki her seyi import eder

dogum_tarihi = datetime.strptime(input("Lutfen dogum tarihiniiz gun.ay.yil seklinde giriniz :"),"%d.%m.%Y")
#strptime fonksiyonu girilen tarihi belirtilen formata gore analiz eder
yas = datetime.now() - dogum_tarihi
print("Siz {} yilindan gunumuze kadar {} saniye yasadiniz".format(dogum_tarihi,yas.total_seconds()))
