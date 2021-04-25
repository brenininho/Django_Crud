from django.views import generic
from .models import Client
from .forms import ClientForm
from django.shortcuts import render


def index(request):
    clientes = Client.objects.all()
    context = {'clientes': clientes}
    return render(request, 'cliente/index.html', context)


def delete(request):
    pass


def cliente(request):

    return render(request, 'cliente/cliente.html', context)




