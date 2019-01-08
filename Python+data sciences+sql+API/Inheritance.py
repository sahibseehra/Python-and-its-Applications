class A:
    def displayA(self):
        print("super A class default const")

class B(A):
    def displayB(self):
        print("sub class function")

obj=B()     #object of inherited class is created
obj.displayA()
obj.displayB()
