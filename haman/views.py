from django.shortcuts import render
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language
from shop.models import Persian_Index, Arabic_Index, English_Index
from blogs.models import Persian_IndexBlog, English_IndexBlog, Arabic_IndexBlog
from news.models import Persian_IndexNews, English_IndexNews, Arabic_IndexNews
from haman.models import ContactUSModel, SliderModel
# Create your views here.
def index(request):
    lang = get_language()
    if lang == "en":
        shop_baner = English_Index.objects.filter(is_enable=True)
        blogs_baner = English_IndexBlog.objects.filter(is_enable=True)
        news_banner = English_IndexNews.objects.filter(is_enable=True)
        foternews = news_banner[:2]
        foterblog = blogs_baner[:2]
    elif lang == "fa":
        shop_baner = Persian_Index.objects.filter(is_enable=True)
        blogs_baner = Persian_IndexBlog.objects.filter(is_enable=True)
        news_banner = Persian_IndexNews.objects.filter(is_enable=True)
        foternews = news_banner[:2]
        foterblog = blogs_baner[:2]
    else:
        shop_baner = Arabic_Index.objects.filter(is_enable=True)
        blogs_baner = Arabic_IndexBlog.objects.filter(is_enable=True)
        news_banner = Arabic_IndexNews.objects.filter(is_enable=True)
        foternews = news_banner[:2]
        foterblog = blogs_baner[:2]

    slider = SliderModel.objects.all()
    context = {
        "probanner":shop_baner,
        "blogsbanner":blogs_baner,
        "newsbanner":news_banner,
        "slides":slider,
        "footernews":foternews,
        "footerblogs":foterblog,
    }
    return render(request, "index.html", context=context)


def contact(request):
    lang = get_language()
    if lang == "en":
        blogs_baner = English_IndexBlog.objects.filter(is_enable=True)
        news_banner = English_IndexNews.objects.filter(is_enable=True)
        foternews = news_banner[:2]
        foterblog = blogs_baner[:2]
    elif lang == "fa":
        blogs_baner = Persian_IndexBlog.objects.filter(is_enable=True)
        news_banner = Persian_IndexNews.objects.filter(is_enable=True)
        foternews = news_banner[:2]
        foterblog = blogs_baner[:2]
    else:
        blogs_baner = Arabic_IndexBlog.objects.filter(is_enable=True)
        news_banner = Arabic_IndexNews.objects.filter(is_enable=True)
        foternews = news_banner[:2]
        foterblog = blogs_baner[:2]
    context = {
        "footernews": foternews,
        "footerblogs": foterblog,
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
    lang = get_language()
    if lang == "en":
        blogs_baner = English_IndexBlog.objects.filter(is_enable=True)
        news_banner = English_IndexNews.objects.filter(is_enable=True)
        foternews = news_banner[:2]
        foterblog = blogs_baner[:2]
    elif lang == "fa":
        blogs_baner = Persian_IndexBlog.objects.filter(is_enable=True)
        news_banner = Persian_IndexNews.objects.filter(is_enable=True)
        foternews = news_banner[:2]
        foterblog = blogs_baner[:2]
    else:
        blogs_baner = Arabic_IndexBlog.objects.filter(is_enable=True)
        news_banner = Arabic_IndexNews.objects.filter(is_enable=True)
        foternews = news_banner[:2]
        foterblog = blogs_baner[:2]
    context = {
        "footernews": foternews,
        "footerblogs": foterblog,
    }
    return render(request, 'about-us.html', context=context)

def team(request):
    lang = get_language()
    if lang == "en":
        blogs_baner = English_IndexBlog.objects.filter(is_enable=True)
        news_banner = English_IndexNews.objects.filter(is_enable=True)
        foternews = news_banner[:2]
        foterblog = blogs_baner[:2]
    elif lang == "fa":
        blogs_baner = Persian_IndexBlog.objects.filter(is_enable=True)
        news_banner = Persian_IndexNews.objects.filter(is_enable=True)
        foternews = news_banner[:2]
        foterblog = blogs_baner[:2]
    else:
        blogs_baner = Arabic_IndexBlog.objects.filter(is_enable=True)
        news_banner = Arabic_IndexNews.objects.filter(is_enable=True)
        foternews = news_banner[:2]
        foterblog = blogs_baner[:2]
    context = {
        "footernews": foternews,
        "footerblogs": foterblog,
    }
    return render(request, 'our-team.html', context=context)


def faq(request):
    lang = get_language()
    if lang == "en":
        blogs_baner = English_IndexBlog.objects.filter(is_enable=True)
        news_banner = English_IndexNews.objects.filter(is_enable=True)
        foternews = news_banner[:2]
        foterblog = blogs_baner[:2]
    elif lang == "fa":
        blogs_baner = Persian_IndexBlog.objects.filter(is_enable=True)
        news_banner = Persian_IndexNews.objects.filter(is_enable=True)
        foternews = news_banner[:2]
        foterblog = blogs_baner[:2]
    else:
        blogs_baner = Arabic_IndexBlog.objects.filter(is_enable=True)
        news_banner = Arabic_IndexNews.objects.filter(is_enable=True)
        foternews = news_banner[:2]
        foterblog = blogs_baner[:2]
    context = {
        "footernews": foternews,
        "footerblogs": foterblog,
    }
    return render(request, 'faq.html', context=context)
