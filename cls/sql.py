import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='admin', password='')
print(mydb)
