from django.shortcuts import render
from django.utils.translation import activate


# Create your views here.
def index(request):
    context = {

    }
    return render(request, "index.html", context=context)


def contact(request):
    context = {

    }
    return render(request, 'contact.html', context=context)

