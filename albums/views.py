from django.shortcuts import render, get_object_or_404
from .models import Album
# Create your views here.


def albums_collection(request, pk):
    albums = Album.objects.all()
    return render(request, 'albums/albums_collection.html', {"albums": albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, "albums/album_detail.html", {"albums": albums})


def create_album(request):
    return render(request, "albums/create_album.html", {"albums": albums})
    # if request.method == "POST":
    #     form = AlbumForm(request.Post)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.author = request.user
    #         post.save()
    #         return redirect('album_detail', pk=post.pk)
    # else:
    #     form = AlbumForm()
    # return render(request, 'albums/create_album.html', {"form": form})

