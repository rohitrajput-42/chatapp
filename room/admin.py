from django.contrib import admin
from .models import Room, Message

class Adminroom(admin.ModelAdmin):
    list_display = ["name", "slug"]

class Adminmessage(admin.ModelAdmin):
    list_display = ["room", "user", "content", 'date_added']

admin.site.register(Room, Adminroom)
admin.site.register(Message, Adminmessage)