from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class ContactUSModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    email = models.EmailField(error_messages=_("your email is not valid"), verbose_name=_("email"))
    message = models.TextField(verbose_name=_("message"))
    subject = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("subject"))
    phone = models.CharField(max_length=16, error_messages=_("your phone number is not valid"), blank=True, null=True, verbose_name=_("phone number"))
    time = models.DateTimeField(auto_now=True, verbose_name=_("time"))
    class Meta:
        verbose_name = _("User Message")
        verbose_name_plural = _("User Messages")

    def __str__(self):
        return f"{self.name} ---> {self.email}   on   {self.time}"


class NewsShelterModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("name"), null=True, blank=True)
    email = models.EmailField(unique=True, verbose_name=_("email"))
    time = models.DateTimeField(auto_now=True, verbose_name=_("time"))
    class Meta:
        verbose_name = _("News Shelter")
        verbose_name_plural = _("News Shelter")
    def __str__(self):
        return f"{self.name} --> {self.email}"
