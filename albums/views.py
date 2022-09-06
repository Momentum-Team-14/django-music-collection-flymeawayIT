from django.shortcuts import render, get_object_or_404
from .models import Album
# from django.views import generic
# from django.urls import reverse_lazy
from .models import Artist


def album_collection(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_collection.html', {"albums": albums})


def album_delete(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_delete.html', {"albums": album_delete})


def album_detail(request, pk):
    albums = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_detail.html', {"albums": album_detail})


def create_album(request):
    return render(request, 'albums/create_album.html', {"albums": create_album})
    # if request.method == "POST":
    #     form = AlbumForm(request.POST)
    #     if form.is_valid():
    #         album = form.save()
    #         return redirect('album_collection')
    # else:
    #     form = AlbumForm()
    # return render(request, 'albums/create_album.html', {"form": form,})

def album_edit(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_edit.html', {"albums": album_edit})

def artist_delete(request):
    artists = Artist.objects.all()
    return render(request, 'albums/artist_delete.html', {"albums": artist_delete})

def artist_detail(request, pk):
    artists = Artist.objects.all()
    return render(request, 'albums/artist_detail.html', {"albums", artist_detail})

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'albums/artist_list.html', {"albums", artist_list})