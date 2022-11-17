from django.shortcuts import render
from django.contrib import messages


def subscription(request):
    if request.method == "POST":
        email = request.POST['email']
        print(email)
        messages.success(request, "Email received. Thank You!")

    return render(request, "newsletter/newsletter.html")
