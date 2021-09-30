from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
	path('user-profile/', views.user_profile, name="user_profile"),
    path('edit-user-profile/', views.edit_user_profile, name="edit_user_profile"),   
]
