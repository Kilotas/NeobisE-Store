from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, Order
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password')) # пароль принимается в виде строки и возвращается в хеш
        return super(UserSerializer, self).create(validated_data) # вызывает родительский метод create для завершеия процесса создания объекта

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

