from django.shortcuts import render, get_object_or_404
from .models import Album
# Create your views here.

# When added pk as 2nd argument, rendering complained missing a positional argument
def albums_collection(request):
    albums = Album.objects.all()
    return render(request, 'albums/albums_collection.html', {"albums": albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, "albums/album_detail.html", {"albums": albums})


def create_album(request,):
    return render(request, "albums/create_album.html", {"albums": albums})
    if request.method == "POST":
        form = AlbumForm(request.Post)
        if form.is_valid():
            album = form.save()
            return redirect('albums_collection')
    else:
        form = AlbumForm()
    return render(request, 'albums/create_album.html', {"form": form})

