str1=input("enter any word=""")
ascii=[]
str2=[]

for ch in str1:
    ascii.append(ord(ch))
for i in ascii:
    i=i+1
    str2.append(chr(i))
delimiter=''
sentence=delimiter.join(str2)
print(sentence)
