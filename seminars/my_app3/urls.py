from django.urls import path

from . import views

app_name = 'seminar_app'

urlpatterns = [
    path('', views.HomeViews.as_view(), name='main_home'),
    path('about/', views.AboutViews.as_view(), name='about'),
    path('heads_game/<int:count>', views.HeadsGame.as_view(), name='heads_game'),
    path('dice_game/<int:count>', views.DiceGame.as_view(), name='dice_game'),
    path('articles/<int:id_author>', views.AllArticlesViews.as_view(), name='articles'),
]
