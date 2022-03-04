from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.fields import CharField
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
