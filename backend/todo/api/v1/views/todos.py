from django.shortcuts import render, redirect
from rest_framework import viewsets

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.v1.serializers.todos import TaskSerializer

from todo.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        queryset = Task.objects.filter(user_id=self.request.user.id).order_by('-id')

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@api_view(['GET'])
@authentication_classes([JWTAuthentication, SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, ])
def apiOverview(request):
    api_urls = {
        'Task List': '/task/task/',
        'Task Detail View': '/task/task/<str:pk>/',
        'Task Create': '/task/task/',
        'Task Update': '/task/task/<str:pk>/',
        'Task Delete': '/task/task/<str:pk>/',
        '-------------': '----------',
        'User List': '/user/user/',
        'User Detail View': '/user/user/<str:pk>/',
        'User Create': '/user/user/',
        'User Update': '/user/user/<str:pk>/',
        'User Delete': '/user/user/<str:pk>/',
    }

    return Response(api_urls)
