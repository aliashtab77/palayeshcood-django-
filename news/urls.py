from django.urls import path, re_path
from news.views import news, detail

urlpatterns = [
    path("", news, name="news"),
    re_path(r'(?P<slug>[-\w]+)/', detail, name="newsdetail"),
]