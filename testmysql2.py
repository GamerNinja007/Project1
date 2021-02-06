import mysql.connector as a
mydb=a.connect(host="localhost",user="root",password="omnitrix3")
mycursor=mydb.cursor()
mycursor.execute("Create table patient(name varchar(200) ,age int(20))")
