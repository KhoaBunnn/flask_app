from models.product import Product
from database.db import db

def get_all_products():
    return Product.query.all()

def get_product_by_id(product_id):
    return Product.query.get(product_id)

def create_product(data):
    new_product = Product(name=data['name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return new_product

def update_product(product_id, data):
    product = Product.query.get(product_id)
    if not product:
        return None
    product.name = data['name']
    product.price = data['price']
    db.session.commit()
    return product

def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return False
    db.session.delete(product)
    db.session.commit()
    return True

def add_product(data):
    product = Product(name=data['name'], price=float(data['price']))
    db.session.add(product)
    db.session.commit()
    return product