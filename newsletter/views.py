from django.shortcuts import render
from django.contrib import messages


def subscription(request):
    """
    View for handle email when user click on submit in newsletter
    form
    """
    if request.method == "POST":
        messages.success(request, "Email received. Thank You!")

    return render(request, "newsletter/newsletter.html")
