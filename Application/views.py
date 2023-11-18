from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Usuario, Empleado, Sucursal, Gerente, JefeTaller, AsesorComercial,Cliente
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import EmpleadoForm, GerenteForm, JefeTallerForm, AsesorComercialForm, SucursalForm, UsuarioForm,ClienteForm
from django.db import IntegrityError
from django.core.exceptions import ValidationError

def home(request):
    return render(request, 'home.html')

"""" esta funcion tiene como objectivo redirigir el login, es deecir con esto miramos que el formulario haga lo correspondiente a una vista en pantalla  """

def signIn(request):
    if request.method == 'GET':
        return render(request, 'fomularioInicio.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, id_usuario = request.POST['username'], contrasena = request.POST['password'])
        if user is None:
            return render(request, 'fomularioInicio.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('home.html')
    
""" fin de la funcion de login """



"""basandonos en la funcion de login y tratando de entender mejor podemos suponer 
lo siguiente, 
para poder hacer funcionar las diferentes interfaces de HTML ya antes definidas
tenemos que tener 

ursl.py -->para redefininr los nombres de los HTML 
views.py  --->  que son las funciones para ejecutar los HTML como vistas 

y esto nos da pie de hacer codigo de python para la misma logica de los formularios 
"""


"""ahora hacemos los otros formularios para que sean como vistas """
def interfaz_P(request):
    # Puedes agregar lógica adicional aquí si es necesario
     clientes = Cliente.objects.all()
     return render(request, 'interfaz_P.html',{'clientes': clientes})

def EdicionEmpleados(request):
    # Puedes agregar lógica adicional aquí si es necesario
    return render(request, 'EdicionEmpleados.html')

def formularioResgistroCliente(request):
    # Puedes agregar lógica adicional aquí si es necesario
    return render(request, 'formularioResgistroCliente.html')

def fromularioRegistroReparacion(request):
    # Puedes agregar lógica adicional aquí si es necesario
    return render(request, 'fromularioRegistroReparacion.html')

def formularioRegistroRepuesto(request):
    # Puedes agregar lógica adicional aquí si es necesario
    return render(request, 'formularioRegistroRepuesto.html')

def formularioRegistroAutomoviles(request):
    # Puedes agregar lógica adicional aquí si es necesario
    return render(request, 'formularioRegistroAutomoviles.html')



""""""

def signUp(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            Empleado = form.save()  # Guardar el empleado en la base de datos
            return redirect('cargoSignUp', empleado_id = Empleado.id)
    else:
        form = EmpleadoForm()
    return render(request, 'CargoForm.html', {'form': form})

def empleadoSignUp(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.save()
            print(f'Registrando empleado con ID: {empleado.id_empleado}') 
            return redirect('cargoSignUp', empleado_id=empleado.id_empleado)
    else:
        form = EmpleadoForm()
    return render(request, 'EmpleadoForm.html', {'form': form})


def cargoSignUp(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    form = None
    if request.method == 'POST':
        if empleado.cargo == 'GERENTE':
            form = GerenteForm(request.POST)
        elif empleado.cargo == 'JEFE DE TALLER':
            form = JefeTallerForm(request.POST)
        elif empleado.cargo == 'ASESOR COMERCIAL':
            form = AsesorComercialForm(request.POST)
        if form and form.is_valid():
            cargo = form.save(commit=False)  # Crea un objeto Cargo pero no lo guarda en la base de datos todavía
            cargo.empleado = empleado  # Asocia el empleado con el cargo
            cargo.save()  # Guarda el objeto Cargo en la base de datos
            return redirect('usuarioSignUp', id_empleado=empleado.id_empleado)
    else:
        if empleado.cargo == 'GERENTE':
            form = GerenteForm()
        elif empleado.cargo == 'JEFE DE TALLER':
            form = JefeTallerForm()
        elif empleado.cargo == 'ASESOR COMERCIAL':
            form = AsesorComercialForm()
    return render(request, 'CargoForm.html', {'form': form})


def usuarioSignUp(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()  # Guarda el objeto Usuario en la base de datos y lo devuelve
            if empleado.cargo == 'GERENTE':
                cargo = Gerente.objects.get(id_gerente=empleado.id_empleado)
            elif empleado.cargo == 'JEFE DE TALLER':
                cargo = JefeTaller.objects.get(id_jefe_taller=empleado.id_empleado)
            elif empleado.cargo == 'ASESOR COMERCIAL':
                cargo = AsesorComercial.objects.get(id_asesor_comercial=empleado.id_empleado)
            cargo.id_usuario = usuario  # Asocia el usuario con el cargo
            cargo.save()  # Guarda el objeto Cargo en la base de datos
            return redirect('SignIn')  # Redirige a la página de inicio de sesión después del registro
    else:
        form = UsuarioForm()
    return render(request, 'UsuarioForm.html', {'form': form})

def ingresarSucursal(request):
    if request.method == 'POST':
        form = SucursalForm(request.POST)
        if form.is_valid():
            try:
                cod_sucursal = form.cleaned_data['cod_sucursal']
                if Sucursal.objects.filter(cod_sucursal=cod_sucursal).exists():
                    raise ValidationError('Este código de sucursal ya existe.')
                form.save()
                print("Ingreso exitoso:", form.cleaned_data)  # Muestra los datos ingresados en consola
                return redirect('home')
            except ValidationError as e:
                form.add_error('cod_sucursal', e)
    else:
        form = SucursalForm()

    context = {
        'form': form,
    }
    return render(request, 'SucursalForm.html', context)












"""registrar un usuario o cliente ...."""


"""""
def formularioRegistroCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)  # Muestra los datos antes de guardarlos
            form.save()
            return redirect('interfaz_P')
    else:
        form = ClienteForm()

    return render(request, 'formularioRegistroCliente.html', {'form': form})
"""

def formularioRegistroCliente(request):
    datos_guardados = None  # Inicializamos la variable para almacenar los datos guardados

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)  # Muestra los datos antes de guardarlos
            datos_guardados = form.cleaned_data  # Almacenamos los datos antes de guardarlos
            form.save()
            return redirect('interfaz_P')
    else:
        form = ClienteForm()

    return render(request, 'formularioRegistroCliente.html', {'form': form, 'datos_guardados': datos_guardados})