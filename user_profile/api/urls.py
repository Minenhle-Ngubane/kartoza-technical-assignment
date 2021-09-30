from django.urls import path
from user_profile.api import views

urlpatterns = [
    path('users/', views.api_users_view, name="users"),
    path("current-user/",views.api_authenticated_user_view, name="current-user")
]

