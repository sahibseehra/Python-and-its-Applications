import pymysql as psql
from tkinter import *
root=Tk()
root.state("zoomed")
root.config(bg="#9999ff")
lbl=Label(root,text="Roll Number",bg="#9999ff",fg="black",font=('arial',15))#or use config function
lbl.place(x=460,y=150)
lbl=Label(root,text="Name",bg="#9999ff",fg="black",font=('arial',15))
lbl.place(x=590,y=150)
lbl=Label(root,text="Marks",bg="#9999ff",fg="black",font=('arial',15))
lbl.place(x=680,y=150)

con=psql.connect("localhost","root","","sahib")
cr=con.cursor()
qry="select * from student"
cr.execute(qry)
rows=cr.fetchall()

y_value=200
for row in rows:
    x_value=500

    for r in row:
        lbl=Label(root)
        lbl.config(text=r)
        lbl.place(x=x_value,y=y_value)
        x_value=x_value+100
    y_value=y_value+70
root.mainloop()
