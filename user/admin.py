from django.contrib import admin

from .models import Redditor


@admin.register(Redditor)
class RedditorAdmin(admin.ModelAdmin):
    """ Settings for the Redditor table in admin page. """
    list_display = ('username', 'analysis_date')
    list_filter = ['analysis_date', 'result']
    search_fields = ['username']
