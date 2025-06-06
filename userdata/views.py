from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language
from django.http import JsonResponse
from json import loads, JSONDecodeError
from haman.models import NewsShelterModel, ContactUSModel
from shop.models import ReviewModel, ProductsModel
from blogs.models import BlogsModel, ReviewModelBlog
from news.models import NewsModel, ReviewModelNews
from django.db.utils import IntegrityError
# Create your views here.


def newsletter(request):
    x1 = _('you are subscribe successfully')
    x3 = _('Invalid request')
    x2 = _('your email is subscribed already')
    x4 = _('Method Not allowed')
    if request.method == 'POST':
        try:

            data = loads(request.body)
            name = data['name']
            email = data['email']
            user = NewsShelterModel(name=name, email=email)
            user.save()
            return JsonResponse({'status':'success', 'message':x1})
        except JSONDecodeError:
            return JsonResponse({'status':'error', 'message':x3}, status=400)
        except IntegrityError:
            return JsonResponse({'status': 'error', 'message': x2}, status=400)
        except:
            return JsonResponse({'status': 'error', 'message': x3}, status=400)
    return JsonResponse({'status':'error', 'message':x4}, status=405)


def shop_comment(request):
    x1 = _('you comment save successfully')
    x3 = _('Invalid request')
    x4 = _('Method Not allowed')
    if request.method == 'POST':
        try:

            data = loads(request.body)
            name = data['name']
            email = data['email']
            phone = data['phone']
            comment = data['comment']
            prikey = data['prikey']
            usercomment = ReviewModel.objects.create(name=name, email=email, phone=phone, comment=comment, rate="*****")
            product = ProductsModel.objects.get(id=prikey)
            product.comments.add(usercomment)
            product.save()
            return JsonResponse({'status': 'success', 'message': x1})
        except JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': x3}, status=400)
        except:
            return JsonResponse({'status': 'error', 'message': x3}, status=400)
    return JsonResponse({'status': 'error', 'message': x4}, status=405)


def blog_comment(request):
    x1 = _('you comment save successfully')
    x3 = _('Invalid request')
    x4 = _('Method Not allowed')
    if request.method == 'POST':
        try:

            data = loads(request.body)
            name = data['name']
            email = data['email']
            phone = data['phone']
            comment = data['comment']
            prikey = data['prikey']
            usercomment = ReviewModelBlog.objects.create(name=name, email=email, phone=phone, comment=comment, rate="*****")
            product = BlogsModel.objects.get(id=prikey)
            product.comments.add(usercomment)
            product.save()
            return JsonResponse({'status': 'success', 'message': x1})
        except JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': x3}, status=400)
        except:
            return JsonResponse({'status': 'error', 'message': x3}, status=400)
    return JsonResponse({'status': 'error', 'message': x4}, status=405)



def news_comment(request):
    x1 = _('you comment save successfully')
    x3 = _('Invalid request')
    x4 = _('Method Not allowed')
    if request.method == 'POST':
        try:

            data = loads(request.body)
            name = data['name']
            email = data['email']
            phone = data['phone']
            comment = data['comment']
            prikey = data['prikey']
            usercomment = ReviewModelNews.objects.create(name=name, email=email, phone=phone, comment=comment, rate="*****")
            product = NewsModel.objects.get(id=prikey)
            product.comments.add(usercomment)
            product.save()
            return JsonResponse({'status': 'success', 'message': x1})
        except JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': x3}, status=400)
        except:
            return JsonResponse({'status': 'error', 'message': x3}, status=400)
    return JsonResponse({'status': 'error', 'message': x4}, status=405)


def contact_ua(request):
    x1 = _('your message save successfully')
    x3 = _('Invalid request')
    x4 = _('Method Not allowed')
    if request.method == 'POST':
        try:
            data = loads(request.body)
            name = data['name']
            email = data['email']
            phone = data['phone']
            message = data['message']
            subject = data['subject']
            usermessage = ContactUSModel(name=name, phone=phone, email=email, subject=subject, message=message)
            usermessage.save()
            return JsonResponse({'status': 'success', 'message': x1})
        except JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': x3}, status=400)
        except:
            return JsonResponse({'status': 'error', 'message': x3}, status=400)
    return JsonResponse({'status': 'error', 'message': x4}, status=405)



def contact_ua_footer(request):
    x1 = _('your message save successfully')
    x3 = _('Invalid request')
    x4 = _('Method Not allowed')
    if request.method == 'POST':
        try:
            data = loads(request.body)
            name = data['name']
            email = data['email']
            message = data['message']
            usermessage = ContactUSModel(name=name, email=email, message=message)
            usermessage.save()
            return JsonResponse({'status': 'success', 'message': x1})
        except JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': x3}, status=400)
        except:
            return JsonResponse({'status': 'error', 'message': x3}, status=400)
    return JsonResponse({'status': 'error', 'message': x4}, status=405)
