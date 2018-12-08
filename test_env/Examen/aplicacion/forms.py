from django import forms
from .models import user,Tienda
import logging

class UsuarioModelForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ["username","password","is_staff"]

    def clean_nomUsuario(self):
        nombre = self.cleaned_data.get("username")
        #validaciones
        logger = logging.getLogger(__name__)
        logger.error(nombre)
        return nombre

    def clean_contrasenia(self):
        contrasenia = self.cleaned_data.get("password")
        #validaciones
        return contrasenia
    
    def clean_staff(self):
        logger = logging.getLogger(__name__)
        is_staff = self.cleaned_data.get("staff")
        logger.error(is_staff)
        return is_staff

class TiendaModelForm(forms.ModelForm):
    class Meta:
        model = Tienda
        fields = ["nombreTienda","nombreSucursal","direccion"]
    
    def clean_nomTienda(self):
        nombre = self.cleaned_data.get("nombreTienda")
        return nombre
    
    def clean_nomSucursal(self):
        sucursal = self.cleaned_data.get("nombreSucursal")
        return sucursal

    def clean_direc(self):
        direc = self.cleaned_data.get("direccion")
        return direc

class regUsuario(forms.Form):
    usuario = forms.CharField(max_length=50)
    contraseña = forms.CharField(max_length=50)

class regTienda(forms.Form):
    nombretienda = forms.CharField()
    nombresucursal = forms.CharField()
    direccion = forms.CharField()