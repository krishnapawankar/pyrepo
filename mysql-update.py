#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      krishna
#
# Created:     09/03/2016
# Copyright:   (c) krishna 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import mysql.connector
from mysql.connector import Error

def update_emp(eid,eadd):

    # prepare query and data
    query = "update emp set eadd=%s where eid=%s"

    data = (eadd,eid)

    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='test',
                                       user='root',
                                       password='mysql')

        # update book title
        cursor = conn.cursor()
        cursor.execute(query, data)

        # accept the changes
        conn.commit()
        cursor.close()
        conn.close()

    except Error as error:

        print(error)


if __name__ == '__main__':
    update_emp('E007', 'Gulbarga')