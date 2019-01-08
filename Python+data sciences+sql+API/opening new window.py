from tkinter import *
from tkinter import messagebox
import re

def button1_click():
    name1=tbname1.get()
    name2=tbname2.get()
    if(name1==''and name2==''):
        messagebox.showinfo("ERROR!!!","enter details")
    elif(name1==''):
         messagebox.showinfo("ERROR!!!","enter username")
    elif(not(re.match('^[a-zA-Z]{3,10}',name1))):
         messagebox.showinfo("ERROR!!!","enter valid username")   
    elif(name2==''):
         messagebox.showinfo("ERROR!!!","enter mobile no.")
    
    else:
          if(not(re.match('^[0-9]{10}$',name2))):
              messagebox.showinfo("ERROR!!!","Enter valid mobile no.")
          else:
              messagebox.showinfo("Details","Name :"+name1+"\n"+"Mobile no:"+name2) 
              new_win=Tk()
              new_win.geometry("500x400")
              new_win.title("login")
              new_win.mainloop()
   


    
   
def button2_click():
    new_win=Tk()
    new_win.geometry("500x400")
    new_win.title("Signup")
    new_win.mainloop()
    
    





win=Tk()

win.state("zoomed")

win.config(bg='#9999ff')


btn1=Button(win,text="login",bg="blue",fg="white",command=button1_click) #command is button event
btn1.place(x=550,y=300)

btn2=Button(win,text="signup",bg="blue",fg="white",command=button2_click) #command is button event
btn2.place(x=650,y=300)

lbl=Label(win,text="Enter username:",bg="#9999ff",fg="red",font=('arial',15))#or use config function
lbl.place(x=320,y=195)
lbl=Label(win,text="mobile no.",bg="#9999ff",fg="red",font=('arial',15))
lbl.place(x=330,y=225)

tbname1=Entry(win,width=80)
tbname1.place(x=500,y=200)
tbname2=Entry(win,width=80)
tbname2.place(x=500,y=230)





