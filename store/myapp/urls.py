from django.urls import path
from .views import RegisterAPIView, UserAPIView, ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, OrderListCreateAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('users/', UserAPIView.as_view(), name='users'),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
]
