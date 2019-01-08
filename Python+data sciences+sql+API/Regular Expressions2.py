
import re


m=input("enter the mobile no.")

if(re.match('^[+][9][1][0-9]{10}$',m)):  #we can write [0-9]=[\d]
    print("valid mobile no")
else:
    print("invalid mobile no")
#see tutorialspoint for regular expressions
