from django.views import generic
from .models import Client
from .forms import ClientForm
from django.shortcuts import render


def index(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'cliente/index.html', context)


class DetailView(generic.DetailView):
    model = Client
    template_name = 'cliente/detail.html'



