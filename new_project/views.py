from django.http import HttpResponse
from django.template import Template,Context
from django.template import loader
from AppProject.models import Curso

def saludo(request):
    return HttpResponse("Hola mundo")

def mostrar_nombre(request,nombre):
    return HttpResponse(f"Buenos dias {nombre}")

def probando_template(request):
    nombre = "Jorge"
    apellido = "Viano"
    diccionario = {"nombre":nombre, "apellido":apellido,"notas":[3,2,4,5,6,7]}
    plantilla = loader.get_template('index.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def curso(request,nombre,numero):
    curso = Curso(nombre=nombre,camada = int(numero))
    curso.save()
    documento = f"Curso: {curso.nombre} <br>Camada:{curso.camada}"
    return HttpResponse(documento)
