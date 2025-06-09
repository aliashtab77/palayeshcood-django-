from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

class SliderModel(models.Model):
    avatar = models.ImageField(upload_to="slider", verbose_name=_("slide picture"))
    title_persian = models.CharField(max_length=255, verbose_name=_("persian title"), blank=True, null=True)
    title_english = models.CharField(max_length=255, verbose_name=_("english title"), blank=True, null=True)
    title_arabic = models.CharField(max_length=255, verbose_name=_("arabic description"), blank=True, null=True)
    description_persian = CKEditor5Field(max_length=255, verbose_name=_("persian description"), blank=True, null=True, config_name="short")
    description_english = CKEditor5Field(max_length=255, verbose_name=_("english description"), blank=True, null=True, config_name="short")
    description_arabic = CKEditor5Field(max_length=255, verbose_name=_("arabic description"), blank=True, null=True, config_name="short")
    # XPOS = (
    # ("right",_("right")),
    # ("left",_("left")),
    # ("center",_("center"))
    # )
    # YPOS = (
    # ("top", _("top")),
    # ("center", _("center"))
    # )
    # title_position_y = models.CharField(choices=YPOS, verbose_name=_("title_position_y"), null=True, blank=True)
    # title_position_x = models.CharField(choices=XPOS, verbose_name=_("title_position_x"), null=True, blank=True)



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
