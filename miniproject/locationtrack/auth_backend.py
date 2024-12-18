# locationtrack/auth_backend.py

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .models import Student
from django.contrib.auth.hashers import check_password

class StudentBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = Student.objects.get(email=username)
            if check_password(password, user.password):
                return user
        except Student.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Student.objects.get(pk=user_id)
        except Student.DoesNotExist:
            return None
