from tkinter import *
from tkinter import ttk,messagebox
from textblob import TextBlob

class Correct(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.resizable(False,False)
        self.config(bg="lightblue")
        

    def monk(self,event):
         x = self.ser.get()
         a = TextBlob(x)
         right = str(a.correct())
         self.lbl.config(text=right)

        #  x =  self.ser.get()
        #  a = TextBlob(x)
        #  right = str(a.correct())
        #  self.lbl.config(text=right)

         if self.ser.get() == "":
            messagebox.showerror("hi!!...","Enter your word or spelling")
         else:
            pass


    def torkit(self):

        Label(text="Cheak Your Spelling",font=("consolas",30),bg="lightblue").pack(pady=(50,0))

        self.ser = Entry(justify="center",font=("consolas",20),border=1)
        self.ser.pack()

        self.lbl = Label(bg="lightblue",font=("consolas",30),text="correct spell is")
        self.lbl.pack(pady=(20,0))

        Button(text="Cheak",font=("TKMenuFont",20),bd=0,relief=RAISED,cursor="trek",command=self.monk).pack(pady=10)

        self.bind('<Return>' , self.monk)



   
       

obj = Correct()
obj.torkit()

obj.mainloop()

#win.bind('<Return>' , function)