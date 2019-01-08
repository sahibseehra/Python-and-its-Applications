sum=int(0)
r=int(0)
n=int(input(""))
i=n
while(i!=0):
    r=i%10
    sum=sum*10+r
    i//=10
print(sum+n)    

