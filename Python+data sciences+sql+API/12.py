a=input("enter first no a=")
a=int(a)
b=input("enter second no b=")
b=int(b)
c=input("enter third no c=")
c=int(c)

if(a>b):
    if(a>c):
       print("a is greatest")
    else:
       print("c is the greatest")
elif(b>c):
       print("b is greatest number")
else:
    print("c is greatest number")
