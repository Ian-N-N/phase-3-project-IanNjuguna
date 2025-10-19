import sqlite3

def get_connection():
    conn = sqlite3.connect("db/database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Create tables if not exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER DEFAULT 0,
            supplier_id INTEGER,
            FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            quantity INTEGER,
            date TEXT,
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    """)

    
    cursor.execute("PRAGMA table_info(sales)")
    columns = [col["name"] for col in cursor.fetchall()]
    if "date" not in columns:
        cursor.execute("ALTER TABLE sales ADD COLUMN date TEXT")
        print("🛠️ Added missing 'date' column to 'sales' table.")

    conn.commit()
    conn.close()
    print(" Database initialized successfully!")
