from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class EmployeeReg(UserCreationForm):
    
    class Meta:
        model=User
        fields=['username','password1','password2','email','is_employee']

class EmployerReg(UserCreationForm):
    
    class Meta:
        model=User
        fields=['username','password1','password2','email','is_employer']

class LoginForm(forms.Form):

    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"id":"username"}))
    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"id":"password"}))

