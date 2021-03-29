from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views import generic, View

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


class SearchView(View):
    """
    The search page view, with form processing.

    This class provides the view for the search page (which is
    also the homepage). It also provides the search form processing.
    """

    form_class = SearchForm
    template_name = 'user/search.html'
    initial = {}

    # if a GET request, render the search page
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    # if a POST request, process the data and redirect to detail of user
    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            # if the user is not already in the database, create a new entry
            if not Redditor.objects.filter(pk=username).exists():
                new_redditor = Redditor(username=username,
                                        analysis_date=timezone.now(),
                                        result=0.1)
                new_redditor.save()
            return HttpResponseRedirect(reverse('user:detail', args=(username,)))
        return render(request, self.template_name, {'form': form})
