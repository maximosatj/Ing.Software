from abc import ABC, abstractmethod
from app.models.product_brand import ProductBrand



class Create(ABC):
    @abstractmethod
    def create(self, entity:ProductBrand):
        pass

class Read(ABC):
    @abstractmethod
    def find_by_id(self, id:int):
        pass

class Update(ABC):
    @abstractmethod
    def update(self, entity:ProductBrand, id:int):
        pass

class Delete(ABC):
    @abstractmethod
    def delete(self, entity:ProductBrand):
        pass