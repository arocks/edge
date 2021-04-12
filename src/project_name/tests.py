from django.test import TestCase
from django.urls import reverse


class PageOpenTestCase(TestCase):
    def test_home_page_exists(self):
        url = reverse("site_home")
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
