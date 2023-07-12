from django.test import SimpleTestCase
from django.urls import reverse
from .models import Snack
from django.contrib.auth.models import User
import random
import string

class SnackPageTests(SimpleTestCase):
    databases = ['default']
    def setUp(self):
        username = ''.join(random.choices(string.ascii_lowercase, k=10))
        self.user = User.objects.create_user(username=username, password='testpass')
        self.snack = Snack.objects.create(name='Chips', purchaser=self.user, description='Delicious chips')

    def test_snack_list_page(self):
        response = self.client.get(reverse('snack_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_list.html')

    def test_snack_detail_page(self):
        url = reverse('snack_detail', args=[self.snack.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_detail.html')
