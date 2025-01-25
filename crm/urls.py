from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # صفحه اصلی
    path('customers/', views.customer_list, name='customer_list'),  # لیست مشتری‌ها
    path('customer/<int:pk>/', views.customer_detail, name='customer_detail'),  # جزئیات مشتری
]