from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('products/',views.products, name='products'),
    path('wiki/',views.wiki, name='wiki'),
    path('forum/',views.forum, name='forum'),

]