from tkinter import * 
import random

attempts = 10
num = random.randint(1,100)

def check_answer():
    global attempts
    global text

    attempts-=1
    user = int(entry_window.get())

    if num==user:
        text.set("Well Done , you won ")
        btn.pack_forget()

    elif attempts == 0:
        text.set("you are out of attempts!")
        btn.pack_forget()

    elif user < num:
        text.set("Incorrect! enter a Higher number, " + str(attempts) + " chances Left")

    elif user > num:
        text.set("Incorrect! enter a Lower number,  " + str(attempts) + " chances Left")

root = Tk()
root.title("Number guessing game")
root.geometry("500x200")
root.config(background="#FFFFFF")
root.resizable(0,0)

label = Label(
    root,
    text="Enter any number between 1 and 100 ",
    font=("Bold",15),
    foreground="#0066FF",
    background="#FFFFFF"
)
label.pack() 

entry_window= Entry(root , width=40 , borderwidth=5)
entry_window.pack(ipady=5) 

btn = Button(
    root,
    text="Check",
    font=("Arial",15),
    foreground="#3AA655",
    padx=50,
    command=check_answer
)
btn.pack()

btn_quit = Button(
    root,
    text="Quit",
    font=("Arial",15),
    foreground="#ED0A3F",
    padx=60,
    command=root.destroy
)
btn_quit.pack()

text = StringVar()
text.set("You Have 10 Chances to guess The number")

chances = Label(
    root,
    textvariable=text,
    font=("Comicsans" , 15),
    foreground="#FF007C",
    background="#FFFFFF"
)
chances.pack() 

root.mainloop()
