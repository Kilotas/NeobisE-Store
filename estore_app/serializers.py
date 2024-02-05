from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, Order, Comment, Review
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password')) # пароль принимается в виде строки и возвращается в хеш
        return super(UserSerializer, self).create(validated_data) # вызывает родительский метод create для завершеия процесса создания объекта

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

class OrderSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField()
    class Meta:
        model = Order
        fields = ['id', 'products', 'created_at', 'shipping_address', 'quantity']
        read_only_fields = ('is_completed', 'total_price')

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        quantity = validated_data.pop('quantity')

        # Создаем новый экземпляр Order, используя оставшиеся данные из validated_data
        order = Order.objects.create(**validated_data)

        for product in products_data:
            order.products.add(product)


        order.quantity = quantity
        order.calculate_total_price()

        # Рассчитываем и устанавливаем общую стоимость заказа
        total_price = order.calculate_total_price()
        order.total_price = total_price
        order.save()

        # Расчитываем и устанавливаем общую стоимость заказа
        return order








#class ProductSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Product
#        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

#будет включать в себя все поля модели Product, а также сериализовать связанные комментарии и отзывы, используя соответствующие вложенные сериализаторы.
class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True) # указывает что у продукта может быть несколько комментариев , и что это поле только для чтения, данные будут выводиться, но не приниматься
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


