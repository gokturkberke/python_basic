a=10;
b=15;
print("{} sayisi ile {} sayisinin carpimi {}'dir" .format(a,b,a*b))
print("{2}{0}{1}".format("Gokturk","Berke","Korkut"))

liste1=list("berke korkut")
print(liste1)

tuple1 = (1,2,3,4,5,6,7,8,9,10) #tuple lar bu parantezle yapilir degistirilemezler
print(tuple1[-1])
sozluk1 = {"apple" : "Elma" , "watermelon" : "karpuz" , "cat" : " kedi" , "dog" : "kopek"};
print(sozluk1["cat"]);
#sozlukler degistirilebilir sozluk1["cat"]= aslan diyerek mesela

sayi1= int(input("lutfen bir sayi giriniz")); #int eklememiz onemli yoksa alttaki satirda error aliriz
print("Girmis oldugunuz sayinin 5 fazlasi :", sayi1 +5);

#string.strip() komutu basindaki ve sonundkai bosluklari kaldirir(arasindaki degil)
#string.count("yusuf") burdaki count da kac defa yusuf olduguna bakar stringimizdeki

kisakenar=int(input("lutfen dikdortgenin kisa kenarini girin"));
uzunkenar=int(input("lutfen uzun kenari girin"));

alan=kisakenar * uzunkenar;
cevre = 2* (kisakenar+uzunkenar);

print("Dikdortgenin alani :" , alan );
print("dikdortgenin cevresi :" , cevre);
#!= iki taraf esit olmadiginda true dondurur

# for i in range(0,20):
#     if(i==5 or i==8):
#         continue;
#     print("sayi degeriniz : " ,i)
# 5 ve 8i atlar continue o kosulu atlamaya yariyo break direkt sonlandiriyo kodu

# for i in range(101):
#     if i%2 ==0 :
#         print(i ,"cift sayidir")
#     else:
#         print(i,"tek sayidir")           tek cift yazdirma komutu

#iki sayi arasindaki sayilari ekrana bastirma
sayi1=int(input("lutfen ilk sayiyi girin : "));
sayi2=int(input("Lutfen ikinci sayiyi girin : "));

for i in range(sayi1 +1 ,sayi2):
    print(i);

def topla (a,b,c):
    return a+b+c

def beskatinial(a):
    return a*5

print("toplayacaginiz 3 sayiyi giriniz")
sayi1=int(input("1. sayiyi giriniz : "))
sayi2=int(input("2. sayiyi giriniz : "))
sayi3=int(input("3. sayiyi giriniz : "))

print("bu topladiginiz degerleri carpacaginiz sayiyi girin : ")

carpim=int(input("toplamin kac kati ile carpilacagini girin : "))

toplam=topla(sayi1,sayi2,sayi3)
sonuc=beskatinial(toplam)
print(" vermis oldugunuz sayilarin {} ile carpiminin sonucu : {}".format(carpim,sonuc))

#fonksiyonda veridgimiz degerleri baska yerde kullanicaksak return onemli

# def f(*par,**pars):
#     print("Konum eslestirmeli parametre :", par)
#     print("isim eslestirmeli parametre :", pars)
    
# f(1,2,3,4,5,6,a=10,b="Yusuf",c ="Kaya")

# def f(a,b,c,d):
#     print(a,b,c,d)
    
# x=(1,2,3,4)
# f(*x)

#Fonksiyon icerisinde degerini degistirmek istersek hata aliriz

# m=10
# def f():
#     m=m*2
#     print(m)
    
# f()        bu error verir

m=10
def f():
    global m #fonksiyon icersiindeki deger degisimlerinde global kullaniriz
    m=m*5
    print(m)
    
f()

# x= []

# def elemanekle(m):
#     x.append(m)
    