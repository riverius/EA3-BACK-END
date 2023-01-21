from django.urls import path
from .views import home, inicio

urlpatterns = [
    path('',home,name="home"),
    path('',inicio,name="inicio"),
]