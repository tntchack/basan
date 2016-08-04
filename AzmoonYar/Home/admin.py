from django.contrib import admin
from .models import Profile, Message


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'status', 'type', 'publish']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Message, MessageAdmin)