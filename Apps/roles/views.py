from datetime import date, time
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Rol, RolAsignado, RegistroAsistencia, Sucursal, Departamento, Jefes, Colaboradores
from Apps.permisos.models import Sucursal, Departamento, Colaboradores, Jefes
# Create your views here.
'''
Codigo necesario para la creacion de roles
'''


@login_required
def crear_rol(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        hora_inicio_semana = request.POST.get('hora_inicio_semana')
        hora_fin_semana = request.POST.get('hora_fin_semana')
        hora_inicio_sabado = request.POST.get('hora_inicio_sabado') or None
        hora_fin_sabado = request.POST.get('hora_fin_sabado') or None
        hora_inicio_domingo = request.POST.get('hora_inicio_domingo') or None
        hora_fin_domingo = request.POST.get('hora_fin_domingo') or None

        # Crear el rol
        Rol.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            hora_inicio_semana=hora_inicio_semana,
            hora_fin_semana=hora_fin_semana,
            hora_inicio_sabado=hora_inicio_sabado,
            hora_fin_sabado=hora_fin_sabado,
            hora_inicio_domingo=hora_inicio_domingo,
            hora_fin_domingo=hora_fin_domingo
        )
        return redirect('listar_roles')
    elif request.method == 'GET':
        return render(request, 'crear_rol.html')


@login_required
def listar_roles(request):
    roles = Rol.objects.all()
    return render(request, 'listar_roles.html', {'roles': roles})


'''
Codigo necesario para la asignacion de roles
'''


@login_required
def asignar_rol(request):
    if request.method == 'POST':
        empleado_id = request.POST.get('empleado')
        rol_id = request.POST.get('rol')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        empleado = User.objects.get(id=empleado_id)
        rol = Rol.objects.get(id=rol_id)

        # Asignar el rol
        RolAsignado.objects.create(
            empleado=empleado,
            rol=rol,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin
        )
        return redirect('listar_roles_asignados')

    empleados = User.objects.all()
    roles = Rol.objects.all()
    return render(request, 'asignar_rol.html', {'empleados': empleados, 'roles': roles})


@login_required
def listar_roles_asignados(request):
    roles_asignados = RolAsignado.objects.select_related('empleado', 'rol')
    return render(request, 'listar_roles_asignados.html', {'roles_asignados': roles_asignados})


'''
Codigo necesario para el registro de asistencias
'''


@login_required
def registrar_asistencia(request):
    if request.method == 'POST':
        empleado_id = request.POST.get('empleado')
        hora_entrada = request.POST.get('hora_entrada')
        hora_salida = request.POST.get('hora_salida')
        fecha_actual = date.today()

        empleado = User.objects.get(id=empleado_id)

        # Obtener el rol asignado vigente
        rol_asignado = RolAsignado.objects.filter(
            empleado=empleado,
            fecha_inicio__lte=fecha_actual,
            fecha_fin__gte=fecha_actual
        ).first()

        cumplimiento = False
        if rol_asignado:
            # Validar si la hora de entrada cumple con el horario del rol
            hora_inicio_rol = rol_asignado.rol.hora_inicio_semana
            cumplimiento = time.fromisoformat(hora_entrada) <= hora_inicio_rol

        # Registrar la asistencia
        RegistroAsistencia.objects.create(
            empleado=empleado,
            fecha=fecha_actual,
            hora_entrada=hora_entrada,
            hora_salida=hora_salida,
            cumplimiento=cumplimiento
        )
        return redirect('listar_asistencias')

    empleados = User.objects.all()
    return render(request, 'registrar_asistencia.html', {'empleados': empleados})


@login_required
def listar_asistencias(request):
    asistencias = RegistroAsistencia.objects.select_related('empleado')
    return render(request, 'listar_asistencias.html', {'asistencias': asistencias})


'''
A continuacion se presentan las vistas de prueba
'''


@login_required
def sucursales(request):
    if request.method == 'POST':
        # Crear una nueva sucursal
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        estado = request.POST.get('estado', 'ACTIVO')
        Sucursal.objects.create(
            nombre_sucursal=nombre,
            estado=estado,
            fechacreacion=request.user
        )
        return redirect('sucursales')

    # Listar todas las sucursales
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursales.html', {'sucursales': sucursales})


@login_required
def departamentos(request):
    if request.method == 'POST':
        # Crear un nuevo departamento
        nombre = request.POST.get('nombre')
        sucursal_id = request.POST.get('sucursal')
        sucursal = Sucursal.objects.get(id=sucursal_id)
        estado = request.POST.get('estado', 'ACTIVO')
        Departamento.objects.create(
            nombre_departamento=nombre,
            estado=estado,
            fechacreacion=request.user
        )
        return redirect('departamentos')

    # Listar todos los departamentos y sucursales para el formulario
    departamentos = Departamento.objects.all()
    sucursales = Sucursal.objects.all()
    return render(request, 'departamentos.html', {'departamentos': departamentos, 'sucursales': sucursales})


@login_required
def colaboradores(request):
    if request.method == 'POST':
        # Crear un nuevo colaborador
        codigo = request.POST.get('codigo')
        identidad = request.POST.get('identidad')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        departamento_id = request.POST.get('departamento')
        departamento = Departamento.objects.get(id=departamento_id)
        estado = request.POST.get('estado', 'ACTIVO')
        Colaboradores.objects.create(
            codigocolaborador=codigo,
            nombrecolaborador=nombre,
            departamento=departamento,
            estado=estado,
            fechacreacion=request.user
        )
        return redirect('colaboradores')

    # Listar todos los colaboradores y departamentos para el formulario
    colaboradores = Colaboradores.objects.select_related('departamento')
    departamentos = Departamento.objects.all()
    return render(request, 'colaboradores.html', {'colaboradores': colaboradores, 'departamentos': departamentos})


@login_required
def jefes(request):
    if request.method == 'POST':
        # Crear un nuevo jefe
        codigo = request.POST.get('codigo')
        identidad = request.POST.get('identidad')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        sucursal_id = request.POST.get('sucursal')
        sucursal = Sucursal.objects.get(id=sucursal_id)
        estado = request.POST.get('estado', 'ACTIVO')
        Jefes.objects.create(
            codigo=codigo,
            identidadjefe=identidad,
            nombrejefe=nombre,
            estado=estado,
            fechacreacion=request.user
        )
        return redirect('jefes')

    # Listar todos los jefes y sucursales para el formulario
    jefes = Jefes.objects.all()
    sucursales = Sucursal.objects.all()
    return render(request, 'jefes.html', {'jefes': jefes, 'sucursales': sucursales})


@login_required
def registro_asistencia(request):
    if request.method == 'POST':
        # Registrar asistencia
        colaborador_id = request.POST.get('colaborador')
        fecha = request.POST.get('fecha')
        hora_entrada = request.POST.get('hora_entrada')
        hora_salida = request.POST.get('hora_salida')
        colaborador = Colaboradores.objects.get(id=colaborador_id)

        # Obtener el rol asignado y validar el cumplimiento
        rol = colaborador.departamento.sucursal.roles.filter(
            estado='ACTIVO').first()
        cumplimiento = 'NO_CUMPLIO'
        if rol:
            if hora_entrada and hora_salida:
                hora_inicio = rol.hora_inicio_semana if int(
                    fecha.weekday()) < 5 else rol.hora_inicio_sabado
                cumplimiento = '<' if hora_entrada <= hora_inicio else '>'

        RegistroAsistencia.objects.create(
            colaborador=colaborador,
            sucursal=colaborador.departamento.sucursal,
            rol=rol,
            fecha=fecha,
            hora_entrada=hora_entrada,
            hora_salida=hora_salida,
            cumplimiento=cumplimiento,
            creado_por=request.user
        )
        return redirect('registro_asistencia')

    # Listar asistencias y colaboradores
    asistencias = RegistroAsistencia.objects.select_related(
        'colaborador', 'rol', 'sucursal')
    colaboradores = Colaboradores.objects.all()
    return render(request, 'registro_asistencia.html', {'asistencias': asistencias, 'colaboradores': colaboradores})
