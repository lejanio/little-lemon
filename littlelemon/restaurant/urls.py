from django.urls import path
from .views import sayHello, index

urlpatterns = [
    path('', index, name='index'),
    path('hello/', sayHello, name='sayHello'),
]