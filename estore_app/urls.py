from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


#router = DefaultRouter()
#router.register(r'orders', OrderViewSet, basename='orders')


urlpatterns = [
    #path('', include(router.urls)),
    path('api/orders/create/', views.OrderCreateView.as_view(), name='order-create'),
    path('api/orders/user/', views.UserOrderListView.as_view(), name='user-orders'),
    path('api/orders/admin/', views.AdminOrderListView.as_view(), name='admin-orders'),
    path('api/products/', views.ProductListView.as_view(), name='product-list'),
    path('api/products/<int:pk>', views.ProductDetailView.as_view(), name='product'),
    path('api/category/<str:category>', views.ProductCategoryView.as_view(), name='category'),
    path('api/v1/register/', views.RegisterView.as_view(), name='register'),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
]




