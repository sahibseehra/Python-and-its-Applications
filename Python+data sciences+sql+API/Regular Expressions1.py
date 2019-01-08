
import re


m=input("enter the mobile no.") #[a-zA-Z] =>for both small and big ALPHABETS

if(re.match('^[0-9]{10}$',m)): #$ sign states only to take 10 character 
    print("valid mobile no")
else:
    print("invalid mobile no")
