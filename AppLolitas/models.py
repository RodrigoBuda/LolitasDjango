from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Usuaria(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '-' + self.user.username


class Producto(models.Model):
    name = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.FloatField()
    stock = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to='productos/', blank=True, null=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.name + ' - ' + self.marca


class Servicios(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='servicios/')
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
