from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):

    def __init__(self, nombre, apellido):

        self.nombre = nombre

        self.apellido = apellido


def saludo(request):

    p1 = Persona("Camila" , "Arigón")

    #nombre = "Camila"

    #apellido = "Arigón"

    temas = [1, 2, 3, 4, 5]

    ahora = datetime.datetime.now()

    #doc_externo = open("C:/Users/Matias/Desktop/django.code/Proyecto1/Proyecto1/plantillas/miplantilla.html") #se abre la ruta del documento

    #plt = Template(doc_externo.read()) #se lo prepara para leerlo

    #doc_externo.close() #se cierra el flujo
    
    #doc_externo = get_template("miplantilla.html")
    
    #aca se quita el doc_externo = loader.get_template() #da un pemplate pero diferente que no se admite por render

    #ctx = Context({"mi_nombre": p1.nombre, "mi_apellido": p1.apellido, "este_momento": ahora, "temas_uno": temas}) #se crea el contexto

    #documento = plt.render(ctx) #reenderizar el documento
    
    #documento = doc_externo.render({"mi_nombre": p1.nombre, "mi_apellido": p1.apellido, "este_momento": ahora, "temas_uno": temas})#se pone directamente el diccionario en el render
    
    #return HttpResponse(documento) #con el modulo shortcuts y metodo render esta linea no es necesaria

    return render(request, "miplantilla.html", {"mi_nombre": p1.nombre, "mi_apellido": p1.apellido, "este_momento": ahora, "temas_uno": temas})
    
def paghijados (request):

    p1 = Persona("Camila" , "Arigón")

    return render(request, "paghijados.html", {"mi_nombre": p1.nombre})

def paghija(request):

    ahora = datetime.datetime.now()

    return render(request, "paghija.html", {"este_momento": ahora})

def despedida(request):

    return HttpResponse("chau")

def damefecha(request):

    fecha_actual = datetime.datetime.now()

    documento=f"""<html><body><h2>fecha y hora actuales {fecha_actual}</h2></body><html>"""

    return HttpResponse(documento)

def calculaedad(request,edad, agno):

    #edadActual = 20
    periodo=agno-2020
    edadFutura=edad+periodo
    documento=f"""<html><body><h2>En el año {agno}, tendrás {edadFutura} años</h2></body><html>"""  

    return HttpResponse(documento)  
