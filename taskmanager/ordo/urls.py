from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meetings/', views.meetings, name='meetings'),
    path('community/', views.community, name='community'),
    path('wiki/', views.wiki, name='wiki'),
    path('forum_home', views.forum_home, name='forum-home'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('about_us', views.about_us, name = 'about_us'),
]
