from django.shortcuts import render

# Create your views here.
def services(request):
    context = {

    }
    return render(request, 'services.html', context=context)

def refinery(request):
    context = {
        "name":'refinery',
    }
    return render(request, 'refinery.html', context=context)