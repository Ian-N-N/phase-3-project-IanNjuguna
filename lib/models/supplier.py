#model for suppliers
from lib.database import CONN, cursor

class Supplier:
    def __init__(self, name, contact, id=None):
        self.id = id
        self.name = name
        self.contact = contact
    
    def save(self):
        cursor.execute("INSERT INTO suppliers (name, contact) VALUES (?, ?)", (self.name, self.contact))
        CONN.commit()
        self.id = cursor.lastrowid
# getting alll suppliers
    @classmethod
    def get_all(cls):
        rows = cursor.execute("SELECT * FROM suppliers").fetchall()
        return [cls(id=row[0], name=row[1], contact=row[2]) for row in rows]
    
    @classmethod
    def find(cls, supplier_id):
        row = cursor.execute("SELECT * FROM suppliers WHERE id = ?", (supplier_id,)).fetchone()
        if row:
            return cls(id=row[0], name=row[1], contact=row[2]) if row else None
        
    
    
