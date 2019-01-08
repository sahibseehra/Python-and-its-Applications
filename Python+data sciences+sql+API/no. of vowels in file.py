myfile=open("D:\\demo.txt","r")
str=myfile.read()

count=0
for v in str:
    if(v=='a' or v=='i' or v=='e' or v=='o' or v=='u' or v=='A' or v=='E' or v=='I' or v=='O' or v=='U'):
       count+=1
print(count)       
