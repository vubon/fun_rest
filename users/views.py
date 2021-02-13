"""User Views"""

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User


class CreateUserAPI(APIView):
    """Creating a new user"""

    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        """
         URL: URI/users
        :return:
        """
        user = User.objects.create_user(self.request.data)
        return Response(data={"id": user.pk}, status=status.HTTP_201_CREATED)


class UserDetailsAPI(APIView):
    """Get user details"""
    permission_classes = ()
    authentication_classes = ()

    def get(self, request, pk):
        """
        :param request:
        :param pk:
        :return:
        """

        user = User.objects.get_user_details(pk=pk)
        if user:
            return Response(data=user, status=status.HTTP_200_OK)
        return Response(data={"status": "User Not found"}, status=status.HTTP_404_NOT_FOUND)
