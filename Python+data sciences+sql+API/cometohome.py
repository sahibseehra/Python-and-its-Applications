str1=input("enter any word:""")
str2=""
str3=""
for i in range(len(str1)):
    if(i%2)==0:
        str2+=str1[i]
    else:
        str3+=str1[i]
print(str3+str2)        
