from tkinter import *

root=Tk()
root.state("normal")
root.title("Tushar's notepad")



def menu_click():
  print("menu is clicked")
  
 



    
menubar=Menu(root)
root.config(menu=menubar)

filemenu=Menu()
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',command=menu_click)
filemenu.add_command(label='Open')
filemenu.add_command(label='Save')
filemenu.add_command(label='Close')





editmenu=Menu()
menubar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')




viewmenu=Menu()
menubar.add_cascade(label='View',menu=viewmenu)



helpmenu=Menu()
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About')












root.mainloop()
