def add():#>defination scope
    c=a+b
    print("result:",c)

a=input("enter the first number=")
a=int(a)
b=input("enter the second number")
b=int(b)

        
add() #> caller scope
#there are two scopes in above program
#data goes from caller scope to the defination scope
#call by value-transfer data from caller to defination function
