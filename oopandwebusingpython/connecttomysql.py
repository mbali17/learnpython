import pymysql as sql

# Connect to the database
def connectToDatabase():
    
    host = input("Enter the hostname or the ip to connect (eg: localhost if the database is on remote machine then the ip address): ")
    port = int(input("Enter the port to connect to :"))
    userName = input("Enter the userName for the databse: ")
    password = input("Enter the password for the database: ")
    database = input("Enter the name of the database to connect: ") 
    connection = sql.connect(host=host,
                             port=port,
                             user=userName,
                             password=password,
                             db=database,
                             charset='utf8mb4',
                             cursorclass=sql.cursors.DictCursor)                
    return connection

#this is a scripting question and would not be executed when the file is imported 
#but when this file is executed this method is invoked.
if __name__ == '__main__':
    connection = connectToDatabase()
    try:
        with connection.cursor() as cursor:
            sql_statement='select * from country'
            cursor.execute(sql_statement)
            results = cursor.fetchall()
            for row in results:
                print(row['Country_Name'])
    finally:
        connection.close()