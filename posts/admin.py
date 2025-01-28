from django.contrib import admin
from .models import Message, CustomUser

admin.site.register(Message)
admin.site.register(CustomUser)
