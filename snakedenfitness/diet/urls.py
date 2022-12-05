from . import views
from django.urls import path

urlpatterns = [
    path('', views.diet_home, name="diet_home"),
    path('dietitian/', views.dietitian_home, name="dietitian_home"),
    path('meal_form/', views.meal_form, name="meal_form"),
    path('request_dietician/', views.request_dietician, name="request_dietician"),
    path('delete_meal/<int:id>', views.delete_meal, name="delete_meal"),
    path('edit_meal/<int:id>', views.edit_meal, name="edit_meal"),
    path('calories/', views.diet_home, name="calories"),
    path('meal_log/', views.user_meal_data, name="user_meal_data"),
    path('trainer_meal_log/', views.trainer_meal_data, name="trainer_meal_data"),
]