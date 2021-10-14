from os import path
import sqlite3

# Connection settings
con = sqlite3.connect("deneme.db")
cursor = con.cursor()


def createTable():
    # Execute SQL and commit to db
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users(name TEXT, lastName TEXT, age INT)")
    con.commit()


con.close()
