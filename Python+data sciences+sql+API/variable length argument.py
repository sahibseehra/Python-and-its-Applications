#variable length argument
def area(x,*t):
    if(len(t)==0):
        a=3.14*x**2
        print("area of circle:",a)
    elif(len(t)==1):
        a=x*t[0]
        print("area of rectangle:",a)
    elif(len(t)==2):
        v=x*t[0]*t[1]
        print("volume:",v)
area(10)  #area of circle
area(10,20) #area of rectangle
area(10,20,30) #volume
    


