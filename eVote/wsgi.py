"""
WSGI config for eVote project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eVote.settings')

application = get_wsgi_application()

# added
application = DjangoWhiteNoise(application)