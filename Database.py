import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="testuser", password="1234")
db_cursor = mydb.cursor()

db_cursor.execute(" create database LearnCoding")
print("database created")