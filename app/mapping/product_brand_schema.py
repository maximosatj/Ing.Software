from app.models.product_brand import ProductBrand
from marshmallow import Schema, fields, post_load

class ProductBrandSchema(Schema):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    id = fields.Integer(attribute='id', data_key='id')
    name = fields.String(attribute='name', data_key='name')
    description = fields.String(attribute='description', data_key='description')

    @post_load
    def make_product_brand(self, data, **kwargs):
        return ProductBrand(**data)