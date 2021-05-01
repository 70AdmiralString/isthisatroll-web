from django.forms import Form, CharField

from .models import Redditor


class SearchForm(Form):
    """
    A simple search form. The only entry is the username (pk of models.Redditor)
    """

    username = CharField(
        required=True,
        min_length=Redditor.UsernameValidation.min_length,
        max_length=Redditor.UsernameValidation.max_length,
        validators=[Redditor.UsernameValidation.validation]
    )

    username.widget.attrs.update({
        'class': 'form-control needs-validation',
        'placeholder': 'username',
        'data-validation-regex': Redditor.UsernameValidation.regex,
        'data-validation-message': Redditor.UsernameValidation.message,
    })
