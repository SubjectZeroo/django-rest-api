
from datetime import datetime
from django.contrib.sessions.models import Session
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from apps.users.api.serializers import UserTokenSerializer

# Create your views here.

class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kawargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request':request})
        if login_serializer.is_valid():
           user = login_serializer.validated_data['user']
           if user.is_active:
               token,created = Token.objects.get_or_create(user = user)
               user_serializer = UserTokenSerializer(user)
               if created:
                   return Response({
                       'token': token.key,
                       'user': user_serializer.data,
                       'message': 'Inicio de Sesion Exitoso.'
                   }, status = status.HTTP_201_CREATED)
               else:
                   
                    # all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    # if all_sessions.exists():
                    #     for session in all_sessions:
                    #         session_data = session.get_decoded()
                    #         if user.id == int(session_data.get('__auth_user_id')):
                    #             session.delete()
                    # token.delete()
                    # token = Token.objects.create(user = user)
                    # return Response({
                    #     'token': token.key,
                    #     'user': user_serializer.data,
                    #     'message': 'Inicio de Sesion Exitoso.'
                    # }, status = status.HTTP_201_CREATED)
                    return Response({
                        'error' : 'Ya se ha iniciado session con este usuario.'
                    }, status = status.HTTP_409_CONFLICT)
           else:
               return Response({'error': 'Este usuario no puede iniciar sesion.'}, status = status.HTTP_401_UNAUTHORIZED)
        else:
             return Response({'error': 'Nombre de usuario o contrasena incorrectos'}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Hola desde Response'}, status = status.HTTP_200_OK)
            
    