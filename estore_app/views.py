from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from .serializers import UserSerializer, OrderSerializer, ProductSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Order, Product


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer) # Сохранение оъекта пользователя в базе данных
        headers = self.get_success_headers(serializer.data) # Получет заголовки для ответа
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers) # возвращает http ответ с данными созданого пользователя

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Product.objects.filter(category=category)
        # Create your views here.







