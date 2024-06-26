from django import forms
from .models import Musician, Album

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['musician', 'album_name', 'release_date', 'rating']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'})
        }