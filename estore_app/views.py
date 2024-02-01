from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status, generics, viewsets, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
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

#class OrderViewSet(viewsets.ModelViewSet): # представляет получение списка заказов, получение всех возможных деталей заказа, update
#    queryset = Order.objects.all()
#    serializer_class = OrderSerializer


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

class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) #  создание нового заказа через API-точку только для аутентифицированных пользователей и автоматически устанавливает пользователя, создавшего заказ,





class UserOrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class AdminOrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Order.objects.all()


