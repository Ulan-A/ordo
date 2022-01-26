from pyexpat import model

from django.forms import models
from ordo.models import Ordo
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def products(request):
    return render(request, 'main/products.html')


def contact(request):
    return render(request, 'main/contact.html')


def wiki(request):
    return render(request, 'main/wiki.html')


def forum(request):
    return render(request, 'main/forum.html')



