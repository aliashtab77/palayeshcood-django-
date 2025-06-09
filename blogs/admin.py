from django.contrib import admin
from blogs.models import BlogsModel, ReviewModelBlog, Persian_IndexBlog, English_IndexBlog, Arabic_IndexBlog
# Register your models here.

@admin.register(BlogsModel)
class BlogsModelAdmin(admin.ModelAdmin):
    list_display = ['title_persian', 'title_english', 'title_arabic', 'show_on_persian', 'show_on_english', 'show_on_arabic', 'time_created']
    list_filter = ['show_on_persian', 'show_on_english', 'show_on_arabic', 'time_created']
    search_fields = ['title_persian', 'title_english', 'title_arabic', 'description_persian', 'description_english', 'description_arabic']
    date_hierarchy = 'time_created'
@admin.register(ReviewModelBlog)
class ReviewModelBlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'show', 'phone', 'email', 'comment']
    list_filter = ['show']
    search_fields = ['name', 'phone', 'email', 'comment']

@admin.register(Persian_IndexBlog)
class Persian_IndexBlogAdmin(admin.ModelAdmin):
    list_display = ['is_enable', 'blog']

@admin.register(English_IndexBlog)
class English_IndexBlogAdmin(admin.ModelAdmin):
    list_display = ['is_enable', 'blog']

@admin.register(Arabic_IndexBlog)
class Arabic_IndexBlogAdmin(admin.ModelAdmin):
    list_display = ['is_enable', 'blog']
