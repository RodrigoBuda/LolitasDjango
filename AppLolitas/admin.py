from django.contrib import admin
from .models import Usuaria, Producto, Servicios

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)


admin.site.register(Usuaria, TaskAdmin)
admin.site.register(Producto)
admin.site.register(Servicios)
