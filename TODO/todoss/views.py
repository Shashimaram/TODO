from django.shortcuts import render # type: ignore
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView # type: ignore
from .forms import newnote,EditNote
from django.shortcuts import HttpResponse # type: ignore
from .models import Notes_model 
from django.shortcuts import get_object_or_404 # type: ignore
from django.shortcuts import redirect, reverse # type: ignore

# Create your views here.

def new_note_creation(request):
    mymodel = Notes_model.objects.all()
    
    completed_task = Notes_model.objects.filter(is_complete=True)
    incomplete_task = Notes_model.objects.filter(is_complete=False)
    
    if request.method == 'POST':
        form = newnote(request.POST)
        if form.is_valid():
            form.save()  # Save the form data
            print("Note created")
            # return HttpResponse("Note created")
        else:
            print("Note not created")
    else:
        form = newnote()
        
    return render(request, 'home.html', {'form': form,
                                         'mymodel': mymodel,
                                         'completed_task' : completed_task,
                                         'incomplete_task':incomplete_task})



def note_status(request,pk):
    statusnote = get_object_or_404(Notes_model, pk=pk)
    statusnote.is_complete=True
    statusnote.save() 
    return redirect('note')
    
    
    
    

def note_delete(requesst,pk):
    dele = Notes_model.objects.filter(pk=pk)
    dele.delete()
    return redirect('note')

def note_update(request, pk):
    curnt_note = get_object_or_404(Notes_model, pk=pk)
    
    if request.method == 'POST':
        form = EditNote(request.POST, instance=curnt_note)
        if form.is_valid():
            form.save()
            return redirect('note')
    else:
        form = EditNote(instance=curnt_note)
        
    return render(request, 'update.html', {'form': form,
                                           'notepk':pk})
