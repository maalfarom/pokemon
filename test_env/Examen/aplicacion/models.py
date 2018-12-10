from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class user(AbstractUser):
    pass
    extraData = models.CharField(max_length=100, null=True)

class Lista(models.Model):
    nombreLista = models.CharField(max_length=50)
    total =  models.IntegerField(default=0)
    nombreUsuario = models.ForeignKey(user, on_delete=models.CASCADE, related_name='usuarioLista')

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=50)

class Tienda(models.Model):
    nombreTienda = models.CharField(max_length=50, primary_key=True)
    nombreSucursal = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)


class DetalleLista(models.Model):
    idLista = models.ForeignKey(Lista, on_delete=models.CASCADE, related_name='listaDetalleLista')
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='productoDetalleLista')

class DetalleTienda(models.Model):
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='productoDetalleTienda')
    nombreTienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, related_name='tiendaDetalleTienda')
    precio = models.IntegerField(default=0)

