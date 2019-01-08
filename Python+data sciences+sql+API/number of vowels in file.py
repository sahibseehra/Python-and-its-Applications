#no. of vowels in file

myfile=open("D:\\demo.txt","r")
text=myfile.read().split()
countv=0
for v in text:
    if(v=='a' or v=='i' or v=='e' or v=='o' or v=='u' or v=='A' or v=='E' or v=='I' or v=='O' or v=='U'):
        countv=countv+1
print("the number of vowels is:",count)        
