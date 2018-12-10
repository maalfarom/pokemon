from django.shortcuts import render
from django.contrib.auth import authenticate,login
from .forms import regUsuario, UsuarioModelForm , regTienda,TiendaModelForm
from .models import user,Tienda,DetalleTienda,Producto
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
# Create your views here.

@login_required
def logiin(request):
    return render(request, 'aplicacion/index.html')

def index(request):
    form = UsuarioModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "el_form": form,
    }
    return render(request, 'aplicacion/usuario.html',context)

def loginn(request):
    return render(request, 'registration/login.html')

def indexs(request):
    return render(request, 'aplicacion/index.html')

def registro(request):
    form = UsuarioModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "el_form":form,
    }
    return render(request, 'aplicacion/registro.html', context)

def forma(request):
    return render(request, 'aplicacion/foma.html')

def tienda(request):
    form = TiendaModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "el_form": form,
    }
    return render(request, 'aplicacion/tienda.html',context)

class ProductoList(ListView):
    model = Producto
    template_name = 'aplicacion/menu.html'
    paginate_by = 6

def menuu(request):
    lista = DetalleTienda.objects.all()
    return render(request, 'aplicacion/detalle.html',{'listas':lista})

