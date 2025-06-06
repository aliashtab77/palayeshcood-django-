from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class BlogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogs'
    verbose_name = _("blogs")
