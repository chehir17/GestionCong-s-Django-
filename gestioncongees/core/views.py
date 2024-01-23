from django.shortcuts import get_object_or_404, redirect, render

from .models import CustomUser

from .forms import EditUserForm, SignupForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from demandeCongee.models import Cangees
from tache.models import Tache
from conversation.models import Conversation


# Create your views here.
@login_required
def index(request):
    nbusers = User.objects.all()
    nbdemandes = Cangees.objects.all()
    nbtaches = Tache.objects.filter(etat = 'open')

    return render(request, 'core/index.html',{
    'nbusers' : nbusers,
    'nbdemandes' : nbdemandes,
    'nbtaches' : nbtaches
    })

def contact(request):
    return render(request, 'core/contact.html')

def getUser(request):
    user = CustomUser.objects.all()
    return render(request, 'core/listUser.html', {
        'users' : user
    })
    
@login_required
def adduser(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
            
        if form.is_valid():
            form.save()
            return redirect('/listUser/')
    else:
        
        form = SignupForm()

    return render(request, 'core/adduser.html', {
        'form' : form,
        'title': 'Ajouter user'
    })


@login_required
def edit(request, pk):
    editc = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=editc)
        if form.is_valid():
            editc.save()
            return redirect('/listUser/')
    else:
        form = EditUserForm(instance=editc)
    
    return render(request, 'core/adduser.html', {
        'form' : form,
        'title' : 'Modifier User',
    })

@login_required
def delete(request, pk):
    userd = get_object_or_404(CustomUser, pk=pk)
    userd.delete()

    return redirect('core:listUser')




def custom_logout(request):
    logout(request)
    return redirect('/') 

@login_required
def editstatus(request,pk):
    editstatus = get_object_or_404(Tache, pk=pk)
    if request.method == 'POST':
        editstatus.etat = 'terminer'
        editstatus.save()
        return redirect('/index/')


    return render(request, 'tache/addTache.html', {
        'title': 'Approuver la tache ',
        'editstatus': editstatus,
    })