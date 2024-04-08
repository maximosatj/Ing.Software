from flask import Blueprint, jsonify, request
from app.services.product_brand_service import ProductBrandService
from app.mapping.product_brand_schema import ProductBrandSchema

schema = ProductBrandSchema()
product_brand=Blueprint('product_brand',__name__)

@product_brand.route('/product_brand/<string:product_brand_id>', methods=['GET'])
def get_product_brand(product_brand_id):
    product_brand = ProductBrandService().find_by_id(product_brand_id)
    return jsonify(schema.dump(product_brand)), 200

@product_brand.route('/product_brand/name/<string:name>', methods=['GET'])
def get_product_brand_by_name(name):
    product_brand = ProductBrandService().find_by_name(name)
    return jsonify(schema.dump(product_brand)), 200

@product_brand.route('/product_brand/create', methods=['POST'])
def create_product_brand():
    product_brand = ProductBrandService().create(schema.load(request.json))
    return {"product_brand":schema.dump(product_brand)}, 201


@product_brand.route('/product_brand/update/<string:product_brand_id>', methods=['PUT'])
def update_product_brand(product_brand_id):
    updated_product_brand = ProductBrandService().update(schema.load(request.json), product_brand_id)
    return jsonify(schema.dump(updated_product_brand)), 200

@product_brand.route('/product_brand/delete/<string:product_brand_id>', methods=['DELETE'])
def delete_product_brand(product_brand_id):
    return jsonify(ProductBrandService().delete(product_brand_id)), 200