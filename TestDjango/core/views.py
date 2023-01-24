from django.shortcuts import render
from .models import Categoria, Vehiculo

# Create your views here.
def home(request):
    return render(request, 'vehiculos.html')
    
def Vista_Vehiculos(request):
    vVehiculos = Vehiculo.objects.all()
    contexto = {
        'nombre':'PASCUAL DONSON',
        'vehiculos':vVehiculos}
    return render(request, 'core/vehiculos.html',contexto)