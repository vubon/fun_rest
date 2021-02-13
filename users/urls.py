""" User module URLs"""

from django.urls import path

from users.views import UserViewAPI

urlpatterns = [
    path("", UserViewAPI.as_view())
]
