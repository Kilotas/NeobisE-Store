from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
class Product(models.Model):
    TECH = 'техника'
    TOYS = 'игрушки'
    FOOD = 'еда'
    CHOCOLATE = 'chocolate'
    CATEGORY_CHOICES = [
        (TECH, 'Техника'),
        (TOYS, 'Игрушки'),
        (FOOD, 'Еда'),
        (CHOCOLATE, 'chocolate'),
    ]
    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем, который разместил заказ
    products = models.ManyToManyField('Product', related_name='orders')  # Связь с товарами в заказе
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания заказа
    # Другие поля, которые могут быть полезными для вашего приложения
    shipping_address = models.TextField()
    is_completed = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

    def save(self, *args, **kwargs):
        total_price = Decimal(0)
        for order_item in self.order_items.all():
            total_price += order_item.product.price * order_item.quantity
        self.total_price = total_price
        super().save(*args, **kwargs)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)






