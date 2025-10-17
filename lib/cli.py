import click
from lib.models.supplier import Supplier
from lib.models.product import Product
from lib.models.sale import Sale

@click.group()
def main_menu():
    """Inventory & Sales Management CLI"""
    pass

@main_menu.command()
@click.option('--name', prompt="Supplier Name")
@click.option('--contact', prompt="Supplier Contact")
def add_supplier(name, contact):
    supplier = Supplier(name=name, contact=contact)
    supplier.save()
    click.echo(f" Supplier '{name}' added successfully!")

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
@click.option('--product_id', prompt="Product ID", type=int)
@click.option('--quantity', prompt="Quantity Sold", type=int)
def record_sale(product_id, quantity):
    try:
        sale = Sale(product_id=product_id, quantity=quantity)
        sale.record_sale()
        click.echo(" Sale recorded successfully and stock updated!")
    except ValueError as e:
        click.echo(f" Error: {e}")

@main_menu.command()
@click.option('--month', prompt="Enter month (1-12)", type=int)
def monthly_report(month):
    report = Sale.monthly_report(month)
    click.echo("\n Monthly Sales Report:")
    for item in report:
        click.echo(f"{item['product']} - Sold: {item['total_sold']} | Revenue: ${item['total_revenue']}")

@main_menu.command()
def view_products():
    products = Product.all()
    click.echo("\n Products in Inventory:")
    for p in products:
        click.echo(f"[{p.id}] {p.name} | Ksh {p.price} | Stock: {p.stock} | Supplier ID: {p.supplier_id}")
