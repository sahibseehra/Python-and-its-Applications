class A:
    def __init__(self):     #(self,a,b)
        print("super class const") #,a,b

class B(A):
    def __init__(self):
        super().__init__(#(10,20))  
        print("sub class const")
        
obj=B()     #object of inherited class is created
