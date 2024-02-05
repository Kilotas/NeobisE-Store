from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status, generics, viewsets, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import UserSerializer, OrderSerializer, ProductSerializer, CommentSerializer, ReviewSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Order, Product, Comment, Review
from rest_framework.decorators import api_view
from django.db.models import Sum, F
from decimal import Decimal

# Реализация регистрации для пользователя
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) # выводит исключение если валидация не проходит успешно
        self.perform_create(serializer) # Сохранение оъекта пользователя в базе данных
        headers = self.get_success_headers(serializer.data) # Получет заголовки для ответа
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers) # возвращает http ответ с данными созданого пользователя

#class OrderViewSet(viewsets.ModelViewSet): # представляет получение списка заказов, получение всех возможных деталей заказа, update
#    queryset = Order.objects.all()
#    serializer_class = OrderSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# получение конкретной информации о продукте по id
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Возвращает список продуктов относящихся к определенной категории
class ProductCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Product.objects.filter(category=category)
        # Create your views here.

# Создание заказа
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        #  создание нового заказа через API-точку только для аутентифицированных пользователей и автоматически устанавливает пользователя, создавшего заказ,
 #       instance.save()



# Возвращает список заказов
class UserOrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
# Возвращает только заказы, которые принадлежат текущему пользователю
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

# Если вход был под аккаунтом администратора, возвращает весь список объектов
class AdminOrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Order.objects.all()
# Возвращает список продуктов
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

@api_view(['GET']) # получаем средний рейтинг определенного товара и общее количество отзывов
def product_ratings(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    reviews = product.reviews.all()
    total_reviews = len(reviews)
    if total_reviews == 0:
        average_rating = 0
    else:
        total_rating = sum(review.rating for review in reviews)
        average_rating = total_rating / total_reviews

    return Response({"average_rating": average_rating, "total_reviews": total_reviews})





@api_view(['GET'])
def user_total_order_price(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        orders = Order.objects.filter(user=user)

        total_order_price = Decimal('0')  # Используйте Decimal для инициализации total_order_price

        for order in orders:
            total_order_price += order.total_price

        discount_percentage = Decimal('0')  # Используйте Decimal для инициализации discount_percentage

        # Применяем скидку в зависимости от суммы заказа
        if total_order_price > Decimal('20000'):
            discount_percentage = Decimal('0.15')
        elif total_order_price > Decimal('10000'):
            discount_percentage = Decimal('0.10')

        discounted_price = total_order_price * (Decimal('1') - discount_percentage)

        return Response({
            "user_id": user_id,
            "total_order_price": total_order_price,
            "discount_percentage": discount_percentage * Decimal('100'),
            "discounted_price": discounted_price
        })

    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

