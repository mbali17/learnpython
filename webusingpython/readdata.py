import sqlite3

connection = sqlite3.connect("tutorial.db")
cursor =  connection.cursor()

def read_all_data():
    sql = "SELECT * FROM example"
    result = cursor.execute(sql)
    for row in result:
        print(row)
        
def select_specific_data():
    skillLevel = input("what skill level are you looking for: ")
    lang = input("what language are you looking for: ")
    sqltoread = "SELECT * FROM example WHERE experiencelevel = ? AND language = ?"
    #for the dynamic queries the excute method take 2 params one is the sql and the other is the list of values for the question mark.
    for row in cursor.execute(sqltoread,[(skillLevel),(lang)]):
        print(row)
#read_all_data()
select_specific_data()
connection.close()
