# gestionAsistenciaPermisos/auth/urls.py
from django.urls import path
from . import views
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('base/', views.base_view, name='base'),
    path('signin/', views.signin, name='signin'),
]
