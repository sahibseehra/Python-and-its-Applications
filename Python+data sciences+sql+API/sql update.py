import pymysql as psql

r1=input("Enter Roll Number you want to update:")
print("now Enter new values:")
r=input("Enter Roll Number: ")
n=input("Enter Name:")
m=input("Enter Marks:")

try:
   con=psql.connect("localhost","root","","sahib")

   qry="update student set Roll_Number="+r+",Name='"+n+"',Marks="+m+" where Roll_Number="+r1+""

   cr=con.cursor()
   

   result=cr.execute(qry)  #(qry): returns no. of affected records
   if(result>0):
       print("Record has been updated")
   else:
      print("No record found or updated")
       
   






except Exception as ex:
    print(ex)
    
