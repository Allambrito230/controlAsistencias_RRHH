from django.shortcuts import render
from django.http import JsonResponse


def politicas_upload_view(request):
    return render(request, 'politicasAsistencia.html')
