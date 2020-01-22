import mysql.connector

MyDb = mysql.connector.connect(host='localhost', user='admin', password='', database='test')
cursor = MyDb.cursor()
cursor.execute('delete from lessons where lessonID=7')
MyDb.commit()
# a = cursor.fetchall()
# print(a)
