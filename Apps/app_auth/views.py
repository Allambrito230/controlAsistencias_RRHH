from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as login_sesion, logout, authenticate
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def login(request):
    return render(request, 'login.html')
    # return HttpResponse("Hello World")


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'formulario': UserCreationForm()})
        # print('Enviando formulario')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Registrar usuario
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login_sesion(request, user)
                # return HttpResponse('Usuario registrado correctamente')
                # return render(request, 'signup.html', {'formulario': UserCreationForm(), 'mensaje': 'Usuario registrado correctamente'})
                return redirect('base')
            except:
                # return HttpResponse('El usuario ya existe')
                return render(request, 'signup.html', {'formulario': UserCreationForm(), 'mensaje': 'El usuario ya existe'})
        else:
            return HttpResponse('Las contraseñas no coinciden')


def base(request):
    return render(request, '../base.html')


def signin(request):

    if request.method == 'GET':
        return render(request, 'signin.html', {'formulario': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            mensaje = 'Usuario o contraseña incorrectos'
            return render(request, 'signin.html', {
                'formulario': AuthenticationForm(),
                'mensaje': mensaje
            })
        else:
            login_sesion(request, user)
            return redirect('base')
        # print(request.POST)
        # return render(request, 'signin.html', {'formulario': AuthenticationForm()})
    # return render(request, 'signin.html', {'formulario': AuthenticationForm()})
