from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase


class PageOpenTestCase(TestCase):
    def test_home_page_exists(self):
        url = reverse('home')
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)

    def test_about_page_exists(self):
        url = reverse('about')
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)


User = get_user_model()


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="dummy@example.com",
            password='password'
        )

    def test_profiles_created(self):
        self.assertIsNotNone(self.user.profile)

    def test_profiles_without_created(self):
        self.assertIsNotNone(self.user.profile)

    def test_edit_profile_success_view(self):
        self.client.login(username='dummy@example.com',
                          password='password')
        response = self.client.post(reverse('profiles:edit_self'), {
            'name': 'test user',
            'bio': 'bio',
        })
        self.assertRedirects(response, reverse('profiles:show_self'))

    def test_edit_profile_invalid_view(self):
        self.client.login(username='dummy@example.com',
                          password='password')
        response = self.client.post(reverse('profiles:edit_self'), {
            'name': '',
        })
        self.assertEqual(response.status_code, 200)
        message = list(response.context['messages'])[0]
        self.assertEqual(message.message, 'There was a problem with the form. Please check the details.')
