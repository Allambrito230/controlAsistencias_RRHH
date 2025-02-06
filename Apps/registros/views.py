from django.shortcuts import render
from Apps.permisos.models import Jefes, Colaboradores  # Importa el modelo Jefes desde la app permisos


# Create your views here.

def jefes_view(request):
    if request.method == 'GET':
        jefes = Jefes.objects.all()  # Obtener todos los jefes

        context = {
            'jefes': jefes
        }

        return render(request, 'jefes.html', context)
    
def colaboradores_view(request):
    if request.method == 'GET':
        colaboradores = Colaboradores.objects.all()  # Obtener todos los jefes

        context = {
            'colaboradores': colaboradores
        }

        return render(request, 'colaboradores.html', context)


