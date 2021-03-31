from django.db import models


class Redditor(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    analysis_date = models.DateTimeField('date analyzed')
    result = models.FloatField()
