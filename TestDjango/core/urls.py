from django.urls import path
from .views import home, Vista_Vehiculos

urlpatterns = [
    path('',home,name="home"),
    path('vehiculos',Vista_Vehiculos,name="vehiculos"),
]

