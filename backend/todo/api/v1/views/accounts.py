from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.decorators import api_view

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.response import Response

from api.v1.serializers.accounts import UserSerializer
from accounts.models import User


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        pk = self.kwargs.get('pk')

        if pk == "current":
            return self.request.user

        return super().get_object()


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task/task/',
        'Detail View': '/task/task/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
        'User List': '/user_list/',
        'Detail View': '/user_detail/<str:pk>/',
        'Create': '/user_create/',
        'Update': '/user_update/<str:pk>/',
        'Delete': '/user_delete/<str:pk>/',
    }

    return Response(api_urls)
