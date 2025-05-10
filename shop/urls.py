from django.urls import path, re_path
from shop.views import shop, detail

urlpatterns = [
    path("", shop, name="shop"),
    re_path(r'(?P<slug>[-\w]+)/', detail, name="shopdetail"),
]