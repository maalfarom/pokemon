from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import user,Tienda,Producto,Lista,DetalleTienda,DetalleLista

# Register your models here.

admin.site.register(user, UserAdmin)
admin.site.register(Producto)
admin.site.register(Lista)
admin.site.register(DetalleLista)
admin.site.register(DetalleTienda)
admin.site.register(Tienda)