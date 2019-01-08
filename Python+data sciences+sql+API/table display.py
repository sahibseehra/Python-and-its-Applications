import pymysql as psql

con=psql.connect("localhost","root","","sahib")

cr=con.cursor()

qry="select * from student"
cr.execute(qry)
rows=cr.fetchall()
for row in rows:
    for r in row:
        print(r,end=" ")
    print()    
#rows=cr.fetchone()


#print(rows)

