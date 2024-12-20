from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User
from django.apps import apps
import re

class Command(BaseCommand):
    help = 'Create models from existing database and register them to admin site.'

    def handle(self, *args, **kwargs):
        # Generate models from existing database
        with open('core/models.py', 'w') as models_file:
            call_command('inspectdb', stdout=models_file)

        # Replace ForeignKey(unique=True) with OneToOneField
        with open('core/models.py', 'r') as models_file:
            models_content = models_file.read()
        models_content = re.sub(r'ForeignKey\(([^)]+),\s*unique=True\)', r'OneToOneField(\1)', models_content)
        with open('core/models.py', 'w') as models_file:
            models_file.write(models_content)

        # Register models to admin site
        with open('core/admin.py', 'w') as admin_file:
            admin_file.write('from django.contrib import admin\n')
            admin_file.write('from .models import *\n')
            for model in apps.get_models():
                if model._meta.app_label == 'core':
                    admin_file.write(f'admin.site.register({model.__name__})\n')

        # Make migrations and migrate
        call_command('makemigrations', 'core')
        call_command('migrate')

        # Create superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin')

        self.stdout.write(self.style.SUCCESS('Successfully built admin panel.'))
        self.stdout.write(self.style.SUCCESS('You can now run the server and access the admin panel.'))
        self.stdout.write(self.style.SUCCESS('Run the following command: python manage.py runserver'))
        self.stdout.write(self.style.SUCCESS('Access the admin panel at http://localhost:8000/admin/'))
        self.stdout.write(self.style.SUCCESS('Login with the following credentials:'))
        self.stdout.write(self.style.SUCCESS('Username: admin'))
        self.stdout.write(self.style.SUCCESS('Password: admin'))
        self.stdout.write(self.style.SUCCESS('You can change the username and password later.'))
