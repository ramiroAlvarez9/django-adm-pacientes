from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('medicos/', views.medicos, name = "medicos"),
    path('mesaentrada/', views.mesaentrada, name = "mesaentrada"),
    path('eliminar_pacientes/<id>/', views.eliminar_pacientes, name = "eliminar_pacientes"),
    path('registro-exitoso/', views.registro_exitoso, name = "registro_exitoso"),

]