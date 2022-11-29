from django.test import TestCase
from django.contrib.auth.models import User


class TestView(TestCase):
    """ Inherits Testcase for all function tests """

    def test_basket_page_opens(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')