"""project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import main.views
from django.conf import settings
from django.conf.urls.static import static
import login.views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.main, name="main"),
    path('other/', main.views.other, name="other"),
    path('blog/<int:blog_id>/', main.views.detail, name="detail"),
    path('blog/news/', main.views.news, name="news"),
    path('blog/create/', main.views.create, name="create"),
    path('blog/delete/', main.views.delete, name="delete"),
    path('portfolio/', main.views.port, name="port"),
    path('login/', login.views.login, name="login"),
    path('signup/', login.views.signup, name="signup"),
    path('logout/', login.views.logout, name="logout"),
    path('like/<int:blog_id>/', main.views.like, name="like"),
    path('blog/edit/<int:blog_id>/', main.views.edit, name="edit"),
    path('blog/recreate/<int:blog_id>/', main.views.recreate, name="recreate"),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
