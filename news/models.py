from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class ReviewModelNews(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    email = models.CharField(max_length=255, verbose_name=_("email"), blank=True, null=True)
    phone = models.CharField(max_length=255, verbose_name=_("phone"), blank=True, null=True)
    comment = models.TextField(verbose_name=_("comment"))
    rate = models.CharField(max_length=255, verbose_name=_("rate"))
    show = models.BooleanField(default=False, verbose_name=_("SHOW"))
    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")
    def __str__(self):
        return self.name


class NewsModel(models.Model):
    persian_slug = models.SlugField(verbose_name=_("persian slug"), allow_unicode=True, unique=True)
    english_slug = models.SlugField(verbose_name=_("english slug"), allow_unicode=True, unique=True)
    arabic_slug = models.SlugField(verbose_name=_("arabic slug"), allow_unicode=True, unique=True)
    show_on_english = models.BooleanField(default=False, verbose_name=_("show on English"))
    show_on_persian = models.BooleanField(default=False, verbose_name=_("show on Persian"))
    show_on_arabic = models.BooleanField(default=False, verbose_name=_("show on Arabic"))
    title_english = models.CharField(max_length=255, verbose_name=_("English Title"), null=True, blank=True)
    title_persian = models.CharField(max_length=255, verbose_name=_("Persian Title"), null=True, blank=True)
    title_arabic = models.CharField(max_length=255, verbose_name=_("Arabic Title"), null=True, blank=True)
    avatar = models.ImageField(upload_to="news", verbose_name=_("news image"))
    comments = models.ManyToManyField('ReviewModelNews', related_name="commentof", verbose_name="Comments", null=True, blank=True)
    description_english = CKEditor5Field(verbose_name=_("English description"), config_name="extends", null=True, blank=True)
    description_persian = CKEditor5Field(verbose_name=_("Persian description"), config_name="extends", null=True, blank=True)
    description_arabic = CKEditor5Field(verbose_name=_("Arabic description"), config_name="extends", null=True, blank=True)
    short_description_english = CKEditor5Field(verbose_name=_("Short English description"), config_name="extends", null=True,
                                         blank=True)
    short_description_persian = CKEditor5Field(verbose_name=_("Short Persian description"), config_name="extends", null=True,
                                         blank=True)
    short_description_arabic = CKEditor5Field(verbose_name=_("Short Arabic description"), config_name="extends", null=True,
                                        blank=True)
    tags = models.TextField(verbose_name=_("tags"), null=True, blank=True)
    time_created = models.DateField(auto_now=True, verbose_name=_("time created"))
    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")
    def __str__(self):
        return self.title_english


class English_IndexNews(models.Model):
    news = models.ForeignKey(to="NewsModel", verbose_name=_("baner news"), on_delete=models.CASCADE, related_name="english_index")
    is_enable = models.BooleanField(default=True, verbose_name=_("enable"))
    class Meta:
        verbose_name = _("english baner news")
        verbose_name_plural = _("english baner news")
    def __str__(self):
        return self.news.title_english

class Persian_IndexNews(models.Model):
    news = models.ForeignKey(to="NewsModel", verbose_name=_("baner news"), on_delete=models.CASCADE,
                                related_name="persian_index")
    is_enable = models.BooleanField(default=True, verbose_name=_("enable"))

    class Meta:
        verbose_name = _("persian baner news")
        verbose_name_plural = _("persian baner news")

    def __str__(self):
        return self.news.title_persian


class Arabic_IndexNews(models.Model):
    news = models.ForeignKey(to="NewsModel", verbose_name=_("baner news"), on_delete=models.CASCADE,
                                related_name="arabic_index")
    is_enable = models.BooleanField(default=True, verbose_name=_("enable"))

    class Meta:
        verbose_name = _("arabic baner news")
        verbose_name_plural = _("arabic baner news")

    def __str__(self):
        return self.news.title_arabic