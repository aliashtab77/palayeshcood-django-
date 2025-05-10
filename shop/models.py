from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

class ReviewModel(models.Model):
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


class ProductsModel(models.Model):
    persian_slug = models.SlugField(verbose_name=_("persian slug"), allow_unicode=True)
    english_slug = models.SlugField(verbose_name=_("english slug"), allow_unicode=True)
    arabic_slug = models.SlugField(verbose_name=_("arabic slug"), allow_unicode=True)
    show_on_english = models.BooleanField(default=False, verbose_name=_("show on English"))
    show_on_persian = models.BooleanField(default=False, verbose_name=_("show on Persian"))
    show_on_arabic = models.BooleanField(default=False, verbose_name=_("show on Arabic"))
    title_english = models.CharField(max_length=255, verbose_name=_("English Title"), null=True, blank=True)
    title_persian = models.CharField(max_length=255, verbose_name=_("Persian Title"), null=True, blank=True)
    title_arabic = models.CharField(max_length=255, verbose_name=_("Arabic Title"), null=True, blank=True)
    price_english = models.IntegerField(verbose_name=_("English Price"), null=True, blank=True)
    price_persian = models.IntegerField(verbose_name=_("Persian Price"), null=True, blank=True)
    price_arabic = models.IntegerField(verbose_name=_("Arabic Price"), null=True, blank=True)
    is_new = models.BooleanField(default=False, verbose_name=_("enable if this product is new"))
    inventory = models.BooleanField(default=True, verbose_name=_("inventory"))
    avatar = models.ImageField(upload_to="products", verbose_name=_("product image"))
    related_products = models.ManyToManyField('self', related_name="product", verbose_name=_("related products"), null=True, blank=True)
    comments = models.ManyToManyField('ReviewModel', related_name="commentof", verbose_name="Comments", null=True, blank=True)
    description_english = CKEditor5Field(verbose_name=_("English description"), config_name="extends", null=True, blank=True)
    description_persian = CKEditor5Field(verbose_name=_("Persian description"), config_name="extends", null=True, blank=True)
    description_arabic = CKEditor5Field(verbose_name=_("Arabic description"), config_name="extends", null=True, blank=True)
    STAR_CHOICE = [
        (1,"⭐"),
        (2,"⭐⭐"),
        (3,"⭐⭐⭐"),
        (4,"⭐⭐⭐⭐"),
        (5,"⭐⭐⭐⭐⭐")
    ]
    star = models.IntegerField(choices=STAR_CHOICE, default=5, verbose_name=_("Rate"))
    tags = models.TextField(verbose_name=_("tags"), null=True, blank=True)
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
    def __str__(self):
        return self.title_english


class English_Index(models.Model):
    product = models.ForeignKey(to="ProductsModel", verbose_name=_("baner product"), on_delete=models.CASCADE, related_name="english_index")
    is_enable = models.BooleanField(default=True, verbose_name=_("enable"))
    class Meta:
        verbose_name = _("english baner product")
        verbose_name_plural = _("english baner products")
    def __str__(self):
        return self.product.title_english

class Persian_Index(models.Model):
    product = models.ForeignKey(to="ProductsModel", verbose_name=_("baner product"), on_delete=models.CASCADE,
                                related_name="persian_index")
    is_enable = models.BooleanField(default=True, verbose_name=_("enable"))

    class Meta:
        verbose_name = _("persian baner product")
        verbose_name_plural = _("persian baner products")

    def __str__(self):
        return self.product.title_persian


class Arabic_Index(models.Model):
    product = models.ForeignKey(to="ProductsModel", verbose_name=_("baner product"), on_delete=models.CASCADE,
                                related_name="arabic_index")
    is_enable = models.BooleanField(default=True, verbose_name=_("enable"))

    class Meta:
        verbose_name = _("arabic baner product")
        verbose_name_plural = _("arabic baner products")

    def __str__(self):
        return self.product.title_arabic