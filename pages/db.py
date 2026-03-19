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

import os
import mysql.connector
from urllib.parse import urlparse

def get_db_connection():
    url = os.getenv("DATABASE_URL")

    if not url:
        raise Exception("DATABASE_URL no está definida")

    parsed = urlparse(url)

    return mysql.connector.connect(
        host=parsed.hostname,
        port=parsed.port,
        user=parsed.username,
        password=parsed.password,
        database=parsed.path.lstrip('/')
    )