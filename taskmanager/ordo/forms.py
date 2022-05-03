from django import forms
from .models import *





class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['message', 'name']
        widgets = {
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'message'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
        }
