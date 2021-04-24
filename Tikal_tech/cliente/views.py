from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, cliente_id):
    return HttpResponse("You're looking at question %s." % cliente_id)


def results(request, cliente_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % cliente_id)


def vote(request, cliente_id):
    return HttpResponse("You're voting on question %s." % cliente_id)
