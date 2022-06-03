from django import forms

class ProductoFormulario (forms.Form):
    nombre= forms.CharField(max_length=30)
    seccion= forms.CharField(max_length=20)
    precio= forms.IntegerField() 

class ClientesFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    direccion= forms.CharField(max_length=50)
    email= forms.EmailField(max_length=50)
    telefono= forms.CharField(max_length=10)

class PedidosFormulario(forms.Form):
    numero= forms.IntegerField()
    fecha= forms.DateField()
    entregado= forms.BooleanField()