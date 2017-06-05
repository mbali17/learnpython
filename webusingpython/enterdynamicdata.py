import sqlite3;

connection = sqlite3.connect("tutorial.db")

cursor = connection.cursor()

def enter_dynamic_data():
    language = input("what language?")
    version = float(input("what is the version"))
    skilllevel = input("what is the skill level?") 
    cursor.execute("INSERT INTO example ('language','version','experiencelevel') values (?,?,?)", (language,version,skilllevel))
    connection.commit()

enterdata = int(input("Enter 1 to insert data"))
while(enterdata == 1):
    enter_dynamic_data();
    enterdata = int(input("Enter 1 to insert data else 0 to quit"))
connection.close();
