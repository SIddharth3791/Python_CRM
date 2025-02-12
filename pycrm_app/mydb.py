
import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '{REPLACE_ME}'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE customer_mngt_db")

print("Database Created")