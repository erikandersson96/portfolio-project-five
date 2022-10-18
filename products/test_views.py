"""
Products app test for Views
"""
from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    """ Unit test for products app Views """

    def test_all_products_is_resolved(self):
        """ Test products page renders correct page """

        url = reverse('products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_detail_is_resolved(self):
        """ Test products page renders correct page """

        url = reverse('products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
