from django.shortcuts import render,get_object_or_404
from .models import Alumno,Frase
# Create your views here.

def Index_Vista(request):
    misalumnos=Alumno.objects.all().order_by("id")
    return render (request, 'index.html',{"misalumnos":misalumnos})

def Alumno_Vista(request,id):
    alumno= get_object_or_404(Alumno,id=id)
    return render (request, 'Alumno.html',{"objeto":alumno})