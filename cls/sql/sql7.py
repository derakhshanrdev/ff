import mysql.connector

db = mysql.connector.connect(host='localhost', user='admin', password='', database='test')
cursor = db.cursor()
cursor.execute('drop table lessons')
