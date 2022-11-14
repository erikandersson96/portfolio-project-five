from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about(request):
    """
    A view for render about us page
    """

    return render(request, 'about/about.html')


def contact(request):
    """
    A view for render contact us page
    """

    return render(request, 'contact/contact.html')
