import sqlite3

connection = sqlite3.connect("tutorial.db")
cursor =  connection.cursor()

def read_all_data():
    sql = "SELECT * FROM example"
    result = cursor.execute(sql)
    for row in result:
        print(row)
        
def limit_data():
    sqltoread = "SELECT * FROM example limit 1"
    #for the dynamic queries the excute method take 2 params one is the sql and the other is the list of values for the question mark.
    for row in cursor.execute(sqltoread):
        print(row)
def update_data():
    sql = "UPDATE example SET experiencelevel='Beginner' where experiencelevel='beginner'"
    cursor.execute(sql)
    connection.commit();

def delete_data():
    sql = "DELETE FROM example  where experiencelevel='Beginner'"
    cursor.execute(sql)
    connection.commit()
#limit_data()
#update_data()
delete_data()
read_all_data()
connection.close()
