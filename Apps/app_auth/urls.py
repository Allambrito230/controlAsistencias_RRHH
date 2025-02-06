# gestionAsistenciaPermisos/auth/urls.py
from django.urls import path
from . import views
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('base/', views.base_view, name='base'),
    path('signin/', views.signin, name='signin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('users/', views.listar_usuarios, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/update/<int:user_id>/', views.user_update, name='user_update'),
    path('users/inactivate/<int:user_id>/', views.user_inactivate, name='user_inactivate'),
]
