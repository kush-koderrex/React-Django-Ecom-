from django.shortcuts import render
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout
import random
# Create your views here.
def generate_seesion_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)]+[str(i) for i in range(10)])for _ in range(length))