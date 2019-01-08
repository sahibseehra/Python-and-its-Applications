from tkinter import *
from next_window import *


def valueGetter():
    name=tbName.get()
    Email=tbEmail.get()
    load_new_window(main_window,name,Email)
main_window=Tk()

main_window.title("Registration form")

main_window.state('zoomed')

tbName=Entry(main_window,width=100)
tbName.place(x=300,y=200)
tbEmail=Entry(main_window,width=100)
tbEmail.place(x=300,y=270)

btnSubmit=Button(main_window,text="submit",command=valueGetter)
btnSubmit.place(x=300,y=340)

main_window.mainloop()
