try:
  l=[10,20,30,40,50]

  i=int(input("index to get element="))
#n=10/0  it is exception error which is zero detection error

  print("Result:",l[i])
#except IndexError as ex:   #ex is index variable
    #print("invalid index")
    #print(ex)
#except ValueError as ex:
    #print("index should be numeric")
#for any type of error
except Exception as ex:
    print(ex)
