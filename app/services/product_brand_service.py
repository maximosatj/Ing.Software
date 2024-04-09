from app.repositories.product_brand_repository import ProductBrandRepository

class ProductBrandService:
    def __init__(self):
        self.__repo=ProductBrandRepository()

    def find_by_id(self, product_brand_id):
        return self.__repo.find_by_id(product_brand_id)
    
    def find_by_name(self, name):
        return self.__repo.find_by_name(name)
    
    def update(self, product_brand, product_brand_id):
        return self.__repo.update(product_brand, product_brand_id)
    
    def delete(self, product_brand_id):
        return self.__repo.delete(product_brand_id)
    
    def create(self, product_brand):
        return self.__repo.create(product_brand)