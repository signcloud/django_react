import os

from django.urls import path, include

from rest_framework import routers

from api.v1.views import TaskViewSet
from api.v1.views import UserViewSet
from api.v1.views import apiOverview


router = routers.SimpleRouter()
router.register(r'task', TaskViewSet)

user_router = routers.SimpleRouter()
user_router.register(r'user', UserViewSet)


template_path = os.path.dirname(os.path.dirname(__file__))

urlpatterns = [
    path('task/', include(router.urls)),
    path('user/', include(user_router.urls)),
    path('', apiOverview, name="todo-overview"),
    path('__debug__/', include('debug_toolbar.urls')),
]
