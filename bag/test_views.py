"""
Home app test for Views
"""
from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    """ Unit test for bag app Views """

    def test_bag_is_resolved(self):
        """ Test bag page renders correct page """

        url = reverse('view_bag')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
