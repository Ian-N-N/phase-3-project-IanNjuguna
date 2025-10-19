import click
from lib.models.supplier import Supplier
from lib.models.product import Product
from lib.models.sale import Sale
from lib.helpers import print_table

@click.group()
def main_menu():
    """Tech Store Inventory & Sales CLI"""
    click.echo(" Welcome to Tech Store Management System")
    click.echo("Use the commands below to manage suppliers, products, and sales.\n")

# ---------------------- SUPPLIERS ----------------------
@main_menu.command()
@click.option('--name', prompt="Supplier Name")
@click.option('--contact', prompt="Supplier Contact")
def add_supplier(name, contact):
    supplier = Supplier(name=name, contact=contact)
    supplier.save()
    click.echo(f" Supplier '{name}' added successfully!")

@main_menu.command()
def view_suppliers():
    suppliers = Supplier.all()
    if not suppliers:
        click.echo("  No suppliers found.")
        return
    data = [(s.id, s.name, s.contact) for s in suppliers]
    print_table(data, headers=["ID", "Name", "Contact"])

# ---------------------- PRODUCTS ----------------------
@main_menu.command()
@click.option('--name', prompt="Product Name")
@click.option('--price', prompt="Product Price", type=float)
@click.option('--stock', prompt="Initial Stock", type=int)
@click.option('--supplier_id', prompt="Supplier ID", type=int)
def add_product(name, price, stock, supplier_id):
    product = Product(name=name, price=price, stock=stock, supplier_id=supplier_id)
    product.save()
    click.echo(f" Product '{name}' added successfully!")

@main_menu.command()
def view_products():
    products = Product.all()
    if not products:
        click.echo("  No products found.")
        return
    data = [(p.id, p.name, f"Ksh {p.price:,.2f}", p.stock, p.supplier_id) for p in products]
    print_table(data, headers=["ID", "Name", "Price", "Stock", "Supplier ID"])

# ---------------------- SALES ----------------------
@main_menu.command()
@click.option('--product_id', prompt="Product ID", type=int)
@click.option('--quantity', prompt="Quantity Sold", type=int)
def record_sale(product_id, quantity):
    try:
        sale = Sale(product_id=product_id, quantity=quantity)
        sale.record_sale()
        click.echo(" Sale recorded and stock updated successfully!")
    except ValueError as e:
        click.echo(f" Error: {e}")

@main_menu.command()
@click.option('--month', prompt="Enter month (1-12)", type=int)
def monthly_report(month):
    report = Sale.monthly_report(month)
    if not report:
        click.echo("  No sales for this month.")
        return
    data = [(r['product'], r['total_sold'], f"Ksh {r['total_revenue']:,.2f}") for r in report]
    print_table(data, headers=["Product", "Total Sold", "Total Revenue"])
