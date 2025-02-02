from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Album,Song

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email','password']

class AddAlbumForm(ModelForm):
    class Meta:
        model=Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']

class AddSongForm(ModelForm):
    class Meta:
        model=Song
        fields=['song_title','audio_file']

