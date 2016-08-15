from django.contrib import admin
from .models import Profile, Message, Quran


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'status', 'type', 'publish']


class QuranAdmin(admin.ModelAdmin):
    list_display = ['aye', 'tarjome', 'created', 'status', 'publish']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Quran, QuranAdmin)
