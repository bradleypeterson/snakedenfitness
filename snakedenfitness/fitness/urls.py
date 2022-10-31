from . import views
from django.urls import path

urlpatterns = [
    path('', views.fitness_home, name="fitness_home"),
    path('trainer/', views.trainer_home, name="trainer_home"),
    path('workout_form/', views.workout_form, name="workout_form"),
    path('request_trainer/', views.request_trainer, name="request_trainer"),
]