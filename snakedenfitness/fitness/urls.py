from . import views
from django.urls import path

urlpatterns = [
    path('', views.fitness_home, name="fitness_home"),
    path('trainer/', views.trainer_home, name="trainer_home"),
    path('workout_form/', views.workout_form, name="workout_form"),
    path('workout_log/', views.user_workout_data, name="user_workout_data"),
    path('trainer_workout_log/', views.trainer_workout_data, name="trainer_workout_data"),
]