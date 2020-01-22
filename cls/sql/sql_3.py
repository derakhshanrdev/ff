import mysql.connector

MyDb = mysql.connector.connect(host='localhost', user='admin', password='', database='test')
MyCursor = MyDb.cursor()
MyCursor.execute('select lesson from lessons')

result = MyCursor.fetchone()
print(result)
