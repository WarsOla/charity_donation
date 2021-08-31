from django.core.management import BaseCommand

from donations.management.commands._private import update_institutions


class Command(BaseCommand):
    help = "Update institutions with categories"

    def handle(self, *args, **options):
        update_institutions()
        self.stdout.write(self.style.SUCCESS("Successfully updated models for Institution"))