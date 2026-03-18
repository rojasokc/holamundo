#import mysql.connector

#def get_db_connection():
#    return mysql.connector.connect(
#        host="localhost",      # o la IP del servidor MySQL
#        user="root",           # tu usuario MySQL
#        password="Tucodata1!",# tu clave
#        database="tucodata"     # tu base de datos
#    )

#import mysql.connector
#import os

#def get_db_connection():
#    return mysql.connector.connect(
#        host=os.getenv("DB_HOST"),
#        user=os.getenv("DB_USER"),
#        password=os.getenv("DB_PASSWORD"),
#        database=os.getenv("DB_NAME")
#    )

import mysql.connector
import os

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQLHOST"),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        database=os.getenv("MYSQLDATABASE"),
        port=int(os.getenv("MYSQLPORT", 3306))
    )