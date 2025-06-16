from flask import Blueprint, render_template, request, redirect, url_for
from controllers.product_controller import get_all_products, get_product_by_id, update_product, delete_product, add_product

view_bp = Blueprint('view_bp', __name__)

@view_bp.route('/')
def index():
    products = get_all_products()
    return render_template('index.html', products=products)

@view_bp.route('/detail/<int:id>')
def detail(id):
    product = get_product_by_id(id)
    return render_template('detail.html', product=product)

@view_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    product = get_product_by_id(id)
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'price': request.form['price']
        }
        update_product(id, data)
        return redirect(url_for('view_bp.detail', id=id))
    return render_template('edit.html', product=product)

@view_bp.route('/delete/<int:id>')
def delete(id):
    delete_product(id)
    return redirect(url_for('view_bp.index'))

@view_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'price': request.form['price']
        }
        add_product(data)
        return redirect(url_for('view_bp.index'))
    return render_template('form.html', action="Add", product=None)
