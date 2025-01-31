from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Message


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    

class RegisterForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields = ['username','email','password1','password2'] 

class CreatePostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 400px; height: 200px; vertical-align: top;'}))

    class Meta: 
        model = Message
        fields = ['content']
