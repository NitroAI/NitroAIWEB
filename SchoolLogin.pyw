# from tkinter import *
# win = Tk()
# win.title("Test.py")
# win.attributes('-fullscreen',0.5)
# mainloop()
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox

class Win(Tk):
    def __init__(self):
        super().__init__()
        #self.geometry("500x600")
        self.maxsize(width=500,height=600)
        self.minsize(width=500,height=600)
        self.title("Login Now")
        self.config(bg="white")

        Label(text="                 Login Now for free service                ",font=("consolas",20)).pack()

        self.photo = ImageTk.PhotoImage(file="Dp1.jpg")
        Label(image=self.photo,bg="white").pack()


    def Getter(self):
        x = self.bin.get()
        print("Student's Name:",x)
        y = self.bin1.get()
        print("School Name:",y)
        z = self.Combo.get()
        print("Class:",z)
        q = self.win2.get()
        print("Roll No:",q)
        r = self.win3.get()
        print("Section:",r)
        # M = self.Ank.get()
        # print(M)
        # G = self.Ank2.get()
        # print("Female",G)




        if self.bin.get() == "":
            messagebox.askretrycancel("Warning!","Enter Your Information")
        elif self.bin.get() == int():
            messagebox.showerror("Error","Wrong Input Name Can't Be Number!!!")






    def Blink(self):
        self.var = StringVar()
        Label(text="               Name:               ", font=("Times")).pack()
        self.bin = Entry(width=20,bd=2,font=("Times"),textvariable=self.var)
        self.bin.pack()
        Label(text="               School:             ",font=("Times")).pack()


        self.bin1 = Entry(width=20,bd=2,font=("Times"))
        self.bin1.pack()

        Label(text="                Class:               ", font=("Times")).pack()
        self.Combo = ttk.Combobox(width=30,values=['1',
                                          '2',
                                          '3',
                                          '4',
                                          '5',
                                          '6',
                                          '7',
                                          '8',
                                          '9',
                                          '10',
                                          '11',
                                          '12', ])
        self.Combo.pack()

        Label(text="Roll No: ", font=("Times")).place(x=140,y=370)
        self.win2 = Entry(bd=2,font=("Times"))
        self.win2.place(x=215,y=370,width=50)
        Label(text="Section: ",font=("Times")).place(x=265,y=370)
        self.win3 = ttk.Combobox(values=[''
                                         'A',
                                         'B',
                                         'C',])
        self.win3.place(x=335, y=370, width=30,height=27)

        self.Ank = Radiobutton(text="Male",value=1,font=("Times")).place(x=265, y=410)
        self.Ank2 = Radiobutton(text="Female",value=0,font=("Times")).place(x=160, y=410)

        self.bramha = ImageTk.PhotoImage(file="Slash.jpg")

        Button(bg="white",image=self.bramha,command=self.Getter,bd=1).place(x=103,y=500,width=298,height=75)


        # self.bin1 = Entry(width=20, bg="lightgrey", font=("Times"))
        # self.bin1.place(x=80, y=307)









if __name__ == "__main__":
    wino = Win()
    wino.Blink()
    wino.mainloop()







