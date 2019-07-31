from django.conf.urls import url, include
from . import views
from django.contrib import admin
from home.views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/', views.index, name='index'),
    url(r'catview$', views.catview, name='catview'),
    url(r'softname/$', views.softname, name='softname'),
    url(r'softname/os/$', views.os, name='os'),
    url(r'^search/', views.search, name='search'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
