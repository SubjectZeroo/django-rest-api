from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import get_authorization_header
from apps.users.authentication import ExpiringTokenAuthentication

class Authentication(object):
    
    def get_user(self, request):
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()
            except:
                return None
            token_expire = ExpiringTokenAuthentication()
            user, token, message = token_expire
            if user != None and token != None:
                return user
            return message
            # try:
            #     user, token = token_expire.authenticate_credentials(token)
            # except:
            #     message = token_expire.authenticate_credentials(token)
        return None
        
    def dispatch(self, request, *args, **kwargs):
        user = self.get_user(request)
        # found token is request
        if user is not None:
            if type(user) == str:
                # return Response({'error':user})
                response = Response({'error':user})
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = 'application/json'
                response.renderer_context = {}
            return super().dispatch(request, *args, **kwargs)
        response = Response({'error': 'No se han enviado las credenciales.'})
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}
        return response
    
    