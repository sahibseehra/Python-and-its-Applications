sum=int(0)
r=int(0)
n=int(input(""))
while(n!=0):
    r=n%10
    sum+=r
    n//=10
print(sum)    
  
