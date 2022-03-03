from django.contrib import admin
from .models import Meetings, Room, Message

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Meetings)
