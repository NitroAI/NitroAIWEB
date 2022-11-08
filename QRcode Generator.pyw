import tkinter
from turtle import bgcolor 
import customtkinter as c
import qrcode as qr
from PIL import Image,ImageTk
from tkinter import messagebox
import random

win = c.CTk()
win.geometry("500x350")
win.title("QRcode Generator")
win.resizable(False,False)

def generator():
    ent = inpute.get()
    if ent == "":
        messagebox.showerror("QRcode Generator","Enter your link or text!!")
    else:
        qrc = qr.make(ent)
        bin = ["ORcode.png","qrcode.png","Qrcode.png"]
        ch = random.choice(bin)
        print(ch)
        qrc.save(ch)
        messagebox.askokcancel("QRcode Generator","QRcode is generated !!\nOpen the QRcode.png file")
def dark(event):
    ent = inpute.get()
    if ent == "":
        messagebox.showerror("QRcode Generator","Enter your link or text!!")
    else:
        qrc = qr.make(ent)
        bin = ["ORcode.png","qrcode.png","Qrcode.png"]
        ch = random.choice(bin)
        print(ch)
        qrc.save(ch)
        messagebox.askokcancel("QRcode Generator","QRcode is generated !!\nOpen the QRcode.png file")
    

    



frame = c.CTkFrame(win)
frame.pack(pady=20)

# inputlb = c.CTkLabel(master=frame,text="Enter Link :",text_font=("consolas",15))
# inputlb.grid(pady=10,padx=5)
# img = ImageTk.PhotoImage(file="working1.jpg")

inpute = c.CTkEntry(master=frame,text_font=("consolas",15),placeholder_text="Enter your link here",width=400)
inpute.grid(pady=10,padx=10)

# name = c.CTkEntry(master=frame,text_font=("consolas",15),placeholder_text="Scanner Name",width=400)
# name.grid(pady=10,padx=7)

button = c.CTkButton(master=frame,text="Generate now",text_font=("consolas",15),command=generator)
button.grid(pady=10,padx=8)

instruction = c.CTkLabel(text="How to Generate-\nStep 1 - Paste your link or text in Entry.\nStep 2 - Click on Generate button or enter.\nYour qrcode will save in a png file in your working folder!" ,text_font=("consolas",10))
instruction.pack()

footer = c.CTkFrame(win)
footer.pack(pady=15)

c.CTkLabel(master=footer,text="Follow us on - ").pack()

social = c.CTkFrame(win)
social.pack()

social2 = c.CTkFrame(master=social)
social2.pack(pady=5,padx=5)
c.CTkLabel(master=social2,text="Twitter - MR X ").pack(pady=3,padx=90)

social1 = c.CTkFrame(master=social)
social1.pack(pady=5,padx=5)
c.CTkLabel(master=social1,text="Youtube - MR0X ").pack(pady=5,padx=90)






win.bind("<Return>",dark)
win.mainloop()























# import qrcode as qr
# #inatsll qrcode module using cmd command >>

# a = input("Enter Link or Word: ")
# scanner = qr.make(a)
# print(a)
# b = input("Enter Scanner file name: ")
# c = b + ".png"
# print(c)
# scanner.save(c)
# #It will save on your working directory >> folder