myfile=open("D:\\demo.txt","r")
str=myfile.readline()


s=0
while(str!=""):

    n=len(str)
    s=s+n
    print(n)
    str=myfile.readline()

print("total number of words:",s)
