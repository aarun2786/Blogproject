"""
URL configuration for blogproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from app.views import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",HomeView.as_view(),name='home'),
    path("profile/user/",login_required(ProfileView.as_view()),name='profile_view'),
    path('categories/<str:tag>',login_required(TagView.as_view()),name="tag"),
    path('post/<str:slug>',login_required(PostDetailView.as_view()),name="post_view"),
    path('sign-up/',SignUpView.as_view(),name='signup'),
    path('login/',Loginview.as_view(),name='login'),
    path('logout/', login_required(Logoutview.as_view()),name="logout"),
    path('create-post/', login_required(PostCreateView.as_view()),name="create-post"),
    
    
    path('summernote/', include('django_summernote.urls')),
    
    
]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
