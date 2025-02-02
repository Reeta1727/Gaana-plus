from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Album(models.Model):
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    artist=models.CharField(max_length=250)
    album_title=models.CharField(max_length=500)
    genre=models.CharField(max_length=100)
    album_logo=models.FileField()
    album_is_fav=models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'album_id':self.pk})

    def __str__(self):
        return self.album_title + "-" + self.artist

class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE,blank=True,null=True)
    song_title=models.CharField(max_length=250)
    audio_file=models.FileField(default='')
    song_is_fav=models.BooleanField(default=False)

    def __str__(self):
        return self.song_title