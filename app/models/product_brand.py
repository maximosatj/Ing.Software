from app import db
from dataclasses import dataclass
from sqlalchemy import Column

@dataclass
class ProductBrand (db.Model):
    tablename__ = 'product_brand'
    id = Column(db.Integer, primary_key=True, autoincrement=True)
    name  = Column(db.String(50))
    description  = Column(db.String(50))

def __init__(self, name, description):
    self.name = name
    self.description = description