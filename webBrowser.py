from tkinter import *
import webbrowser

def searchAnything():
    link = data.get()
    webbrowser.open(f"https://www.google.com/search?q={link}")
    data.set("")

def openGoogle():
    webbrowser.open("https://www.google.com/")

def openYT():
    webbrowser.open("https://www.youtube.com/")

def openInsta():
    webbrowser.open("https://www.instagram.com/")

def openWhatsapp():
    webbrowser.open("https://web.whatsapp.com/")

root = Tk()
root.geometry("650x400")
root.title("My Web Browser")
root.resizable(0,0)
root.config(bg="yellow")

text = Label(root,bg="yellow",fg="blue",text="Cool Programmer",font=("comic sans",30))
text.pack()

data = StringVar()
url_entry = Entry(root,width=25,font=("comic sans",20),textvariable=data)
url_entry.place(x=60,y=80)

Search = Button(root,bg="blue",fg="black",text="Search",font=("bold",20),command=searchAnything)
Search.place(x=500,y=65)
google = Button(root,bg="skyblue",fg="Black",text="Google",font=("bold",30),command=openGoogle)
google.place(x=90,y=150)
youtube = Button(root,bg="red",fg="black",text="Youtube",font=("bold",30),command=openYT)
youtube.place(x=350,y=150)
instagram = Button(root,bg="pink",fg="black",text="Instagram",font=("bold",30),command=openInsta)
instagram.place(x=85,y=250)
whatsapp = Button(root,bg="green",fg="black",text="Whatsapp",font=("bold",30),command=openWhatsapp)
whatsapp.place(x=350,y=250)

root.mainloop()