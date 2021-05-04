from django.urls import reverse
from django.utils import timezone
from django.test import TestCase

from .forms import SearchForm
from .models import Redditor
from .views import DetailView


class DetailViewTests(TestCase):
    """Tests for DetailView view."""

    def test_not_existing_redditor(self):
        """If a redditor doesn't exist, the user/notfound.html template is rendered."""
        url = reverse('user:detail', args=('not_existing_redditor',))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'user/notfound.html')

    def test_existing_redditor(self):
        """If a redditor exists, the user/redditor_detail.html template is rendered."""
        redditor = Redditor(
            username='existing_redditor',
            analysis_date=timezone.now(),
            result=2.122
        )
        redditor.save()
        url = reverse('user:detail', args=('existing_redditor',))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'user/redditor_detail.html')


class SearchFormTest(TestCase):
    """Tests for SearchForm form."""

    def test_valid_username(self):
        """If a valid username is provided, the form is valid."""
        form = SearchForm(
            {'username': 'weirD_but-ok1'}
        )
        self.assertTrue(form.is_valid())

    def test_too_short_username_0(self):
        """If a username is too short (0 chars), the form is not valid."""
        form = SearchForm(
            {'username': ''}
        )
        self.assertFalse(form.is_valid())

    def test_too_short_username_1(self):
        """If a username is too short (1 char), the form is not valid."""
        form = SearchForm(
            {'username': '1'}
        )
        self.assertFalse(form.is_valid())

    def test_too_short_username_2(self):
        """If a username is too short (2 chars), the form is not valid."""
        form = SearchForm(
            {'username': 'ts'}
        )
        self.assertFalse(form.is_valid())

    def test_too_long_username(self):
        """If a username is too long, the form is not valid."""
        form = SearchForm(
            {'username': 'way_too_long_username_to_pass_theTEST'}
        )
        self.assertFalse(form.is_valid())

    def test_invalid_username_1(self):
        """If a username has an invalid character (]), the form is not valid."""
        form = SearchForm(
            {'username': 'asda]'}
        )
        self.assertFalse(form.is_valid())

    def test_invalid_username_2(self):
        """If a username has an invalid character ([), the form is not valid."""
        form = SearchForm(
            {'username': 'a[avl'}
        )
        self.assertFalse(form.is_valid())

    def test_invalid_username_3(self):
        """If a username has an invalid character ( ), the form is not valid."""
        form = SearchForm(
            {'username': 'john milnor'}
        )
        self.assertFalse(form.is_valid())

    def test_existing_redditor(self):
        """If the redditor is already in the database, the form is valid."""
        redditor = Redditor(
            username='existing_redditor',
            analysis_date=timezone.now(),
            result=2.122
        )
        redditor.save()
        form = SearchForm(
            {'username': 'existing_redditor'}
        )
        self.assertTrue(form.is_valid())
