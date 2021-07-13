from tkinter import *
import time

root = Tk()
root.title("Digital Clock")
root.geometry("420x150")
root.resizable(0,0)

text_font = ("Boulder" , 68 , "bold")
background = "#FFAD1D"
text_color = "#363529"
border_width = 25

label = Label(root , font=text_font , bg = background , fg = text_color , bd = border_width)
label.grid(row=0 , column=1)

def clock():
      current_time = time.strftime("%H:%M:%S")
      label.config(text = current_time)
      label.after(200 , clock)
      
clock()
root.mainloop()
