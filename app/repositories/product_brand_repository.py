from app.models.product_brand import *
from app import db
from app.repositories.base_repository import BaseRepository
from app.config.database import db

class ProductBrandRepository(BaseRepository):
    def _init_(self):
        super()._init_(ProductBrand)
        self.__model = ProductBrand

    def update(self, entity: db.Model, id: int):
        try:
            existing_entity = db.session.query(self.__model).get(id)
            if existing_entity:
                existing_entity.name = entity.name
                existing_entity.description = entity.description
                db.session.commit()
                return existing_entity
            else:
                return None
        except Exception as e:
            db.session.rollback()
            raise e