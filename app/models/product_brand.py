from app.config.database import db
from sqlalchemy.ext.hybrid import hybrid_property
from dataclasses import dataclass

@dataclass
class ProductBrand (db.Model):
    tablename__ = 'product_category'
    id = db.Column("id",db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("name",db.String(50))
    description = db.Column("price",db.String(100))
    

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