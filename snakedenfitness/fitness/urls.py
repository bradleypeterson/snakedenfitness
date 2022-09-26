from . import views
from django.urls import path

urlpatterns = [
    path('', views.fitness_home, name="fitness_home"),
    path('trainer/', views.trainer_home, name="trainer_home")
]