#model for suppliers
from lib.database import CONN, cursor

class Supplier:
    def __init__(self, name, contact, id=None):
        self.id = id
        self.name = name
        self.contact = contact
    
