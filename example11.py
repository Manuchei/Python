import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE animal (id INTEGER PRIMARY kEY AUTOINCREMENT, name VARCHAR(100)) ')
connection.commit()

connection.close()