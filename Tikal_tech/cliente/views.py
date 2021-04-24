from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the client index.")


def detail(request, cliente_id):
    return HttpResponse("You're looking at client %s." % cliente_id)


def results(request, cliente_id):
    response = "You're looking at the results of client %s."
    return HttpResponse(response % cliente_id)
