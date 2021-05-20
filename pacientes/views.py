from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente


def inicio(request):
    return render(request, 'index.html')

 
def medicos(request):

    pacientes_atr = Paciente.objects.all()
    
    args = {"pacientes_info": pacientes_atr}   

    return render(request, 'medicos.html', args)

def mesaentrada(request):

    nombre_paciente = request.POST.get('nombre', False)
    telefono_paciente = request.POST.get('telefono', False)
    sintomas_paciente = request.POST.get('sintomas', False)

    if nombre_paciente == False and telefono_paciente == 0 and sintomas_paciente == False:
        print('No se guarda en la base de datos.')
        return render(request, "mesaentrada.html")

    else:
         pacientes_info = Paciente(nombre = nombre_paciente, telefono = telefono_paciente, sintomas = sintomas_paciente)
         pacientes_info.save()
                                                     
    return render(request, 'mesaentrada.html')


def eliminar_pacientes(request,id):
    Paciented = get_object_or_404(Paciente, id = id)
    Paciented.delete()
    return redirect(to = 'medicos')





