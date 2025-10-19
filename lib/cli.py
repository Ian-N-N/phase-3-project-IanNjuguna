import click
from lib.models.supplier import Supplier
from lib.models.product import Product
from lib.models.sale import Sale
from lib.helpers import print_table


@click.group()
def main_menu():
    """Inventory & Sales Management CLI"""
    click.echo("\n📦 Welcome to the Inventory & Sales Management System!")
    click.echo("Use one of the following commands to get started:\n")
    click.echo("  ➤ add-supplier      Add a new supplier")
    click.echo("  ➤ add-product       Add a new product")
    click.echo("  ➤ view-products     View all available products")
    click.echo("  ➤ record-sale       Record a product sale")
    click.echo("  ➤ monthly-report    View monthly sales summary\n")
    click.echo("Example usage: python main.py view-products\n")


# -------------------------------
# SUPPLIER COMMANDS
# -------------------------------
@main_menu.command()
@click.option('--name', prompt="Supplier Name")
@click.option('--contact', prompt="Supplier Contact")
def add_supplier(name, contact):
    """Add a new supplier."""
    supplier = Supplier(name=name, contact=contact)
    supplier.save()
    click.echo(f"✅ Supplier '{name}' added successfully!")


# -------------------------------
# PRODUCT COMMANDS
# -------------------------------
@main_menu.command()
@click.option('--name', prompt="Product Name")
@click.option('--price', prompt="Product Price", type=float)
@click.option('--stock', prompt="Initial Stock", type=int)
@click.option('--supplier_id', prompt="Supplier ID", type=int)
def add_product(name, price, stock, supplier_id):
    """Add a new product."""
    product = Product(name=name, price=price, stock=stock, supplier_id=supplier_id)
    product.save()
    click.echo(f"✅ Product '{name}' added successfully!")


@main_menu.command()
def view_products():
    """Display all available products."""
    products = Product.all()
    if not products:
        click.echo("⚠️  No products found.")
        return

    table_data = [
        (p.id, p.name, getattr(p, "category", "N/A"), p.stock, f"Ksh {p.price:,.2f}")
        for p in products
    ]
    print_table(table_data, headers=["ID", "Name", "Category", "Stock", "Price"])


# -------------------------------
# SALES COMMANDS
# -------------------------------
@main_menu.command()
@click.option('--product_id', prompt="Product ID", type=int)
@click.option('--quantity', prompt="Quantity Sold", type=int)
def record_sale(product_id, quantity):
    """Record a new sale and update stock."""
    try:
        sale = Sale(product_id=product_id, quantity=quantity)
        sale.record_sale()
        click.echo("✅ Sale recorded successfully and stock updated!")
    except ValueError as e:
        click.echo(f"❌ Error: {e}")


# -------------------------------
# REPORT COMMANDS
# -------------------------------
@main_menu.command()
@click.option('--month', prompt="Enter month (1-12)", type=int)
def monthly_report(month):
    """Generate a monthly sales report."""
    report = Sale.monthly_report(month)
    if not report:
        click.echo("⚠️  No sales data found for that month.")
        return

    click.echo("\n📊 Monthly Sales Report:")
    table_data = [
        (item["product"], item["total_sold"], f"Ksh {item['total_revenue']:,.2f}")
        for item in report
    ]
    print_table(table_data, headers=["Product", "Units Sold", "Total Revenue"])
