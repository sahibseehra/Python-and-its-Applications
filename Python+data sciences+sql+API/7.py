#declaring list:
l=[]
n=input("enter no of students")
n=int(n)

for i in range(0,n):
    name=input("enter student name=")
    l.append(name)#if there is no list , then elements are appended on the next memory location
print(l)
