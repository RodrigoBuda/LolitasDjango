from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from AppLolitas.models import Producto
from django.utils.decorators import method_decorator


def index(request):
    context = {
        'active_page': 'inicio'
    }
    return render(request, 'AppLolitas/index.html', context)


def base(request):
    return render(request, 'AppLolitas/base.html')


def servicio(request):
    return render(request, 'AppLolitas/servicio.html')


def servicios(request):
    context = {
        'active_page': 'servicios'
    }
    return render(request, 'AppLolitas/servicios.html', context)


def sobre_nosotras(request):
    context = {
        'active_page': 'sobre_nosotras'
    }
    return render(request, 'AppLolitas/sobre_nosotras.html', context)


def tyc(request):
    context = {
        'active_page': 'tyc'
    }
    return render(request, 'AppLolitas/tyc.html', context)


def registro(request):

    if request.method == 'GET':
        return render(request, 'AppLolitas/registro.html', {
            'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('perfil')
            except IntegrityError:
                return render(request, 'AppLolitas/registro.html', {
                    'form': UserCreationForm,
                    "error": 'Username Already Exists'
                })
        return render(request, 'AppLolitas/registro.html', {
            'form': UserCreationForm,
            "error": 'Password do not match'
        })


@login_required
def perfil(request):
    users = User.objects.all()
    return render(request, 'AppLolitas/perfil.html', {'users': users})


def iniciar_sesion(request):

    if request.method == 'GET':
        return render(request, 'AppLolitas/iniciar_sesion.html', {'form': AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'AppLolitas/iniciar_sesion.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o Contraseña Incorrecta'
            })

        else:
            login(request, user)
            return redirect('perfil')


def cerrar_sesion(request):
    logout(request)
    return redirect('index')


@login_required
def reservas(request):

    return render(request, 'AppLolitas/reservas.html')


@login_required
class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.carrito = self.session.get("carrito", {})

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito:
            self.carrito[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "acumulado": producto.precio,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            item = self.carrito[id]
            item["cantidad"] -= 1
            item["acumulado"] -= producto.precio
            if item["cantidad"] <= 0:
                self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True


def get(self, request):
    context = {
        'active_page': 'tienda'
    }
    return render(request, 'AppLolitas/tienda.html', context)


class TiendaViewProductos(View):
    model: Producto
    success_url = reverse_lazy("Productos")

    def get(self, request):
        Productos = Producto.objects.all()
        context = {
            'active_page': 'tienda',
            'Productos': Productos
        }
        return render(request, 'AppLolitas/tienda.html', context)


@method_decorator(login_required, name='dispatch')
class CrearViewProducto(LoginRequiredMixin, CreateView):
    template_name = "crear_producto.html"
    model = Producto
    fields = ["name", "marca", "description", "price", "stock", "image"]
    success_url = reverse_lazy("crear_producto")
