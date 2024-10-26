#listeler farkli typelardan olusabilir(str,int,fload) vs

liste3=[["sukru","ahmet","ayse"],["kaya","yilmaz","korkut"],[20,21,22]]
print(liste3[1])
print(liste3[0][0])

#listeler basit bi sekilde birlestirilebilir
liste1=["python","java","C"]
liste2=["c#","JavaScript","Kotlin"]
birlestirilmis_liste=liste1+liste2
print(birlestirilmis_liste)
#liste silme
#del birlestirilmis_liste
#Liste kopyalama(kopyalama onemli onun ustunde kolayca islem yapabiliriz)
bl = birlestirilmis_liste
#veya
bl=birlestirilmis_liste.copy()
#eleman ekleme
bl.append("matlab")
print(bl)
del bl[-2]
print(bl)
#-------------------
liste5 = [1,2,3]
liste6 = [4,5,6]
liste5.append(liste6)
print(liste5) #toplam 4 elemandan olusur ayri ayri 1,2,3 ve 4 5 6yi birlikte tek eleman olarak ekler
liste5.extend(liste6)
print(liste5) #extend de hepsini ayri ayri ekleriz
#----------------------
#indexle eleman ekleme
liste10=["elma","armut","Kivi"]
liste10.insert(1,"Erik")
print(liste10)
liste10.remove("Kivi")
#Listeyi cevirmek tersine
print(liste10[::-1])
#veya
print(list(reversed(liste10)))
#list yazisini eklemezsek farkli bir print yazisi gelir
#pop kodunu kullanmak
print(liste10.pop(0))
#popun remove ile farki pop da cikarilan elemani gosterir remove da kalan listeyi
#sort metodu kucukten buyuge veya stringler de alfabetik siraya gore siralar
liste10.clear()
#bu da listedeki elemanlari bosaltir
#----------------------------------------
#Tuplelar
tuple1=("berke","korkut",15,18.5)
#tuplelar listeler gibi degistirilemez
#tuple1[1]="ahmet" yapamiyoruz error verir
#ayrica liste de yapabilgimiz su eklemeyi burda yapamayiz
#tuple1 + "yusuf" error verir
print(tuple1.index("berke"))
print(tuple1.count("berke"))
#------------------------------------
#Kumeler
#benzersiz ve degistirilebilir ogeler icin kullanilir
kume = set(['Yusuf',"Ahmet","ayse"])
print(kume)
#bir yusuf daha eklesek yani tek yusuf gozukur
isim = "berke korkut"
kume = set(isim)
print(kume)
#ayni sekilde copy kodumuz calisir
kume.add("Ayse") #kumeye eleman ekleme
print(kume)

k1 = set([1,2,3,4,5,6])
k2 = set([4,5,6,7,8,9])
fark=k1.difference(k2)
print(fark)

#isim = set("Yusuf","ahmet","mehmet"])
#isim.discard("Yusuf") dersek yusufu cikaririz ayni sekilde remove da ayni islevi gorur

kesisim=k1.intersection(k2)
print(kesisim)
#k1.isdisjoint(k2) ifadesi ortak ifaddeler varsa false yoksa true cevirir

birlestirme = k1.union(k2)
#symmetric_difference da ortak olmayan seyleri farkliliklari yazdirir
