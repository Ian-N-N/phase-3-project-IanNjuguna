from datetime import datetime
from lib.database import get_connection
from lib.models.product import Product

class Sale:
    def __init__(self, product_id, quantity, id=None):
        self.id = id
        self.product_id = product_id
        self.quantity = quantity

    def record_sale(self):
        """Record a sale and update product stock."""
        conn = get_connection()
        cursor = conn.cursor()

        # Validate product exists and has enough stock
        cursor.execute("SELECT stock FROM products WHERE id = ?", (self.product_id,))
        row = cursor.fetchone()
        if not row:
            conn.close()
            raise ValueError("Product not found.")
        if row["stock"] < self.quantity:
            conn.close()
            raise ValueError("Insufficient stock available.")

        #  Record sale with current date (YYYY-MM-DD format)
        sale_date = datetime.now().strftime("%Y-%m-%d")
        cursor.execute(
            "INSERT INTO sales (product_id, quantity, date) VALUES (?, ?, ?)",
            (self.product_id, self.quantity, sale_date)
        )

        #  Update stock after sale
        cursor.execute(
            "UPDATE products SET stock = stock - ? WHERE id = ?",
            (self.quantity, self.product_id)
        )

        conn.commit()
        conn.close()

    @classmethod
    def monthly_report(cls, month):
        """Generate a monthly sales report."""
        conn = get_connection()
        cursor = conn.cursor()

        # Format month as two digits (e.g., 3 -> "03")
        month_str = f"{month:02d}"

        query = """
        SELECT p.name AS product,
               SUM(s.quantity) AS total_sold,
               SUM(s.quantity * p.price) AS total_revenue
        FROM sales s
        JOIN products p ON s.product_id = p.id
        WHERE strftime('%m', s.date) = ?
        GROUP BY p.name
        """

        cursor.execute(query, (month_str,))
        rows = cursor.fetchall()
        conn.close()

        return [
            {
                "product": row["product"],
                "total_sold": row["total_sold"],
                "total_revenue": row["total_revenue"],
            }
            for row in rows
        ]
