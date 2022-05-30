import sqlite3
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect(query):
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result
