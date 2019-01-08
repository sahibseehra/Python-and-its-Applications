myfile=open("D:\\demo.txt","r")
#str=myfile.read()
str=myfile.readline()
c=0
while(str!=""):
    print(str)
    str=myfile.readline()
    c=c+1
print("total no. of lines:",c)
