from tkinter import *
from tkinter messagebox
import re


def button1_click(name,mobile):

    name=tbname.get()
    mobile=tbmobile.get()
    mobile=tbmobile.get()
    r=validation(name,mobile);
    print(r)

    if(r):
        new_window()

def button2_click():
    print("ed")

win=Tk()

win.state('zoomed')
win.config(bg='#9999ff')
win.title('python windows app')
btn1=Button(win,text="Submit",bg="blue",fg="white",command=button1__click)
btn1.place(x=550,y=300)
btn2=Button(win,text="cancel",bg="blue",fg="white",command=button2__click)
btn2.place(x=650,y=300)
lbl=Label(win,text="Enter username:",bg="#9999ff",fg="red",font=('arial',15))
lbl.place(x=320,y=195)
lbl=Label(win,text="Password",bg="#9999ff",fg="red",font=('arial',15))
lbl.place(x=330,y=225)
tbname1=Entry(win,width=80)
tbname1.place(x=500,y=200)
tbname2=Entry(win,width=80)
tbname2.place(x=500,y=230)
    new_win=Tk()
