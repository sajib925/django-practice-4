from django.urls import path
from .views import *

urlpatterns = [
    path('', MusicianListView.as_view(), name='musician_list'),
    path('musician/add/', MusicianCreateView.as_view(), name='musician_add'),
    path('musician/<int:pk>/', MusicianUpdateView.as_view(), name='musician_update'),
    path('album/add/', AlbumCreateView.as_view(), name='album_add'),
    path('album/<int:pk>/', AlbumUpdateView.as_view(), name='album_update'),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album_delete'),
]
