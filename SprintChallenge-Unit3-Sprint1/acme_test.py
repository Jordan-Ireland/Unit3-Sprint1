import unittest
from acme import Product
from acme_report import generate_products, possible_adj, possible_noun


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
        self.assertEqual(prod.weight, 20)
        self.assertEqual(prod.flammability, 0.5)

    def test_new_products(self):
        prod = Product("name", price=4, weight=10, flammability=1)
        self.assertEqual(prod.stealability(), 'Not so stealable...')
        self.assertEqual(prod.explode(), '...boom!')


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        products = generate_products()
        self.assertEqual(len(products), 30)
        for product in products:
            split = product.name.split()
            self.assertIn(split[0], possible_adj)
            self.assertIn(split[1], possible_noun)


if __name__ == '__main__':
    unittest.main()
