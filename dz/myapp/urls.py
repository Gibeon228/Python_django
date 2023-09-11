from django.urls import path
from . import views
from .views import client_orders

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/<int:client_id>', client_orders, name='client_orders'),
]
