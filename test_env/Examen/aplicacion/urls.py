from django.urls import path

from . import views

urlpatterns = [
    path('', views.loginn, name='loginn'),
    path('oauth', views.logiin, name='logiin'),
]