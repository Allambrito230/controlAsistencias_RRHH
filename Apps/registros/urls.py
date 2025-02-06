from django.urls import path
from . import views


urlpatterns = [
    path('jefes/', views.jefes_view, name='jefes'),
    path('jefes/<int:id>/', views.jefes_view, name='jefe_update'), 
    path('colaboradores/', views.colaboradores_view, name='colaboradores'),
    path('colaboradores/<int:id>/', views.colaboradores_view, name='colaboradores_update'),
]