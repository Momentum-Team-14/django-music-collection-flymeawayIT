from django.shortcuts import render, get_object_or_404
from .models import Album
from django.views import generic
from django.urls import reverse_lazy
from .models import Artist


def album_collection(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_collection.html', {"albums": albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, "albums/album_detail.html", {"albums": album_detail})


def create_album(request,):
    return render(request, "albums/create_album.html", {"albums": create_album})
    if request.method == "POST":
        form = AlbumForm(request.Post)
        if form.is_valid():
            album = form.save()
            return redirect('album_collection')
    else:
        form = AlbumForm()
    return render(request, 'albums/create_album.html', {"form": form})