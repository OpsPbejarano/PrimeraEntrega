import re
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from GestionPedidos.models import *
from GestionPedidos.forms import *
# Create your views here.

def index(request):
    return render(request, 'GestionPedidos/index.html') 

def agregarProducto(request): 
    if request.method == 'POST':

        formularioProdcuto = ProductoFormulario(request.POST)
        print (formularioProdcuto)

        if formularioProdcuto.is_valid:
            informacion = formularioProdcuto.cleaned_data
            producto= Articulos(nombre=informacion['nombre'], seccion=informacion['seccion'], precio=informacion['precio'])
            producto.save()

            return render (request,"GestionPedidos/index.html" )
    
    else:
        formularioProdcuto= ProductoFormulario() 
        return render(request, 'GestionPedidos/ingresarproducto.html', {'formularioProdcuto': formularioProdcuto})

def agregarCliente(request):
    if request.method == 'POST':

        formularioCliente = ClientesFormulario(request.POST)
        print (formularioCliente)

        if formularioCliente.is_valid:
            informacion = formularioCliente.cleaned_data
            cliente= Clientes(nombre=informacion['nombre'], direccion=informacion['direccion'], email=informacion['email'], telefono=informacion['telefono'])
            cliente.save()

            return render (request,"GestionPedidos/index.html" )
    
    else:
        formularioCliente= ClientesFormulario() 
        return render(request, 'GestionPedidos/ingresarcliente.html', {'formularioCliente': formularioCliente})

def hacerPedido(request):
    if request.method == 'POST':

        formularioPedido = PedidosFormulario(request.POST)
        print (formularioPedido)

        if formularioPedido.is_valid:
            informacion = formularioPedido.cleaned_data
            pedido= Pedidos(numero=informacion['numero'], fecha=informacion['fecha'], entregado=informacion['entregado'])
            pedido.save()

            return render (request,"GestionPedidos/index.html" )
    
    else:
        formularioPedido= PedidosFormulario() 
        return render(request, 'GestionPedidos/hacerpedido.html', {'formularioPedido': formularioPedido})

def busquedaProducto(request):

    return render(request, "GestionPedidos/busquedaproducto.html")

def buscar(request):

    if request.GET["producto"]:

        busqueda= request.GET['producto']
        productos= Articulos.objects.filter(nombre__icontains=busqueda)

        return render (request, "GestionPedidos/resultadobusqueda.html", {"busqueda": busqueda, "productos": productos}  )

    else: 
        respuesta = "no se enviaron datos"
        return HttpResponse(respuesta)
