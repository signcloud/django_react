from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task


# Create your views here.
# @login_required()
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, ])
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    if not request.user:
        redirect("/login")
    tasks = Task.objects.filter(user_id=request.user.id).order_by('-id')
    serializer = TaskSerializer(tasks, context={'request': request}, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    data = request.data
    data['user'] = request.user.id
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    data = request.data
    data['user'] = request.user.id
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Item succsesfully delete!')
