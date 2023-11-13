from django.urls import path

from .views import SignupView, GetCSRFToken, LoginView, LogoutView, CheckAuthenticatedView, DeleteAccountView, GetUsersView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('authenticated/', CheckAuthenticatedView.as_view(), name='check_authenticated'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register', SignupView.as_view(), name='register'),
    path('csrf-cookie/', GetCSRFToken.as_view(), name='get_csrf'),
    path('delete/', DeleteAccountView.as_view(), name='delete_account'),
    path('users/', GetUsersView.as_view(), name='get_users'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]