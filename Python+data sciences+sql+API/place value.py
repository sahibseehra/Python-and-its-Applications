import string 
lowercase = list(map(str,string.ascii_lowercase[:26]))
uppercase = list(map(str,string.ascii_uppercase[:26]))
name= list(map(str,input("enter you password: ")))
l=[]
for x in name:
    if x.isupper()== True : 
       place_value= uppercase.index(x)+1
       a=name.index(x) + 1 
       new_place_value= place_value + a
       l.append((uppercase[new_place_value-1]))
       
    else:
        place_value= lowercase.index(x)+1
        a=name.index(x) + 1 
        new_place_value= place_value + a
        l.append((lowercase[new_place_value-1]))

print("".join(l))





       


