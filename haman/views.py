from django.shortcuts import render
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from haman.models import ContactUSModel
# Create your views here.
def index(request):
    context = {

    }
    return render(request, "index.html", context=context)


def contact(request):
    context = {

    }
    return render(request, 'contact.html', context=context)

def contactformsaver(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        username = request.POST['username']
        if username == '':
            return JsonResponse({'success': False, 'message': _('name is required')})
        email = request.POST['email']
        if email == '':
            return JsonResponse({'success': False, 'message': _('email is required')})
        number = request.POST['number']
        message = request.POST['message']
        if message == '':
            return JsonResponse({'success': False, 'message': f"{_('message is required')}"})
        print(request.POST)



    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

def about(request):
    context = {

    }
    return render(request, 'about-us.html', context=context)

def team(request):
    context = {

    }
    return render(request, 'our-team.html', context=context)


def faq(request):
    context = {

    }
    return render(request, 'faq.html', context=context)
