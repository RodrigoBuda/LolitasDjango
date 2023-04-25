from django.urls import path
from AppLolitas.views import index, servicio, servicios, sobre_nosotros, tyc, registro, perfil, iniciar_sesion, cerrar_sesion, reservas
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', index),
    path('index/', index, name="index"),
    path('servicio/', servicio, name="servicio"),
    path('servicios/', servicios, name="servicios"),
    path('sobre_nosotros/', sobre_nosotros, name="sobre_nosotros"),
    path('tyc', tyc, name="tyc"),
    path('registro/', registro, name="registro"),
    path('perfil/', perfil, name="perfil"),
    path('reservas/', reservas, name="reservas"),
    path('iniciar_sesion/', iniciar_sesion, name="iniciar_sesion"),
    path('logout/', cerrar_sesion, name="cerrar_sesion"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
