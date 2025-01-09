from django.shortcuts import render
from django.utils.translation import activate


# Create your views here.
def index(request):
    # activate('fa')
    context = {
        "test":"zahra is debar"
    }
    return render(request, "index.html", context=context)


def index2(request):
    # activate('fa')
    return render(request, "index.html")

