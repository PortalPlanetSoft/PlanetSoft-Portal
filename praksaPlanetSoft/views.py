from django.shortcuts import render


def error_500(request, exception=None):
    return render(request, "errors/500.html", {'error_message': exception})


def error_404(request, exception):
    return render(request, "errors/404.html", {'error_message': exception})


def error_403(request, exception=None):
    return render(request, "errors/403.html", {'error_message': exception})


def error_400(request, exception=None):
    return render(request, "errors/400.html", {'error_message': exception})
