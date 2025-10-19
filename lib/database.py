import sqlite3
CONN = sqlite3.connect('db/database.db')
cursor = CONN.cursor()
"""create a table in the database if it does not exist"""
def create_tables():
    cursor.execute("""CREATE TABLE IF NOT EXISTS suppliers (
                   id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   name TEXT NOT NULL,
                   contact TEXT)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    stock INTEGER DEFAULT 0,
                    supplier_id INTEGER,
                    FOREIGN KEY (supplier_id) REFERENCES suppliers(id))""") 
    cursor.execute("""CREATE TABLE IF NOT EXISTS sales (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER,
                    quantity INTEGER,
                    sale_date TEXT,
                    FOREIGN KEY (product_id) REFERENCES products(id))""")
    CONN.commit()