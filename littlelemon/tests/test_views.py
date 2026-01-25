from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemsSerializer
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="Pizza", price=40, inventory=50)
        MenuItem.objects.create(title="Minetrone", price=30, inventory=70)
        
    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        items = MenuItem.objects.all()
        serializer = MenuItemsSerializer(items, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        
        