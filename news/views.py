from django.shortcuts import render
from django.utils.translation import get_language
from news.models import NewsModel, Arabic_IndexNews, English_IndexNews, Persian_IndexNews
from blogs.models import Persian_IndexBlog, English_IndexBlog, Arabic_IndexBlog
from django.core.paginator import Paginator
from django.http import HttpResponse
# Create your views here.
def news(request):
    page_number = request.GET.get("page", default=1)
    q = request.POST.get("search-field", default="").strip()
    lang = get_language()
    if lang == "fa":
        products1 = NewsModel.objects.filter(show_on_persian=True, title_persian__contains=q)
        shop_baner = Persian_IndexNews.objects.filter(is_enable=True)
        blogs_baner = Persian_IndexBlog.objects.filter(is_enable=True)
        foternews = shop_baner[:2]
        foterblog = blogs_baner[:2]
    elif lang == "en":
        products1 = NewsModel.objects.filter(show_on_english=True, title_english__contains=q)
        shop_baner = English_IndexNews.objects.filter(is_enable=True)
        blogs_baner = English_IndexBlog.objects.filter(is_enable=True)
        foternews = shop_baner[:2]
        foterblog = blogs_baner[:2]
    else:
        products1 = NewsModel.objects.filter(show_on_arabic=True, title_arabic__contains=q)
        shop_baner = Arabic_IndexNews.objects.filter(is_enable=True)
        blogs_baner = Arabic_IndexBlog.objects.filter(is_enable=True)
        foternews = shop_baner[:2]
        foterblog = blogs_baner[:2]
    products = Paginator(products1, 9)
    try:
        page = products.page(page_number)
    except:
        page = products.page(1)
    context = {
        "pagenator": products,
        "blogs": page,
        "blogsbaner": shop_baner,
        "footernews": foternews,
        "footerblogs": foterblog,
    }
    return render(request, 'news.html', context=context)
def detail(request, slug):
    lang = get_language()
    try:
        if lang == "fa":
            blog = NewsModel.objects.get(persian_slug=slug)
            shop_baner = Persian_IndexNews.objects.filter(is_enable=True)
            blogs_baner = Persian_IndexBlog.objects.filter(is_enable=True)
            foternews = shop_baner[:2]
            foterblog = blogs_baner[:2]
        elif lang == "en":
            blog = NewsModel.objects.get(english_slug=slug)
            shop_baner = English_IndexNews.objects.filter(is_enable=True)
            blogs_baner = English_IndexBlog.objects.filter(is_enable=True)
            foternews = shop_baner[:2]
            foterblog = blogs_baner[:2]
        else:
            blog = NewsModel.objects.get(arabic_slug=slug)
            shop_baner = Arabic_IndexNews.objects.filter(is_enable=True)
            blogs_baner = Arabic_IndexBlog.objects.filter(is_enable=True)
            foternews = shop_baner[:2]
            foterblog = blogs_baner[:2]
    except:
        return HttpResponse(f"Bad request with {slug}")

    tags = blog.tags.split(",")
    comm = blog.comments.filter(show=True)
    rev = len(comm)
    context = {
        "blogs": blog,
        "blogbaner": shop_baner,
        "tags": tags,
        "rev": rev,
        "comments": comm,
        "footernews": foternews,
        "footerblogs": foterblog,
    }
    return render(request, 'news-single.html', context=context)