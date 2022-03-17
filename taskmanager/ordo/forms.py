from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'text')
        widgets = {
            'name': forms.TextInput(attrs={'class': "feedback", "placeholder": "Name", }),
            'email': forms.TextInput(attrs={'class': "feedback", "placeholder": "Email", }),
            'text': forms.TextInput(attrs={'class': "feedback", "placeholder": "Text", }),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['message', 'name']
        widgets = {
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'message'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
        }
