from pytube import YouTube
from tkinter import *

root = Tk()
root.geometry("500x200")
root.title("Yt downloader (cool_programmer7)")
root.resizable(0,0)

title = Label(
    root,
    text="Youtube Video Downloader",
    font="arial 20 bold",
    foreground="#0000ff"
)
title.pack()

link = StringVar()
var = Label(
    root,
    text="Paste link here",
    font="arial 15 bold"
)
var.place(x=160 , y=60)

url_entry = Entry(
    root,
    width=70,
    textvariable=link
)
url_entry.place(x=32 , y=90)

def downloader():
    url=YouTube(str(link.get()))
    video=url.streams.first()
    video.download() 

button=Button(
    root,
    text="DOWNLOAD",
    font="arial 15 bold",
    bg="#ff8000",
    command=downloader
    )
button.place(x=160 , y=130) 
root.mainloop()
