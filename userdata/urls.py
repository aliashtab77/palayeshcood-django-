from django.urls import path
from userdata.views import newsletter, shop_comment

urlpatterns = [
    path("newsletter", newsletter, name="newslettr"),
    path("shopcomment", shop_comment, name="saveshopcomment"),
]