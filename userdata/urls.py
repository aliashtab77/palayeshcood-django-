from django.urls import path
from userdata.views import newsletter, shop_comment, blog_comment, news_comment, contact_ua, contact_ua_footer

urlpatterns = [
    path("newsletter", newsletter, name="newslettr"),
    path("shopcomment", shop_comment, name="saveshopcomment"),
    path("blogcomment", blog_comment, name="saveblogcomment"),
    path("newscomment", news_comment, name="savenewscomment"),
    path("contact_us", contact_ua, name="savecontactus"),
    path("contact_us_footer", contact_ua_footer, name="savecontactusfooter"),
]