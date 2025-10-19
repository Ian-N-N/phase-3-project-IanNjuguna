from lib.database import initialize_database
from lib.cli import main_menu

if __name__ == "__main__":
    initialize_database()
    print(" Welcome to Tech Store Management System")
    print("Use the commands below to manage suppliers, products, and sales.\n")
    main_menu()
