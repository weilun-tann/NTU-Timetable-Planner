from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm

class UserLogIn(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'password']
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder': 'Name'}),
            'password' : forms.PasswordInput(attrs={'placeholder': 'Password'})
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = "__all__"
