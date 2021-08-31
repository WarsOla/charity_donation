from django.core.management import BaseCommand

from donations.management.commands._private import create_institutions


class Command(BaseCommand):
    help = "Populates database with institutions"

    def handle(self, *args, **options):
        create_institutions()
        self.stdout.write(self.style.SUCCESS("Successfully populates models for Institution"))