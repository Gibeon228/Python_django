from django.urls import path
from . import views
from .views import client_orders, OrderProductsView, add_product, upload_image

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/<int:client_id>', client_orders, name='client_orders'),
    path('order_list', OrderProductsView.get_context_data, name='get_context_data'),
    path('product/', add_product, name='add_product'),
    path('upload/', upload_image, name='upload_image'),
]
