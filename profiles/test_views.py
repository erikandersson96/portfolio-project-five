"""
Profiles app test for Views
"""
from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    """ Unit test for profiles app Views """

    def test_profile_is_resolved(self):
        """ Test profiles page renders correct page """

        url = reverse('profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
