from django.urls import path
from . import views


urlpatterns = [
    path('jefes/', views.jefes_view, name='jefes'),
    path('colaboradores/', views.colaboradores_view, name='colaboradores'),
]