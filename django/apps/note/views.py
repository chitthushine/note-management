from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NoteForm, NoteSearchForm
from .models import Note

def index(request):
    """
    Main page of the system.
    """
    return redirect('note_list')

# function-based view to display all notees
@login_required
def note_list(request):
    """
    Display all notees in the database.
    """
    notes = Note.objects.filter(user=request.user)
    return render(request, 'note_list.html', {'notes': notes})

# function-based view to display create Note form
@login_required
def note_new(request):
    """
    Display the create Note form.
    Only logged-in users can access this endpoint.
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()

    return render(request, 'note_edit.html', {'form': form, \
                                               'header_label': "Add New Note"})

# function-based view to display update Note form
@login_required
def note_edit(request, pk):
    """
    Display the update Note form for the given primary key.
    Only logged-in users can access this endpoint.
    """
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)

    return render(request, 'note_edit.html', {'form': form, \
                                               'header_label': "Edit Note"})

# function-based view to delete Note data
@login_required
def note_delete(request, pk):
    """
    Delete note data for the given primary key.
    Only logged-in users can access this endpoint.
    """
    note = get_object_or_404(Note, pk=pk, user=request.user)
    note.delete()
    return redirect('note_list')

@login_required
def note_search(request):
    form = NoteSearchForm(request.GET or None)
    title = ''
    if form.is_valid():
        title = form.cleaned_data["title"]

        notes = Note.objects.filter(
            Q(title__icontains=title),
            user=request.user,
        )

    else:
        notes = Note.objects.filter(user=request.user)

    context = {
        "search_data": title,
        "notes": notes,
    }

    return render(request, 'note_list.html', context)