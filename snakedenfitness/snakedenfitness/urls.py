"""snakedenfitness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as authViews
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from users import views as userViews
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('diet/', include('diet.urls')),
    path('fitness/', include('fitness.urls')),
    path('community/', include('community.urls')),
    path('register/', userViews.register, name='register'),
    path('login/', authViews.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', authViews.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', userViews.profile, name='profile'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
# urlpatterns = patterns('',
#    url(r'^create_user/$',(CreateView.as_view(model=CustomUser, get_success_url =lambda: reverse('create_user'),
#     form_class=UserCreationForm, template_name="create_user.html")), name='create_user'),
# )
