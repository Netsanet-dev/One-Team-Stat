import os
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

# Render shell is not availbale for free account
# Need to create a super user my render account

class Command(BaseCommand):
    help = 'Creates Default superuser'
    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(is_superuser=True).exists:
            User.objects.create_superuser(
                username=os.environ.get('DJANGO_SUPERUSER_NAME'),
                email=os.environ.get('DJANGO_SUPERUSER_EMAIL'),
                password=os.environ.get('DJANGO_SUPERUSER_PASSWORD')
            )
            self.stdout.write(self.style.SUCCESS('Default Superuser Created!'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists.'))