from django.shortcuts import render



# Create your views here.
def index(request):
    context = {

    }
    return render(request, "index.html", context=context)


def contact(request):
    context = {

    }
    return render(request, 'contact.html', context=context)



def about(request):
    context = {

    }
    return render(request, 'about-us.html', context=context)

def team(request):
    context = {

    }
    return render(request, 'our-team.html', context=context)

