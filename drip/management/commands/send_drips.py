from django.core.management.base import BaseCommand

from ...utils import get_drip_models


class Command(BaseCommand):
    def handle(self, *args, **options):
        for drip_model in get_drip_models():
            for drip in drip_model.objects.filter(enabled=True):
                drip.drip.run()
