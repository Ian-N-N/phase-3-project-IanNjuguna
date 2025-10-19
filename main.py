from lib.database import create_tables
from lib.cli import main_menu

if __name__ == "__main__":
    # Initialize the database and tables
    create_tables()
    print(" Database initialized successfully!")

    # Start the CLI
    main_menu()
