from typing import Any
from django.core.management import BaseCommand
from portfolio import models


class Command(BaseCommand):

    help = ""

    def handle(self, *args: Any, **options: Any):

        print('Filling all tables')

        models.Region.objects.create(name="RU")

        return "ok"
    