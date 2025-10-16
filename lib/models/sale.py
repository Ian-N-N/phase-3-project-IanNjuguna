# sales, recording and reporting
from lib.database import CONN, cursor
from datetime import datetime
from lib.models.product import product

class Sale:
    def __init__(self, product_id, quantity, sale_date=None, id=None):
        self.id = id
        self.product_id = product_id
        self.quantity = quantity
        self.sale_date = sale_date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def record_sale(self):
        # record sale and update stock automatically
        product = product.find(self.product_id)
        if not product:
            raise ValueError("Product not found")
        if product.stock < self.quantity:
            raise ValueError("Insufficient stock")
        cursor.execute("INSERT INTO sales (product_id, quantity, sale_date) VALUES (?, ?, ?)", 
                       (self.product_id, self.quantity, self.sale_date))
        product.update_stock(-self.quantity)
        CONN.commit()

    @classmethod
    def monthly_report(cls, month):
        # generate sales report for a given month
        rows = cursor.execute("""
            SELECT products.name, SUM(sales.quantity) as total_sold,
            SUM(sales.quantity * products.price) as total_revenue
            FROM sales
            JOIN products ON sales.product_id = products.id
            WHERE strftime('%m', sales.sale_date) = ?
            GROUP BY products.name
        """, (f"{int(month):02d}",)).fetchall()
        report = []
        for row in rows:
            report.append({
                'product_name': row[0],
                'total_sold': row[1],
                'total_revenue': row[2]
            })
        return report