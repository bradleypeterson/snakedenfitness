from . import views
from django.urls import path

urlpatterns = [
    path('', views.diet_home, name="diet_home"),
    path('dietician/', views.dietician_home, name="dietician_home"),
]
