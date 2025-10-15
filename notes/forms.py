from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tytuł'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Treść'}),
        }
