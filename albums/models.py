from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)

    def __str__(self):
        # for artist in Album.all.objects.order_by("artist"):
        return f'{self.title} by {self.artist}'


class Artist(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a band or artist')

    def get_absolute_url(self):
        return reverse('artist-detail', args=[str(self.id)])

    def __str__(self):
        return self.name