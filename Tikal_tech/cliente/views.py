from django.views import generic
from .models import Client
from .forms import ClientForm, EmailForm, TelephoneForm
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def index(request):
    clientes = Client.objects.all()
    context = {'clientes': clientes}
    return render(request, 'cliente/index.html', context)


def delete(request):
    pass


def cliente(request, pk=None):
    if pk is not None:
        obj = get_object_or_404(Client, pk=pk)
        form_client = ClientForm(instance=obj)
        form_email = EmailForm(instance=obj)
        form_telephone = TelephoneForm(instance=obj)
    else:
        form_client = ClientForm()
        form_email = EmailForm()
        form_telephone = TelephoneForm()

    if request.method == 'POST':
        form_client = ClientForm(request.POST)
        form_email = EmailForm(request.POST)
        form_telephone = TelephoneForm(request.POST)

        if request.POST['form'] == "cliente":
            if form_client.is_valid():
                form_client.save()

        if request.POST['form'] == "email":
            if form_email.is_valid():
                form_email.save()

        if request.POST['form'] == "telephone":
            if form_telephone.is_valid():
                form_telephone.save()

    context = {
        'form_client': form_client,
        'form_email': form_email,
        'form_telephone': form_telephone,
    }

    return render(request, 'cliente/cliente.html', context)




