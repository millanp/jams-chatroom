from django.views.generic import ListView, DetailView
from suggestionsapp import models
import nav_urls

class NavUrlsMixin(object):
    def get_context_data(self, **kwargs):
        context = super(NavUrlsMixin, self).get_context_data(**kwargs)
        context['navurls'] = nav_urls.navurlpatterns
        return context


class SuggestionsListView(NavUrlsMixin, ListView):
    model = models.Suggestion
    template_name = 'suggestionsapp/home.html'


class SuggestionDetailView(DetailView):
    model = models.Suggestion
    template_name = 'suggestionsapp/suggestion.html'
