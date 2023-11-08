from django.urls import path

from .views import SignupView, GetCSRFToken

urlpatterns = [
    # path('csrf/', views.get_csrf, name='api-csrf'),
    # path('login/', views.login_view, name='api-login'),
    # path('session/', views.session_view, name='api-session'),
    path('register', SignupView.as_view()),
    path('csrf_cookie', GetCSRFToken.as_view()),
]