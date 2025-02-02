from django.urls import path
from . import views

urlpatterns = [
    path('politicas/', views.politicas_upload_view, name="politicas"),
]
