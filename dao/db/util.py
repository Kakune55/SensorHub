import sqlite3

def getConn():
    return sqlite3.connect("./data/data.db")