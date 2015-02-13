from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from .views import SignInAndSignUp


class PageOpenTestCase(TestCase):
    def test_home_page_exists(self):
        url = reverse('home')
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)

    def test_home_page_resolves(self):
        url = reverse('home')
        found = resolve(url)
        self.assertEqual(found.func.__name__,
                         SignInAndSignUp.as_view().__name__)

    def test_about_page_exists(self):
        url = reverse('about')
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
