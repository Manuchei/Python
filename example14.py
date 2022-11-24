import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('SELECT * FROM animal WHERE id=2')
animal = cursor.fetchone()
print(animal)
print('Nombre:', animal[1])
connection.close()