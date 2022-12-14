from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('rooms/', views.rooms, name='rooms'),
    path('<slug:slug>/', views.room, name='room'),
    path('rooms/groupForm/', views.groupForm, name='groupForm'),
    path('rooms/editGroup/<str:name>', views.edit_group, name='edit_group'),
    path('rooms/acceptInvite/<str:group>/<int:id>', views.accept_invite, name='acceptInvite'),
    path('rooms/declineInvite/<int:id>', views.decline_invite, name='declineInvite'),
    path('rooms/guides', views.guides, name='guides'),
    path('rooms/displayGuides', views.displayGuides, name='displayGuides'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
    # urlpatterns += static("/")
    #urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)