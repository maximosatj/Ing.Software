from app.repositories.CRUD_repository import Read, Update, Create, Delete
from app import db
from app.models.product_brand import ProductBrand

# Base repository for all the other ones. Aplying DRY and IoC principle
class BaseRepository(Read, Update, Create, Delete):
    def __init__(self, model):
        self.__model = model
    
    def find_by_id(self, id):
        return db.session.query(self.__model).get(id)
    
    def find_all(self):
        return db.session.query(self.__model).all()
    
    def create(self, entity: ProductBrand):
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def delete(self, id: str):
        try:
            id = int(id)
        except ValueError:
            raise ValueError("id must be an integer")

        existing_entity = db.session.query(self.__model).get(id)
        if existing_entity is not None:
            db.session.delete(existing_entity)
            db.session.commit()
            return {"message": "Successfully deleted"}
        else:
            return {"message": "Not found"}