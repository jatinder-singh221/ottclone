from django.forms import ModelForm
from django import forms
from .models import show

class showform(ModelForm):
    class Meta:
        model = show
        fields = ['show_name', 'show_title', 'show_description', 'show_caption','show_catagory', 'show_vedio']
        widgets = {
            'show_name':forms.TextInput(attrs={'class':'form-control  bg-dark text-white', 'autofocus':True}),
            'show_title':forms.TextInput(attrs={'class':'form-control  bg-dark text-white'}),
            'show_description':forms.TextInput(attrs={'class':'form-control  bg-dark text-white'}),
            'show_caption':forms.FileInput(attrs={'class':'form-control  bg-dark text-white ','aria-label':"file example"}),
            'show_catagory':forms.Select(attrs={'class':'form-control  bg-dark text-white'}),
            'show_vedio':forms.FileInput(attrs={'class':'form-control  bg-dark text-white'}),
        }