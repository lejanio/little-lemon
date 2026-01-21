from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuItemsSerializer, UserSerializer

def sayHello(request):
    return HttpResponse("Hello World!")

def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 
    
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemsSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemsSerializer
    
class BookingViewSet(viewsets.ViewSet):
    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many=True)
        return Response(serializer.data)



# Class defined using APIView
    
# class MenuView(APIView):
#     def get(self, request):
#         items = MenuItem.objects.all()
#         serializer = MenuItemsSerializer(items, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = MenuItemsSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data})