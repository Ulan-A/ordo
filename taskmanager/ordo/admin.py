from django.contrib import admin


from .models import Meetings, Meets, Room, Message, Contact

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Meetings)
admin.site.register(Contact)
admin.site.register(Meets)
