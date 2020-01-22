import mysql.connector

db = mysql.connector.connect(host='localhost', user='admin', password='', database='test')
c = db.cursor()
c.execute('update reza set id=1 where firstname="reza"')
