from django.shortcuts import render
from django.utils.translation import get_language
from news.models import Persian_IndexNews, English_IndexNews, Arabic_IndexNews
from blogs.models import Persian_IndexBlog, English_IndexBlog, Arabic_IndexBlog
# Create your views here.
def services(request):
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
    return render(request, 'services.html', context=context)

def refinery(request):
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
    return render(request, 'refinery.html', context=context)

def petrochemical(request):
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
    return render(request, 'Petrochemicals.html', context=context)

def global_trade(request):
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
    return render(request, 'global.html', context=context)

def food(request):
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
    return render(request, 'food.html', context=context)


def agriculture(request):
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
    return render(request, 'agriculture.html', context=context)

def support(request):
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
    return render(request, 'support.html', context=context)