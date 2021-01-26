from django.test import TestCase

# Create your tests here.

from django.core.urlresolvers import reverse
from django.urls import resolve
from .views import sign_in_page

class SignUpTests(TestCase):
    def test_sign_in_status_code(self):
        url = reverse('sign_in')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_signup_url_resolves_sign_in_view(self):
        view = resolve('/sign_in/')
        self.assertEquals(view.func, sign_in_page)
