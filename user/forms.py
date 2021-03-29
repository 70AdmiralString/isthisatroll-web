from django import forms

class SearchForm(forms.Form):
    username = forms.CharField(label="Username", max_length=20, min_length=3)
