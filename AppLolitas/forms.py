from AppLolitas.models import Producto
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Product_Form(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["name", "marca", "description", "price", "stock", "image"]
