from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product, Category
from .forms import ProductForm


class TestView(TestCase):
    """ Inherits Testcase for all function tests """

    def test_products_page_opens(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')


class TestForms(TestCase):
    """ Inherits Testcase for all function tests """

    def title_is_required(self):
        """ Test to see fi the title of a new product is requried """
        form = ProductForm({title: ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def price_is_required(self):
        """ Test to see fi the title of a new product is requried """
        form = ProductForm({price: ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')


class TestProductModels(TestCase):
    """ Inherits Testcase for all function tests """

    def test_product_title(self):
        """ Tests a product can be create and the title is returned """

        product = Product.objects.create(title="Test Product", price=1)
        self.assertEqual(product.title, "Test Product")
