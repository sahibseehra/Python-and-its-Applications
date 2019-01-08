myfile=open("D:\\demo2.txt","r")
str=myfile.readline()
str=myfile.readline()
list1=[]
list2=[]
while(str!=""):
    l=str.split()
    str=myfile.readline()

    list1.append(l[0])
    list2.append(l[1])
print(list1)
print(list2)
myfile.close()
