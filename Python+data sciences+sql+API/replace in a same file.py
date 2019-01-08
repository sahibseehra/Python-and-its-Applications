myfile=open("D:\\demo.txt","r")

str=myfile.read()
str=str.replace('oops','open source')
myfile=open("D:\\demo1.txt","w")
myfile.write(str)
myfile.close()
