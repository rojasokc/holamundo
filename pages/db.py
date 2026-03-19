

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