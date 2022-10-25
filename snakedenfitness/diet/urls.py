from . import views
from django.urls import path

urlpatterns = [
    path('', views.diet_home, name="diet_home"),
    path('dietitian/', views.dietitian_home, name="dietitian_home"),
    path('meal_form/', views.meal_form, name="meal_form"),
    path('request_dietician/', views.request_dietician, name="request_dietician"),
]
