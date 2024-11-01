from tkinter import *
from tkinter import messagebox
import base64
import os

def sifrele():
    sifre = code.get()
    
    if sifre == "1234":
        ekran1 = Toplevel(ekran)
        ekran1.title("Mesaj Şifreleme")
        ekran1.geometry("400x200")
        ekran1.configure(bg="#ed3833")
        
        mesaj = yazi1.get(1.0, END)
        sifrelenen_mesaj = mesaj.encode("ascii")
        base64_bytes = base64.b64encode(sifrelenen_mesaj)
        sifreleme = base64_bytes.decode("ascii")
        
        Label(ekran1, text="Şifreleme", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        yazi2 = Text(ekran1, font="Robote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        yazi2.place(x=10, y=40, width=380, height=150)
        yazi2.insert(END, sifreleme)
    elif sifre == "":
        messagebox.showerror("Key hatası", "Lütfen mesaj şifreleme KEY'inizi giriniz")
    else:
        messagebox.showerror("KEY Hatası", "Hatalı Key Lütfen tekrar giriniz")

def sifre_coz():
    sifre = code.get()
    
    if sifre == "1234":
        ekran2 = Toplevel(ekran)
        ekran2.title("Mesaj Şifre Çözme")
        ekran2.geometry("400x200")
        ekran2.configure(bg="#ed3833")
        
        mesaj = yazi1.get(1.0, END)
        base64_bytes = base64.b64decode(mesaj.encode("ascii"))
        sifresi_acilan_mesaj = base64_bytes.decode("ascii")  # Bu satırda düzeltme yapıldı
        
        Label(ekran2, text="Şifre çözme", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        yazi2 = Text(ekran2, font="Robote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        yazi2.place(x=10, y=40, width=380, height=150)
        yazi2.insert(END, sifresi_acilan_mesaj)
    elif sifre == "":
        messagebox.showerror("Key hatası", "Lütfen mesaj şifreleme KEY'inizi giriniz")
    else:
        messagebox.showerror("KEY Hatası", "Hatalı Key Lütfen tekrar giriniz")

def ana_ekran():
    global ekran
    global code
    global yazi1
    
    ekran = Tk()
    ekran.geometry("425x500")
    
    logo = PhotoImage(file="/Users/gokturkberkekorkut/key.png")
    ekran.iconphoto(False, logo)
    ekran.title("Şifreleme ve Şifre Çözme Uygulaması")
    
    def temizle():
        code.set("")
        yazi1.delete(1.0, END)
    
    Label(text="Şifrelemek veya şifresini çözmek istediğiniz metni giriniz", fg="black", font=("calibri", 13)).place(x=10, y=10)
    yazi1 = Text(font="Rebote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    yazi1.place(x=10, y=40, width=355, height=100)
    
    Label(text="Şifreleme veya şifre çözme keyinizi giriniz", fg="black", font=("calibri", 14)).place(x=10, y=170)
    
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial 25"), show="*").place(x=10, y=200)
    
    Button(text="Şifrele", height="3", width=23, bg="Red", fg="White", bd=0, command=sifrele).place(x=10, y=250)
    Button(text="Şifre Çöz", height="3", width=23, bg="Green", fg="White", bd=0, command=sifre_coz).place(x=200, y=250)
    Button(text="Temizle", height=3, width=23, bg="Blue", fg="White", bd=0, command=temizle).place(x=10, y=310)
    
    ekran.mainloop()

ana_ekran()
