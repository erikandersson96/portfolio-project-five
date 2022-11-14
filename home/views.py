from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about(request):
    """
    A view for render about us page
    """

    return render(request, 'about/about.html')
