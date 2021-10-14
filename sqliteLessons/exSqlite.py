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


def insertToTable():
    #cursor.execute("INSERT INTO users VALUES('Yusuf Sina', 'Bakan', 22)")
    cursor.execute("INSERT INTO users VALUES(?,?,?)",
                   ('Yusuf Sina', 'Bakan', 22))
    con.commit()


def selectDataFromTable():
    cursor.execute("SELECT * FROM users")
    liste = cursor.fetchall()
    print(liste)


def updateTable():
    cursor.execute("UPDATE users SET age=23 WHERE age=22")
    con.commit()


def deleteFromTable():
    cursor.execute("DELETE FROM users WHERE age=22")
    con.commit()


createTable()
# insertToTable()
# selectDataFromTable()
# updateTable()

con.close()
