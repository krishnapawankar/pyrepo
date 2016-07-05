import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root', password='mysql', host='127.0.0.1', database='test')
cursor = cnx.cursor()

query = ("SELECT * FROM login WHERE loginid = 'krishna'")

cursor.execute(query)

for list in cursor:
  print(list)

cursor.close()
cnx.close()