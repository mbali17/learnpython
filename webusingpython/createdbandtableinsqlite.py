'''
    The following code creates the database and as well creates a table in the
    database.sqlite is the databse used and the library used to connect to this
    is sqlite3
'''
import sqlite3
#obtain connection to the database.
#the following line connects to the database named tutorial.db if present
#or creates a new one.
connection = sqlite3.connect('tutorial.db')
'''
cursor is like a pointer used for traversal.
refer:https://stackoverflow.com/questions/6318126/why-do-you-need-to-create-a-cursor-when-querying-a-sqlite-database
'''
cursor = connection.cursor();

#once the connection is obtained we would create the table.
#This function creates the table with out checking if it exists.
#TODO:Inorder to fix this we would have to check for existance.
def create_table():
    #we can write sql queries inside the execute method.It is a standard
    #to write sql related content in caps and others in samll letter.
    #datatypes in sqlite:https://www.tutorialspoint.com/sqlite/sqlite_data_types.htm
    cursor.execute("CREATE TABLE example(language TEXT,version REAL,experiencelevel TEXT)")

create_table()

connection.close()
