from django.shortcuts import render


def index(request):
    return render(request, 'portal/global/base.html')
