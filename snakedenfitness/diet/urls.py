from . import views
from django.urls import path

urlpatterns = [
    path('', views.diet_home, name="diet_home"),
    path('dietitian/', views.dietitian_home, name="dietitian_home"),
    path('meal_form/', views.meal_form, name="meal_form"),
    path('meal_log/', views.user_meal_data, name="user_meal_data"),
    path('trainer_meal_log/', views.trainer_meal_data, name="trainer_meal_data"),

]
