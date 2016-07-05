#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      krishna
#
# Created:     02/07/2015
# Copyright:   (c) krishna 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import mysql.connector
cnx = mysql.connector.connect(user='root', password='mysql', host='127.0.0.1', database='test')
cursor = cnx.cursor()
query = """SELECT * FROM book"""
cursor.execute(query)
data = cursor.fetchall()
l = list(data)
for c in l:
    print(c)
cnx.close()

# 'E001' | 'Krishna'    | 141000 | 'Pune'
# 'E002' | 'Karnsai'    | 150000 | 'Udgir'
