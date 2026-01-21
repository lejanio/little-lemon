from django.urls import path, include
from .views import sayHello, index, MenuItemsView, SingleMenuItemView, BookingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', BookingViewSet, basename='booking')

urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuItemsView.as_view(), name='menu_item_view'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='single_menu_item_view'),
    
    path('booking/', include(router.urls)),
    path('hello/', sayHello, name='sayHello'),
    # path('menu/', MenuView.as_view(), name='menu_view'),
]