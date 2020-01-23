import mysql.connector

# values = ([(2, 'ali'), (3, 'mmd'), (4, 'dara'), (5, 'elmira')]
DataB = mysql.connector.connect(host='localhost', user='admin', password='', database='test')
cursor = DataB.cursor()
ID = [("2", "ali"), ("3", "mmd"), ("4", "dara"), ("5", "elmira")]

# sql = f'insert into f55(id, name) values({ID})'
cursor.executemany(f'insert into f55(id, name) values {ID}', '')
# for i in cursor:
#    print(i)
