from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import user,Tienda,Producto,Lista,DetalleTienda,DetalleLista
from django.contrib.auth.models import User

# Register your models here.

# admin.site.unregister(User)

class MyUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
                'classes': ('wide',),
                'fields': ('extraData')}
    ),
    )

admin.site.register(user, MyUserAdmin)
admin.site.register(Producto)
admin.site.register(Lista)
admin.site.register(DetalleLista)
admin.site.register(DetalleTienda)
admin.site.register(Tienda)