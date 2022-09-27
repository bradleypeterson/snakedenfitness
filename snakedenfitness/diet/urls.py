from . import views
from django.urls import path

urlpatterns = [
    path('', views.diet_home, name="diet_home"),
    path('dietitian/', views.dietitian_home, name="dietitian_home"),
]
