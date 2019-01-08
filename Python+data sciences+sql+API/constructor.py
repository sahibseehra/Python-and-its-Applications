class Addition:
    def __init__(self): #def const. #(self,a,b)      ==>parameterized constructor
        self.a=int(input("enter the first number="))    #self.a=a 
        self.b=int(input("enter the second number="))   #self.b=b


    def sum(self):
        c=self.a+self.b
        print("result:",c)

obj=Addition()  #obj=Additon(10,20)

obj.sum()
