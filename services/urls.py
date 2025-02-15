from django.urls import path
from services.views import services, refinery, petrochemical, global_trade, food, agriculture, support


urlpatterns = [
    path("", services, name="services"),
    path("refinery/", refinery, name="refinary"),
    path("petrochemical/", petrochemical, name="petrochemical"),
    path("global_trade/", global_trade, name="global"),
    path('food/', food, name="food"),
    path('agriculture/', agriculture, name='agriculture'),
    path('support/', support, name='support'),
]