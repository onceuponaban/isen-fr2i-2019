from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('play/', views.play, name='play'),
    path('ranking/', views.ranking, name='ranking'),
    path('signin/', views.signin, name='signin'),
    path('modification/',views.modif, name='modification'),
]