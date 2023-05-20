from django.urls import path
from AppLolitas.views import index, servicio, servicios, sobre_nosotras, tyc, registro, perfil, iniciar_sesion, cerrar_sesion, reservas, base, Carrito, CrearViewProducto, TiendaViewProductos
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', index),
    path('index/', index, name="index"),
    path('base/', base, name="base"),
    path('servicio/', servicio, name="servicio"),
    path('servicios/', servicios, name="servicios"),
    path('sobre_nosotras/', sobre_nosotras, name="sobre_nosotras"),
    path('tyc', tyc, name="tyc"),
    path('registro/', registro, name="registro"),
    path('perfil/', perfil, name="perfil"),
    path('reservas/', reservas, name="reservas"),
    path('iniciar_sesion/', iniciar_sesion, name="iniciar_sesion"),
    path('logout/', cerrar_sesion, name="cerrar_sesion"),
    path('carrito/', Carrito, name="carrito"),
    path('tienda/', TiendaViewProductos.as_view(), name="tienda"),
    path('crear_producto/', CrearViewProducto.as_view(), name="crear_producto"),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
