from django.urls import path, include

from .views import note_list, note_new, note_edit, note_delete, note_search


urlpatterns = [
    path('', note_list, name='note_list'),
    path('new/', note_new, name='note_new'),
    path('<int:pk>/edit/', note_edit, name='note_edit'),
    path('<int:pk>/delete/', note_delete, name='note_delete'),
    path('note_search/', note_search, name='note_search'),
]
