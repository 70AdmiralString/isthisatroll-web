from django.forms import Form, CharField

from .models import Redditor


class SearchForm(Form):
    """
    A simple search form. The only entry is the username (pk of models.Redditor)
    """

    username = CharField(
        required=True,
        min_length=3,
        max_length=20,
        validators=[Redditor.UsernameValidation.validation]
    )
