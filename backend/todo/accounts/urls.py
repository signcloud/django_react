from django.urls import path
from knox import views as knox_views
from . import views
from .views import LoginAPI, RegisterAPI

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('user_list/', views.UserList, name='list_users'),
    path('user_detail/<str:pk>/', views.UserDetail, name='list_users'),
    path('user_delete/<str:pk>/', views.UserDelete, name='user_delete'),
    path('user_update/<str:pk>/', views.UserUpdate, name='user_update'),
    path('user_create/', RegisterAPI.as_view(), name='user_create'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]