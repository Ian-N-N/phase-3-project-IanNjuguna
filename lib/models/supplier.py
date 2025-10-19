from lib.database import get_connection

class Supplier:
    def __init__(self, name, contact, id=None):
        self.id = id
        self.name = name
        self.contact = contact

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO suppliers (name, contact) VALUES (?, ?)",
            (self.name, self.contact)
        )
        conn.commit()
        conn.close()

    @classmethod
    def all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM suppliers")
        rows = cursor.fetchall()
        conn.close()
        return [cls(id=row["id"], name=row["name"], contact=row["contact"]) for row in rows]
