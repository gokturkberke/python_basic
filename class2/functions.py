#lambda arguments: expression
#lambda kullanmanin avantajlari islevsel programlaama,tek ve kisa islemler iicin kullaniliyor

numbers=[1,2,3,4,5]
karesi = list(map(lambda x: x**2,numbers))
print(karesi)
cift_sayilar = list(filter(lambda x : x%2 ==0, karesi))
print(cift_sayilar)
from functools import reduce
toplam = reduce(lambda x,y : x+y,cift_sayilar)
print(toplam)

isimler=["ali","veli","berke","ayse"]
sorted_names = sorted(isimler, key=lambda x: len(x))
print(sorted_names)
#------------------------------------
#Recursive Fonksiyonlar

def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n* faktoriyel(n-1)
print(faktoriyel(5))
#------------------------------------
