import mysql.connector as a
mydb=a.connect(host="localhost",user="root",password="omnitrix3")
if(mydb):
    print("connection successful")
else:
    print("connection unsuccessful")