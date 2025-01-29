from .models import registroPermisos, Colaboradores, Departamento, tiposPermiso
from django.db.models import F
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from .utils import enviar_correo_permiso
from django.utils.timezone import now
from . models import Empresas, Sucursal


# # Create your views here.
# # LISTA DE DEPARTAMENTOS
def lista_departamentos_view(request):
    departamentos = Departamento.objects.filter(
        estado='ACTIVO').values('id', 'nombre_departamento')
    return JsonResponse(list(departamentos), safe=False)


def lista_empresas_view(request):
    empresas = Empresas.objects.filter(
        estado='ACTIVO').values('id', 'nombre_empresa')
    return JsonResponse(list(empresas), safe=False)


def lista_sucursales_view(request):
    sucursales = Sucursal.objects.filter(
        estado='ACTIVO').values('id', 'nombre_sucursal')
    return JsonResponse(list(sucursales), safe=False)

# COLABORADORES POR DEPARTAMENTO


def colaboradores_por_departamento_view(request, departamento_id):
    colaboradores = Colaboradores.objects.filter(departamento_id=departamento_id, estado='ACTIVO').values(
        'id', 'nombrecolaborador', 'codigocolaborador')
    return JsonResponse(list(colaboradores), safe=False)


def cargar_colaboradores(request, jefe_id):
    colaboradores = Colaboradores.objects.filter(
        jefe_id=jefe_id, estado='ACTIVO')
    data = {
        "colaboradores": list(colaboradores.values('id', 'nombrecolaborador')),
    }
    return JsonResponse(data)

# SOLICITUD DE PERMISOS


def permisos_registro_view(request):
    if request.method == "POST":
        try:
            # Captura los datos del formulario
            id_empresa = request.POST.get("id_empresa")
            id_sucursal = request.POST.get("id_sucursal")
            id_departamento = request.POST.get("id_departamento")
            colaborador_nombre = request.POST.get("colaborador")
            id_tipo_permiso = request.POST.get("id_tipo_permiso")
            permiso_de = request.POST.get("permiso_de")
            fecha_inicio = request.POST.get("fecha_inicio")
            fecha_fin = request.POST.get("fecha_fin")
            motivo = request.POST.get("motivo")
            comprobante = request.FILES.get("comprobante")

            # Busca el ID del colaborador a partir del nombre
            try:
                colaborador_obj = Colaboradores.objects.get(
                    nombrecolaborador=colaborador_nombre)
            except Colaboradores.DoesNotExist:
                return JsonResponse({"message": "El colaborador especificado no existe."}, status=400)

            # Verificar si el colaborador ya tiene un permiso activo
            solicitudes_existentes = registroPermisos.objects.filter(
                codigocolaborador=colaborador_obj,
                estado_inicial__in=["Pendiente", "Aprobado"]
            )

            if solicitudes_existentes.exists():
                return JsonResponse({"status": "Error",
                                     "message": "Usted ya tiene una solicitud de permiso activa. No puede enviar otra."
                                     }, status=400)

            # Crea un nuevo registro
            nuevo_permiso = registroPermisos.objects.create(
                id_empresa_id=id_empresa,
                id_sucursal_id=id_sucursal,
                id_departamento_id=id_departamento,
                codigocolaborador=colaborador_obj,
                colaborador=colaborador_nombre,
                id_tipo_permiso_id=id_tipo_permiso,
                permiso_de=permiso_de,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin,
                motivo=motivo,
                comprobante=comprobante,
                estado_inicial="Pendiente",
                estado_final="Pendiente",
                creado_por="Colaborador",
                fecha_creacion=now()
            )

            # Enviar el correo con los detalles del permiso
            enviar_correo_permiso(nuevo_permiso)

            # return redirect('permisos_solicitud_exito')
            return JsonResponse({"status": "Success", "message": "Solicitud de permiso enviada correctamente."}, status=200)
        except Exception as e:
            # print(f"Error al guardar el permiso: {e}")
            return JsonResponse({"status": "Error", "message": f"Error al guardar el la solicitud: {e}"}, status=400)

    return render(request, "solicitud.html")
    # return JsonResponse({"status": "Error", "message": "Método no permitido"}, status=405)


def verificar_solicitud_activa_view(request):
    if request.method == 'POST':
        import json
        body = json.loads(request.body)  # Parsear el cuerpo de la solicitud
        # Obtener el nombre del empleado
        nombre_empleado = body.get('nombreEmpleado')

        if not nombre_empleado:
            return JsonResponse({'error': 'El nombre del empleado es requerido.'}, status=400)

        # Verificar si el empleado tiene una solicitud activa
        tiene_solicitud_activa = registroPermisos.objects.filter(
            codigocolaborador__nombrecolaborador=nombre_empleado,
            fecha_fin__gte=timezone.now()  # Asegurarse de que la solicitud no haya finalizado
        ).exists()

        return JsonResponse({'activa': tiene_solicitud_activa})
    return JsonResponse({'error': 'Método no permitido'}, status=405)


def exito_view(request):
    return render(request, 'permisos/exito.html')

# GESTION DE PERMISOS


def permisos_gestion_view(request):
    # Consulta para obtener los datos relacionados
    permisos_gestion = registroPermisos.objects.select_related(
        'id_departamento', 'id_tipo_permiso', 'codigocolaborador'
    ).annotate(
        nombre_departamento=F('id_departamento__nombre_departamento'),
        nombre_tipo_permiso=F('id_tipo_permiso__nombre_permiso'),
        nombre_colaborador=F('codigocolaborador__nombrecolaborador'),
    )

    # Pasar los datos al template
    context = {
        'permisos_gestion': permisos_gestion
    }
    return render(request, 'permisos/permisos_gestion.html', context)


# # HISTORIAL DE PERMISOS


def permisos_historial_view(request):
    permisos = registroPermisos.objects.select_related(
        'codigocolaborador', 'id_tipo_permiso', 'id_empresa', 'id_sucursal', 'id_departamento'
    ).annotate(
        nombre_colaborador=F('codigocolaborador__nombrecolaborador'),
        tipo_permiso=F('id_tipo_permiso__nombre_permiso'),
        nombre_empresa=F('id_empresa__nombre_empresa'),
        nombre_sucursal=F('id_sucursal__nombre_sucursal'),
        nombre_departamento=F('id_departamento__nombre_departamento'),
    )

    return render(request, 'permisos_historial.html', {'permisos': permisos})
