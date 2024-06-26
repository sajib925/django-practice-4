from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm

class MusicianListView(ListView):
    model = Musician
    template_name = 'musician_list.html'
    context_object_name = 'musicians'
    def get_queryset(self):
        return Musician.objects.prefetch_related('album_set').all()
    
class MusicianCreateView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician_form.html'
    success_url = reverse_lazy('musician_list')

class MusicianUpdateView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician_form.html'
    success_url = reverse_lazy('musician_list')

class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_form.html'
    success_url = reverse_lazy('musician_list')

class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_form.html'
    success_url = reverse_lazy('musician_list')

class AlbumDeleteView(DeleteView):
    model = Album
    success_url = reverse_lazy('musician_list')
