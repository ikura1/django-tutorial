from django.http import HttpResponse


def index(request):
    return HttpResponse("Helo, world. You're at the polls index.")
