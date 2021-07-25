from tkinter import *
import tkinter.messagebox as tsmg

root = Tk()
root.title("BMI by coolprogrammer")
root.geometry("400x380")
root.resizable(0,0)
root.config(bg="black")

def checkBMI():
    weight = int(kilogram.get())
    Height = int(height.get())
    BMI = round(weight / (Height/100)**2)
    if BMI<18.5:
        index = "Under Weight"
    elif 18.5<BMI<25:
        index = "Normal Weight"
    elif BMI>25:
        index = "Over Weight"
    tsmg.showinfo("BMI",f"Your Current BMI is {BMI} and you are {index}")

kilogram = StringVar()
height = StringVar()
lbl = Label(root,text="BMI Calculator",bg="black",fg="white",font=("verdana",20))
lbl.pack()

enterKG = Label(root,text="Enter Your Weight In KG",bg="black",fg="orange",font=("verdana",15))
enterKG.place(x=10,y=80)
e1 = Entry(root,width=20,font=("verdana",20),textvariable=kilogram)
e1.place(x=10,y=120)

enterft = Label(root,text="Enter Your Height In CM",bg="black",fg="orange",font=("verdana",15))
enterft.place(x=10,y=180)
e2 = Entry(root,width=20,font=("verdana",20),textvariable=height)
e2.place(x=10,y=220)

check = Button(root,text="CHECK",bg="green",fg="black",font=("verdana",20),command=checkBMI)
check.place(x=120,y=300)

root.mainloop()