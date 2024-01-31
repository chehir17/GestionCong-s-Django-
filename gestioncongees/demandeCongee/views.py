from django.shortcuts import redirect, render, get_object_or_404

from .models import Cangees

from .forms import CongeForm, EditCongeForm
from django.contrib.auth.decorators import login_required
from core.models import CustomUser

# Create your views here.
@login_required
def ListConges(request):
    congees = Cangees.objects.all().order_by('-created_at')
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
              return redirect('/demande/listc/')
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
def editstatus(request,pk,pk_demandeur):
    editstatus = get_object_or_404(Cangees, pk=pk)
    editsold = get_object_or_404(CustomUser, id = pk_demandeur )

    if request.method == 'POST':
        editstatus.status = True
        editstatus.save()

        newsold = editsold.sold - editstatus.dure
        editsold.sold = newsold 
        editsold.save()
        return redirect('/demande/listc/')


    return render(request, 'demandeCongee/dCongee.html', {
        'title': 'Approuver la demande ',
        'editstatus': editstatus,
    })