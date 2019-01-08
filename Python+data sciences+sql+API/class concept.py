class factorial:
    a=10
    def fact(self):
        a=100
        print("hello fact method",a)
    def fact2(self):
        print("hello fact method",self.a)
        self.fact()



obj=factorial()#class with object
obj.fact()
obj.fact2()

