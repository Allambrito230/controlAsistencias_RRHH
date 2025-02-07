from django.contrib import messages
from django.contrib.auth.models import User, Group, Permission
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as login_sesion, logout, authenticate
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.

def base_view(request):
    return render(request, 'base.html')

from django.contrib.auth.models import Group
@login_required
def base_view(request):
    usuario_es_jefe = request.user.groups.filter(name="Jefes").exists()
    return render(request, "base.html", {"usuario_es_jefe": usuario_es_jefe})


@login_required
def dashboard(request):
    return render(request, "dashboard.html")

def login_view(request):

    if request.method == 'GET':
        return render(request, 'login.html', {'formulario': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'].upper(), password=request.POST['password'])
        if user is None:
            mensaje = 'Usuario o contraseña incorrectos'
            return render(request, 'login.html', {
                'formulario': AuthenticationForm(),
                'mensaje': mensaje
            })
        else:
            login_sesion(request, user)
            return redirect('dashboard')
        # print(request.POST)
        # return render(request, 'signin.html', {'formulario': AuthenticationForm()})
    # return render(request, 'signin.html', {'formulario': AuthenticationForm()})



@login_required
def listar_usuarios(request):
    users = User.objects.all()
    groups = Group.objects.all()
    
    # Filtrar permisos solo de las aplicaciones propias
    user_apps = ['app_auth', 'asistencia', 'registros', 'permisos', 'roles']  # Reemplaza con tus apps
    permissions = Permission.objects.filter(content_type__app_label__in=user_apps)
    
    context = {
        'users': users,
        'groups': groups,
        'permissions': permissions,
    }
    return render(request, 'listar_usuarios.html', context)

@login_required
def user_create(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        # Validación sencilla de contraseñas
        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('user_list') 

        # Crear usuario
        user = User(
            username=username.upper(),
            email=email.upper(),
            first_name=first_name.upper(),
            last_name=last_name.upper(),
            password=make_password(password1)  # encripta la contraseña
        )
        user.save()

        # Asignar grupos seleccionados
        selected_groups = request.POST.getlist('groups')  # lista de IDs
        if selected_groups:
            user.groups.set(selected_groups)

        # Asignar permisos seleccionados
        selected_perms = request.POST.getlist('permissions')
        if selected_perms:
            user.user_permissions.set(selected_perms)

        messages.success(request, 'Usuario creado exitosamente.')
        return redirect('user_list')
    else:
        return redirect('user_list')

@login_required
def user_update(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        username = request.POST.get('username', user.username)
        email = request.POST.get('email', user.email)
        first_name = request.POST.get('first_name', user.first_name)
        last_name = request.POST.get('last_name', user.last_name)
        
        user.username = username.upper()
        user.email = email.upper()
        user.first_name = first_name.upper()
        user.last_name = last_name.upper()

        # Si se quiere cambiar la contraseña
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        if password1 and password2:
            if password1 != password2:
                messages.error(request, 'Las contraseñas no coinciden.')
                return redirect('user_list')
            user.password = make_password(password1)

        user.save()

        # Actualizar grupos
        selected_groups = request.POST.getlist('groups')
        user.groups.set(selected_groups)  # Reemplaza con la nueva selección

        # Actualizar permisos
        selected_perms = request.POST.getlist('permissions')
        user.user_permissions.set(selected_perms)

        messages.success(request, 'Usuario actualizado correctamente.')
        return redirect('user_list')
    else:
        return redirect('user_list')

@login_required
def user_inactivate(request, user_id):

    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        messages.success(request, 'Usuario inactivado correctamente.')
        return redirect('user_list')
    else:
        return redirect('user_list')
    
def logout_view(request):
    logout(request)
    return redirect('login') 