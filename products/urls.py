from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.home, name='home'),
    path('checkout/', views.checkout, name='checkout'),
    path('products/', views.products, name='products'),
]