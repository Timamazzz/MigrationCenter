import os
import sys

sys.path.insert(0, '/var/www/u0545518/data/www/cppsta.ru/MigrationCenter')
sys.path.insert(0, '/var/www/u0545518/data/www/cppsta.ru/MigrationCenter/MigrationCenter')
sys.path.insert(1, '/var/www/u0545518/data/djangoenv/lib/python3.10.1/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'MigrationCenter.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()