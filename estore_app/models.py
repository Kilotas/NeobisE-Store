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

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_address = models.TextField()
    is_completed = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

#    def save(self, *args, **kwargs):
#        self.total_price = sum(product.price * self.quantity for product in self.products.all())

#        super().save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(verbose_name='Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.product.name}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(verbose_name='Текст отзыва')
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name='Рейтинг')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.product.name}"

