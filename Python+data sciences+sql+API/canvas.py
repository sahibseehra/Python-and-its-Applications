from tkinter import *
from next_window import *







main_window=Tk()

main_window.title("Registration form")

main_window.state('zoomed')
can=Canvas(main_window,bg="#9999ff",height=400,width=500)
can.place(x=300,y=340)

btnSubmit=Button(main_window,text="submit")
btnSubmit.place(x=350,y=380)
