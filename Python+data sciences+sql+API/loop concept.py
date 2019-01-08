#write program to find value of 'a^ raise  to power using for loop
a=int(input("enter the number"))
b=int(input("enter the power"))

p=1
for i in range(1,b+1):
   p=p*a
print(p)