from django.db import models
import architect


@architect.install('partition', type='range', subtype='date', constraint='day', column='timestamp')
class Event(models.Model):
    timestamp = models.DateTimeField()
    name = models.TextField()
    details = models.TextField()
