from . import views
from django.urls import path

urlpatterns = [
    path('', views.community_home, name="community_home"),
    #path('<str:room_name>/', views.room, name='room'),
    path('rooms/', views.rooms, name='rooms'),
    path('<slug:slug>/', views.room, name='room'),
    path('rooms/groupForm/', views.groupForm, name='groupForm'),
]

