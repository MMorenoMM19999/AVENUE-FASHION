"""
URL configuration for Concesionario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Application import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('SignIn/', views.signIn, name='SignIn'),
    path('empleadoSignUp/', views.empleadoSignUp, name='empleadoSignUp'),
    path('ingresar_sucursal/', views.ingresarSucursal, name='ingresar_sucursal'),
    path('cargoSignUp/<int:id_empleado>/', views.cargoSignUp, name='cargoSignUp'),
    path('usuarioSignUp/<int:id_empleado>/', views.usuarioSignUp, name='usuarioSignUp'),



    path('interfaz_P/', views.interfaz_P, name='interfaz_P'),
    path('EdicionEmpleados/', views.EdicionEmpleados, name='EdicionEmpleados'),
    path('formularioResgistroCliente/', views.formularioResgistroCliente, name='formularioResgistroCliente'),
 path('fromularioRegistroReparacion/', views.fromularioRegistroReparacion, name='fromularioRegistroReparacion'),
path('formularioRegistroRepuesto/', views.formularioRegistroRepuesto, name='formularioRegistroRepuesto'),
path('formularioRegistroAutomoviles/', views.formularioRegistroAutomoviles, name='formularioRegistroAutomoviles'),


 path('formularioRegistroCliente/', views.formularioRegistroCliente, name='formularioRegistroCliente'),
 
 
]
