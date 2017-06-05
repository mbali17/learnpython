import pymysql

from connecttomysql import connectToDatabase

connection = connectToDatabase()

def insertData():
    try:
        with connection.cursor() as cursor:
            insert_sql = 'insert into country values("Mandya",10000,4,"bhutia")'
            cursor.execute(insert_sql)
            #commit the changes to complete the insertion.
            connection.commit()
            print("sucessfully inserted.")
    finally:
        connection.close()
#insertData()

def dynamicData():
    try:
        with connection.cursor() as cursor:
            insert_sql = 'insert into country values(%s,%s,%s,%s)'
            #assuming the value obtained from the user.
            listOfParams = ['malaysia', 11111, 2, 'somebody']
            cursor.execute(insert_sql,listOfParams)
            #commit the changes to complete the insertion.
            connection.commit()
            print("sucessfully inserted.")
    finally:
        connection.close()
dynamicData()