from django.shortcuts import render
from django.utils.translation import get_language
from blogs.models import BlogsModel, Arabic_IndexBlog, English_IndexBlog, Persian_IndexBlog
from news.models import Persian_IndexNews, English_IndexNews, Arabic_IndexNews
from django.core.paginator import Paginator
from django.http import HttpResponse
# Create your views here.




def blogs(request):
    page_number = request.GET.get("page", default=1)
    q = request.POST.get("search-field", default="").strip()
    lang = get_language()
    if lang == "fa":
        products1 = BlogsModel.objects.filter(show_on_persian=True, title_persian__contains=q)
        shop_baner = Persian_IndexBlog.objects.filter(is_enable=True)
        news_banner = Persian_IndexNews.objects.filter(is_enable=True)
        foternews = news_banner[:2]
        foterblog = shop_baner[:2]
    elif lang == "en":
        products1 = BlogsModel.objects.filter(show_on_english=True, title_english__contains=q)
        shop_baner = English_IndexBlog.objects.filter(is_enable=True)
        news_banner = English_IndexNews.objects.filter(is_enable=True)
        foternews = news_banner[:2]
        foterblog = shop_baner[:2]
    else:
        products1 = BlogsModel.objects.filter(show_on_arabic=True, title_arabic__contains=q)
        shop_baner = Arabic_IndexBlog.objects.filter(is_enable=True)
        news_banner = Arabic_IndexNews.objects.filter(is_enable=True)
        foternews = news_banner[:2]
        foterblog = shop_baner[:2]
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
    return render(request, 'blog.html', context=context)

def detail(request, slug):
    lang = get_language()
    try:
        if lang == "fa":
            blog = BlogsModel.objects.get(persian_slug=slug)
            shop_baner = Persian_IndexBlog.objects.filter(is_enable=True)
            news_banner = Persian_IndexNews.objects.filter(is_enable=True)
            foternews = news_banner[:2]
            foterblog = shop_baner[:2]
        elif lang == "en":
            blog = BlogsModel.objects.get(english_slug=slug)
            shop_baner = English_IndexBlog.objects.filter(is_enable=True)
            news_banner = English_IndexNews.objects.filter(is_enable=True)
            foternews = news_banner[:2]
            foterblog = shop_baner[:2]
        else:
            blog = BlogsModel.objects.get(arabic_slug=slug)
            shop_baner = Arabic_IndexBlog.objects.filter(is_enable=True)
            news_banner = Arabic_IndexNews.objects.filter(is_enable=True)
            foternews = news_banner[:2]
            foterblog = shop_baner[:2]
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
    return render(request, 'blog-single.html', context=context)