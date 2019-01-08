myfile=open("D:\\demo.txt","r")

str=myfile.read()
myfile2=open("D:\\demo1.txt","w")

myfile2.write(str)
myfile2.close()
