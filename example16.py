import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

"""cursor.execute('UPDATE animal SET name="cat" WHERE id=4 ')"""

cursor.execute('UPDATE animal SET id="2" WHERE id=4 ')
connection.commit()

connection.close()

