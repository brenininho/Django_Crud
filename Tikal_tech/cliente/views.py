from django.views import generic
from .models import Client
from .forms import ClientForm, EmailForm, TelephoneForm
from django.shortcuts import render


def index(request):
    clientes = Client.objects.all()
    context = {'clientes': clientes}
    return render(request, 'cliente/index.html', context)


def delete(request):
    pass


def cliente(request):
    form_client = ClientForm()
    form_email = EmailForm()
    form_telephone = TelephoneForm

    if request.method == 'POST':
        form_client = ClientForm(request.POST)
        form_email = EmailForm(request.POST)
        form_telephone = TelephoneForm(request.POST)

        if form_client == "cliente":
            if form_client.is_valid():
                form_client.save()

        if form_email == "email":
            if form_email.is_valid():
                form_email.save()

        if form_telephone == "telephone":
            if form_telephone.is_valid():
                form_telephone.save()

    context = {'form': form_client}
    return render(request, 'cliente/cliente.html', context)




