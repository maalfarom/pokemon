from django.shortcuts import render
from django.contrib.auth import authenticate,login
from .forms import regUsuario, UsuarioModelForm , regTienda,TiendaModelForm
from .models import user,Tienda

# Create your views here.

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

