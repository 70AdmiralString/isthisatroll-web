from django import forms


class SearchForm(forms.Form):
    """
    A simple search form. The only entry is the username (pk of models.Redditor)
    """

    username = forms.CharField(label="Username", max_length=20, min_length=3)
