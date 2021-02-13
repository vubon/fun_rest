""" User module URLs"""

from django.urls import path

from users.views import CreateUserAPI, UserDetailsAPI, CreateTagAPI

urlpatterns = [
    path("", CreateUserAPI.as_view()),
    path("/<int:pk>", UserDetailsAPI.as_view()),
    path("/<int:pk>/tags", CreateTagAPI.as_view()),
]
