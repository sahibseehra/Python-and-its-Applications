num=input("Enter the number for FACTORIAL=")
num=int(num)
factorial=1
i=1
for i in range(1,num+1):
    factorial=factorial*i
print("factorial is",factorial)
