m=input("enter mobile no=")   #using flag variable

flag=0
l=len(m)
if(m==10):
    for x in m:
        if(not(x>='0' and x<='9')):
            flag=1
if(flag==1):
    print("number is invalid")
else:
    print("number is valid")
