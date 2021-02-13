"""User Views"""

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User


class UserViewAPI(APIView):
    """Creating a new user"""

    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        """
         URL: /users/
        :return:
        """
        user = User.objects.create_user(request.data)
        return Response(data={"id": user.pk}, status=status.HTTP_201_CREATED)
