from flask import Blueprint, jsonify, request
from controllers import product_controller as pc

api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/products', methods=['GET'])
def get_all():
    products = pc.get_all_products()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in products])

@api_bp.route('/products/<int:id>', methods=['GET'])
def get_one(id):
    product = pc.get_product_by_id(id)
    if product:
        return jsonify({'id': product.id, 'name': product.name, 'price': product.price})
    return jsonify({'error': 'Not found'}), 404

@api_bp.route('/products', methods=['POST'])
def create():
    data = request.json
    product = pc.create_product(data)
    return jsonify({'id': product.id}), 201

@api_bp.route('/products/<int:id>', methods=['PUT'])
def update(id):
    data = request.json
    product = pc.update_product(id, data)
    if not product:
        return jsonify({'error': 'Not found'}), 404
    return jsonify({'message': 'Updated'})

@api_bp.route('/products/<int:id>', methods=['DELETE'])
def delete(id):
    if pc.delete_product(id):
        return jsonify({'message': 'Deleted'})
    return jsonify({'error': 'Not found'}), 404