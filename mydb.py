import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'ParvSaf667'
)


cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE safuradev")

print("All Done!")