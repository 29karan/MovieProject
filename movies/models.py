from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=128)
    rating =  models.FloatField()
    year = models.IntegerField()
    duration = models.DurationField(blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name
        