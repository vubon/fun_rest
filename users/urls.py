""" User module URLs"""

from django.urls import path

from users.views import CreateUserAPI, UserDetailsAPI

urlpatterns = [
    path("", CreateUserAPI.as_view()),
    path("/<int:pk>", UserDetailsAPI.as_view()),
]
