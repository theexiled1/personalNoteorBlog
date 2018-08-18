"""newblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from newblog import settings
from django.urls import path
from django.conf.urls import url
from django.views.static import serve
from one.views import Login,Index,Ele,robot

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    path('',Login.as_view()),
    path('index/',Index),
    path('update',Ele),
    path('robot/',robot.as_view())

]
