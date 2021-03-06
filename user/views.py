from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Redditor
from .forms import SearchForm


class DetailView(generic.DetailView):
    """
    The detail view for Redditors.

    This class provides the view for the results of the analysis
    on a redditor. If the redditor is not present in the database,
    it gives the option of performing the analysis.
    """

    model = Redditor

    def get(self, request, *args, **kwargs):
        """Handle 404 exception by redirecting to the prefilled search form."""
        try:
            response = super().get(request, *args, **kwargs)
        except Http404:
            form = SearchForm(initial={'username': kwargs['pk']})
            response = render(request, 'user/notfound.html', {'form': form})
        return response


class SearchView(generic.edit.FormView):
    """
    The search page view, with form processing.

    This class provides the view for the search page (which is
    also the homepage). It also provides the search form processing.
    """

    form_class = SearchForm
    template_name = 'user/search.html'

    def form_valid(self, form):
        """Handle form creating a new entry if user is not in database, redirecting otheriwse."""
        username = form.cleaned_data['username']
        # if the user is not already in the database, create a new entry
        if not Redditor.objects.filter(pk=username).exists():
            new_redditor = Redditor(username=username,
                                    analysis_date=timezone.now(),
                                    result=0.1)
            new_redditor.save()
        return HttpResponseRedirect(reverse('user:detail', args=(username,)))
