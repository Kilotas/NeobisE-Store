from django.contrib import admin
from .models import Product, Order, Comment, Review
# Register your models here.
admin.site.register(Product)

admin.site.register(Order)
admin.site.register(Comment)

admin.site.register(Review)

