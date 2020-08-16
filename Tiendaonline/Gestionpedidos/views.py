from django.shortcuts import render
from django.http import HttpResponse
from Gestionpedidos.models import Articulo
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def busqueda_productos (request):
    return render(request, "busquedaproductos.html")

def buscar (request):

    if request.GET["prd"]:

        #mensaje= "Artículo buscado: %r" %request.GET["prd"]
        producto = request.GET["prd"]

        if len(producto)>20:
            mensaje="Texto demasiado largo"
        
        else:

            articulos = Articulo.objects.filter(nombre__icontains=producto)

            return render(request, "resultados_busqueda.html", {"articulos":articulos, "query":producto})

    
    else:
        mensaje="Debe de introducir un Artículo"

    return HttpResponse(mensaje)

def contacto(request):

        if request.method == "POST":

            subject=request.POST["asunto"]

            message=request.POST["mensaje"] + " " + request.POST["email"]

            email_from=settings.EMAIL_HOST_USER

            recipient_list=["proyectgit@gmail.com"]

            send_mail(subject,message,email_from,recipient_list)

            return render(request, "gracias.html")

        return render(request, "contacto.html")
