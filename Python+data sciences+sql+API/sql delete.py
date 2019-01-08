import pymysql as psql

r=input("Enter Roll NO:")
#we can also use other data elements


try:
   con=psql.connect("localhost","root","","sahib")

   qry="delete from student where Roll_Number="+r+""

   cr=con.cursor()

   result=cr.execute(qry)  #(qry): returns no. of affected records
   if(result>0):
       print("Record has been deleted")
   else:
      print("no Record found")
       
   






except Exception as ex:
    print(ex)
    
