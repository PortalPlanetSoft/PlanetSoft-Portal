from django.http import HttpResponse

def index(request):
    return HttpResponse("index")

def employees(request):
    return HttpResponse("employees")