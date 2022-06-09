from rest_framework import generics
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from api.v1.serializers.accounts import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from accounts.models import User

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
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


@api_view(['GET'])
def UserList(request):
    Users = User.objects.all().order_by('-id')
    serializer = UserSerializer(Users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def UserDetail(request, pk):
    print(pk)
    if pk == "n":
        pk = request.user.id

    Users = User.objects.get(id=pk)
    serializer = UserSerializer(Users, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def UserCreate(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def UserUpdate(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def UserDelete(request, pk):
    user = User.objects.get(id=pk)
    user.delete()

    return Response('Item successfully deleted!')


#
# class ListUsers(ListAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#
#
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


# class UserDelete(DestroyAPIView):
#     serializer_class = UserSerializer
#
#     def get_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404
#
#     def get_queryset(self):
#         queryset = User.objects.filter(id=self.kwargs['pk'])
#         return queryset
#
#     def delete(self, request, pk):
#         user = self.get_object(pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class UserUpdate(APIView):
#     """
#     Retrieve, update or delete a User instance.
#     """
#
#     def get_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         User = self.get_object(pk)
#         serializer = UserSerializer(User)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         User = self.get_object(pk)
#         serializer = UserSerializer(User, data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data[" "]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
