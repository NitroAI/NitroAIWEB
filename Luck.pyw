from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pickle

class First(Tk):
    def __init__(self):
        super().__init__()
        self.title("Password keeper")
        self.geometry("450x315")
        self.resizable(False,False)
        self.config(bg="white")
        self.bind("<Return>",self.work)
        self.bind("x",self.bring)


    def labels(self):
        Label(text="Keep Password Safe!!",font=("consolas",25),bg="white").pack(pady=7)
        self.entry = Entry(bd=4,font=("consolas",15,"bold"))
        self.entry.pack(pady=6)
        self.display = Label(font=("consolas",10),bg="white")
        self.display.pack(pady=10)
        Label(text="Press enter to save the password", font=("consolas", 12), bg="white").pack()
        Label(text="Press x to show the password", font=("consolas", 12), bg="white").pack()
        self.im = ImageTk.PhotoImage(file="Man1.jpg")
        self.img = ImageTk.PhotoImage(file="Man3.jpg")
        self.mi = Label(image=self.im,bg="white",fg="white")
        self.mi.pack()

        self.lack = Label(font=("consolas",20),bg="white")
        self.lack.pack(pady=15)


        # self.ar.destroy()




    def work(self,event):
        x = self.entry.get()
        self.display.config(text="!Password Saved!")
        self.entry.delete(0,END)
        ############################################
        password = x
        file = open("Bidin.txt","wb")
        pickle.dump(password,file)
        file.close()
        messagebox.showinfo("info","password saved")
        self.entry.destroy()
    def bring(self,event):
        file = open("Bidin.txt","rb")
        f = pickle.load(file)
        file.close()
        print(f)
        messagebox.askokcancel("Your Password",f)
    # def last(self,event):
    #     self.entry.pack()




obj = First()
obj.labels()
obj.mainloop()

