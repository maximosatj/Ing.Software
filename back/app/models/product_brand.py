from app.config.database import db
from sqlalchemy.ext.hybrid import hybrid_property

class ProductBrand (db.Model):
    __tablename__ = 'product_category'
    __id = db.Column("id",db.Integer, primary_key=True, autoincrement=True)
    __name = db.Column("name",db.String(50))
    __description = db.Column("price",db.String(100))
    
    def __init__(self, name, description, id=None):
        self.__id = id
        self.__name = name
        self.__description = description

    @property
    def id(self)->int:
        return self.__id
    
    @id.setter
    def id(self, id:int):
        self.__id = id

    @hybrid_property
    def name(self)->str:
        return self.__name
    
    @name.setter
    def name(self, name:str):
        self.__name = name

    @hybrid_property
    def description(self)->str:
        return self.__description
    
    @description.setter
    def description(self, description:str):
        self.__description = description

    def __repr__(self):
        return f"ProductBrand (id_product_brand{self.__id}, {self.__name}, {self.__description})"
    
    def __eq__(self, o:object) -> bool:
        return self.__id==o.id and self.__name==o.name