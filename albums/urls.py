# from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('', views.albums_collection, name='albums_collection'),
    path('albums/<int:pk>', views.album_detail, name='album_detail'),
]