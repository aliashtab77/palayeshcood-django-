from django.urls import path
from services.views import services, refinery


urlpatterns = [
    path("", services, name="services"),
    path("refinery/", refinery, name="refinary"),

]