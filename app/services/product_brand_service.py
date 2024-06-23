from app.repositories.product_brand_repository import ProductBrandRepository
from app import cache

class ProductBrandService:
    def __init__(self):
        self.__repo=ProductBrandRepository()

    def find_by_id(self, product_brand_id):
        product_brand = cache.get(f'{product_brand_id}')	
        if product_brand is None:
            product_brand = self.__repo.find_by_id(product_brand_id)
            cache.set(f'{product_brand_id}', product_brand, timeout = 50)
        return product_brand
    
    def find_by_name(self, name):
        product_brand = cache.get(f'{name}')	
        if product_brand is None:
            product_brand = self.__repo.find_by_name(name)
            cache.set(f'{name}', product_brand, timeout = 50)
        return product_brand
        
    def find_all(self):
        product_brand = cache.get('product_brand')	
        if product_brand is None:
            product_brand = self.__repo.find_all()
            cache.set('product_brand', product_brand, timeout = 50)
        return product_brand

    def update(self, product_brand, product_brand_id):
        return self.__repo.update(product_brand, product_brand_id)
    
    def delete(self, product_brand_id):
        return self.__repo.delete(product_brand_id)
    
    def create(self, product_brand):
        new_product_brand = self.__repo.create(product_brand)
        cache.set(f'{new_product_brand.id}', new_product_brand, timeout = 50)
        return new_product_brand