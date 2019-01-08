from tkinter import *
from tkinter import messagebox

def button1__click():
    name1=tbname1.get()
    name2=tbname2.get()
    if(name2=='12345'):
        messagebox.showinfo("password is",name2)
    if(name1!=''):
        messagebox.showinfo("username is",name1)
    else:
        messagebox.showinfo("Error","Enter details")
      
    #messagebox.showinfo("Button1","this is button 1 clicked")
    #print("testing of button 1 click")
def button2__click():
    
    messagebox.showinfo("Button2","this is button 2 clicked")
    #print("testing button 2 click")


win=Tk()

win.state('zoomed')
win.config(bg='#9999ff')
win.title('python windows app')
btn1=Button(win,text="Submit",bg="blue",fg="white",command=button1__click) #command is button event
btn1.place(x=550,y=300)
btn2=Button(win,text="cancel",bg="blue",fg="white",command=button2__click)
btn2.place(x=650,y=300)
lbl=Label(win,text="Enter username:",bg="#9999ff",fg="red",font=('arial',15))#or use config function
lbl.place(x=320,y=195)
lbl=Label(win,text="Password",bg="#9999ff",fg="red",font=('arial',15))
lbl.place(x=330,y=225)
tbname1=Entry(win,width=80)
tbname1.place(x=500,y=200)
tbname2=Entry(win,width=80)
tbname2.place(x=500,y=230)
win.mainloop()
