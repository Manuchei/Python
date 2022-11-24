import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('DELETE from animal WHERE id=1 ')
cursor.execute('DELETE from animal WHERE id=2 ')
cursor.execute('DELETE from animal WHERE id=3 ')
connection.commit()

connection.close()

