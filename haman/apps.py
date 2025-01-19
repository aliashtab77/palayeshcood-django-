from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class HamanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'haman'
    verbose_name = _('Admin Panel')
