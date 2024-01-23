from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .forms import AddTachForm, EditTache

from .models import Tache

# Create your views here.
def ListTache(request):
    taches = Tache.objects.all()
    
    return render(request, 'tache/listTaches.html',{
         'taches' : taches
    })


@login_required
def addTache(request):
    if request.method == 'POST':
        form = AddTachForm(request.POST)
        if form.is_valid():
            tach = form.save(commit=False)
            tach.save()
            return redirect('/taches/tache_list')
    else:
        form = AddTachForm()
              
    return render(request, 'tache/addTache.html', {
        'form' : form,
        'title' : 'Ajouter une tache ',
    })

@login_required
def editTache(request, pk):
    edittache = get_object_or_404(Tache, pk=pk)
    if request.method == 'POST':
       form = EditTache(request.POST, instance=edittache)
       if form.is_valid():
           edittache.save()
           return redirect('tache:ListTache')
    else:
        form = EditTache(instance=edittache)

    return render(request, 'tache/addTache.html', {
        'form' : form,
        'title' : 'Edit Tache'
    })

@login_required
def deleteTache(request, pk):
    Del_tache = get_object_or_404(Tache, pk=pk)
    Del_tache.delete()

    return redirect('tache:ListTache')