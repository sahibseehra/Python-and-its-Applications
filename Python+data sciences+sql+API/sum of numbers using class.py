class addition:

    def getdata(self): #or def getdata(self,a,b)
        self.a=int(input("enter first number"))
        self.b=int(input("enter second number"))

    def sum(self):
        c=self.a+self.b
        print("result=",c) #return(c)


obj=addition()

obj.getdata() #or obj.getdata(10,20)
obj.sum()
#result=obj.sum()
#print("result:",result)
