import os
from django.urls import path, include
from knox import views as knox_views
from api.v1.views.accounts import RegisterAPI
from api.v1.views.accounts import LoginAPI, LogoutView
from api.v1.views import todos as views
from api.v1.views import accounts as account_views

template_path = os.path.dirname(os.path.dirname(__file__))

urlpatterns = [
    path('', views.apiOverview, name="todo-overview"),
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
    path('task-create/', views.taskCreate, name="task-create"),
    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
    path('user_list/', account_views.UserList, name='list_users'),
    path('user_detail/<str:pk>/', account_views.UserDetail, name='list_users'),
    path('user_delete/<str:pk>/', account_views.UserDelete, name='user_delete'),
    path('user_update/<str:pk>/', account_views.UserUpdate, name='user_update'),
    path('user_create/', RegisterAPI.as_view(), name='user_create'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('__debug__/', include('debug_toolbar.urls')),
]
