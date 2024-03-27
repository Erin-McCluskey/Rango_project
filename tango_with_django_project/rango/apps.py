from django.apps import AppConfig
import os
from django.conf import settings


class RangoConfig(AppConfig):
    name = 'rango'
    path = os.path.join(settings.BASE_DIR, 'rango')