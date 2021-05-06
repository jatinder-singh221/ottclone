from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import fields

class custom_auth_form(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control', 'autofocus':'True'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control', 'autofocus':'False'}))

    class Meta:
        model = User
        fields = ['username','password']

class custom_usercreation_form(UserCreationForm):
    username = forms.CharField(widget = forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control' , 'autofocus':'True'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2']
