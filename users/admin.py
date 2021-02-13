"""User model register here"""
from django.contrib import admin

from users.models import User, Tags

admin.site.register(User)
admin.site.register(Tags)
