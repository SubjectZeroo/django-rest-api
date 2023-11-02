import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
# from django.shortcuts import render
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView

# Create your views here.

def get_csrf(request):
    response = JsonResponse({'detail': 'CSRF cookie set'})
    response['X-CSRFToken'] = get_token(request)
    return response

@require_POST
def login_view(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    
    if username is None or password is None:
        return JsonResponse({'detail': 'Please provide username and password'}, status=400)
    
    user = authenticate(username=username, password=password)
    
    if user is None:
        return JsonResponse({'detail': 'Invalid credentials'})
    login(request, user)
    return JsonResponse({'detail': 'Succesfully logged in.'})
    
@ensure_csrf_cookie
def session_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})
    return JsonResponse({'isAthenticated': True})