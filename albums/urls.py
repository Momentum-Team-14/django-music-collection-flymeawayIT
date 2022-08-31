# from django.shortcuts import render
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.album_collection, name='album_collection'),
    path('albums/<int:pk>', views.album_detail, name='album_detail'),
    path('albums/new', views.create_album, name='create_album'),
    # path('albums/<int:pk>')
]