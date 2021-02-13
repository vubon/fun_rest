"""User Views"""

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class UserViewAPI(APIView):
    """Creating a new user"""

    permission_classes = ()
    authentication_classes = ()

    def post(self):
        """
         URL: /users/
        :return:
        """

        return Response(status=status.HTTP_201_CREATED)
