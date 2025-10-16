import sqlite3
CONN = sqlite3.connect('db/database.db')
cursor = CONN.cursor()
"""create a table in the database if it does not exist"""
def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS suppliers (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, ' \
    'contact TEXT))')
    CONN.commit()