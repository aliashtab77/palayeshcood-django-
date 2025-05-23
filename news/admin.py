from django.contrib import admin
from news.models import NewsModel, ReviewModelNews, Persian_IndexNews, English_IndexNews, Arabic_IndexNews
# Register your models here.

@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    pass

@admin.register(ReviewModelNews)
class ReviewModelNewsAdmin(admin.ModelAdmin):
    pass

@admin.register(Persian_IndexNews)
class Persian_IndexNewsAdmin(admin.ModelAdmin):
    pass

@admin.register(English_IndexNews)
class English_IndexNewsAdmin(admin.ModelAdmin):
    pass

@admin.register(Arabic_IndexNews)
class Arabic_IndexNewsAdmin(admin.ModelAdmin):
    pass
