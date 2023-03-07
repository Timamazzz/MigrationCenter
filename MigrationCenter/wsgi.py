"""
WSGI config for MigrationCenter project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

from django.conf import settings
from django.core.wsgi import get_wsgi_application

if not settings.DEBUG:
    sys.path.append('/home/timama/')
    sys.path.append('/home/timama/MigrationCenter')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MigrationCenter.settings')

application = get_wsgi_application()
