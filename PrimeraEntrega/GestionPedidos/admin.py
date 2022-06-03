from django.contrib import admin
from GestionPedidos.models import *
# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "telefono")
    search_fields=("nombre", "telefono")

class ArticulosAdmin(admin.ModelAdmin):
    list_filter =("seccion",) 

class PedidosAdmin(admin.ModelAdmin):
    list_display = ("fecha", "entregado")
    list_filter = ("fecha",)
    date_hierarchy= "fecha"

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos,ArticulosAdmin)
admin.site.register(Pedidos,PedidosAdmin)