from django.core.management import BaseCommand

from donations.management.commands._private import create_categories


class Command(BaseCommand):
    help = "Populates database with categories of donation"

    def handle(self, *args, **options):
        create_categories()
        self.stdout.write(self.style.SUCCESS("Successfully populates models for Category"))