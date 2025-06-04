from django.contrib import admin
from haman.models import ContactUSModel, NewsShelterModel, SliderModel
# Register your models here.

@admin.register(SliderModel)
class SliderModelAdmin(admin.ModelAdmin):
    list_display = ['title_persian', 'title_arabic', 'title_english', 'description_persian', 'description_english', 'description_arabic']
    search_fields = ['title_persian', 'title_arabic', 'title_english']

@admin.register(ContactUSModel)
class ContactUSModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'phone', 'time']
    list_filter = ['name', 'email', 'time', 'subject']
    search_fields = ['email', 'phone', 'name', 'message']
    date_hierarchy = 'time'

@admin.register(NewsShelterModel)
class NewsShelterModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'time']
    list_filter = ['name', 'time']
    search_fields = ['email', 'name']
    date_hierarchy = 'time'
