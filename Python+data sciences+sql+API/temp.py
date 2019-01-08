from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

new_win=Tk()
new_win.state("zoomed")
new_win.title("Admin")
canv=Canvas(new_win,height=768,width=1366)

canv.place(x=0,y=0)

img=ImageTk.PhotoImage(Image.open("travel.jpg"))
canv.create_image(683,384,image=img)
def button1__click():
    
    print("hello")
lbl=Label(new_win,text="Click Below button to know nearby places",fg="black",bg="white",font=('arial',15))
lbl.place(x=360,y=200)    
btn1=Button(new_win,text="GO",bg="#4d88ff",fg="white",height=3,width=10,command=button1__click) 
btn1.place(x=400,y=240)
new_win.mainloop()
