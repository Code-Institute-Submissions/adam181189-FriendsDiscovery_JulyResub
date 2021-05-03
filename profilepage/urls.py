from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('userprofile', views.userprofile, name='userprofile'),
    path('newpost', views.newpost, name='newpost'),
    path('update_info', views.update_info, name='update_info'),
    path('update_image', views.update_image, name='update_image'),
    path('profile_list', views.profile_list, name='profile_list'),
]
