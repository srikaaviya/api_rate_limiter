from django.urls import path
from .views import my_protected_api

urlpatterns = [
    path('protected/', my_protected_api),
]
