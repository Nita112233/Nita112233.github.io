"""
WSGI config for EMR project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# HEROKU DJANGO SETTINGS ====================
from whitenoise.django import DjangoWhiteNoise

# ===========================================

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EMR.settings")

application = get_wsgi_application()

# HEROKU DJANGO SETTINGS ====================
application = DjangoWhiteNoise(application)
# ===========================================
