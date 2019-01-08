def summ():
    x=int(input("enter first number:"))
    y=int(input("enter the second number:"))
    t=x+y
    print("total:",t)
def sub():
    x=int(input("enter first number:"))
    y=int(input("enter the second number:"))
    d=x-y
    print("diff:",d)

d={1:summ,2:sub}
i=int(input("enter your choice 1: add ,2:sub\n"))
d[i]()
  
