class A:
    def display(self):
        print("super A class default const")

class B(A):
    def display(self):
        print("sub class function")
        super().display()

obj=B()     #object of inherited class is created
obj.display()

#obj2=A()
#obj2.display()
