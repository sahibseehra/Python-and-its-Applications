from tkinter import *
def load_new_window(mwindow,n,e):
 mwindow.destroy()  
    
 next_window=Tk()
 
 next_window.title("Confermation page")

 next_window.state('zoomed')

 lbl=Label(next_window,text="Name:",bg="#9999ff")#or use config function
 lbl.place(x=320,y=195)
 lbl=Label(next_window,text="Email:",bg="#9999ff")
 lbl.place(x=330,y=225)
 lblName=Label(next_window)
 lblName.place(x=430,y=195)
 lblName.config(text=n)
 lblEmail=Label(next_window)
 lblEmail.place(x=430,y=230)
 lblEmail.config(text=e)

 next_window.mainloop
