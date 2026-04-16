import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="testuser", password="1234", database="LearnCoding")
db_cursor = mydb.cursor()
# db_cursor.execute(" create table Emp(id int , Ename varchar(20), email varchar(50))")
# print("table created")

# db_cursor.execute(" create table Emp2(id int , Ename varchar(20), email varchar(50))")
# print("table created")

db_cursor.execute(" Show tables")
for i in db_cursor:
    print(i)

