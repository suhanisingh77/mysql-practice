import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="testuser", password="1234", database="LearnCoding")
db_cursor = mydb.cursor()
db_insert= "insert into Emp(id,Ename,email) values(%s , %s , %s)"
db_list = [(2,"Arun","arun@gmail.com") , (3,"Riya","riya@gmail.com")]
db_cursor.executemany(db_insert , db_list)

#db_cursor.execute(" insert into Emp(id,Ename,email) values(%s , %s , %s)",(1,"Ankit","ankit@gmail.com"))     #only one record insert at a time
mydb.commit()
print(db_cursor.rowcount,"values inserted")