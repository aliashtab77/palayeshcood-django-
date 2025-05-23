from django.urls import path, re_path
from blogs.views import blogs, detail

urlpatterns = [
    path("", blogs, name="blogs"),
    re_path(r'(?P<slug>[-\w]+)/', detail, name="blogsdetail"),
]