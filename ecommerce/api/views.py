from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from django.contrib.auth.models import User
from .serializers import ProductSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
