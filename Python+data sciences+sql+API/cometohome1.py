name=input("enter any name")
l=len(name)
if l%2==0:
    s=(name[1:l:2]+name[0:l-1:2])
else:
    
    s=(name[1:l-1:2]+name[0:l:2])
print(s)
