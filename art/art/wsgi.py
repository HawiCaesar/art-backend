"""
WSGI config for art project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

import dotenv

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise


dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "art.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
