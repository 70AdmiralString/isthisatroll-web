from django.db import models
from django.core.validators import RegexValidator


class Redditor(models.Model):
    class UsernameValidation:
        min_length = 3
        max_length = 20
        regex = r'^[A-Za-z0-9\-\_]{' + str(min_length) + r',' + str(max_length) + r'}$'
        message = 'Username must be between 3 and 20 alphanumeric characters, plus - and _.'
        validation = RegexValidator(
            regex=regex,
            message=message,
        )

    username = models.CharField(
        primary_key=True,
        max_length=UsernameValidation.max_length,
        validators=[UsernameValidation.validation]
    )
    analysis_date = models.DateTimeField('date analyzed')
    result = models.FloatField()

    def __str__(self):
        return f"""Username: {self.username}
            Date analyzed: {self.analysis_date}
            Result: {self.result}"""
