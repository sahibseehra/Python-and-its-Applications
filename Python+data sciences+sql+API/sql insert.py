import pymysql as psql

r=input("Enter Roll NO:")
n=input("Enter Name:")
m=input("Enter Marks:")

try:
   con=psql.connect("localhost","root","","sahib")

   qry="insert into student values("+r+",'"+n+"',"+m+")"

   cr=con.cursor()

   result=cr.execute(qry)  #(qry): returns no. of affected records
   if(result>0):
       print("Record has been inserted")
       
   






except Exception as ex:
    print(ex)
    
