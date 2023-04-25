from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
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
from django.http import HttpResponse
from django.db import IntegrityError


def index(request):
    return render(request, 'AppLolitas/index.html')


def servicio(request):
    return render(request, 'AppLolitas/servicio.html')


def servicios(request):
    return render(request, 'AppLolitas/servicios.html')


def sobre_nosotros(request):
    return render(request, 'AppLolitas/sobre_nosotros.html')


def tyc(request):
    return render(request, 'AppLolitas/tyc.html')


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
    return render(request, 'AppLolitas/perfil.html')


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
