from django.shortcuts import render
from .models import Message

# Create your views here.


def messageView(request):
    posts = Message.objects.filter(replies__isnull=True)
    # replies = Message.objects.filter(parent__isnull=False)
    messages = Message.objects.all()
    context = {"messages": messages, "posts": posts}
    return render(request, 'feed.html', context)

def registerView(request):
    return render(request, 'registration_form.html')

def loginView(request): 
    return render(request, 'login_form.html')
