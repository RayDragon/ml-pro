from django.core.management import execute_from_command_line
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "interface.settings")
execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:8000'])
