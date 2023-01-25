

from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from .models import *


class Logistic:

    @staticmethod
    def create_new_user(request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create(username=username, password=make_password(password))
        return username, password

    @staticmethod
    def login_new_user(request, username, password, *args, **kwargs):
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
