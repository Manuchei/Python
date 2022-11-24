import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('INSERT INTO animal(name) VALUES("perro") ')
cursor.execute('INSERT INTO animal(name) VALUES("gato") ')
connection.commit()

connection.close()