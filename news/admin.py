from django.contrib import admin
from news.models import NewsModel, ReviewModelNews, Persian_IndexNews, English_IndexNews, Arabic_IndexNews
# Register your models here.

@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['title_persian', 'title_english', 'title_arabic', 'show_on_persian', 'show_on_english', 'show_on_arabic', 'time_created']
    list_filter = ['show_on_persian', 'show_on_english', 'show_on_arabic', 'time_created']
    search_fields = ['title_persian', 'title_english', 'title_arabic', 'description_persian', 'description_english', 'description_arabic']
    date_hierarchy = 'time_created'

@admin.register(ReviewModelNews)
class ReviewModelNewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'show', 'phone', 'email', 'comment']
    list_filter = ['show']
    search_fields = ['name', 'phone', 'email', 'comment']

@admin.register(Persian_IndexNews)
class Persian_IndexNewsAdmin(admin.ModelAdmin):
    list_display = ['news', 'is_enable']

@admin.register(English_IndexNews)
class English_IndexNewsAdmin(admin.ModelAdmin):
    list_display = ['news', 'is_enable']

@admin.register(Arabic_IndexNews)
class Arabic_IndexNewsAdmin(admin.ModelAdmin):
    list_display = ['news', 'is_enable']
