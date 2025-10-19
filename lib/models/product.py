from lib.database import cursor, CONN

class Product:
    def __init__(self, name, category, quantity, price, supplier_id=None, id=None):
        self.id = id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier_id = supplier_id

    def save(self):
        """Insert or update a product."""
        if self.id:
            cursor.execute(
                """
                UPDATE products
                SET name=?, category=?, quantity=?, price=?, supplier_id=?
                WHERE id=?
                """,
                (self.name, self.category, self.quantity, self.price, self.supplier_id, self.id),
            )
        else:
            cursor.execute(
                """
                INSERT INTO products (name, category, quantity, price, supplier_id)
                VALUES (?, ?, ?, ?, ?)
                """,
                (self.name, self.category, self.quantity, self.price, self.supplier_id),
            )
            self.id = cursor.lastrowid
        CONN.commit()
        return self

    def delete(self):
        """Delete the product."""
        if not self.id:
            raise ValueError("Product must have an ID before deletion.")
        cursor.execute("DELETE FROM products WHERE id=?", (self.id,))
        CONN.commit()

    @classmethod
    def all(cls):
        """Return all products as a list of Product instances."""
        rows = cursor.execute(
            "SELECT id, name, category, quantity, price, supplier_id FROM products"
        ).fetchall()
        return [
            cls(id=row[0], name=row[1], category=row[2], quantity=row[3], price=row[4], supplier_id=row[5])
            for row in rows
        ]

    @classmethod
    def find_by_id(cls, product_id):
        """Find a single product by ID."""
        row = cursor.execute(
            "SELECT id, name, category, quantity, price, supplier_id FROM products WHERE id=?",
            (product_id,),
        ).fetchone()
        if row:
            return cls(id=row[0], name=row[1], category=row[2], quantity=row[3], price=row[4], supplier_id=row[5])
        return None

    def __repr__(self):
        return f"<Product {self.id}: {self.name} ({self.category}) - {self.quantity} pcs @ Ksh {self.price}>"
