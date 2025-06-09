from django.shortcuts import render
from django.utils.translation import get_language
from shop.models import ProductsModel, Persian_Index, English_Index, Arabic_Index
from news.models import Persian_IndexNews, English_IndexNews, Arabic_IndexNews
from blogs.models import Persian_IndexBlog, English_IndexBlog, Arabic_IndexBlog
from django.core.paginator import Paginator
from django.http import HttpResponse
# Create your views here.


def shop(request):
    page_number = request.GET.get("page", default=1)
    q = request.POST.get("search-field", default="").strip()
    lang = get_language()
    if lang == "fa":
        products1 = ProductsModel.objects.filter(show_on_persian=True, title_persian__contains=q)
        shop_baner = Persian_Index.objects.filter(is_enable=True)
        blogs_baner = Persian_IndexBlog.objects.filter(is_enable=True)
        news_banner = Persian_IndexNews.objects.filter(is_enable=True)
        foternews = news_banner[:2]
        foterblog = blogs_baner[:2]
    elif lang == "en":
        products1 = ProductsModel.objects.filter(show_on_english=True, title_english__contains=q)
        shop_baner = English_Index.objects.filter(is_enable=True)
        blogs_baner = English_IndexBlog.objects.filter(is_enable=True)
        news_banner = English_IndexNews.objects.filter(is_enable=True)
        foternews = news_banner[:2]
        foterblog = blogs_baner[:2]
    else:
        products1 = ProductsModel.objects.filter(show_on_arabic=True, title_arabic__contains=q)
        shop_baner = Arabic_Index.objects.filter(is_enable=True)
        blogs_baner = Arabic_IndexBlog.objects.filter(is_enable=True)
        news_banner = Arabic_IndexNews.objects.filter(is_enable=True)
        foternews = news_banner[:2]
        foterblog = blogs_baner[:2]

    products = Paginator(products1, 9)
    try:
        page =  products.page(page_number)
    except:
        page =  products.page(1)
    context = {
        "pagenator" : products,
        "products" : page,
        "shopbaner":shop_baner,
        "footernews": foternews,
        "footerblogs": foterblog,
    }
    return render(request, "shop.html", context=context)


def detail(request, slug):
    lang = get_language()
    try:
        if lang == "fa":
            product = ProductsModel.objects.get(persian_slug=slug)
            shop_baner = Persian_Index.objects.filter(is_enable=True)
            rel = product.related_products.filter(show_on_persian=True)
            blogs_baner = Persian_IndexBlog.objects.filter(is_enable=True)
            news_banner = Persian_IndexNews.objects.filter(is_enable=True)
            foternews = news_banner[:2]
            foterblog = blogs_baner[:2]
        elif lang == "en":
            product = ProductsModel.objects.get(english_slug=slug)
            shop_baner = English_Index.objects.filter(is_enable=True)
            rel = product.related_products.filter(show_on_english=True)
            blogs_baner = English_IndexBlog.objects.filter(is_enable=True)
            news_banner = English_IndexNews.objects.filter(is_enable=True)
            foternews = news_banner[:2]
            foterblog = blogs_baner[:2]
        else:
            product = ProductsModel.objects.get(arabic_slug=slug)
            shop_baner = Arabic_Index.objects.filter(is_enable=True)
            rel = product.related_products.filter(show_on_arabic=True)
            blogs_baner = Arabic_IndexBlog.objects.filter(is_enable=True)
            news_banner = Arabic_IndexNews.objects.filter(is_enable=True)
            foternews = news_banner[:2]
            foterblog = blogs_baner[:2]
    except:
        return HttpResponse(f"Bad request with {slug}")

    tags = product.tags.split(",")
    comm = product.comments.filter(show=True)
    rev = len(comm)
    print(product.id)
    context = {
        "product":product,
        "shopbaner": shop_baner,
        "tags":tags,
        "rev":rev,
        "comments":comm,
        "related":rel,
        "footernews": foternews,
        "footerblogs": foterblog,
    }
    return render(request, 'shop-single.html', context=context)