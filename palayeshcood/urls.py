"""
URL configuration for palayeshcood project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from haman.views import index, contact, about, team, contactformsaver, faq

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),

    path("servives/", include("services.urls")),
    path("admin/", admin.site.urls),
    path("", index, name="home"),
    path("contact-us/", contact, name="contact"),
    path("save-meassages/", contactformsaver, name="savemessages"),
    path("about-us/", about, name="about"),
    path("our-team/", team, name="team"),
    path("FAQs/", faq, name="faq"),



]


if settings.IS_DEVEL:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

