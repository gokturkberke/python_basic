import turtle
t = turtle.Turtle()
w = turtle.Screen()  # Ekran açmamızı sağlayan komut

w.title("Turk Bayragi")
w.setup(width=720, height=420)  # Pencere boyutu
w.bgcolor("red")  # Arka plan rengi

# Büyük daire
t.up()
t.goto(-100, -100)  # Fare imleci lokasyonu
t.color("white")
t.begin_fill()  # Beyaz renkle boya demek
t.circle(120)
t.end_fill()

# Küçük daire
t.goto(-70, -80)
t.color("red")
t.begin_fill()
t.circle(100)
t.end_fill()

# Yıldız
t.goto(0, 35)
t.color("white")
t.begin_fill()  # Burada yalnızca begin_fill() kullanmalısın

for i in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()

# Yazı
t.goto(-130, -190)
t.color("white")
t.write("Python Vadisi", font=("Verdana", 11, "bold"))

# İmleci uzak bir yere götür
t.goto(-999, 0)  # İmleç ekranda durup görüntüyü bozmasın diye uzak bir yere götürüyor
w.exitonclick()  # Ekrana tıklayınca program kapanması için
