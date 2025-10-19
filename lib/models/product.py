from lib.database import get_connection

class Product:
    def __init__(self, name, price, stock, supplier_id=None, id=None):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.supplier_id = supplier_id

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, price, stock, supplier_id) VALUES (?, ?, ?, ?)",
            (self.name, self.price, self.stock, self.supplier_id)
        )
        conn.commit()
        conn.close()

    @classmethod
    def all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        conn.close()
        return [
            cls(id=row["id"], name=row["name"], price=row["price"],
                stock=row["stock"], supplier_id=row["supplier_id"])
            for row in rows
        ]

    @classmethod
    def update_stock(cls, product_id, quantity):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE products SET stock = stock - ? WHERE id = ? AND stock >= ?",
            (quantity, product_id, quantity)
        )
        if cursor.rowcount == 0:
            conn.close()
            raise ValueError("Not enough stock or invalid product.")
        conn.commit()
        conn.close()
