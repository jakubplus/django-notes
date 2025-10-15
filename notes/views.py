from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Note
from .forms import NoteForm

def notes_list_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:list')
    else:
        form = NoteForm()
    notes = Note.objects.all()
    return render(request, 'notes/list.html', {'form': form, 'notes': notes})

def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes:list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/edit.html', {'form': form, 'note': note})

@require_POST
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('notes:list')
