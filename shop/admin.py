from django.contrib import admin
from shop.models import ProductsModel, ReviewModel, Persian_Index, English_Index, Arabic_Index
# Register your models here.

@admin.register(ProductsModel)
class ProductsModelAdmin(admin.ModelAdmin):
    list_display = ['title_english', 'title_persian', 'title_arabic', 'is_new', 'inventory', 'show_on_english', 'show_on_persian', 'show_on_arabic']
    list_filter = ['show_on_english', 'show_on_persian', 'show_on_arabic', 'is_new', 'inventory']
    search_fields = ['title_persian', 'title_english', 'title_arabic', 'description_persian', 'description_english', 'description_arabic']

@admin.register(ReviewModel)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'show','phone' ,'email' ,'comment']
    list_filter = ['show']
    search_fields = ['name', 'phone', 'email', 'comment']



@admin.register(Persian_Index)
class Persian_IndexAdmin(admin.ModelAdmin):
    list_display = ['is_enable', 'product']


@admin.register(English_Index)
class English_IndexAdmin(admin.ModelAdmin):
    list_display = ['is_enable', 'product']

@admin.register(Arabic_Index)
class Arabic_IndexAdmin(admin.ModelAdmin):
    list_display = ['is_enable', 'product']