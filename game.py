from tkinter import *
import random
from tkinter import messagebox

# you can add more words 
answers = [
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
]

words = [
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
]

num = random.randrange(0,7,1)

def reset():
    global words,answers,num
    num = random.randrange(0,7,1)
    lbl.config(text = words[num])
    e1.delete(0,END)

def word():
    global words,answers,num
    lbl.config(text = words[num])

def check():
    global words,answers,num
    var = e1.get()
    if var==answers[num]:
        messagebox.showinfo("SUCCESS","You guessed the right word .")
        reset()
    else:
        messagebox.showerror("SORRY","You guessed the wrong one .")
        e1.delete(0,END)

root = Tk()
root.geometry("350x400+400+300")
root.title("JUMBLE (cool_programmer7)")
root.config(background="#000000")

lbl = Label(root,text="WELCOME",font=("verdana",18),bg="#000000",fg="#ffffff")
lbl.pack(pady=30)

ans = StringVar()
e1 = Entry(root,font=("verdana",16),textvariable=ans)
e1.pack()

btn = Button(root,text="Check",font=("Comic sans ms",15),width=16,bg="#4C4B4B",fg="#6ab04c",relief=GROOVE,command=check)
btn.pack(pady=40)
reset_btn =Button(root,text="Reset",font=("Comic sans ms",15),width=16,bg="#4C4B4B",fg="#FF0000",relief=GROOVE,command=reset)
reset_btn.pack()

word()
root.mainloop()