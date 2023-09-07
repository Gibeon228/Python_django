from django.urls import path

from myapp2 import views

app_name = 'seminar_app'

urlpatterns = [
    path('', views.index, ),
    path('last/', views.last_game, name='last_games'),
]
