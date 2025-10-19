import re
from datetime import datetime

#  Validation utilities

def validate_email(email: str) -> bool:
    """Validate supplier email format."""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def validate_price(price: str) -> float:
    """Ensure price is a valid positive float."""
    try:
        value = float(price)
        if value < 0:
            raise ValueError
        return value
    except ValueError:
        raise ValueError("Invalid price: must be a positive number.")


def validate_quantity(quantity: str) -> int:
    """Ensure quantity is a valid integer."""
    try:
        value = int(quantity)
        if value < 0:
            raise ValueError
        return value
    except ValueError:
        raise ValueError("Invalid quantity: must be a non-negative integer.")


def validate_non_empty(text: str, field_name: str):
    """Ensure required text fields are not empty."""
    if not text.strip():
        raise ValueError(f"{field_name} cannot be empty.")
    return text.strip()


#  Duplicate checking

def check_duplicate_product(name, all_products):
    """Check if a product with the same name already exists."""
    for product in all_products:
        if product.name.lower() == name.lower():
            raise ValueError(f"A product named '{name}' already exists.")


# Display helpers

def print_table(data, headers):
    """Display records in a clean table format."""
    if not data:
        print("\n  No records found.\n")
        return

    col_widths = [len(str(header)) for header in headers]

    for row in data:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    # Header
    header_row = " | ".join(str(h).ljust(col_widths[i]) for i, h in enumerate(headers))
    divider = "-+-".join("-" * col_widths[i] for i in range(len(headers)))
    print("\n" + header_row)
    print(divider)

    # Rows
    for row in data:
        print(" | ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)))
    print()


# Date utilities (for sales reporting)

def get_month_start_end(month: int, year: int):
    """Return the start and end dates for a given month and year."""
    if not 1 <= month <= 12:
        raise ValueError("Month must be between 1 and 12.")
    start = datetime(year, month, 1)
    if month == 12:
        end = datetime(year + 1, 1, 1)
    else:
        end = datetime(year, month + 1, 1)
    return start, end


def format_currency(value):
    """Format currency neatly for CLI."""
    return f"Ksh {value:,.2f}"
