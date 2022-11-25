"""
Home app test for Views
"""
from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    """ Unit test for Home app Views """

    def test_home_is_resolved(self):
        """ Test home page renders correct page """

        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_about_is_resolved(self):
        """ Test about page renders correct page """

        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')

    def test_contact_is_resolved(self):
        """ Test contact page renders correct page """

        url = reverse('contact')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
