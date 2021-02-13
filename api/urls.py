"""All modules base URL here"""
from django.urls import path, include

urlpatterns = [
    path('users/', include('users.urls')),
]
