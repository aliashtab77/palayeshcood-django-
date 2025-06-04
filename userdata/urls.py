from django.urls import path
from userdata.views import newsletter, shop_comment, blog_comment, news_comment

urlpatterns = [
    path("newsletter", newsletter, name="newslettr"),
    path("shopcomment", shop_comment, name="saveshopcomment"),
    path("blogcomment", blog_comment, name="saveblogcomment"),
    path("newscomment", news_comment, name="savenewscomment"),
]