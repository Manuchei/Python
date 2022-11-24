#pip install mysql-connector-python
import mysql.connector

connection = mysql.connector.connect(host='10.101.11.30', port='3309', user='root', password='Ad1234', database='animal')
cursor = connection.cursor()
#animals = cursor.execute('SELECT * FROM animal')
animals = cursor.execute('INSERT INTO animal(name) VALUES("rata") ')
animals = cursor.fetchall()
for animal in animals:
    print(animal)
connection.close()