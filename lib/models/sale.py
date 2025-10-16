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