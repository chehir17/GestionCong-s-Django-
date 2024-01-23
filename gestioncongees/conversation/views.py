from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Conversation
from .forms import ConversationMessageForm
from django.contrib.auth.models import User

# Create your views here.
@login_required
def conver(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    
    return render(request, 'conversation/conversation.html', {
        'conversations': conversations
    }) 


@login_required
def new_conversation(request,user_pk):
    user = get_object_or_404(User, pk=user_pk)

    conversations = Conversation.objects.filter(members=user).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation:detail', pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create()
            conversation.members.add(request.user)
            conversation.members.add(user)

            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('conversation:conver')
    else:
        form = ConversationMessageForm()
    
    return render(request, 'conversation/new.html', {
        'form': form
    })


@login_required
def detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('conversation:detail', pk=pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form
    })

@login_required
def deleteconv(request, pk):
    Del_dec = get_object_or_404(Conversation, pk=pk)
    Del_dec.delete()

    return redirect('/conversations/')