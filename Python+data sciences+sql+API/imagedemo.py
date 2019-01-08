from tkinter import *
from PIL import ImageTk,Image


root=Tk()
root.state("zoomed")

canv=Canvas(root,height=768,width=1366)


canv.place(x=0,y=0)

img=ImageTk.PhotoImage(Image.open("login_bg.jpg"))
canv.create_image(683,384,image=img)
canv2=Canvas(canv,height=300,width=500,bg="white")
canv2.place(x=450,y=200)






root.mainloop()

