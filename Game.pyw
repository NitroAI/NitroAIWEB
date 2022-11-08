from tkinter import *
import random
from tkinter import ttk
from tkinter import messagebox


win = Tk()
win.title("Rock Paper Sesor")
win.geometry("300x190")
win.resizable(False,False)


def anking():
    lip = ["ROCK","PAPER","SESOR"]
    v = random.choice(lip)
    ank.config(text=v)
    #print(v)
    x = combo.get()
    if x == "ROCK" and v == "PAPER":
        print("PAPER")
        messagebox.askretrycancel("Hurry!","COMPUTER WON :(")
        lv.config(text="PAPER,COM.. WON")
    elif x== "SESOR" and v== "ROCK":
        messagebox.askretrycancel("Hurry!","COMPUTER WON :(")
        lv.config(text="SESOR,YOU WON")
    elif x== "PAPER" and v== "SESOR":
        messagebox.askretrycancel("Hurry!", "COMPUTER WON :(")
        lv.config(text="SESOR,COM.. WON!")
    elif x== "PAPER" and v== "PAPER":
        messagebox.askretrycancel("Hurry!", "DRAW :(")
        lv.config(text="!!DRAW!!")
    elif x== "SESOR" and v== "SESOR":
        messagebox.askretrycancel("Hurry!", "DRAW :(")
        lv.config(text="!!DRAW!!")
    elif x== "ROCK" and v== "ROCK":
        messagebox.askretrycancel("Hurry!", "DRAW :(")
        lv.config(text="!!DRAW!!")

    else:
        messagebox.showinfo("Hurry!", "YOU WON :)")
        lv.config(text="YOU WON")

button = Button(win,text="                                       Cheak                                   ",command=anking,bd=1,bg="lightgrey").pack()


combo = ttk.Combobox(win,font=("consolas",16))
combo['values']=('ROCK',
                 'PAPER',
                 'SESOR')
combo['state']='readonly'
combo.current(0)
combo.pack()

ank = Label(win,text="",font=("consolas",20))
ank.pack()


lv = Label(win,text="",font=("Elephant",20))
lv.pack(pady=10)
#
# lv1 = Label(win,text="",font=("comic",20))
# lv1.place(x=198,y=240)
#
# lv2 = Label(win,text="YOU",font=("comic",15))
# lv2.place(x=10,y=190)
# #
# lv3 = Label(win,text="COM",font=("comic",15))
# lv3.place(x=222,y=190)
#Hellw

mainloop()