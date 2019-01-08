name= input("enter your name: ")
l=[]
for x in name:
    a=ord(x)
    b=a+1
    c=chr(b)
    l.append(c)
new_name="".join(l)    
print(new_name)
