import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    database='ALPROII',
    password=''
)

cursor = mydb.cursor()
cursor.execute("SELECT * FROM tabel1")


