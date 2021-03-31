from django.forms import ModelForm

from .models import Redditor


class SearchForm(ModelForm):
    """
    A simple search form. The only entry is the username (pk of models.Redditor)
    """

    class Meta:
        model = Redditor
        fields = ['username',]
