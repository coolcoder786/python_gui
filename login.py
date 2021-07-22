from tkinter import *
import tkinter.messagebox as tsmg

root = Tk()
root.title("login COOL PROGRAMMER")
root.geometry("500x550")
root.config(bg="skyblue")
root.resizable(0,0)

def Login():
    a = uname.get()
    b = password.get()
    c = cpassword.get()
    mix = a+"-"+b+"-"+c

    with open("login.txt","r") as f:
        data = f.readlines()
        if b==c:
            if str(mix) in str(data):
                tsmg.showinfo("Success","Welcome "+a+" you have succesfully logged in")
            else:
                tsmg.showerror("Error","No user found , pls signup first")
        else:
            tsmg.showerror("Error","both passwords are not same")
        uname.set("")
        password.set("")
        cpassword.set("")

def signUp():
    a = uname.get()
    b = password.get()
    c = cpassword.get()
    mix = a+"-"+b+"-"+c

    if a!="" and b!="" and c!="":
        with open("login.txt","r") as f:
            data = f.readlines()
        if str(mix) in str(data):
            tsmg.showerror("Eror","Account already exist , please Login")
            uname.set("")
            password.set("")
            cpassword.set("")
        elif str(a) in str(data):
            tsmg.showerror("Error","Username already exist")
            uname.set("")
            password.set("")
            cpassword.set("")
        else:
            if b==c:
                with open("login.txt","a") as f:
                    f.write(mix+"\n")
                tsmg.showinfo("Success","Your account is succesfully created!")
                uname.set("")
                password.set("")
                cpassword.set("")

uname=StringVar()
password=StringVar()
cpassword=StringVar()

lbl = Label(root,text="Enter Username",font=("verdana",25),bg="skyblue",fg="black")
lbl.pack(pady=30)

entry1 = Entry(root,width=25,font=("verdana",20),fg="green",textvariable=uname)
entry1.place(x=35,y=90)

pas = Label(root,text="Enter Password",font=("verdana",25),bg="skyblue",fg="black")
pas.pack(pady=60)

entry2 = Entry(root,width=25,font=("verdana",20),fg="green",textvariable=password)
entry2.place(x=35,y=220)

con_pas = Label(root,text="Confirm Password",font=("verdana",25),bg="skyblue",fg="black")
con_pas.place(x=100,y=300)

entry3 = Entry(root,width=25,font=("verdana",20),fg="green",textvariable=cpassword)
entry3.place(x=35,y=350)

signup = Button(root,text="SignUp",font=("verdana",20),bg="black",fg="white",command=signUp)
signup.place(x=100,y=420)

login = Label(root,text="Don't have an account? ,then SignUp",font=("verdana",15),bg="skyblue",fg="red")
login.place(x=50,y=490)

login_button = Button(root,text="Login",font=("verdana",20),bg="black",fg="white",command=Login)
login_button.place(x=300,y=420)

root.mainloop()