from django.shortcuts import render
# Importa el modelo Jefes desde la app permisos
from Apps.permisos.models import Jefes, Colaboradores, Departamento, Empresas, Sucursal, Unidad_Negocio

import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def jefes_view(request, id=None):
    if request.method == 'GET':
        # Verifica si la petición es AJAX o API
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or 'application/json' in request.headers.get('Accept', ''):
            jefes = list(Jefes.objects.values())
            return JsonResponse({'jefes': jefes}, safe=False)

        # Si es una petición normal desde el navegador, renderiza la plantilla HTML
        jefes = Jefes.objects.all()
        context = {'jefes': jefes}
        return render(request, 'jefes.html', context)

    # 🔹 POST: Registrar un nuevo jefe
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            identidadjefe = data.get('identidadjefe')
            nombrejefe = data.get('nombrejefe')
            correo = data.get('correo')
            estado = data.get('estado')

            if not nombrejefe:
                return JsonResponse({'success': False, 'message': 'El nombre del jefe es obligatorio.'}, status=400)

            # Generar código automáticamente
            ultimo = Jefes.objects.order_by('-id').first()
            numero = 1 if not ultimo else int(ultimo.codigo.split('-')[-1]) + 1
            codigo = f"JF-{numero}"

            nuevo_jefe = Jefes.objects.create(
                codigo=codigo,
                identidadjefe=identidadjefe,
                nombrejefe=nombrejefe,
                correo=correo,
                estado=estado
            )

            return JsonResponse({'success': True, 'message': 'Jefe registrado correctamente.', 'jefe': {'codigo': nuevo_jefe.codigo, 'nombrejefe': nuevo_jefe.nombrejefe}}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Formato de JSON no válido.'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    # 🔹 PUT: Actualizar un jefe
    elif request.method == 'PUT':
        if not id:
            return JsonResponse({'success': False, 'message': 'Se requiere el ID para actualizar.'}, status=400)

        try:
            data = json.loads(request.body)
            identidadjefe = data.get('identidadjefe')
            nombrejefe = data.get('nombrejefe')
            correo = data.get('correo')
            estado = data.get('estado')

            jefe = get_object_or_404(Jefes, id=id)

            if identidadjefe:
                jefe.identidadjefe = identidadjefe
            if nombrejefe:
                jefe.nombrejefe = nombrejefe
            if correo:
                jefe.correo = correo
            if estado:
                jefe.estado = estado

            jefe.save()
            return JsonResponse({'success': True, 'message': 'Jefe actualizado correctamente.'}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Formato de JSON no válido.'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    return JsonResponse({'success': False, 'message': 'Método no permitido.'}, status=405)


@csrf_exempt
def colaboradores_view(request, id=None):
    if request.method == 'GET':
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or 'application/json' in request.headers.get('Accept', ''):
            colaboradores = list(Colaboradores.objects.values(
                'id', 'codigocolaborador', 'nombrecolaborador', 'correo', 'estado',
                'departamento_id', 'empresa_id', 'sucursal_id', 'unidad_de_negocio_id', 'jefe_id'
            ))
            departamentos = list(Departamento.objects.values('id', 'nombre_departamento'))
            empresas = list(Empresas.objects.values('id', 'nombre_empresa'))
            sucursales = list(Sucursal.objects.values('id', 'nombre_sucursal'))
            unidades_negocio = list(Unidad_Negocio.objects.values('id', 'nombre_unidad_de_negocio'))
            jefes = list(Jefes.objects.values('id', 'codigo', 'nombrejefe'))

            return JsonResponse({
                'colaboradores': colaboradores,
                'departamentos': departamentos,
                'empresas': empresas,
                'sucursales': sucursales,
                'unidades_negocio': unidades_negocio,
                'jefes': jefes
            }, safe=False)

        colaboradores = Colaboradores.objects.all()
        context = {
            'colaboradores': colaboradores,
            'all_departamentos': Departamento.objects.all(),
            'all_empresas': Empresas.objects.all(),
            'all_sucursales': Sucursal.objects.all(),
            'all_unidades_negocio': Unidad_Negocio.objects.all(),
            'all_jefes': Jefes.objects.all()
        }
        return render(request, 'colaboradores.html', context)


# def colaboradores_view(request):
#     if request.method == 'GET':
#         colaboradores = Colaboradores.objects.all()  # Obtener todos los jefes

#         context = {
#             'colaboradores': colaboradores
#         }

#         return render(request, 'colaboradores.html', context)
