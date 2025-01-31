from django.shortcuts import render,redirect
from .models import Message
from .forms import RegisterForm, LoginForm, CreatePostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404



def feedView(request):
    posts = Message.objects.filter(replies__isnull=True)
    # replies = Message.objects.filter(parent__isnull=False)
    # print(posts.Message``)
    messages = Message.objects.all()
    context = {"messages": messages, "posts": posts}
    return render(request, 'feed.html', context)

def registerView(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account was created for {username}!")
            return redirect("login")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else: 
        form = RegisterForm()
    return render(request, 'registration_form.html', {"form": form})


def loginView(request): 
    if request.method == "POST":
        form  = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None: 
                login(request,user)
                messages.success(request,'You are logged in!')
                return redirect('home')
            else: 
                messages.error(request, 'Invalid username and password OR user doesnt exist')

    else: 
        form = LoginForm()
    
    return render(request, 'login_form.html', {"form": form})

    
            
def logoutView(request):
    if request.method == "POST": 
        logout(request)
        return redirect('home')
        
    return render(request, 'logout_form.html')

@login_required(redirect_field_name="home")
def createPostView(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.save()
            return redirect('home')
            # content = form.cleaned_data.get('content')
    else: 
        form = CreatePostForm()

    return render(request,'create_post_form.html', {"form":form})


def postView(request, pk):
    post = get_object_or_404(Message, id=pk)
    replies = Message.objects.filter(replies_id=pk)

    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.replies_id = pk
            reply.user = request.user
            reply.save()
            return redirect (request.path_info )
        
    else: 
        form = CreatePostForm()
        
    return render(request,'post_view.html',{"post":post,"replies":replies, "form": form}) 