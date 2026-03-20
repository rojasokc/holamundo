#import os
#import mysql.connector

#def get_db_connection():
#    return mysql.connector.connect(
#        host=os.getenv("MYSQLHOST"),
#        port=int(os.getenv("MYSQLPORT")),
#        user=os.getenv("MYSQLUSER"),
#        password=os.getenv("MYSQLPASSWORD"),
#        database=os.getenv("MYSQLDATABASE")
#    )

import os
import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host=os.getenv("MYSQLHOST"),
        port=int(os.getenv("MYSQLPORT")),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        database=os.getenv("MYSQLDATABASE")
    )

    # 👇 AQUÍ va la solución
    cursor = conn.cursor()
    cursor.execute("SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''))")
    cursor.close()

    return conn