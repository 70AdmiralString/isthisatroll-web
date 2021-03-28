from django.shortcuts import render
from django.views import generic

from .models import Redditor


class DetailView(generic.DetailView):
    """
    The detail view for Redditors.

    This class provides the view for the results of the analysis
    on a redditor. If the redditor is not present in the database,
    it gives the option of performing the analysis.
    """

    model = Redditor
