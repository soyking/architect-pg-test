import uuid
import datetime

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from event.models import Event

class Command(BaseCommand):
    def insert(self, days, count):
        now = timezone.now()
        for _ in range(count):
            for day in range(days):
                time = now - datetime.timedelta(days=day)
                Event.objects.create(timestamp=time, name=uuid.uuid4().hex)

    def handle(self, *args, **options):
        days = 360
        count = 1000

        start_time = timezone.now()
        self.insert(days, count)
        end_time = timezone.now()
        duration = (end_time - start_time).total_seconds()

        print('insert {0} records in past {1} days cost {2:.4f} ms'.format(count, days, duration))

