try:
  l=[10,20,30,40,50]

  i=int(input("index to get element="))
  print("Result:",l[i])
  
except Exception as ex:
    print(ex)
else:
    print("your operation is ok") #always written after the except
finally:   #used to close the task which may be completed or not
    print("thanx for using pyhton")
