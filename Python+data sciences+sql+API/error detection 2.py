#nested try except
try:
    #-------------------------operation 1--------------------------------
 try:     #
  l=[10,20,30,40,50]

  i=int(input("index to get element="))
  print("Result:",l[i])
 except Exception as ex:
     print("invalid index")
  #------------------------------------------------
 d=int(input("enter the value of d")) #if first operation is not ok, flow control do not evaluate second operation
 r=10/d
 print("result2:",r)
  
except Exception as ex:
    print(ex)
