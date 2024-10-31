import turtle
#Windows logosunu yapiyoruz
# Turtle ve ekran oluşturma
t = turtle.Turtle()
s = turtle.Screen()

# Ayarları yapma
t.speed(2)
s.bgcolor("white")

# Başlangıç noktası ayarlama
t.penup()
t.goto(-50, 60)  # Başlangıç noktasına git
t.pendown()

# İlk şekli çizme
t.color("#00adef")
t.begin_fill()
t.goto(100, 100)  # Üst sağ nokta
t.goto(100, -100)  # Alt sağ nokta
t.goto(-50, -60)  # Alt sol nokta
t.goto(-50, 60)   # Üst sol nokta
t.end_fill()

# İkinci şekli çizme (beyaz dikey çizgi)
t.color("white")
t.width(10)
t.penup()  # Kalemi kaldır
t.goto(15, 100)  # Dikey çizgi için başlangıç noktasına git
t.pendown()  # Kalemi indir
t.goto(15, -100)  # Dikey çizgiyi çiz

# Üstte yatay beyaz çizgi
t.penup()
t.goto(100, 0)  # Yatay çizgi için başlangıç noktasına git
t.pendown()
t.goto(-50, 0)  # Yatay çizgiyi çiz

# Çizimi tamamla
t.hideturtle()  # Çizim sonrası kaplumbağayı gizle
turtle.done()  # Çizimi bitir

