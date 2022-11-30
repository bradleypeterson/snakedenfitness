from . import views
from django.urls import path

urlpatterns = [
    path('rooms/', views.rooms, name='rooms'),
    path('<slug:slug>/', views.room, name='room'),
    path('rooms/groupForm/', views.groupForm, name='groupForm'),
    path('rooms/editGroup/<str:name>', views.edit_group, name='edit_group'),
    path('rooms/acceptInvite/<str:group>/<int:id>', views.accept_invite, name='acceptInvite'),
    path('rooms/declineInvite/<int:id>', views.decline_invite, name='declineInvite'),
    path('rooms/guides', views.guides, name='guides'),
]

