from django.urls import path

from myapp2_2 import views

app_name = 'seminar_app'

urlpatterns = [
    path('author/', views.author, name='author'),
    path('post/', views.post, name='post'),
    path('category/', views.category, name='category')
]
