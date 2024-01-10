from django.contrib import admin
from .models import BotUser, Feedback

class BotUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'user_id', 'created_at', 'subscribed']

class Feedback1(admin.ModelAdmin):
    list_display = ['user_id', 'created_at', 'body', 'body1', 'body2', 'body3', 'body4', 'body5']

admin.site.register(BotUser, BotUserAdmin)
admin.site.register(Feedback, Feedback1)