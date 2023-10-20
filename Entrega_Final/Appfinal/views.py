from django.shortcuts import render
from django.http import HttpResponse
from .models import Estilos, Ingredientes, User, Imagen
from .forms import (BuscaEstilo, EstiloFormulario, UserRegisterform, UserEditForm,
                    MyUserEditForm)
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def inicio(request):
   
    return render(request, "Appfinal/index.html")

def cargar_estilo(request):

    if request.method == 'POST':
        estilo = Estilos(nombre=request.POST['nombre'],
                      color=request.POST['color'], amargor=request.POST['amargor'],
                      descripcion=request.POST['descripcion'])
        estilo.save()

        return render(request, "Appfinal/index.html")

    return render(request, "Appfinal/cargar_estilo.html")

def cargar_ingredientes(request):

    if request.method == 'POST':
        ingredientes = Ingredientes(estilo=request.POST['estilo'],
                      malta=request.POST['malta'], lupulo=request.POST['lupulo'],
                      levadura=request.POST['levadura'])
        ingredientes.save()

        return render(request, "Appfinal/index.html")

    return render(request, "Appfinal/cargar_ingredientes.html")

def buscar_estilo(request):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = BuscaEstilo(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            estilo = Estilos.objects.filter(
                nombre__icontains=informacion["estilo"])

            return render(request, "Appfinal/lista.html", {"estilos": estilo})
    else:
        miFormulario = BuscaEstilo()

    return render(request, "Appfinal/ver_estilos.html", {"miFormulario": miFormulario})

def ipa(request):
    return render(request, "Appfinal/ipa.html")

def scotish(request):
    return render(request, "Appfinal/scotish.html")

def golden(request):
    return render(request, "Appfinal/golden.html")

def apa(request):
    return render(request, "Appfinal/apa.html")

def blog(request):
    return render(request, "Appfinal/blog.html")

def nosotros(request):
    return render(request, "Appfinal/nosotros.html")

def ver_BD(request):

    estilos = Estilos.objects.all()  # trae todos los cursos

    contexto = {"estilos": estilos}

    return render(request, "Appfinal/leer_BD.html", contexto)

def delete_estilo(request, estilo_id):

    estilo = Estilos.objects.get(id=int(estilo_id))
    estilo.delete()

    # vuelvo al menú
    estilo = Estilos.objects.all()  # trae todos los cursos
    return render(request, "Appfinal/leer_BD.html", {"estilos": estilo})

def edit_estilo(request, estilo_id):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = EstiloFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            estilo = Estilos.objects.get(id=estilo_id)
            estilo.nombre = informacion["nombre"]
            estilo.color = informacion["color"]
            estilo.amargor = informacion["amargor"]
            estilo.descripcion = informacion["descripcion"]
            estilo.save()

            return render(request, "Appfinal/index.html")
    else:
        estilo = Estilos.objects.get(id=estilo_id)
        miFormulario = EstiloFormulario(
            initial={"nombre": estilo.nombre, "color": estilo.color, "amargor": estilo.amargor,
                     "descripcion": estilo.descripcion})

    return render(request, "Appfinal/editar_estilo.html", {"miFormulario": miFormulario})

def receta_blonde(request):
    return render(request, "Appfinal/receta_blonde.html")

def receta_ipa(request):
    return render(request, "Appfinal/receta_ipa.html")


def receta_porter(request):
    return render(request, "Appfinal/receta_porter.html")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request, "Appfinal/index.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                form = AuthenticationForm()
                return render(request, "Appfinal/login.html", {"mensaje": "Error, datos incorrectos", "form": form})

        else:
            return render(request, "Appfinal/index.html", {"mensaje": "Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "Appfinal/login.html", {"form": form})

def registrarse(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = UserRegisterform(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "Appfinal/index.html", {"mensaje": f"{username} Usuario Creado ;)"})
    else:
        # form = UserCreationForm()
        form = UserRegisterform(request.POST)

    return render(request, "Appfinal/registro.html", {"form": form})


def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = MyUserEditForm(request.POST, request.FILES)
        # archivo_form = AvatarForm(request.POST, request.FILES)

        if miFormulario.is_valid():  # and archivo_form.is_valid():

            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            # usuario.password1 = informacion['password1']
            # usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()

            # miFormulario.save()
            # perfil.avatar = archivo_form.cleaned_data["avatar"]
            # perfil.save()

            user = User.objects.get(username=request.user)
            try:
                avat = Imagen.objects.get(user=user)
            except Imagen.DoesNotExist:
                avat = Imagen(user=user, imagen=informacion.get("imagen"))
                avat.save()
            else:
                avat.imagen = miFormulario.cleaned_data["avatar"]
                avat.save()

            # archivo_form.save()

            return render(request, "Appfinal/index.html")
        else:
            miFormulario = MyUserEditForm()

    else:
        miFormulario = MyUserEditForm(
            initial={
                'email': usuario.email,
                'last_name': usuario.last_name,
                'first_name': usuario.first_name
            }
        )
    return render(request, "Appfinal/editarPerfil.html", {"miFormulario": miFormulario,
                                                      "usuario": usuario
                                                      }
                  )