from django.shortcuts import render

# Create your views here.
def services(request):
    context = {

    }
    return render(request, 'services.html', context=context)

def refinery(request):
    context = {

    }
    return render(request, 'refinery.html', context=context)

def petrochemical(request):
    context = {

    }
    return render(request, 'Petrochemicals.html', context=context)

def global_trade(request):
    context = {

    }
    return render(request, 'global.html', context=context)

def food(request):
    context = {

    }
    return render(request, 'food.html', context=context)


def agriculture(request):
    context = {

    }
    return render(request, 'agriculture.html', context=context)

def support(request):
    context = {

    }
    return render(request, 'support.html', context=context)