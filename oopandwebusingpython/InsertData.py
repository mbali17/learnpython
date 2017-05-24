import sqlite3
'''
Steps in connecting to sqlite
    1)import sqlite3 library
    2)obtain connection to the database.
    3)obtain the curor for the databse connected.
'''

connection = sqlite3.connect("tutorial.db")

cursor = connection.cursor()

def insert_data():
    cursor.execute("INSERT INTO example VALUES('python',2.7,'beginner')")
    cursor.execute("INSERT INTO example VALUES('python',3.0,'Intermediate')")
    cursor.execute("INSERT INTO example VALUES('python',3.3,'Expert')")
    #connection.commit()
'''
    unless the connection is not closed the data inserted is written in
    intermediate file and we might not want to create a new connection every
    time for performing any operation. In order to make a single connection and
    use it across we can use the commit method which would write the
    intermediate content to the database.
'''
connection.close()
