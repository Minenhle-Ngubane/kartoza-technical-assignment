from rest_framework.response import Response
from rest_framework.decorators import api_view

from user_profile.models import User
from user_profile.api.serializers import UserSerializer


@api_view(["GET",])
def api_users_view(request):
    # Return only users with valid addresses to be listed on full page map
    queryset = User.objects.filter(profile__address_is_valid=True)
    
    if request.method == "GET":
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(["GET",])
def api_authenticated_user_view(request):

    if request.method == "GET":
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
