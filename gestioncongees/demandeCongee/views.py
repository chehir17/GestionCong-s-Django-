from django.shortcuts import redirect, render, get_object_or_404

from .models import Cangees

from .forms import CongeForm, EditCongeForm
from django.contrib.auth.decorators import login_required
from core.models import CustomUser

# Create your views here.

def ListConges(request):
    congees = Cangees.objects.all()
    return render(request, 'demandeCongee/listCongees.html',{
         'congees' : congees
    })


@login_required
def d_Congee(request,pk):
    alert_message = ""
    user_id = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = CongeForm(request.POST, request.FILES)
        if form.is_valid():
           cong = form.save(commit=False)
           if cong.dure <=  user_id.sold:
              cong.demandeur = request.user
              cong.save()
              return redirect('/index/')
           else:
              alert_message = "vous avez deppaser votre sold des congées !"
    else: 
        form = CongeForm()
    
    return render(request, 'demandeCongee/dCongee.html', {
        'form' : form,
        'title' : 'Demande ',
        'alert_message': alert_message
    })

@login_required
def edit(request, pk):
    editdemande = get_object_or_404(Cangees, pk=pk)
    if request.method == 'POST':
        form = EditCongeForm(request.POST, instance=editdemande)
        if form.is_valid():
            editdemande.save()
            return redirect('/demande/listc/')
    else:
        form = EditCongeForm(instance=editdemande)
    
    return render(request, 'demandeCongee/dCongee.html', {
        'form' : form,
        'title' : 'Edit Demande',
    })




@login_required
def delete(request, pk):
    Del_demande = get_object_or_404(Cangees, pk=pk)
    Del_demande.delete()

    return redirect('/demande/listc/')


@login_required
def editstatus(request,pk):
    editstatus = get_object_or_404(Cangees, pk=pk)
    if request.method == 'POST':
        editstatus.status = True
        editstatus.save()
        return redirect('/')


    return render(request, 'demandeCongee/dCongee.html', {
        'title': 'Approuver la demande ',
        'editstatus': editstatus,
    })