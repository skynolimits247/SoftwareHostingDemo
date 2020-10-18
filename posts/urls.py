"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
from .views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #url(r'^login/$', login),
    url(r'register/$',register),
    url(r'^',home),
    url(r'delete/(\d+)/$',delete),
    url(r'check/$',auth_view),
    url(r'logout/$',logout),
    url(r'edit/(\d+)/$',edit),
    url(r'search/$',search),
    url(r'update/(\d+)/$',update),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
