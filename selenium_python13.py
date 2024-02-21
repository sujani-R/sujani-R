#data base testing mysql
#ibstall package (my sql connector python)
#database operations
import mysql.connector
connection= mysql.connector.connect(host="localhost", user="root", password="<PASSWORD>", database="mybd")
curs=connection.cursor() #cursor is a temp database
try:
    curs.execute("insert into student values (104,'XYZ')")
    connection.commit() #to commit the transacction
    connection.close() #close the connection
    print ("finished") #confirmation message

    curs.execute("update student set sname ='mary' where sid =103")
    connection.commit() #to commit the transacction
    connection.close() #close the connection
    print ("finished") #confirmation message

    curs.execute("delete from student where sid= 104")
    connection.commit()
    connection.close()
except:
    print ("connection unsuccessful")

#SELECT db operation
curs.execute("select * from student") #commit is not required
for row in curs:
    print (row[0], row[1], row[2])
connection.close()


















