from ast import operator
from inspect import formatannotation
import tkinter

from tkinter import *

def butonclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)
    
def butonallclear():
    global operator
    operator=""
    text_input.set("")
    
def butonesittir():
    global operator
    sum = str(eval(operator))
    text_input.set(sum)
    operator=""
calculator = Tk()
calculator.title("Hesap makinesi")
operator = ""
text_input = StringVar() #Tkinter arayüzüyle program içindeki veriler arasında bir "bağ" kurar.
txtDisplay = Entry(calculator,font=('arial',20,'bold'),textvariable=text_input,bd=30,insertwidth=4,bg='powder Blue',justify='right').grid(columnspan=4)
#bd kenarlik genlisigini belirler bg background ayarlar
#insertwidth metin imlecinin genisligini ayarlar
#justify right metin sag tarafa hizalanir .grid columnspan widgetin bulundugu satirda 4 sutun genislgiinde yer kaplayacgini belirtir

buton7 = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="7",bg='powder Blue',command=lambda:butonclick(7)).grid(row=1,column=1)
buton8 = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="8",bg='powder Blue',command=lambda:butonclick(8)).grid(row=1,column=2)
buton9 = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="9",bg='powder Blue',command=lambda:butonclick(9)).grid(row=1,column=3)
usalma=Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="^",bg='powder Blue',command=lambda:butonclick('**')).grid(row=1,column=4)
allclear = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="AC",bg='powder Blue',command=butonallclear).grid(row=1,column=5)

buton4 = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="4",bg='powder Blue',command=lambda:butonclick(4)).grid(row=2,column=1)
buton5 = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="5",bg='powder Blue',command=lambda:butonclick(5)).grid(row=2,column=2)
buton6 = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="6",bg='powder Blue',command=lambda:butonclick(6)).grid(row=2,column=3)
carpma = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="x",bg='powder Blue',command=lambda:butonclick('*')).grid(row=2,column=4)
bolme = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="/",bg='powder Blue',command=lambda:butonclick('/')).grid(row=2,column=5)

buton1 = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="1",bg='powder Blue',command=lambda:butonclick(1)).grid(row=3,column=1)
buton2 = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="2",bg='powder Blue',command=lambda:butonclick(2)).grid(row=3,column=2)
buton3 = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="3",bg='powder Blue',command=lambda:butonclick(3)).grid(row=3,column=3)
toplama = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="+",bg='powder Blue',command=lambda:butonclick('+')).grid(row=3,column=4)
cikarma = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="-",bg='powder Blue',command=lambda:butonclick('-')).grid(row=3,column=5)

buton0 = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="0",bg='powder Blue',command=lambda:butonclick(0)).grid(row=4,column=1)
nokta = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text=".",bg='powder Blue',command=lambda:butonclick('.')).grid(row=4,column=2)
esittir = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="+",bg='powder Blue',command=butonesittir).grid(row=4,column=3)
sag_parantez = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="(",bg='powder Blue',command=lambda:butonclick('(')).grid(row=4,column=4)
sol_parantez = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text=")",bg='powder Blue',command=lambda:butonclick(')')).grid(row=4,column=5)
calculator.mainloop()