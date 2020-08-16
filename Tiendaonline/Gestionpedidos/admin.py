from django.contrib import admin

from Gestionpedidos.models import Cliente, Articulo, Pedido

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","tfno")
    search_fields=("nombre","tfno")

class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero", "fecha","entregado")
    list_filter=("fecha",)
    date_hierarchy="fecha"

admin.site.register(Cliente,ClientesAdmin)
admin.site.register(Articulo, ArticulosAdmin)
admin.site.register(Pedido, PedidosAdmin)
