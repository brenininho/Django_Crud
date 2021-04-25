from .models import Client
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'cliente/index.html'
    context_object_name = 'data'

    def get_queryset(self):
        return Client.objects.order_by('-birth_date')


class DetailView(generic.DetailView):
    model = Client
    template_name = 'cliente/detail.html'

