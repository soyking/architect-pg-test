import uuid
import datetime
import io

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.db import connection

from event.models import Event

class Command(BaseCommand):
    def insert(self, days, count):
        event_stream = io.StringIO()
        sep = '\t'

        now = timezone.now()
        for day in range(days):
            time = now - datetime.timedelta(days=day)
            for _ in range(count):
                event_stream.write(sep.join([time.isoformat(), uuid.uuid4().hex, uuid.uuid4().hex]) + '\n')

        with connection.cursor() as cursor:
            event_stream.seek(0)
            cursor.copy_from(
                file=event_stream,
                table=Event._meta.db_table,
                sep=sep,
                columns=('timestamp', 'name', 'details')
            )

    def handle(self, *args, **options):
        days = 365
        count = 100
        for _ in range(5):
            start_time = timezone.now()
            self.insert(days, count)
            end_time = timezone.now()
            duration = (end_time - start_time).total_seconds()
            print('insert {0} records in past {1} days cost {2:.4f} ms'.format(count, days, duration))
