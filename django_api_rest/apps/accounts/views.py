from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from rest_framework import status, permissions
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from .serializers import UserSerializer
from apps.users.models import User
from rest_framework.authtoken.views import ObtainAuthToken

# Create your views here.

class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        user = self.request.user
        if user.is_authenticated:
            return Response({ 'isAuthenticated': True }, status=status.HTTP_200_OK)
        else:
            return Response({ 'isAuthenticated': False }, status=status.HTTP_200_OK)
    
class SignupView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            Token.objects.create(user=user)
            return Response({'username': user.username}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(ObtainAuthToken):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # login(request, user)
            user.last_login = timezone.now()
            user.save()
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            return Response({'success': 'User authenticated', 'username': username, 'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid username/password.'}, status=status.HTTP_400_BAD_REQUEST)
        
 
# class LogoutView(APIView):
#     def post(self, request, format=None):
#         logout(request)
#         return Response({'success': 'Logged out successfully'}, status=status.HTTP_200_OK)

class LogoutView(APIView):
    def post(self, request, format=None):
        # Elimina el token del usuario para hacer logout
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

    
# @method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request, format=None):
       return Response({'detail': 'CSRF cookie has been set successfully.'}, status=status.HTTP_200_OK)
    
class DeleteAccountView(APIView):
    def delete(self, request, format=None):
        user = self.request.user
        try:
            
            user = User.objects.filter(id=user.id).delete()
            return Response({'success': 'User deleted successfully'})
        except:
            return Response({'success': 'Something went wrong when trying to delete user'})
        
class GetUsersView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request, format=None):
        users = User.objects.all()
        users = UserSerializer(users, many=True)
        return Response(users.data)