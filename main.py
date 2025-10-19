from lib.cli import main_menu
from lib.models import Base, engine

def initialize_database():
    """Create all database tables."""
    from lib.models.supplier import Supplier
    from lib.models.product import Product
    from lib.models.sale import Sale

    Base.metadata.create_all(engine)
    print(" Database initialized successfully!")


if __name__ == "__main__":
    initialize_database()
    main_menu()
