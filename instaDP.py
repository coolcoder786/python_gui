import instaloader
from tkinter import *

root = Tk()
root.geometry("500x250")
root.title("insta dp downloader (cool_programmer7)")
root.resizable(0,0)

title = Label(
    root,
    text="Instagram DP Downloader",
    font="arial 20 bold",
    foreground="#0000ff"
)
title.pack()

img = PhotoImage(file="instagram.png")
label_img = Label(
    root,
    image=img,
)
label_img.pack()

link = StringVar()
var = Label(
    root,
    text="Please enter the username here",
    font="arial 15 bold"
)
var.place(x=100 , y=120)

url_entry = Entry(
    root,
    width=70,
    textvariable=link,
)
url_entry.place(x=32 , y=150)

def downloader():
    insta=instaloader.Instaloader()
    image = url_entry.get()
    insta.download_profile(image,profile_pic_only=True)

button=Button(
    root,
    text="DOWNLOAD",
    font="arial 15 bold",
    bg="#ff8000",
    command=downloader
    )

button.place(x=160 , y=180) 
root.mainloop()