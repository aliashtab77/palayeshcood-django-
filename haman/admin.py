from django.contrib import admin
from haman.models import ContactUSModel, NewsShelterModel
# Register your models here.
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
