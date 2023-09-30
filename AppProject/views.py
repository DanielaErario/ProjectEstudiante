from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return render(request, "AppProject/inicio.html")

def cursos(request):
    return render(request, "AppProject/cursos.html")

def profesores(request):
    return render(request, "AppProject/profesores.html")

def estudiantes(request):
    return render(request, "AppProject/estudiantes.html")

def entregables(request):
    return render(request, "AppProject/entregables.html")