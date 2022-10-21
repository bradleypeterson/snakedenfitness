from . import views
from django.urls import path

urlpatterns = [
    path('', views.community_home, name="community_home"),
    path('newPost/', views.new_post, name="new_post"),
    path('groups/', views.groups, name="groups"),
    path('edit_groups/', views.edit_groups, name="edit_groups"),
]

