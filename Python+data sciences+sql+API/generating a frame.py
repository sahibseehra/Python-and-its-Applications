from tkinter import *

win=Tk() #function to create window
#win.geometry('500x400')
win.state('zoomed')
win.title('singh notepad')
#win.config(bg="blue")
tbuserid=Entry(win,width=60)
tbuserid.place(x=500,y=100)
tbpass=Entry(win,width=60)
tbpass.place(x=500,y=200)
#we have button class
btn=Button(win, text="signup",width=15,height=3,bg="blue",fg='white')
btn.place(x=500,y=300)
#btn.pack() #button frame size will be equal to windows size
btn=Button(win, text="login",width=15,height=3,bg="blue",fg='white')
btn.place(x=660,y=300)

win.mainloop()
