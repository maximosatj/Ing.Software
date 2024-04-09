import unittest
from app import create_app, db
from app.models.product_brand import ProductBrand
from app.services.product_brand_service import ProductBrandService



class ProductBrandTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.service = ProductBrandService()


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_product_brand_create(self):
        
        product_brand = ProductBrand(name="Test Brand", description="Test Description")
        self.service.create(product_brand)
        self.assertIsNotNone(product_brand.id)
        self.assertEqual(product_brand.name, "Test Brand")
        self.assertEqual(product_brand.description, "Test Description")
    

    def test_product_brand_update(self):
        product_brand = ProductBrand(name="Test Brand", description="Test Description")
        product_brand.name = "Updated Brand"
        product_brand.description = "Updated Description"
        self.service.update(product_brand, product_brand.id)
        self.assertEqual(product_brand.name, 'Updated Brand')
        self.assertEqual(product_brand.description, 'Updated Description')

    def test_product_brand_delete(self):
        self.service = ProductBrandService() 
        product_brand = ProductBrand(name='Test Brand', description='Test Description')
        self.service.create(product_brand)
        self.service.delete(product_brand.id)
        self.assertIsNone(ProductBrand.query.get(product_brand.id))
        

if __name__ == '__main__':
    unittest.main()
