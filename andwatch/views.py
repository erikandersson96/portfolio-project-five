from django.shortcuts import render


def handler404(request, exception):
    """
    A view for Error 404 - Page Not Found
    """
    return render(request, "errors/404.html", status=404)


def handler403(request, exception):
    """
    A view for Error 403 - Forbidden resource
    """
    return render(request, "errors/403.html", status=403)


def handler500(request, exception):
    """
    A view for Error 500 - Server not responding
    """
    return render(request, "errors/403.html", status=403)


def handler400(request, exception):
    """
    A view for Error 400 - Bad request
    """
    return render(request, "errors/400.html", status=400)
