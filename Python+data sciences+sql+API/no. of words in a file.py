myfile=open("D:\\demo.txt","r")
str=myfile.readline()


s=0
while(str!=""):
    l=str.split()
    n=len(l)
    s=s+n
    print(n)
    str=myfile.readline()

print("total number of words:",s)
