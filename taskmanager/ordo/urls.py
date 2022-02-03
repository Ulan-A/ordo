from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('meetings/', views.meetings, name='meetings'),
    path('meeting-details/', views.meeting_details, name='meeting-details'),
    path('about/', views.about, name='about'),
    path('wiki/', views.wiki, name='wiki'),
    path('forum/', views.forum, name='forum'),

]
