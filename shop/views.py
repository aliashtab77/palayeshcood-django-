from django.shortcuts import render
from django.utils.translation import get_language
from shop.models import ProductsModel, Persian_Index, English_Index, Arabic_Index
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
    elif lang == "en":
        products1 = ProductsModel.objects.filter(show_on_english=True, title_english__contains=q)
        shop_baner = English_Index.objects.filter(is_enable=True)
    else:
        products1 = ProductsModel.objects.filter(show_on_arabic=True, title_arabic__contains=q)
        shop_baner = Arabic_Index.objects.filter(is_enable=True)

    products = Paginator(products1, 9)
    try:
        page =  products.page(page_number)
    except:
        page =  products.page(1)
    context = {
        "pagenator" : products,
        "products" : page,
        "shopbaner":shop_baner,
    }
    return render(request, "shop.html", context=context)


def detail(request, slug):
    lang = get_language()
    try:
        if lang == "fa":
            product = ProductsModel.objects.get(persian_slug=slug)
            shop_baner = Persian_Index.objects.filter(is_enable=True)
            rel = product.related_products.filter(show_on_persian=True)
        elif lang == "en":
            product = ProductsModel.objects.get(english_slug=slug)
            shop_baner = English_Index.objects.filter(is_enable=True)
            rel = product.related_products.filter(show_on_english=True)
        else:
            product = ProductsModel.objects.get(arabic_slug=slug)
            shop_baner = Arabic_Index.objects.filter(is_enable=True)
            rel = product.related_products.filter(show_on_arabic=True)
    except:
        return HttpResponse(f"Bad request with {slug}")

    tags = product.tags.split(",")
    comm = product.comments.filter(show=True)
    rev = len(comm)
    context = {
        "product":product,
        "shopbaner": shop_baner,
        "tags":tags,
        "rev":rev,
        "comments":comm,
        "related":rel,

    }
    return render(request, 'shop-single.html', context=context)