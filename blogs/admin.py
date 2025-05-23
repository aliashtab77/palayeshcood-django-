from django.contrib import admin
from blogs.models import BlogsModel, ReviewModelBlog, Persian_IndexBlog, English_IndexBlog, Arabic_IndexBlog
# Register your models here.

@admin.register(BlogsModel)
class BlogsModelAdmin(admin.ModelAdmin):
    pass

@admin.register(ReviewModelBlog)
class ReviewModelBlogAdmin(admin.ModelAdmin):
    pass

@admin.register(Persian_IndexBlog)
class Persian_IndexBlogAdmin(admin.ModelAdmin):
    pass

@admin.register(English_IndexBlog)
class English_IndexBlogAdmin(admin.ModelAdmin):
    pass

@admin.register(Arabic_IndexBlog)
class Arabic_IndexBlogAdmin(admin.ModelAdmin):
    pass
