from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core import validators
from .validator import char_validation1,char_validation2
from django.core.exceptions import ValidationError

class custom_auth_form(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control bg-dark text-white', 'autofocus':'True'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control  bg-dark text-white', 'autofocus':'False'}))

    class Meta:
        model = User
        fields = ['username','password']

class custom_usercreation_form(UserCreationForm):
    username = forms.CharField(widget = forms.EmailInput(attrs={'class':'form-control  bg-dark text-white'}))
    first_name = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control  bg-dark text-white' , 'autofocus':'True'}),validators=[char_validation1])
    last_name = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control  bg-dark text-white'}),validators=[char_validation2])
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control  bg-dark text-white'}),label='Password')
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control  bg-dark text-white'}),label='Confirm Password')

    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2']
