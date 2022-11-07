from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("570x600")
root.resizable(False,False)
root.config(bg="#17161b")

equation = ""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result =""
    if equation !="":
        try:
            result= eval(equation)
        except:
            result ="error"
            equation = ""
    label_result.config(text=result)



label_result = Label(root,width=25,height=2,text="",font=("arial",30))
label_result.pack()

Button(text="C",font=("arial",30,"bold"),height=1,width=5,bd=2,fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=10,y=100)
Button(text="/",font=("arial",30,"bold"),height=1,width=5,bd=3,fg="#fff",bg="#2a2d36",command=lambda: show("/")).place(x=150,y=100)
Button(text="%",font=("arial",30,"bold"),height=1,width=5,bd=3,fg="#fff",bg="#2a2d36",command=lambda: show("%")).place(x=290,y=100)
Button(text="*",font=("arial",30,"bold"),height=1,width=5,bd=3,fg="#fff",bg="#2a2d36",command=lambda: show("*")).place(x=430,y=100)

Button(text="7",font=("arial",30,"bold"),height=1,width=5,bd=3,fg="#fff",bg="#2a2d36",command=lambda: show("7")).place(x=10,y=200)
Button(text="8",font=("arial",30,"bold"),height=1,width=5,bd=3,fg="#fff",bg="#2a2d36",command=lambda: show("8")).place(x=150,y=200)
Button(text="9",font=("arial",30,"bold"),height=1,width=5,bd=3,fg="#fff",bg="#2a2d36",command=lambda: show("9")).place(x=290,y=200)
Button(text="-",font=("arial",30,"bold"),height=1,width=5,bd=3,fg="#fff",bg="#2a2d36",command=lambda: show("-")).place(x=430,y=200)

Button(text="4",font=("arial",30,"bold"),height=1,width=5,bd=3,fg="#fff",bg="#2a2d36",command=lambda: show("4")).place(x=10,y=300)
Button(text="5",font=("arial",30,"bold"),height=1,width=5,bd=3,fg="#fff",bg="#2a2d36",command=lambda: show("5")).place(x=150,y=300)
Button(text="6",font=("arial",30,"bold"),height=1,width=5,bd=3,fg="#fff",bg="#2a2d36",command=lambda: show("6")).place(x=290,y=300)
Button(text="+",font=("arial",30,"bold"),height=1,width=5,bd=3,fg="#fff",bg="#2a2d36",command=lambda: show("+")).place(x=430,y=300)

Button(text="1",font=("arial",30,"bold"),height=1,width=5,bd=3,fg="#fff",bg="#2a2d36",command=lambda: show("1")).place(x=10,y=400)
Button(text="2",font=("arial",30,"bold"),height=1,width=5,bd=3,fg="#fff",bg="#2a2d36",command=lambda: show("2")).place(x=150,y=400)
Button(text="3",font=("arial",30,"bold"),height=1,width=5,bd=3,fg="#fff",bg="#2a2d36",command=lambda: show("3")).place(x=290,y=400)
Button(text="0",font=("arial",30,"bold"),height=1,width=11,bd=3,fg="#fff",bg="#2a2d36",command=lambda: show("0")).place(x=10,y=500)

Button(text=".",font=("arial",30,"bold"),height=1,width=5,bd=3,fg="#fff",bg="#2a2d36",command=lambda: show(".")).place(x=290,y=500)
Button(text="=",font=("arial",30,"bold"),width=5,bd=3,fg="#fff",bg="#fe9037",relief=RAISED,command=lambda: calculate()).place(x=430,y=400,height=183)






mainloop()