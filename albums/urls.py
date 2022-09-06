# from django.shortcuts import render
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.album_collection, name='album_collection'),
    path('albums/<int:pk>', views.album_detail, name='album_detail'),
    path('albums/new', views.create_album, name='create_album'),
    path('albums/<int:pk>', views.album_delete, name='album_delete'),
    path('albums/<int:pk>', views.album_edit, name='album_edit'),
    path('albums/<int:pk>', views.artist_delete, name='artist_delete'),
    path('albums/<int:pk>', views.artist_detail, name='artist_detail'),
    path('albums/<int:pk>', views.artist_list, name='artist_list'),
    # path('albums/<int:pk>')
]