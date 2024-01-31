from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import OrderViewSet, ProductDetailView, ProductListView, ProductCategoryView

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/products/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('api/category/<str:category>', ProductCategoryView.as_view(), name='category'),
    path('api/v1/register/', views.RegisterView.as_view(), name='register'),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
]




