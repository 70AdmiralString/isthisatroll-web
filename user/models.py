from django.db import models
from django.core.validators import RegexValidator


class Redditor(models.Model):
    username = models.CharField(
        primary_key=True,
        max_length=20,
        validators=[RegexValidator(
            regex=r'^[A-Za-z0-9\-\_]{3,20}',
            message='Username must be between 3 and 20 alphanumeric characters, plus - and _.'
        )]
    )
    analysis_date = models.DateTimeField('date analyzed')
    result = models.FloatField()

    def __str__(self):
        return f"""Username: {self.username}
            Date analyzed: {self.analysis_date}
            Result: {self.result}"""
