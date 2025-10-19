from lib.database import CONN, cursor

class Product:
    def __init__(self, name, price, stock=0, supplier_id=None, id=None):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.supplier_id = supplier_id
    
    def save(self):
        cursor.execute("INSERT INTO products (name, price, stock, supplier_id) VALUES (?, ?, ?, ?)", 
                       (self.name, self.price, self.stock, self.supplier_id))
        CONN.commit()
        self.id = cursor.lastrowid
    
    # update stock after a sale or restock
    def update_stock(self, quantity_change):
        self.stock += quantity_change
        cursor.execute("UPDATE products SET stock = ? WHERE id = ?", (self.stock, self.id))
        CONN.commit()
    
    @classmethod
    def get_all(cls):
        rows = cursor.execute("SELECT * FROM products").fetchall()
        return [cls(id=row[0], name=row[1], price=row[2], stock=row[3], supplier_id=row[4]) for row in rows]
    
    @classmethod
    def find(cls, product_id):
        row = cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,)).fetchone()
        return cls(id=row[0], name=row[1], price=row[2], stock=row[3], supplier_id=row[4]) if row else None
    
