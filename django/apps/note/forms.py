from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content',)

class NoteSearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
