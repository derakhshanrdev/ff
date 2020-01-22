import mysql.connector

my_db = mysql.connector.connect(host='localhost', user='admin', password='', database='test')

my_cursor = my_db.cursor()
my_cursor.execute('select * from lessons')
result = my_cursor.fetchall()
for n, w in result:
    print('lessonID: ', n, ' lesson: ', w)
