"""User Views"""

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User, Tags


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

    def get(self, request):
        """
        URL: URI/users?tags=<tag1>,<tag2>
        :param request:
        :return:
        """
        params = request.query_params.dict()
        if params:
            tags = params.get("tags").split(",")
            users = User.objects.get_tags(tags=tags)
            return Response(data={"users": users}, status=status.HTTP_200_OK)
        return Response(data={}, status=status.HTTP_200_OK)


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


class CreateTagAPI(APIView):
    """Create Tag API"""
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, pk):
        """
        URL: URI/users/{user_id}/tags
        :param request:
        :param pk:
        :return:
        """
        request.data["id"] = pk
        Tags.objects.create_tag(request.data)
        return Response(data={}, status=status.HTTP_201_CREATED)


# class TagDetailsAPI(APIView):
#     """Tag details"""
#     permission_classes = ()
#     authentication_classes = ()
#
#     def get(self, request):
#         """
#         URL: URI/users?tags=<tag1>,<tag2>
#         :param request:
#         :return:
#         """
#         print(request.query_params.dict())
#         # user = User.objects.get_tags()
#         return Response(data={}, status=status.HTTP_200_OK)
