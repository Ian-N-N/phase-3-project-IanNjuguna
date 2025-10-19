from lib.database import get_connection
from lib.models.product import Product

class Sale:
    def __init__(self, product_id, quantity, id=None):
        self.id = id
        self.product_id = product_id
        self.quantity = quantity

    def record_sale(self):
        conn = get_connection()
        cursor = conn.cursor()

        # Validate product
        cursor.execute("SELECT stock FROM products WHERE id = ?", (self.product_id,))
        row = cursor.fetchone()
        if not row:
            conn.close()
            raise ValueError("Product not found.")
        if row["stock"] < self.quantity:
            conn.close()
            raise ValueError("Insufficient stock available.")

        # Record sale and update stock
        cursor.execute("INSERT INTO sales (product_id, quantity) VALUES (?, ?)", (self.product_id, self.quantity))
        cursor.execute("UPDATE products SET stock = stock - ? WHERE id = ?", (self.quantity, self.product_id))

        conn.commit()
        conn.close()

    @classmethod
    def monthly_report(cls, month):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT p.name AS product, SUM(s.quantity) AS total_sold, 
                   SUM(s.quantity * p.price) AS total_revenue
            FROM sales s
            JOIN products p ON s.product_id = p.id
            WHERE strftime('%m', s.sale_date) = ?
            GROUP BY p.name
        """, (f"{month:02}",))
        rows = cursor.fetchall()
        conn.close()
        return [{"product": r["product"], "total_sold": r["total_sold"], "total_revenue": r["total_revenue"]} for r in rows]
