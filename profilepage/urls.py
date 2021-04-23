from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('userprofile', views.userprofile, name='userprofile'),
    path('newpost', views.newpost, name='newpost'),
]
