from django.contrib import admin
from shop.models import ProductsModel, ReviewModel, Persian_Index, English_Index, Arabic_Index
# Register your models here.

@admin.register(ProductsModel)
class ProductsModelAdmin(admin.ModelAdmin):
    pass

@admin.register(ReviewModel)
class ReviewModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Persian_Index)
class Persian_IndexAdmin(admin.ModelAdmin):
    pass

@admin.register(English_Index)
class English_IndexAdmin(admin.ModelAdmin):
    pass

@admin.register(Arabic_Index)
class Arabic_IndexAdmin(admin.ModelAdmin):
    pass