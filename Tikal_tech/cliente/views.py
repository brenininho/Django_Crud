from django.http import HttpResponse
from .models import Client
from .models import Email
from .models import Telephone


def index(request):
    latest_client_list = Client.objects.order_by('-birth_date')
    print(latest_client_list[0].client_age())
    # output = ', '.join([q.question_text for q in latest_client_list])
    return HttpResponse("Hello, world. You're at the client index.")


def detail(request, cliente_id):
    return HttpResponse("You're looking at client %s." % cliente_id)


def results(request, cliente_id):
    response = "You're looking at the results of client %s."
    return HttpResponse(response % cliente_id)
