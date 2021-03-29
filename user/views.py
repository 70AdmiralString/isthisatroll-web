from django.http import HttpResponseRedirect
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


def search(request):
    """
    The search page view, with form processing.

    This function provides the view for the search page (which is
    also the homepage). It also provides the search form processing.
    """

    # if a POST request, process the data and redirect to detail of user
    if request.method == 'POST':
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

    else:
        form = SearchForm()

    return render(request, 'user/search.html', {'form': form})
