from tkinter import *
from tkinter import messagebox

def button1__click():
    messagebox.showinfo("Button1","this is button 1 clicked")
    #print("testing of button 1 click")
def button2__click():
    messagebox.showinfo("Button2","this is button 2 clicked")
    #print("testing button 2 click")


win=Tk()

win.state('zoomed')

win.title('python windows app')
lbl=Label(win,text="Welcome",fg="red",font=('arial',44))
lbl.place(x=500,y=100)
btn1=Button(win,text="Submit",bg="blue",fg="white",command=button1__click) #command is button event
btn1.place(x=550,y=300)
btn2=Button(win,text="cancel",bg="blue",fg="white",command=button2__click)
btn2.place(x=650,y=300)

win.mainloop()
