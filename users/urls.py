from django.urls import path
from users.views import user_home

urlpatterns = [
    path('users-task/',user_home),
]
