"""
URL configuration for myblogs project.

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
from django.urls import path
from mriic import views
from django.conf import settings
from django.conf.urls.static import static
from mriic.views import home, blogPage
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('about/', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('', views.home, name = 'home'),
    path('blogPage/<int:Blog_id>/', views.blogPage, name='blogPage'),
    path('blog', views.blog, name = 'blog'),
    path('loginUser', views.loginUser, name='loginUser'),
    path('signupUser', views.signupUser, name='signupUser'),
    path('logOut', views.logOut, name='logOut'),
    path('findBlog', views.findBlog, name = 'findBlog'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
